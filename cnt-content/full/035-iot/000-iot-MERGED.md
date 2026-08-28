---
order: 10
title: iot 模块文档合集
module: 'iot'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：035-iot/001-OverviewArchitecture.md ============ -->


## 1. IoT 概念

### 1.1 定义

物联网（Internet of Things, IoT）是通过**传感器、软件和网络连接**将物理设备与互联网连接起来的技术体系，实现物与物、人与物的智能互联。

### 1.2 发展历程

| 阶段       | 时间      | 特点             | 代表技术           |
| :--------- | :-------- | :--------------- | :----------------- |
| **萌芽期** | 1990s     | RFID 和 M2M 概念 | 条形码、RFID       |
| **起步期** | 2008-2012 | 传感器网络       | WSN、Zigbee        |
| **发展期** | 2013-2018 | 云平台和大数据   | AWS IoT、MQTT      |
| **成熟期** | 2019-2022 | 边缘计算和 AIoT  | 边缘推理、5G       |
| **智能化** | 2023-     | AI Agent + IoT   | 自主决策、数字孪生 |

### 1.3 IoT 核心特征

| 特征         | 描述                       |
| :----------- | :------------------------- |
| **全面感知** | 通过传感器获取物理世界信息 |
| **可靠传输** | 通过网络传输感知数据       |
| **智能处理** | 对数据进行存储、分析和决策 |
| **自动执行** | 根据决策自动控制设备       |

## 2. IoT 架构层次

### 2.1 四层架构

```mermaid
flowchart TD
    App[应用层<br/>智能家居/工业监控/智慧城市/智慧农业] --> Plat[平台层<br/>设备管理/规则引擎/数据存储/AI 分析]
    Plat --> Net[网络层<br/>MQTT/CoAP/LoRa/NB-IoT/5G/Wi-Fi]
    Net --> Per[感知层<br/>传感器/执行器/MCU/嵌入式系统]
```

### 2.2 各层详解

| 层次       | 核心功能           | 关键技术             | 代表产品             |
| :--------- | :----------------- | :------------------- | :------------------- |
| **感知层** | 数据采集与执行     | 传感器、MCU、ADC/DAC | STM32、ESP32         |
| **网络层** | 数据传输           | MQTT、LoRa、NB-IoT   | EMQX、LoRa网关       |
| **平台层** | 设备管理与数据处理 | 云平台、规则引擎     | AWS IoT、ThingsBoard |
| **应用层** | 业务逻辑与用户交互 | Web/App、AI 分析     | 智能家居 App         |

### 2.3 边缘-云协同架构

```mermaid
flowchart LR
    T[终端设备<br/>传感器 执行器<br/>实时控制 毫秒级] --> E[边缘节点<br/>网关/边缘 AI 推理<br/>本地决策 秒级]
    E --> C[云平台<br/>大数据分析 模型训练<br/>全局优化 分钟/小时级]
```

## 3. 通信协议总览

### 3.1 协议分类

| 类别           | 协议               | 范围  | 特点           |
| :------------- | :----------------- | :---- | :------------- |
| **短距离**     | BLE、Zigbee、Wi-Fi | <100m | 高速率、低延迟 |
| **低功耗广域** | LoRa、NB-IoT       | <15km | 低功耗、低速率 |
| **蜂窝网络**   | 4G、5G             | 全国  | 高速率、高成本 |
| **应用层**     | MQTT、CoAP、HTTP   | -     | 设备-云通信    |

### 3.2 协议选型矩阵

| 场景     | 数据量 | 功耗 | 距离 | 推荐协议        |
| :------- | :----- | :--- | :--- | :-------------- |
| 智能家居 | 中     | 低   | 短   | Wi-Fi + BLE     |
| 环境监测 | 小     | 极低 | 远   | LoRa + MQTT     |
| 车联网   | 大     | 不限 | 远   | 5G + MQTT       |
| 工业控制 | 中     | 不限 | 短   | Ethernet + MQTT |
| 智慧农业 | 小     | 极低 | 远   | NB-IoT + CoAP   |

## 4. 应用场景

### 4.1 消费级 IoT

| 场景         | 设备             | 核心需求         |
| :----------- | :--------------- | :--------------- |
| **智能家居** | 灯光、空调、门锁 | 便捷、安全、互联 |
| **可穿戴**   | 手表、健康监测   | 低功耗、实时     |
| **车联网**   | T-Box、OBD       | 高可靠、低延迟   |

### 4.2 工业级 IoT（IIoT）

| 场景         | 设备            | 核心需求         |
| :----------- | :-------------- | :--------------- |
| **预测维护** | 振动/温度传感器 | 高精度、实时分析 |
| **数字孪生** | 全类型传感器    | 数据融合、可视化 |
| **质量检测** | 视觉/光谱传感器 | 高精度、AI 推理  |

### 4.3 城市级 IoT

| 场景         | 设备            | 核心需求       |
| :----------- | :-------------- | :------------- |
| **智慧照明** | 路灯控制器      | 节能、远程控制 |
| **环境监测** | 空气/噪声传感器 | 广覆盖、低功耗 |
| **智慧停车** | 地磁/摄像头     | 实时、准确     |

## 5. 行业趋势

### 5.1 技术趋势

| 趋势            | 描述               | 影响                   |
| :-------------- | :----------------- | :--------------------- |
| **AIoT**        | AI + IoT 融合      | 设备从感知走向认知     |
| **边缘智能**    | AI 推理下沉到边缘  | 降低延迟、保护隐私     |
| **5G IoT**      | 5G 网络切片        | 支持大规模、低延迟场景 |
| **数字孪生**    | 物理世界的数字映射 | 仿真、预测、优化       |
| **Matter 协议** | 智能家居统一标准   | 打破生态壁垒           |
| **卫星 IoT**    | 低轨卫星通信       | 覆盖偏远地区           |

### 5.2 市场规模

| 领域     | 2025 连接数(亿) | 2030 预测(亿) | CAGR |
| :------- | :-------------- | :------------ | :--- |
| 消费 IoT | 120             | 250           | 15%  |
| 工业 IoT | 50              | 150           | 25%  |
| 智慧城市 | 30              | 80            | 22%  |
| 智慧农业 | 10              | 40            | 32%  |

## 6. IoT 开发入门

### 6.1 技术栈

```
硬件层: 传感器 → MCU (STM32/ESP32) → 通信模块
  ↓
协议层: MQTT / CoAP / HTTP
  ↓
平台层: EMQX / ThingsBoard / AWS IoT Core
  ↓
应用层: Web / App / 数据分析
```

### 6.2 快速体验

```python
# 使用 paho-mqtt 连接 MQTT 服务器
import paho.mqtt.client as mqtt
import json
import time
import random

# 连接回调
def on_connect(client, userdata, flags, rc):
    print(f"连接结果: {rc}")
    client.subscribe("iot/sensor/commands")

# 消息回调
def on_message(client, userdata, msg):
    print(f"收到命令: {msg.topic} - {msg.payload.decode()}")

# 创建客户端
client = mqtt.Client(client_id="sensor_node_001")
client.on_connect = on_connect
client.on_message = on_message

# 连接服务器
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()

# 模拟传感器数据上报
try:
    while True:
        data = {
            "device_id": "sensor_001",
            "temperature": round(random.uniform(20, 35), 1),
            "humidity": round(random.uniform(40, 80), 1),
            "timestamp": int(time.time())
        }
        client.publish("iot/sensor/data", json.dumps(data))
        print(f"上报数据: {data}")
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
```

## 7. 学习路线

```
入门 → 传感器与嵌入式 → 通信协议 → IoT 平台
  → 数据处理与分析 → 边缘计算 → 安全与隐私 → 实战项目
```

### 推荐学习顺序

1. 理解 IoT 架构和核心概念
2. 学习嵌入式开发（ESP32/STM32）
3. 掌握 MQTT 等通信协议
4. 了解 IoT 云平台
5. 学习时序数据库和流处理
6. 探索边缘计算和 AI 推理
7. 关注安全和隐私保护
8. 完成端到端实战项目

## 8. 小结

IoT 是连接物理世界和数字世界的桥梁：

1. **四层架构**（感知/网络/平台/应用）是理解 IoT 系统的基础
2. **通信协议**选型需综合考虑数据量、功耗、距离和成本
3. **AIoT** 是未来趋势，AI 能力正从云端下沉到边缘
4. 消费级 IoT 关注便捷和互联，工业级 IoT 关注可靠和实时
5. 入门建议从 ESP32 + MQTT 开始，逐步构建完整的 IoT 系统



<!-- ============ 文档分隔线：035-iot/002-SensorEmbedded.md ============ -->


## 1. 传感器类型与原理

### 1.1 传感器分类

| 类型       | 测量对象  | 代表传感器       | 输出信号 |
| :--------- | :-------- | :--------------- | :------- |
| **温度**   | 温度      | DS18B20、DHT22   | 数字/I2C |
| **湿度**   | 湿度      | DHT22、SHT30     | 数字/I2C |
| **压力**   | 气压/液压 | BMP280、MPX5010  | I2C/模拟 |
| **加速度** | 加速度    | MPU6050、ADXL345 | I2C/SPI  |
| **光照**   | 光强      | BH1750、光敏电阻 | I2C/模拟 |
| **气体**   | 气体浓度  | MQ-2、BME680     | 模拟/I2C |
| **距离**   | 距离      | HC-SR04、VL53L0X | 数字/I2C |
| **GPS**    | 位置      | NEO-6M、NEO-M8N  | UART     |

### 1.2 模拟与数字传感器

| 类型     | 原理             | 优点           | 缺点             |
| :------- | :--------------- | :------------- | :--------------- |
| **模拟** | 输出连续电压信号 | 简单、低成本   | 需 ADC、抗干扰差 |
| **数字** | 输出数字信号     | 抗干扰、精度高 | 协议复杂         |

### 1.3 ADC/DAC

```c
// STM32 ADC 读取模拟传感器
#include "stm32f4xx_hal.h"

ADC_HandleTypeDef hadc1;

void ADC_Init(void) {
    hadc1.Instance = ADC1;
    hadc1.Init.ClockPrescaler = ADC_CLOCK_SYNC_PCLK_DIV4;
    hadc1.Init.Resolution = ADC_RESOLUTION_12B;      // 12位精度
    hadc1.Init.ScanConvMode = DISABLE;
    hadc1.Init.ContinuousConvMode = ENABLE;           // 连续转换
    hadc1.Init.DMAContinuousRequests = ENABLE;
    HAL_ADC_Init(&hadc1);
}

uint16_t ADC_Read(uint32_t channel) {
    ADC_ChannelConfTypeDef sConfig = {0};
    sConfig.Channel = channel;
    sConfig.Rank = 1;
    sConfig.SamplingTime = ADC_SAMPLETIME_480CYCLES;
    HAL_ADC_ConfigChannel(&hadc1, &sConfig);

    HAL_ADC_Start(&hadc1);
    HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
    return HAL_ADC_GetValue(&hadc1);
}

// 将 ADC 值转换为电压和温度
float read_temperature(void) {
    uint16_t adc_value = ADC_Read(ADC_CHANNEL_0);
    float voltage = (adc_value / 4095.0f) * 3.3f;  // 12位, 3.3V参考
    float temperature = voltage * 100.0f;           // LM35: 10mV/°C
    return temperature;
}
```

## 2. 嵌入式开发

### 2.1 MCU 对比

| MCU             | 架构           | 主频   | Flash    | RAM   | Wi-Fi | 价格 |
| :-------------- | :------------- | :----- | :------- | :---- | :---- | :--- |
| **ESP32**       | Xtensa         | 240MHz | 4MB      | 520KB |       | ¥15  |
| **ESP32-S3**    | Xtensa         | 240MHz | 8-16MB   | 512KB |       | ¥20  |
| **STM32F4**     | ARM Cortex-M4  | 168MHz | 1MB      | 192KB |       | ¥25  |
| **STM32H7**     | ARM Cortex-M7  | 480MHz | 2MB      | 1MB   |       | ¥60  |
| **RP2040**      | ARM Cortex-M0+ | 133MHz | 16MB(外) | 264KB |       | ¥8   |
| **Arduino Uno** | AVR            | 16MHz  | 32KB     | 2KB   |       | ¥25  |

### 2.2 ESP32 开发（Arduino）

```cpp
// ESP32 + DHT22 温湿度传感器
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// 引脚定义
#define DHT_PIN 4
#define LED_PIN 2
#define DHT_TYPE DHT22

// WiFi 配置
const char* ssid = "YourWiFi";
const char* password = "YourPassword";

// MQTT 配置
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;
const char* mqtt_topic = "iot/sensor/data";

DHT dht(DHT_PIN, DHT_TYPE);
WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
    delay(10);
    Serial.println("Connecting to WiFi...");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi connected, IP: " + WiFi.localIP().toString());
}

void reconnect() {
    while (!client.connected()) {
        String clientId = "ESP32-" + String(random(0xffff), HEX);
        if (client.connect(clientId.c_str())) {
            Serial.println("MQTT connected");
            client.subscribe("iot/sensor/commands");
        } else {
            Serial.print("MQTT failed, rc=");
            Serial.print(client.state());
            delay(5000);
        }
    }
}

void callback(char* topic, byte* payload, unsigned int length) {
    String message;
    for (int i = 0; i < length; i++) {
        message += (char)payload[i];
    }
    Serial.println("Command: " + message);

    if (message == "LED_ON") digitalWrite(LED_PIN, HIGH);
    else if (message == "LED_OFF") digitalWrite(LED_PIN, LOW);
}

void setup() {
    Serial.begin(115200);
    dht.begin();
    pinMode(LED_PIN, OUTPUT);

    setup_wifi();
    client.setServer(mqtt_server, mqtt_port);
    client.setCallback(callback);
}

void loop() {
    if (!client.connected()) reconnect();
    client.loop();

    // 读取传感器
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    if (isnan(humidity) || isnan(temperature)) {
        Serial.println("Sensor read failed!");
        delay(2000);
        return;
    }

    // 构建 JSON
    String payload = "{\"device\":\"ESP32-001\","
                     "\"temperature\":" + String(temperature, 1) + ","
                     "\"humidity\":" + String(humidity, 1) + "}";

    client.publish(mqtt_topic, payload.c_str());
    Serial.println("Published: " + payload);

    delay(5000);  // 每5秒上报
}
```

### 2.3 ESP32 开发（MicroPython）

```python
# MicroPython - ESP32 温湿度上报
import machine
import dht
import time
import json
from umqtt.simple import MQTTClient

# 配置
WIFI_SSID = "YourWiFi"
WIFI_PASS = "YourPassword"
MQTT_BROKER = "broker.emqx.io"
MQTT_TOPIC = b"iot/sensor/data"

# 初始化
d = dht.DHT22(machine.Pin(4))
led = machine.Pin(2, machine.Pin.OUT)

def connect_wifi():
    import network
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(WIFI_SSID, WIFI_PASS)
    while not sta.isconnected():
        time.sleep(0.5)
    print("WiFi connected:", sta.ifconfig()[0])

def publish_data():
    mqtt = MQTTClient("esp32-001", MQTT_BROKER)
    mqtt.connect()

    while True:
        try:
            d.measure()
            data = {
                "device": "ESP32-001",
                "temperature": d.temperature(),
                "humidity": d.humidity(),
                "timestamp": time.time()
            }
            mqtt.publish(MQTT_TOPIC, json.dumps(data).encode())
            print("Published:", data)
        except Exception as e:
            print("Error:", e)

        time.sleep(5)

connect_wifi()
publish_data()
```

## 3. 通信接口

### 3.1 接口对比

| 接口       | 类型     | 速率           | 距离 | 设备数   | 用途              |
| :--------- | :------- | :------------- | :--- | :------- | :---------------- |
| **GPIO**   | 数字 I/O | -              | 板级 | 1        | LED、按键、继电器 |
| **I2C**    | 总线     | 100K-3.4Mbps   | 板级 | 127      | 传感器、EEPROM    |
| **SPI**    | 总线     | 10-80Mbps      | 板级 | 理论无限 | Flash、显示屏     |
| **UART**   | 点对点   | 9600-921600bps | 15m  | 1        | GPS、调试         |
| **1-Wire** | 总线     | 16.3kbps       | 100m | 100+     | DS18B20           |

### 3.2 I2C 示例

```cpp
// ESP32 I2C 读取 BH1750 光照传感器
#include <Wire.h>

#define BH1750_ADDR 0x23

void setup() {
    Serial.begin(115200);
    Wire.begin(21, 22);  // SDA=21, SCL=22
}

uint16_t readLight() {
    Wire.beginTransmission(BH1750_ADDR);
    Wire.write(0x10);  // 连续高分辨率模式
    Wire.endTransmission();
    delay(120);

    Wire.requestFrom(BH1750_ADDR, 2);
    if (Wire.available() == 2) {
        uint16_t lux = (Wire.read() << 8) | Wire.read();
        return lux / 1.2;
    }
    return 0;
}

void loop() {
    uint16_t light = readLight();
    Serial.printf("Light: %d lux\n", light);
    delay(1000);
}
```

### 3.3 SPI 示例

```cpp
// ESP32 SPI 读取数据
#include <SPI.h>

#define CS_PIN 5

void setup() {
    Serial.begin(115200);
    SPI.begin(18, 19, 23);  // SCK=18, MISO=19, MOSI=23
    pinMode(CS_PIN, OUTPUT);
    digitalWrite(CS_PIN, HIGH);
}

uint16_t spiRead16(uint8_t reg) {
    digitalWrite(CS_PIN, LOW);
    SPI.transfer(reg | 0x80);  // 读命令
    uint8_t msb = SPI.transfer(0x00);
    uint8_t lsb = SPI.transfer(0x00);
    digitalWrite(CS_PIN, HIGH);
    return (msb << 8) | lsb;
}
```

## 4. 实时操作系统（RTOS）

### 4.1 FreeRTOS

```c
// FreeRTOS 多任务示例
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"

// 数据队列
QueueHandle_t sensor_queue;

// 传感器读取任务
void sensor_task(void *pvParameters) {
    float sensor_data;
    while (1) {
        sensor_data = read_temperature();
        xQueueSend(sensor_queue, &sensor_data, portMAX_DELAY);
        vTaskDelay(pdMS_TO_TICKS(1000));  // 1秒周期
    }
}

// 数据上报任务
void upload_task(void *pvParameters) {
    float received_data;
    while (1) {
        if (xQueueReceive(sensor_queue, &received_data, portMAX_DELAY)) {
            mqtt_publish("iot/sensor/temp", &received_data);
        }
    }
}

// LED 闪烁任务
void led_task(void *pvParameters) {
    while (1) {
        gpio_set_level(LED_PIN, 1);
        vTaskDelay(pdMS_TO_TICKS(500));
        gpio_set_level(LED_PIN, 0);
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void app_main() {
    sensor_queue = xQueueCreate(10, sizeof(float));

    xTaskCreate(sensor_task, "sensor", 4096, NULL, 2, NULL);
    xTaskCreate(upload_task, "upload", 4096, NULL, 1, NULL);
    xTaskCreate(led_task, "led", 2048, NULL, 0, NULL);
}
```

### 4.2 任务优先级设计

| 任务       | 优先级 | 周期  | 说明               |
| :--------- | :----- | :---- | :----------------- |
| 安全监控   | 最高   | 10ms  | 紧急停止、过温保护 |
| 传感器采集 | 高     | 100ms | 数据采集           |
| 通信上报   | 中     | 1s    | MQTT 数据上报      |
| 显示更新   | 低     | 100ms | UI 刷新            |
| 系统维护   | 最低   | 10s   | 看门狗、日志       |

## 5. 低功耗设计

### 5.1 功耗模式

| 模式            | 电流      | 唤醒方式         | 适用场景 |
| :-------------- | :-------- | :--------------- | :------- |
| **Active**      | 100-240mA | -                | 正常运行 |
| **Light Sleep** | 0.8mA     | GPIO/Timer       | 短暂空闲 |
| **Deep Sleep**  | 10μA      | GPIO/Timer/Touch | 长期待机 |
| **Power Off**   | ~1μA      | 复位             | 极低功耗 |

### 5.2 Deep Sleep 示例

```cpp
// ESP32 Deep Sleep 低功耗采集
#define uS_TO_S_FACTOR 1000000ULL
#define TIME_TO_SLEEP  300  // 5分钟

RTC_DATA_ATTR int bootCount = 0;  // RTC 内存保持

void setup() {
    Serial.begin(115200);
    bootCount++;
    Serial.printf("Boot #%d\n", bootCount);

    // 1. 唤醒后快速采集数据
    float temp = read_temperature();
    float humi = read_humidity();

    // 2. 连接 WiFi 并上报
    connect_wifi();
    mqtt_publish(temp, humi);

    // 3. 断开连接
    WiFi.disconnect(true);
    WiFi.mode(WIFI_OFF);

    // 4. 进入 Deep Sleep
    esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
    esp_deep_sleep_start();
}

void loop() {
    // Deep Sleep 后不会执行到这里
}
```

### 5.3 低功耗策略

| 策略         | 描述                 | 节电效果 |
| :----------- | :------------------- | :------- |
| **间歇工作** | 周期性唤醒采集       | 90-99%   |
| **降低频率** | 降低 CPU 主频        | 30-50%   |
| **关闭外设** | 不用时关闭 Wi-Fi/BLE | 60-80%   |
| **数据压缩** | 减少传输数据量       | 10-30%   |
| **批量传输** | 积攒后一次发送       | 20-40%   |

## 6. 小结

传感器与嵌入式是 IoT 的硬件基础：

1. **传感器选型**需考虑精度、功耗、接口和成本
2. **ESP32** 是 IoT 开发的首选 MCU，内置 Wi-Fi/BLE，生态丰富
3. **I2C** 适合连接传感器，**SPI** 适合高速设备，**UART** 适合调试和 GPS
4. **FreeRTOS** 是嵌入式实时系统的标准，多任务协作提高效率
5. **Deep Sleep** 是电池供电设备的关键，可将功耗降至 μA 级
6. 低功耗设计需从硬件选型、软件策略和通信协议三方面综合考虑
## DHT22 温湿度

**基本写法：包含 DHT 库**
`#include <DHT.h>`
```cpp
// 引入 Adafruit DHT 传感器库
#include <DHT.h>
```

---

**基本写法：初始化 DHT**
`DHT <名称>(<引脚>, <型号>);`
```cpp
// GPIO4 上接 DHT22
DHT dht(4, DHT22);
```

---

**基本写法：开始采集**
`<名称>.begin();`
```cpp
// 在 setup 中初始化传感器
dht.begin();
```

---

**基本写法：读取温度**
`<名称>.readTemperature()`
```cpp
// 返回摄氏温度
float t = dht.readTemperature();
```

---

**基本写法：读取湿度**
`<名称>.readHumidity()`
```cpp
// 返回相对湿度百分比
float h = dht.readHumidity();
```

---

**基本写法：检查读取失败**
```cpp
// 判断是否为 NaN 读取失败
if (isnan(t) || isnan(h)) {
  Serial.println("Failed to read DHT");
}
```

---

## BME280 温湿度气压

**基本写法：包含 BME280 库**
`#include <Adafruit_BME280.h>`
```cpp
// 引入 BME280 库
#include <Adafruit_BME280.h>
```

---

**基本写法：初始化 BME280**
`<名称>.begin(<I2C 地址>);`
```cpp
// 默认地址 0x76 或 0x77
Adafruit_BME280 bme;
bool ok = bme.begin(0x76);
```

---

**基本写法：读取气压**
`<名称>.readPressure()`
```cpp
// 返回气压 Pa
float p = bme.readPressure();
```

---

**基本写法：读取海拔**
`<名称>.readAltitude(<海平面气压>);`
```cpp
// 计算海拔米
float alt = bme.readAltitude(1013.25);
```

---

## DS18B20 单总线温度

**基本写法：包含 OneWire 与 DallasTemperature**
```cpp
// 引入单总线与 Dallas 温度库
#include <OneWire.h>
#include <DallasTemperature.h>
```

---

**基本写法：初始化 DS18B20**
```cpp
// GPIO5 接 DS18B20 数据线
OneWire oneWire(5);
DallasTemperature sensors(&oneWire);
sensors.begin();
```

---

**基本写法：请求温度转换**
`<名称>.requestTemperatures();`
```cpp
// 向所有传感器请求温度
sensors.requestTemperatures();
```

---

**基本写法：读取温度**
`<名称>.getTempCByIndex(<索引>)`
```cpp
// 读取第 0 个传感器温度
float t = sensors.getTempCByIndex(0);
```

---

**基本写法：按地址读取**
`<名称>.getTempC(<地址数组>)`
```cpp
// 通过 8 字节 ROM 地址读取
DeviceAddress addr;
sensors.getAddress(addr, 0);
float t = sensors.getTempC(addr);
```

---

## 光敏传感器

**基本写法：模拟读取光强**
`analogRead(<引脚>)`
```cpp
// 读取 GPIO32 光敏电阻值 0-4095
int light = analogRead(32);
```

---

**基本写法：转换为 lux**
```cpp
// 简单映射到 0-1000 lux
float lux = map(light, 0, 4095, 0, 1000);
```

---

**基本写法：判断明暗**
```cpp
// 阈值判断白天黑夜
if (light < 1000) {
  Serial.println("Dark");
} else {
  Serial.println("Bright");
}
```

---

## 土壤湿度传感器

**基本写法：模拟读取土壤湿度**
`analogRead(<引脚>)`
```cpp
// 读取 GPIO33 土壤湿度
int moisture = analogRead(33);
```

---

**基本写法：标定并换算百分比**
```cpp
// 通过标定值映射到 0-100%
int dry = 4095;
int wet = 1500;
int pct = map(moisture, dry, wet, 0, 100);
pct = constrain(pct, 0, 100);
```

---

**基本写法：电容式传感器读取**
```cpp
// 电容式土壤湿度需更长稳定时间
int moisture = analogRead(33);
delay(100);
```

---

## 超声波测距 HC-SR04

**基本写法：定义触发与回响引脚**
```cpp
// 触发接 GPIO5 回响接 GPIO18
#define TRIG 5
#define ECHO 18
pinMode(TRIG, OUTPUT);
pinMode(ECHO, INPUT);
```

---

**基本写法：发送触发脉冲**
```cpp
// 10 微秒高电平触发测距
digitalWrite(TRIG, LOW);
delayMicroseconds(2);
digitalWrite(TRIG, HIGH);
delayMicroseconds(10);
digitalWrite(TRIG, LOW);
```

---

**基本写法：读取距离**
```cpp
// 通过回响高电平时长计算距离
long duration = pulseIn(ECHO, HIGH);
float distance = duration * 0.034 / 2;
```

---

**基本写法：过滤无效读数**
```cpp
// 过滤超出范围的读数
if (distance < 2 || distance > 400) {
  return -1;
}
```

---

## PIR 人体感应

**基本写法：配置 PIR 引脚**
`pinMode(<引脚>, INPUT);`
```cpp
// GPIO14 接 PIR 输出
pinMode(14, INPUT);
```

---

**基本写法：读取 PIR 状态**
`digitalRead(<引脚>)`
```cpp
// 检测到人体返回 HIGH
int motion = digitalRead(14);
```

---

**基本写法：中断方式检测**
```cpp
// 通过中断实时响应
attachInterrupt(14, motionISR, RISING);
volatile bool motionDetected = false;
void motionISR() {
  motionDetected = true;
}
```

---

## 继电器控制

**基本写法：配置继电器引脚**
`pinMode(<引脚>, OUTPUT);`
```cpp
// GPIO26 控制继电器
pinMode(26, OUTPUT);
```

---

**基本写法：打开继电器**
`digitalWrite(<引脚>, HIGH);`
```cpp
// 高电平触发继电器吸合
digitalWrite(26, HIGH);
```

---

**基本写法：关闭继电器**
`digitalWrite(<引脚>, LOW);`
```cpp
// 低电平释放继电器
digitalWrite(26, LOW);
```

---

## MQ-2 气体检测

**基本写法：读取模拟气体值**
`analogRead(<引脚>)`
```cpp
// 读取 GPIO35 MQ-2 气体浓度
int gas = analogRead(35);
```

---

**基本写法：设置阈值告警**
```cpp
// 超过阈值判定为泄漏
if (gas > 2000) {
  Serial.println("Gas leak detected");
}
```

---

**基本写法：预热读取**
```cpp
// MQ-2 上电需预热 1-3 分钟
unsigned long start = millis();
while (millis() - start < 180000) {
  delay(1000);
}
```

---

## 数据上报

**基本写法：周期性上报**
```cpp
// 每 60 秒读取并上报一次
unsigned long last = 0;
if (millis() - last >= 60000) {
  last = millis();
  float t = dht.readTemperature();
  publishSensor(t);
}
```

---

**基本写法：JSON 格式封装**
```cpp
// 将多传感器数据打包为 JSON
String json = "{";
json += "\"temp\":" + String(t) + ",";
json += "\"hum\":" + String(h) + ",";
json += "\"light\":" + String(light);
json += "}";
```

---

**基本写法：MQTT 上报**
```cpp
// 通过 PubSubClient 上报传感器数据
#include <PubSubClient.h>
client.publish("sensor/esp32-001", json.c_str());
```

---

## 数据校准

**基本写法：多点标定**
```cpp
// 通过两点线性标定
float raw = analogRead(32);
float calibrated = (raw - rawLow) * (refHigh - refLow) / (rawHigh - rawLow) + refLow;
```

---

**基本写法：滑动平均滤波**
```cpp
// 滑动窗口平均减少抖动
const int N = 10;
int readings[N];
int idx = 0;
long total = 0;
total -= readings[idx];
readings[idx] = analogRead(32);
total += readings[idx];
idx = (idx + 1) % N;
float avg = total / (float)N;
```

---

**基本写法：剔除异常值**
```cpp
// 剔除超出合理范围的异常值
float value = readSensor();
if (value < MIN_VALID || value > MAX_VALID) {
  return lastValid;
}
lastValid = value;
```



<!-- ============ 文档分隔线：035-iot/003-CommunicationProtocol.md ============ -->



## 1. MQTT

### 1.1 协议概述

MQTT（Message Queuing Telemetry Transport）是 IoT 最广泛使用的**发布/订阅**消息协议，轻量、可靠、支持弱网络。

| 特性         | 描述                                        |
| :----------- | :------------------------------------------ |
| **协议层级** | 应用层（基于 TCP）                          |
| **消息模型** | 发布/订阅（Pub/Sub）                        |
| **最小报文** | 2 字节                                      |
| **QoS 等级** | 0（最多一次）/ 1（至少一次）/ 2（恰好一次） |
| **适用场景** | 设备上报、命令下发、状态同步                |

### 1.2 核心概念

```mermaid
flowchart LR
    P[Publisher 传感器] -->|publish| B[Broker 服务器<br/>Topic: iot/sensor/temp] -->|push| S[Subscriber 应用]
```

| 概念       | 描述                       |
| :--------- | :------------------------- |
| **Broker** | 消息代理服务器             |
| **Topic**  | 消息主题（层级结构）       |
| **Client** | 发布者或订阅者             |
| **QoS**    | 服务质量等级               |
| **Retain** | 保留最后一条消息           |
| **Will**   | 遗嘱消息（异常断开时发送） |

### 1.3 Topic 设计

```
# 推荐的 Topic 层级结构
iot/{product_id}/{device_id}/event/{event_type}    # 设备事件上报
iot/{product_id}/{device_id}/property/{prop_name}  # 属性上报
iot/{product_id}/{device_id}/command/{cmd_type}    # 命令下发
iot/{product_id}/{device_id}/status                # 设备状态

# 示例
iot/sensor-hub/device-001/event/temperature        # 温度事件
iot/sensor-hub/device-001/property/humidity         # 湿度属性
iot/sensor-hub/device-001/command/reboot            # 重启命令
iot/sensor-hub/device-001/status                    # 在线状态

# 通配符
iot/sensor-hub/+/event/temperature    # + 匹配单层
iot/sensor-hub/device-001/#           # # 匹配多层
```

### 1.4 Python MQTT 客户端

```python
import paho.mqtt.client as mqtt
import json
import time

class IoTSensor:
    def __init__(self, device_id, broker="broker.emqx.io", port=1883):
        self.device_id = device_id
        self.client = mqtt.Client(client_id=device_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

        # 遗嘱消息
        self.client.will_set(
            f"iot/sensor/{device_id}/status",
            payload=json.dumps({"status": "offline"}),
            qos=1,
            retain=True
        )

        self.client.connect(broker, port, 60)
        self.client.loop_start()

    def _on_connect(self, client, userdata, flags, rc):
        print(f"Connected with code {rc}")
        # 上报在线状态
        client.publish(
            f"iot/sensor/{self.device_id}/status",
            json.dumps({"status": "online"}),
            qos=1, retain=True
        )
        # 订阅命令 Topic
        client.subscribe(f"iot/sensor/{self.device_id}/command/#", qos=1)

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload.decode())
        print(f"Command: {topic} -> {payload}")

        if "reboot" in topic:
            self._handle_reboot(payload)
        elif "config" in topic:
            self._handle_config(payload)

    def publish_data(self, data: dict, qos=1):
        """上报传感器数据"""
        topic = f"iot/sensor/{self.device_id}/event/data"
        self.client.publish(topic, json.dumps(data), qos=qos)

    def _handle_reboot(self, payload):
        print(f"Rebooting... {payload}")

    def _handle_config(self, payload):
        print(f"Updating config: {payload}")

# 使用
sensor = IoTSensor("sensor-001")
while True:
    data = {
        "temperature": 25.5,
        "humidity": 60.2,
        "timestamp": int(time.time())
    }
    sensor.publish_data(data)
    time.sleep(5)
```

### 1.5 MQTT 5.0 新特性

| 特性                       | 描述                    |
| :------------------------- | :---------------------- |
| **Reason Code**            | 更详细的错误码          |
| **Session/Message Expiry** | 会话和消息过期          |
| **Shared Subscription**    | 负载均衡订阅            |
| **Topic Alias**            | 减少 Topic 名称传输     |
| **User Property**          | 自定义键值对            |
| **Flow Control**           | 流控（Receive Maximum） |

## 2. CoAP

### 2.1 协议概述

CoAP（Constrained Application Protocol）是专为**资源受限设备**设计的 Web 协议，基于 UDP。

| 特性         | MQTT     | CoAP             |
| :----------- | :------- | :--------------- |
| **传输层**   | TCP      | UDP              |
| **模型**     | Pub/Sub  | Request/Response |
| **最小报文** | 2B       | 4B               |
| **发现**     | 无       | 支持             |
| **适用**     | 事件驱动 | 资源访问         |

### 2.2 CoAP 请求

```python
# aiocoap 客户端
import asyncio
from aiocoap import *

async def coap_get():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://[::1]/sensors/temperature')
    response = await protocol.request(request).response
    print(f"Temperature: {response.payload.decode()}")

async def coap_observe():
    """观察模式（类似订阅）"""
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://[::1]/sensors/temperature', observe=0)
    observation = await protocol.request(request).observation
    async for response in observation:
        print(f"Update: {response.payload.decode()}")

asyncio.run(coap_get())
```

## 3. LoRa / LoRaWAN

### 3.1 LoRa 物理层

| 参数     | 描述                                           |
| :------- | :--------------------------------------------- |
| **频段** | 470MHz（中国）/ 868MHz（欧洲）/ 915MHz（美国） |
| **速率** | 0.3-50 kbps                                    |
| **距离** | 城区 2-5km，郊区 15km                          |
| **功耗** | 发射 ~45mA，睡眠 ~1μA                          |

### 3.2 LoRaWAN 架构

```mermaid
flowchart LR
    D[终端设备] -->|LoRa| G[网关 Gateway] -->|IP| NS[网络服务器 NS]
    NS --> AS[应用服务器 AS]
    NS --> JS[加入服务器 JS]
```

### 3.3 LoRaWAN 设备类别

| 类别        | 接收窗口   | 功耗 | 适用场景       |
| :---------- | :--------- | :--- | :------------- |
| **Class A** | 上行后开启 | 最低 | 电池供电传感器 |
| **Class B** | 定时开启   | 中   | 需要定时下发   |
| **Class C** | 持续开启   | 最高 | 常电设备       |

### 3.4 LoRaWAN 数据上报

```cpp
// LMIC LoRaWAN 上报示例（Arduino）
#include <lmic.h>
#include <hal/hal.h>

void onEvent(ev_t ev) {
    switch (ev) {
        case EV_TXCOMPLETE:
            Serial.println("TX complete");
            // 进入低功耗
            break;
        case EV_JOINING:
            Serial.println("Joining...");
            break;
        case EV_JOINED:
            Serial.println("Joined!");
            break;
    }
}

void do_send(osjob_t* j) {
    uint8_t payload[4];
    int16_t temp = (int16_t)(read_temperature() * 100);
    payload[0] = temp >> 8;
    payload[1] = temp & 0xFF;
    // ... 其他数据

    LMIC_setTxData2(1, payload, sizeof(payload), 0);
}

void setup() {
    os_init();
    LMIC_reset();
    LMIC_startJoining();
    do_send(&sendjob);
}

void loop() {
    os_runloop_once();
}
```

## 4. NB-IoT

### 4.1 特性

| 特性       | 描述                       |
| :--------- | :------------------------- |
| **技术**   | 蜂窝网络（LTE 简化版）     |
| **速率**   | 上行 ~60kbps，下行 ~30kbps |
| **覆盖**   | 比 GSM 增强 20dB           |
| **连接数** | 单小区 10 万+              |
| **功耗**   | PSM 模式 ~5μA              |
| **运营商** | 中国电信/移动/联通         |

### 4.2 NB-IoT AT 命令

```c
// NB-IoT 模组 AT 命令操作
// 1. 检查模块
AT                           // → OK
AT+CGMI                      // → 厂商信息
AT+CSQ                       // → 信号质量

// 2. 网络注册
AT+CGATT=1                   // 附着网络
AT+CGDCONT=1,"IP","CTNB"     // 设置 APN
AT+CEREG?                    // 查询注册状态

// 3. 创建连接
AT+NSOCR="STREAM",6,8883,1   // 创建 TCP socket

// 4. 发送数据
AT+NSOSD=1,12,"48656C6C6F"   // 发送十六进制数据

// 5. PSM 低功耗
AT+CPSMS=1,"","00000100","00000001"  // 进入 PSM
```

## 5. Zigbee

### 5.1 特性

| 特性       | 描述                 |
| :--------- | :------------------- |
| **频段**   | 2.4GHz               |
| **速率**   | 250kbps              |
| **距离**   | 10-100m              |
| **节点数** | 理论 65535           |
| **拓扑**   | 星型/树型/网状       |
| **功耗**   | 极低（纽扣电池数年） |

### 5.2 Zigbee 设备类型

| 类型            | 描述               | 供电 |
| :-------------- | :----------------- | :--- |
| **Coordinator** | 网络协调者         | 常电 |
| **Router**      | 路由节点，转发数据 | 常电 |
| **End Device**  | 终端设备           | 电池 |

### 5.3 Zigbee2MQTT

```yaml
# Zigbee2MQTT 配置
mqtt:
  base_topic: zigbee2mqtt
  server: mqtt://localhost:1883

serial:
  port: /dev/ttyUSB0

devices:
  '0x00158d0004567890':
    friendly_name: living_room_temp
  '0x00158d0004567891':
    friendly_name: bedroom_light

advanced:
  network_key: GENERATE
  channel: 25
```

## 6. BLE（低功耗蓝牙）

### 6.1 BLE 版本

| 版本    | 速率  | 特点               |
| :------ | :---- | :----------------- |
| BLE 4.0 | 1Mbps | 基础版             |
| BLE 4.2 | 1Mbps | 数据长度扩展       |
| BLE 5.0 | 2Mbps | 2倍速率、4倍距离   |
| BLE 5.3 | 2Mbps | 周期广播、信道分类 |

### 6.2 BLE GATT 服务

```cpp
// ESP32 BLE 传感器服务
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

#define SERVICE_UUID        "181A"  // Environmental Sensing
#define TEMP_CHAR_UUID      "2A6E"  // Temperature
#define HUMI_CHAR_UUID      "2A6F"  // Humidity

BLEServer* pServer = NULL;
BLECharacteristic* pTempChar = NULL;
BLECharacteristic* pHumiChar = NULL;

void setup() {
    BLEDevice::init("ESP32-Sensor");
    pServer = BLEDevice::createServer();

    BLEService* pService = pServer->createService(SERVICE_UUID);

    pTempChar = pService->createCharacteristic(
        TEMP_CHAR_UUID,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
    );

    pHumiChar = pService->createCharacteristic(
        HUMI_CHAR_UUID,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
    );

    pService->start();
    BLEAdvertising* pAdvertising = BLEDevice::getAdvertising();
    pAdvertising->addServiceUUID(SERVICE_UUID);
    BLEDevice::startAdvertising();
}

void loop() {
    float temp = read_temperature();
    float humi = read_humidity();

    pTempChar->setValue((uint8_t*)&temp, sizeof(temp));
    pTempChar->notify();

    pHumiChar->setValue((uint8_t*)&humi, sizeof(humi));
    pHumiChar->notify();

    delay(1000);
}
```

## 7. 协议选型对比

| 维度     | MQTT | CoAP     | LoRaWAN | NB-IoT | Zigbee   | BLE    |
| :------- | :--- | :------- | :------ | :----- | :------- | :----- |
| **层级** | 应用 | 应用     | 网络    | 网络   | 网络     | 网络   |
| **传输** | TCP  | UDP      | LoRa    | 蜂窝   | 802.15.4 | 2.4GHz |
| **距离** | 不限 | 不限     | 15km    | 全国   | 100m     | 100m   |
| **功耗** | 中   | 低       | 极低    | 低     | 极低     | 低     |
| **速率** | 高   | 中       | 极低    | 低     | 低       | 中     |
| **成本** | 低   | 低       | 中      | 中     | 低       | 低     |
| **场景** | 通用 | 受限设备 | 远距离  | 广覆盖 | 智能家居 | 可穿戴 |

## 8. 小结

通信协议是 IoT 的神经网络：

1. **MQTT** 是 IoT 通信的事实标准，适合设备-云通信
2. **CoAP** 适合资源极度受限的设备，基于 UDP
3. **LoRaWAN** 适合远距离低功耗场景，但速率极低
4. **NB-IoT** 利用运营商网络，覆盖好但需资费
5. **Zigbee** 适合智能家居网状网络，通过 Zigbee2MQTT 桥接
6. **BLE** 适合近距离可穿戴和手机交互场景
7. 实际项目通常**组合使用**多种协议，如 LoRa + MQTT、BLE + Wi-Fi



<!-- ============ 文档分隔线：035-iot/004-EdgeComputing.md ============ -->



## 1. 边缘计算架构

### 1.1 为什么需要边缘计算

| 挑战       | 云计算   | 边缘计算         |
| :--------- | :------- | :--------------- |
| **延迟**   | 50-200ms | 1-10ms           |
| **带宽**   | 高成本   | 本地处理减少传输 |
| **隐私**   | 数据上云 | 数据本地处理     |
| **可靠性** | 依赖网络 | 离线可用         |
| **实时性** | 不确定   | 确定性延迟       |

### 1.2 三层架构

```mermaid
flowchart LR
    C[云端<br/>模型训练 全局分析 长期存储<br/>分钟/小时级] <-->|模型/策略| E[边缘层<br/>数据预处理 AI 推理 规则引擎<br/>毫秒/秒级] <-->|采集/控制| D[设备层<br/>传感器 执行器 MCU<br/>实时]
```

### 1.3 边缘节点类型

| 类型       | 算力 | 示例           | 用途               |
| :--------- | :--- | :------------- | :----------------- |
| **薄边缘** | 低   | 树莓派、网关   | 协议转换、简单过滤 |
| **厚边缘** | 中   | 工控机、Jetson | AI 推理、数据聚合  |
| **微边缘** | 极低 | 边缘MCU        | 实时控制、数据采集 |

## 2. 边缘节点部署

### 2.1 k3s（轻量级 Kubernetes）

```bash
# 安装 k3s Server
curl -sfL https://get.k3s.io | sh -s - server \
  --tls-san=edge-server.local \
  --datastore-endpoint="mysql://user:pass@tcp(db:3306)/k3s"

# 获取 Token
cat /var/lib/rancher/k3s/server/node-token

# 在边缘节点安装 Agent
curl -sfL https://get.k3s.io | K3S_URL=https://edge-server:6443 \
  K3S_TOKEN=<token> sh -

# 查看节点
kubectl get nodes
```

### 2.2 KubeEdge

```bash
# Cloud 端安装
keadm init --advertise-address=cloud-ip

# 获取 Token
keadm gettoken

# Edge 端安装
keadm join --cloudcore-ipport=cloud-ip:10000 \
  --token=<token> \
  --edgenode-name=edge-node-1
```

### 2.3 边缘应用部署

```yaml
# 边缘节点标签
kubectl label node edge-node-1 node-type=edge location=factory-a

# 边缘部署（仅调度到边缘节点）
apiVersion: apps/v1
kind: Deployment
metadata:
  name: edge-gateway
spec:
  replicas: 1
  selector:
    matchLabels:
      app: edge-gateway
  template:
    metadata:
      labels:
        app: edge-gateway
    spec:
      nodeSelector:
        node-type: edge
      containers:
      - name: gateway
        image: myregistry/edge-gateway:v1
        env:
        - name: MQTT_BROKER
          value: "mqtt://localhost:1883"
        - name: CLOUD_ENDPOINT
          value: "https://cloud.example.com/api"
        resources:
          limits:
            cpu: "1"
            memory: 512Mi
        volumeMounts:
        - name: config
          mountPath: /app/config
      volumes:
      - name: config
        configMap:
          name: edge-config
```

## 3. 数据预处理

### 3.1 边缘数据流水线

```python
# 边缘数据预处理
import json
from collections import deque
from datetime import datetime

class EdgeDataProcessor:
    def __init__(self, window_size=60, sample_rate=5):
        self.window_size = window_size
        self.sample_rate = sample_rate
        self.data_buffer = deque(maxlen=window_size)
        self.last_upload = 0

    def process(self, raw_data: dict) -> dict | None:
        """处理单条传感器数据"""
        # 1. 数据清洗
        cleaned = self._clean(raw_data)
        if not cleaned:
            return None

        # 2. 添加到缓冲区
        self.data_buffer.append(cleaned)

        # 3. 异常检测
        if self._is_anomaly(cleaned):
            return {"type": "alert", "data": cleaned}

        # 4. 降采样（减少上传频率）
        if len(self.data_buffer) % self.sample_rate != 0:
            return None

        # 5. 聚合上传
        return self._aggregate()

    def _clean(self, data: dict) -> dict | None:
        """数据清洗"""
        # 去除超出范围的数据
        if not (-40 <= data.get("temperature", 0) <= 80):
            return None
        if not (0 <= data.get("humidity", 0) <= 100):
            return None
        return data

    def _is_anomaly(self, data: dict) -> bool:
        """简单异常检测"""
        if len(self.data_buffer) < 10:
            return False
        recent = list(self.data_buffer)[-10:]
        avg_temp = sum(d["temperature"] for d in recent) / len(recent)
        return abs(data["temperature"] - avg_temp) > 15

    def _aggregate(self) -> dict:
        """数据聚合"""
        data_list = list(self.data_buffer)
        temps = [d["temperature"] for d in data_list]
        humis = [d["humidity"] for d in data_list]

        return {
            "type": "aggregate",
            "count": len(data_list),
            "temperature": {
                "avg": sum(temps) / len(temps),
                "min": min(temps),
                "max": max(temps)
            },
            "humidity": {
                "avg": sum(humis) / len(humis),
                "min": min(humis),
                "max": max(humis)
            },
            "timestamp": datetime.now().isoformat()
        }
```

## 4. AI 推理

### 4.1 TensorFlow Lite

```python
# 边缘 AI 推理
import tflite_runtime.interpreter as tflite
import numpy as np

class EdgeAI:
    def __init__(self, model_path: str):
        self.interpreter = tflite.Interpreter(
            model_path=model_path,
            num_threads=4
        )
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def predict(self, input_data: np.ndarray) -> np.ndarray:
        """执行推理"""
        self.interpreter.set_tensor(
            self.input_details[0]['index'], input_data
        )
        self.interpreter.invoke()
        return self.interpreter.get_tensor(
            self.output_details[0]['index']
        )

# 异常检测模型推理
model = EdgeAI("anomaly_detection.tflite")

# 传感器数据 → 特征 → 推理
sensor_window = np.array([...], dtype=np.float32).reshape(1, -1)
result = model.predict(sensor_window)
is_anomaly = result[0][0] > 0.5
```

### 4.2 ONNX Runtime

```python
import onnxruntime as ort
import numpy as np

class ONNXInference:
    def __init__(self, model_path: str):
        # 优化边缘推理
        sess_options = ort.SessionOptions()
        sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        sess_options.intra_op_num_threads = 4

        self.session = ort.InferenceSession(
            model_path,
            sess_options,
            providers=['CPUExecutionProvider']
        )

    def predict(self, input_data: np.ndarray) -> np.ndarray:
        input_name = self.session.get_inputs()[0].name
        output = self.session.run(None, {input_name: input_data})
        return output[0]
```

### 4.3 模型优化

| 技术             | 描述               | 精度损失 | 加速比 |
| :--------------- | :----------------- | :------- | :----- |
| **量化（INT8）** | FP32 → INT8        | 1-3%     | 2-4x   |
| **剪枝**         | 移除冗余参数       | 1-5%     | 1.5-3x |
| **蒸馏**         | 大模型教小模型     | 2-5%     | 3-10x  |
| **TFLite 转换**  | 优化为 TFLite 格式 | <1%      | 1.5-2x |

```python
# TFLite 量化转换
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model("saved_model")
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # 动态量化
converter.target_spec.supported_types = [tf.float16]   # FP16 量化

tflite_model = converter.convert()
with open("model_quant.tflite", "wb") as f:
    f.write(tflite_model)
```

## 5. 雾计算

### 5.1 雾计算 vs 边缘计算

| 维度     | 边缘计算 | 雾计算        |
| :------- | :------- | :------------ |
| **位置** | 设备附近 | 网络中间层    |
| **节点** | 单一节点 | 多层节点      |
| **延迟** | 1-10ms   | 10-50ms       |
| **计算** | 有限     | 中等          |
| **典型** | 工控机   | 路由器/交换机 |

### 5.2 雾节点架构

```
终端设备 → 雾节点1(近端) → 雾节点2(中间) → 云端
  实时控制   本地过滤/聚合    区域分析      全局优化
```

## 6. 边云协同

### 6.1 协同模式

| 模式                   | 描述                       | 示例     |
| :--------------------- | :------------------------- | :------- |
| **边端推理，云端训练** | 边缘推理，云端训练模型     | 异常检测 |
| **边缘过滤，云端存储** | 边缘过滤无效数据           | 数据归档 |
| **边缘实时，云端批量** | 边缘实时响应，云端批量分析 | 预测维护 |
| **边缘自治，云端同步** | 断网时边缘自治             | 远程站点 |

### 6.2 模型更新流程

```
云端训练新模型 → 模型压缩/量化 → 推送到边缘节点
    → 灰度验证 → 全量替换 → 反馈效果 → 云端迭代
```

```python
# 边缘模型热更新
class ModelManager:
    def __init__(self, model_dir="/models"):
        self.model_dir = model_dir
        self.current_version = 0
        self.model = None

    def load_model(self, version: int):
        path = f"{self.model_dir}/model_v{version}.tflite"
        self.model = EdgeAI(path)
        self.current_version = version

    def check_update(self):
        """检查云端是否有新模型"""
        response = requests.get(
            "https://cloud.example.com/api/model/latest",
            headers={"current_version": str(self.current_version)}
        )
        if response.status_code == 200:
            # 下载新模型
            model_data = response.content
            new_version = response.headers["model-version"]
            path = f"{self.model_dir}/model_v{new_version}.tflite"
            with open(path, "wb") as f:
                f.write(model_data)
            # 验证后切换
            self.load_model(int(new_version))
```

## 7. 边缘安全

### 7.1 安全挑战

| 挑战         | 描述             | 解决方案      |
| :----------- | :--------------- | :------------ |
| **物理安全** | 边缘设备易被接触 | TPM、安全启动 |
| **网络安全** | 边缘网络开放     | VPN、mTLS     |
| **数据安全** | 本地数据泄露     | 加密存储      |
| **更新安全** | 恶意模型注入     | 签名验证      |
| **访问控制** | 未经授权访问     | 证书认证      |

### 7.2 边缘安全架构

```python
# 边缘节点安全通信
import ssl
import paho.mqtt.client as mqtt

def create_secure_client(device_id, cert_path, key_path, ca_path):
    client = mqtt.Client(client_id=device_id)

    # TLS 配置
    context = ssl.create_default_context()
    context.load_verify_locations(ca_path)
    context.load_cert_chain(cert_path, key_path)
    context.verify_mode = ssl.CERT_REQUIRED

    client.tls_set_context(context)
    return client
```

## 8. 小结

边缘计算是 IoT 系统的关键中间层：

1. **边缘计算**解决延迟、带宽和隐私问题，是 IoT 的必选项
2. **k3s/KubeEdge** 将 K8s 能力延伸到边缘，统一管理云和边
3. **数据预处理**在边缘完成清洗、聚合和降采样，减少云端压力
4. **AI 推理**通过 TFLite/ONNX 在边缘执行，实现实时智能决策
5. **边云协同**是最佳实践，边缘负责实时，云端负责全局
6. **模型热更新**使边缘 AI 持续进化，无需停机



<!-- ============ 文档分隔线：035-iot/005-IoT.md ============ -->



## 1. IoT 平台概述

### 1.1 核心功能

| 功能         | 描述                         |
| :----------- | :--------------------------- |
| **设备管理** | 设备注册、认证、生命周期管理 |
| **数据接入** | MQTT/HTTP/CoAP 协议接入      |
| **规则引擎** | 数据流转、条件触发           |
| **数据存储** | 时序数据、设备影子           |
| **消息推送** | 命令下发、属性设置           |
| **监控告警** | 设备状态监控、异常告警       |

### 1.2 平台选型

| 平台              | 类型   | 特点               | 适用场景   |
| :---------------- | :----- | :----------------- | :--------- |
| **AWS IoT Core**  | 云服务 | 全球部署、生态完善 | 海外业务   |
| **Azure IoT Hub** | 云服务 | 企业集成、安全     | 微软生态   |
| **阿里云 IoT**    | 云服务 | 中文友好、国内合规 | 国内业务   |
| **ThingsBoard**   | 开源   | 可私有化、功能全   | 中小企业   |
| **EMQX**          | 开源   | MQTT 专用、高性能  | 消息中间件 |

## 2. AWS IoT Core

### 2.1 核心组件

| 组件               | 描述               |
| :----------------- | :----------------- |
| **Device Gateway** | MQTT/HTTP 接入网关 |
| **Rules Engine**   | SQL 风格规则引擎   |
| **Device Shadow**  | 设备状态同步       |
| **Registry**       | 设备注册表         |
| **Security**       | X.509 证书认证     |

### 2.2 设备连接

```python
# AWS IoT Device SDK
import awsiot
from awsiot import mqtt_connection_builder

# 使用证书连接
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint="xxxxx-ats.iot.us-east-1.amazonaws.com",
    cert_filepath="device-certificate.pem.crt",
    pri_key_filepath="device-private-key.pem.key",
    ca_filepath="AmazonRootCA1.pem",
    client_id="my-device-001"
)

connect_future = mqtt_connection.connect()
connect_future.result()

# 发布消息
mqtt_connection.publish(
    topic="my-device-001/data",
    payload=json.dumps({"temperature": 25.5}),
    qos=mqtt.QoS.AT_LEAST_ONCE
)

# 订阅
def on_message(topic, payload, **kwargs):
    print(f"Received: {payload}")

mqtt_connection.subscribe(
    topic="my-device-001/command",
    qos=mqtt.QoS.AT_LEAST_ONCE,
    callback=on_message
)
```

### 2.3 规则引擎

```sql
-- AWS IoT 规则：将温度数据写入 DynamoDB
SELECT device_id, temperature, timestamp
FROM 'iot/+/data'
WHERE temperature > 30

-- 动作：
-- 1. 写入 DynamoDB
-- 2. 发送 SNS 通知
-- 3. 调用 Lambda 函数
```

### 2.4 Device Shadow

```json
// 设备影子（期望状态 vs 报告状态）
{
  "state": {
    "desired": {
      "led": "on",
      "interval": 10
    },
    "reported": {
      "led": "off",
      "interval": 5,
      "temperature": 25.5
    }
  },
  "metadata": {
    "desired": {
      "led": { "timestamp": 1718300000 },
      "interval": { "timestamp": 1718300000 }
    }
  },
  "version": 5,
  "timestamp": 1718300100
}
```

## 3. Azure IoT Hub

### 3.1 核心功能

```python
# Azure IoT Device SDK
from azure.iot.device import IoTHubDeviceClient, Message

# 连接字符串
conn_str = "HostName=my-hub.azure-devices.net;DeviceId=device-001;SharedAccessKey=xxx"
client = IoTHubDeviceClient.create_from_connection_string(conn_str)

client.connect()

# 发送遥测数据
message = Message(json.dumps({"temperature": 25.5}))
message.content_type = "application/json"
client.send_message(message)

# 接收云端命令
def message_handler(message):
    print(f"Command: {message.data}")

client.on_message_received = message_handler
```

### 3.2 IoT Edge

```json
// deployment.json - 边缘模块部署
{
  "modulesContent": {
    "$edgeAgent": {
      "properties.desired": {
        "modules": {
          "tempSensor": {
            "settings": {
              "image": "mcr.microsoft.com/azureiotedge-simulated-temperature-sensor:1.0",
              "createOptions": "{}"
            }
          },
          "edgeAI": {
            "settings": {
              "image": "myregistry/edge-ai:v1",
              "createOptions": "{\"HostConfig\":{\"PortBindings\":{\"5000/tcp\":[{\"HostPort\":\"5000\"}]}}}"
            }
          }
        }
      }
    }
  }
}
```

## 4. 阿里云 IoT

### 4.1 平台架构

```
设备 → MQTT/HTTP → IoT 接入层 → 规则引擎 → 数据流转
                                    ↓
                              设备管理/物模型
```

### 4.2 物模型（Thing Model）

```json
{
  "productKey": "a1BcDEfG",
  "deviceName": "sensor-001",
  "properties": [
    {
      "identifier": "Temperature",
      "name": "温度",
      "dataType": "float",
      "accessMode": "r",
      "unit": "°C",
      "range": [-40, 80]
    },
    {
      "identifier": "Humidity",
      "name": "湿度",
      "dataType": "float",
      "accessMode": "r",
      "unit": "%",
      "range": [0, 100]
    },
    {
      "identifier": "Switch",
      "name": "开关",
      "dataType": "bool",
      "accessMode": "rw"
    }
  ],
  "services": [
    {
      "identifier": "Reboot",
      "name": "重启",
      "inputData": [],
      "outputData": []
    }
  ],
  "events": [
    {
      "identifier": "HighTemp",
      "name": "高温告警",
      "type": "alert",
      "outputData": [{ "identifier": "Temperature", "name": "温度" }]
    }
  ]
}
```

### 4.3 设备端 SDK

```python
# 阿里云 IoT Device SDK
import linkkit

lk = linkkit.LinkKit(
    host_name="iot-as-mqtt.cn-shanghai.aliyuncs.com",
    product_key="a1BcDEfG",
    device_name="sensor-001",
    device_secret="xxx"
)

# 属性上报
def on_connect(session):
    props = {"Temperature": 25.5, "Humidity": 60.2}
    lk.thing_post_property(props)

# 命令接收
def on_thing_call(session, identifier, params):
    if identifier == "Reboot":
        print("Rebooting...")
        lk.thing_answer_service(identifier, {"code": 200})

lk.on_connect = on_connect
lk.on_thing_call = on_thing_call
lk.connect()
```

## 5. ThingsBoard

### 5.1 部署

```yaml
# docker-compose.yml
version: '3.8'
services:
  thingsboard:
    image: thingsboard/tb-postgres:latest
    ports:
      - '9090:9090' # Web UI
      - '1883:1883' # MQTT
      - '7070:7070' # Edge RPC
      - '5683-5688:5683-5688/udp' # CoAP/LwM2M
    environment:
      TB_QUEUE_TYPE: in-memory
      SPRING_DATASOURCE_URL: 'jdbc:postgresql://postgres:5432/thingsboard'
    volumes:
      - tb-data:/data
      - tb-logs:/var/log/thingsboard

  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: thingsboard
      POSTGRES_USER: thingsboard
      POSTGRES_PASSWORD: thingsboard
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  tb-data:
  tb-logs:
  pgdata:
```

### 5.2 规则链

```
消息输入 → 消息类型切换 → 脚本处理 → 保存时序数据
                                ↓
                          条件判断 → 告警通知
                                ↓
                          数据转发 → Kafka/HTTP
```

### 5.3 设备接入

```python
# ThingsBoard MQTT 接入
import paho.mqtt.client as mqtt
import json
import time

THINGSBOARD_HOST = "localhost"
ACCESS_TOKEN = "your-device-token"

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

def on_connect(rc):
    print(f"Connected: {rc}")
    # 订阅命令
    client.subscribe("v1/devices/me/rpc/request/+")

def on_message(client, userdata, msg):
    request_id = msg.topic.split("/")[-1]
    data = json.loads(msg.payload.decode())
    print(f"RPC: {data}")

    # 响应 RPC
    response = {"result": "ok"}
    client.publish(
        f"v1/devices/me/rpc/response/{request_id}",
        json.dumps(response)
    )

client.on_connect = on_connect
client.on_message = on_message
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

# 遥测数据上报
while True:
    telemetry = {
        "temperature": 25.5,
        "humidity": 60.2
    }
    client.publish("v1/devices/me/telemetry", json.dumps(telemetry))

    # 属性上报
    attributes = {
        "firmware_version": "1.2.0",
        "location": "factory-a"
    }
    client.publish("v1/devices/me/attributes", json.dumps(attributes))

    time.sleep(5)
```

## 6. EMQX

### 6.1 部署

```bash
# Docker 部署
docker run -d \
  --name emqx \
  -p 1883:1883 \
  -p 8083:8083 \
  -p 8084:8084 \
  -p 8883:8883 \
  -p 18083:18083 \
  emqx/emqx:5.7
```

### 6.2 规则引擎

```sql
-- EMQX 规则：温度告警
SELECT
  payload.temperature as temp,
  payload.device_id as device_id,
  clientid,
  timestamp
FROM "iot/sensor/+/data"
WHERE payload.temperature > 35

-- 动作：发送到 Webhook
-- URL: https://alert.example.com/api/temperature-alert
-- Body: {"device_id": "${device_id}", "temperature": ${temp}, "time": ${timestamp}}
```

### 6.3 性能调优

| 参数                           | 默认值  | 建议值 | 说明           |
| :----------------------------- | :------ | :----- | :------------- |
| `listener.tcp.max_connections` | 1024000 | 按需   | 最大连接数     |
| `listener.tcp.backlog`         | 1024    | 4096   | 连接队列       |
| `zone.max_mqueue_len`          | 10000   | 50000  | 消息队列长度   |
| `zone.keepalive_multiplier`    | 1.5     | 1.5    | Keepalive 倍数 |

## 7. 设备管理

### 7.1 设备生命周期

```
注册 → 激活 → 在线 → 离线 → 禁用 → 删除
  │      │      │      │      │
  预注册  首次连接  正常运行  断网   异常设备
```

### 7.2 设备认证方式

| 方式           | 安全性 | 复杂度 | 适用场景   |
| :------------- | :----- | :----- | :--------- |
| **Token**      | 低     | 低     | 开发测试   |
| **X.509 证书** | 高     | 中     | 生产环境   |
| **一机一密**   | 中     | 低     | 大规模部署 |
| **一型一密**   | 中     | 低     | 同类设备   |

### 7.3 OTA 固件更新

```python
# OTA 更新流程
class OTAManager:
    def __init__(self, mqtt_client):
        self.client = mqtt_client
        self.current_version = "1.0.0"

    def check_update(self):
        """检查固件更新"""
        self.client.publish(
            "ota/check",
            json.dumps({"current_version": self.current_version})
        )

    def download_firmware(self, url: str, checksum: str):
        """下载固件"""
        import hashlib
        import requests

        response = requests.get(url, stream=True)
        firmware_data = b""
        for chunk in response.iter_content(chunk_size=8192):
            firmware_data += chunk

        # 校验
        actual = hashlib.sha256(firmware_data).hexdigest()
        if actual != checksum:
            raise ValueError("固件校验失败")

        # 写入
        with open("/tmp/firmware.bin", "wb") as f:
            f.write(firmware_data)

    def apply_update(self):
        """应用更新"""
        import subprocess
        result = subprocess.run(
            ["sysupgrade", "/tmp/firmware.bin"],
            capture_output=True
        )
        return result.returncode == 0
```

## 8. 小结

IoT 平台是连接设备和应用的桥梁：

1. **AWS/Azure IoT** 适合海外和大型企业，功能完善但成本较高
2. **阿里云 IoT** 国内首选，物模型设计规范，合规性好
3. **ThingsBoard** 开源可私有化，适合中小企业和定制需求
4. **EMQX** 是高性能 MQTT Broker，适合纯消息场景
5. **设备管理**需关注认证方式、生命周期和 OTA 更新
6. **规则引擎**是平台的核心，实现数据流转和业务逻辑



<!-- ============ 文档分隔线：035-iot/006-DataProcessingAnalysis.md ============ -->



## 1. IoT 数据特征

### 1.1 数据特点

| 特点           | 描述           | 影响         |
| :------------- | :------------- | :----------- |
| **时序性**     | 数据带时间戳   | 需时序数据库 |
| **高频**       | 传感器秒级上报 | 高写入吞吐   |
| **海量**       | 千万级设备     | 分布式存储   |
| **多源**       | 异构传感器     | 数据融合     |
| **低价值密度** | 大量正常数据   | 需过滤和分析 |

### 1.2 数据处理流水线

```
采集 → 传输 → 预处理 → 存储 → 分析 → 可视化
  │      │      │       │      │      │
  边缘   MQTT   边缘/云  TSDB  流/批  Grafana
```

## 2. 时序数据库

### 2.1 对比

| 数据库          | 写入性能 | 查询性能 | 压缩率 | 集群   | 特点              |
| :-------------- | :------- | :------- | :----- | :----- | :---------------- |
| **InfluxDB**    | 高       | 高       | 好     | 企业版 | 生态好、Flux 查询 |
| **TDengine**    | 很高     | 很高     | 很好   |        | 国产、超高性能    |
| **TimescaleDB** | 高       | 高       | 中     |        | 基于 PostgreSQL   |
| **QuestDB**     | 很高     | 很高     | 好     |        | SQL 兼容、零依赖  |
| **IoTDB**       | 高       | 高       | 好     |        | Apache、国产      |

### 2.2 InfluxDB

```python
# InfluxDB 写入和查询
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# 连接
client = InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org")
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

# 写入数据
point = Point("sensor_data") \
    .tag("device_id", "sensor-001") \
    .tag("location", "factory-a") \
    .field("temperature", 25.5) \
    .field("humidity", 60.2) \
    .time(datetime.utcnow(), WritePrecision.MS)

write_api.write(bucket="iot-bucket", record=point)

# 批量写入
points = []
for i in range(100):
    p = Point("sensor_data") \
        .tag("device_id", f"sensor-{i:03d}") \
        .field("temperature", 20 + i * 0.1) \
        .time(datetime.utcnow() + timedelta(seconds=i), WritePrecision.MS)
    points.append(p)

write_api.write(bucket="iot-bucket", record=points)

# 查询
query = '''
from(bucket: "iot-bucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "sensor_data")
  |> filter(fn: (r) => r.device_id == "sensor-001")
  |> filter(fn: (r) => r._field == "temperature")
  |> aggregateWindow(every: 5m, fn: mean)
'''

tables = query_api.query_data_frame(query)
print(tables)
```

### 2.3 TDengine

```sql
-- 创建数据库和超级表
CREATE DATABASE iot_db KEEP 3650 DAYS 10 BLOCKS 6;
USE iot_db;

-- 超级表（模板）
CREATE STABLE sensor_data (ts TIMESTAMP, temperature FLOAT, humidity FLOAT)
TAGS (device_id NCHAR(32), location NCHAR(64), product_key NCHAR(32));

-- 自动建表写入
INSERT INTO d001 USING sensor_data TAGS ("sensor-001", "factory-a", "pk001")
VALUES (NOW, 25.5, 60.2);

-- 查询
-- 最近1小时平均温度
SELECT _wstart, AVG(temperature)
FROM sensor_data
WHERE ts > NOW - 1h AND device_id = "sensor-001"
INTERVAL(5m);

-- 异常检测：超过 2σ 的数据
SELECT ts, temperature
FROM sensor_data
WHERE ABS(temperature - (SELECT AVG(temperature) FROM sensor_data WHERE ts > NOW - 1h)) >
      2 * (SELECT STDDEV(temperature) FROM sensor_data WHERE ts > NOW - 1h)
AND ts > NOW - 1h;

-- 降采样
SELECT _wstart, AVG(temperature) as avg_temp, MIN(temperature) as min_temp, MAX(temperature) as max_temp
FROM sensor_data
WHERE ts > NOW - 24h
INTERVAL(1h);
```

### 2.4 TimescaleDB

```sql
-- 创建超表
CREATE TABLE sensor_data (
    time        TIMESTAMPTZ NOT NULL,
    device_id   TEXT NOT NULL,
    temperature DOUBLE PRECISION,
    humidity    DOUBLE PRECISION,
    location    TEXT
);

SELECT create_hypertable('sensor_data', 'time',
    chunk_time_interval => INTERVAL '1 day'
);

-- 创建索引
CREATE INDEX idx_device ON sensor_data (device_id, time DESC);

-- 连续聚合（实时物化视图）
CREATE MATERIALIZED VIEW sensor_5min
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('5 minutes', time) AS bucket,
    device_id,
    AVG(temperature) AS avg_temp,
    MIN(temperature) AS min_temp,
    MAX(temperature) AS max_temp,
    COUNT(*) AS samples
FROM sensor_data
GROUP BY bucket, device_id;

-- 查询
SELECT * FROM sensor_5min
WHERE device_id = 'sensor-001'
AND bucket > NOW() - INTERVAL '1 hour'
ORDER BY bucket DESC;
```

## 3. 流处理

### 3.1 Kafka

```python
# Kafka IoT 数据采集
from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 发送传感器数据
def send_sensor_data(device_id, data):
    producer.send(
        topic=f'iot-sensor-{device_id[:3]}',  # 按前缀分区
        key=device_id.encode('utf-8'),
        value=data
    )

# 消费
consumer = KafkaConsumer(
    'iot-sensor-.*',
    bootstrap_servers=['kafka:9092'],
    group_id='iot-processor',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value
    process_sensor_data(data)
```

### 3.2 Flink

```python
# PyFlink 流处理
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

# Kafka Source
t_env.execute_sql("""
    CREATE TABLE sensor_source (
        device_id STRING,
        temperature DOUBLE,
        humidity DOUBLE,
        event_time TIMESTAMP(3),
        WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'iot-sensor-data',
        'properties.bootstrap.servers' = 'kafka:9092',
        'properties.group.id' = 'flink-processor',
        'format' = 'json',
        'scan.startup.mode' = 'latest-offset'
    )
""")

# 5分钟窗口平均温度
result = t_env.sql_query("""
    SELECT
        TUMBLE_START(event_time, INTERVAL '5' MINUTE) AS window_start,
        device_id,
        AVG(temperature) AS avg_temp,
        MIN(temperature) AS min_temp,
        MAX(temperature) AS max_temp,
        COUNT(*) AS sample_count
    FROM sensor_source
    GROUP BY
        TUMBLE(event_time, INTERVAL '5' MINUTE),
        device_id
""")

# 输出到 InfluxDB
t_env.execute_sql("""
    CREATE TABLE influx_sink (
        window_start TIMESTAMP(3),
        device_id STRING,
        avg_temp DOUBLE,
        min_temp DOUBLE,
        max_temp DOUBLE,
        sample_count BIGINT
    ) WITH (
        'connector' = 'influxdb',
        'url' = 'http://influxdb:8086',
        'database' = 'iot_db',
        'measurement' = 'sensor_5min_agg'
    )
""")

result.execute_insert("influx_sink")
```

## 4. 数据清洗

### 4.1 常见问题与处理

| 问题           | 描述         | 处理方法      |
| :------------- | :----------- | :------------ |
| **缺失值**     | 传感器断线   | 插值/前值填充 |
| **异常值**     | 传感器故障   | 统计检测/过滤 |
| **重复值**     | 网络重传     | 去重          |
| **时间漂移**   | 设备时钟不准 | NTP 同步/校正 |
| **单位不一致** | 不同传感器   | 统一转换      |

### 4.2 数据清洗实现

```python
import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, config: dict):
        self.ranges = config.get("ranges", {})
        self.fill_method = config.get("fill_method", "ffill")

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # 1. 去重
        df = df.drop_duplicates(subset=["device_id", "timestamp"])

        # 2. 范围过滤
        for col, (min_val, max_val) in self.ranges.items():
            if col in df.columns:
                mask = (df[col] >= min_val) & (df[col] <= max_val)
                df.loc[~mask, col] = np.nan

        # 3. 异常值检测（IQR 方法）
        for col in self.ranges.keys():
            if col in df.columns:
                df = self._remove_outliers_iqr(df, col)

        # 4. 缺失值填充
        df = df.sort_values("timestamp")
        if self.fill_method == "ffill":
            df = df.fillna(method="ffill")
        elif self.fill_method == "interpolate":
            df = df.interpolate(method="time")

        return df

    def _remove_outliers_iqr(self, df: pd.DataFrame, col: str) -> pd.DataFrame:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        mask = (df[col] >= lower) & (df[col] <= upper)
        df.loc[~mask, col] = np.nan
        return df

# 使用
config = {
    "ranges": {
        "temperature": (-40, 80),
        "humidity": (0, 100),
        "pressure": (800, 1200)
    },
    "fill_method": "interpolate"
}
cleaner = DataCleaner(config)
clean_df = cleaner.clean(raw_df)
```

## 5. 异常检测

### 5.1 检测方法

| 方法         | 原理            | 适用场景   | 实时性 |
| :----------- | :-------------- | :--------- | :----- |
| **阈值检测** | 超过固定阈值    | 简单场景   | 高     |
| **3σ 准则**  | 超过 3 倍标准差 | 正态分布   | 高     |
| **IQR**      | 四分位距        | 非正态分布 | 高     |
| **移动平均** | 偏离移动平均    | 趋势数据   | 中     |
| **孤立森林** | 树模型          | 多维异常   | 中     |
| **LSTM-AE**  | 自编码器        | 时序模式   | 低     |

### 5.2 实时异常检测

```python
import numpy as np
from collections import deque

class RealtimeAnomalyDetector:
    def __init__(self, window_size=100, threshold=3.0):
        self.window = deque(maxlen=window_size)
        self.threshold = threshold

    def detect(self, value: float) -> dict:
        self.window.append(value)

        if len(self.window) < 30:
            return {"is_anomaly": False, "reason": "insufficient_data"}

        data = np.array(self.window)
        mean = np.mean(data)
        std = np.std(data)

        if std == 0:
            return {"is_anomaly": False, "z_score": 0}

        z_score = abs(value - mean) / std
        is_anomaly = z_score > self.threshold

        return {
            "is_anomaly": is_anomaly,
            "z_score": z_score,
            "mean": mean,
            "std": std,
            "value": value
        }

# 使用
detector = RealtimeAnomalyDetector(window_size=100, threshold=3.0)
for value in sensor_stream:
    result = detector.detect(value)
    if result["is_anomaly"]:
        send_alert(f"异常值: {value}, Z-Score: {result['z_score']:.2f}")
```

## 6. 数字孪生

### 6.1 概念

数字孪生是物理实体在数字空间的**实时映射**，通过传感器数据驱动数字模型同步更新。

```mermaid
flowchart LR
    P[物理实体 设备/系统] -->|实时数据| T[数字孪生 数字模型] -->|分析决策| O[优化控制 指令]
    O -->|控制指令| P
```

### 6.2 数字孪生层次

| 层次         | 描述       | 技术               |
| :----------- | :--------- | :----------------- |
| **数据孪生** | 数据可视化 | Grafana、3D 可视化 |
| **模型孪生** | 仿真模拟   | 物理模型、统计模型 |
| **智能孪生** | 预测优化   | AI 模型、优化算法  |

### 6.3 实时数据同步

```python
class DigitalTwin:
    """设备数字孪生"""
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.state = {}
        self.model = None

    def update_state(self, sensor_data: dict):
        """更新孪生状态"""
        self.state.update(sensor_data)

        # 运行仿真模型
        if self.model:
            prediction = self.model.predict(sensor_data)
            self.state["prediction"] = prediction

        # 检查是否需要干预
        if self._needs_intervention():
            self._send_control_command()

    def _needs_intervention(self) -> bool:
        """判断是否需要干预"""
        temp = self.state.get("temperature", 0)
        pred = self.state.get("prediction", {})
        # 如果当前温度正常但预测将超温
        if temp < 35 and pred.get("temperature_1h", 0) > 40:
            return True
        return False

    def _send_control_command(self):
        """发送控制命令"""
        command = {"action": "reduce_load", "target": self.device_id}
        mqtt_client.publish(f"iot/command/{self.device_id}", json.dumps(command))
```

## 7. 小结

数据处理与分析是 IoT 价值的核心：

1. **时序数据库**是 IoT 数据存储的首选，TDengine 性能最优，TimescaleDB 兼容 SQL
2. **Kafka + Flink** 是流处理的黄金组合，支持实时聚合和窗口计算
3. **数据清洗**需处理缺失、异常、重复和时间漂移等问题
4. **异常检测**从简单阈值到深度学习，需根据场景选择
5. **数字孪生**是 IoT 的高级应用，实现预测性维护和优化控制



<!-- ============ 文档分隔线：035-iot/007-SecurityAndPrivacy.md ============ -->



## 1. IoT 安全威胁

### 1.1 威胁模型

```mermaid
flowchart TD
    T[IoT 安全威胁]
    T --> D[设备层威胁<br/>物理攻击 固件篡改 侧信道攻击]
    T --> N[网络层威胁<br/>中间人攻击 DDoS 协议攻击]
    T --> A[应用层威胁<br/>数据泄露 权限提升 注入攻击]
```

### 1.2 典型攻击案例

| 案例               | 攻击方式     | 影响        |
| :----------------- | :----------- | :---------- |
| **Mirai 僵尸网络** | 默认密码爆破 | 大规模 DDoS |
| **Stuxnet**        | USB 传播     | 破坏核设施  |
| **智能摄像头劫持** | 固件漏洞     | 隐私泄露    |
| **汽车远程控制**   | CAN 总线注入 | 安全威胁    |

### 1.3 IoT 安全挑战

| 挑战           | 描述                          |
| :------------- | :---------------------------- |
| **资源受限**   | MCU 算力不足以运行复杂加密    |
| **数量庞大**   | 数十亿设备难以逐一管理        |
| **生命周期长** | 设备运行 10+ 年，安全更新困难 |
| **物理暴露**   | 设备部署在不可控环境          |
| **供应链复杂** | 多方组件，安全责任不清        |

## 2. 设备认证

### 2.1 认证方式对比

| 方式           | 安全性 | 性能开销 | 管理复杂度 | 适用场景   |
| :------------- | :----- | :------- | :--------- | :--------- |
| **预共享密钥** | 低     | 低       | 低         | 开发测试   |
| **Token**      | 中     | 低       | 中         | 临时接入   |
| **X.509 证书** | 高     | 中       | 高         | 生产环境   |
| **TPM**        | 很高   | 中       | 高         | 高安全需求 |

### 2.2 X.509 证书认证

```python
# 生成设备证书
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import NameOID
import datetime

def generate_device_certificate(device_id: str, ca_key, ca_cert):
    # 生成设备密钥对
    device_key = ec.generate_private_key(ec.SECP256R1())

    # 构建证书
    subject = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, device_id),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "IoT Corp"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        ca_cert.subject
    ).public_key(
        device_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(
        x509.BasicConstraints(ca=False, path_length=None),
        critical=True,
    ).add_extension(
        x509.KeyUsage(
            digital_signature=True, key_encipherment=False,
            content_commitment=False, data_encipherment=False,
            key_agreement=True, key_cert_sign=False,
            crl_sign=False, encipher_only=False, decipher_only=False
        ),
        critical=True,
    ).sign(ca_key, hashes.SHA256())

    return device_key, cert
```

### 2.3 Token 认证（JWT）

```python
import jwt
import time

def generate_device_token(device_id: str, secret: str, ttl: int = 3600):
    """生成设备 JWT Token"""
    payload = {
        "device_id": device_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + ttl,
        "permissions": ["publish", "subscribe"]
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def verify_device_token(token: str, secret: str) -> dict:
    """验证设备 Token"""
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return {"valid": True, "device_id": payload["device_id"]}
    except jwt.ExpiredSignatureError:
        return {"valid": False, "reason": "token_expired"}
    except jwt.InvalidTokenError:
        return {"valid": False, "reason": "invalid_token"}
```

### 2.4 一机一密

```python
# 一机一密：每个设备有唯一密钥
import hmac
import hashlib

class DeviceAuth:
    def __init__(self, product_secret: str):
        self.product_secret = product_secret

    def generate_device_secret(self, device_name: str) -> str:
        """根据设备名生成设备密钥"""
        return hmac.new(
            self.product_secret.encode(),
            device_name.encode(),
            hashlib.sha256
        ).hexdigest()

    def generate_mqtt_password(self, device_name: str, timestamp: str) -> str:
        """生成 MQTT 连接密码"""
        content = f"{device_name}{timestamp}"
        return hmac.new(
            self.generate_device_secret(device_name).encode(),
            content.encode(),
            hashlib.sha256
        ).hexdigest()

# 使用
auth = DeviceAuth("product_secret_key")
device_secret = auth.generate_device_secret("sensor-001")
mqtt_password = auth.generate_mqtt_password("sensor-001", "1718300000")
```

## 3. 数据加密

### 3.1 加密层次

| 层次           | 方法       | 保护对象 |
| :------------- | :--------- | :------- |
| **传输加密**   | TLS/DTLS   | 通信链路 |
| **存储加密**   | AES-256    | 存储数据 |
| **端到端加密** | 应用层加密 | 全链路   |

### 3.2 TLS/DTLS

```python
# MQTT over TLS
import ssl
import paho.mqtt.client as mqtt

client = mqtt.Client()

# TLS 配置
context = ssl.create_default_context()
context.load_verify_locations("ca-certificate.pem")
context.load_cert_chain(
    "device-certificate.pem",
    "device-private-key.pem"
)
context.verify_mode = ssl.CERT_REQUIRED

client.tls_set_context(context)
client.connect("mqtt.example.com", 8883, 60)
```

### 3.3 数据加密

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

class IoTDataEncryption:
    """IoT 数据加密"""
    def __init__(self, key: bytes):
        self.key = key  # 32 bytes for AES-256

    def encrypt(self, plaintext: bytes) -> dict:
        """AES-256-CBC 加密"""
        iv = os.urandom(16)

        # PKCS7 填充
        padder = padding.PKCS7(128).padder()
        padded = padder.update(plaintext) + padder.finalize()

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded) + encryptor.finalize()

        return {"iv": iv.hex(), "ciphertext": ciphertext.hex()}

    def decrypt(self, iv_hex: str, ciphertext_hex: str) -> bytes:
        """AES-256-CBC 解密"""
        iv = bytes.fromhex(iv_hex)
        ciphertext = bytes.fromhex(ciphertext_hex)

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(padded) + unpadder.finalize()
```

### 3.4 轻量级加密（资源受限设备）

| 算法         | 密钥长度 | 性能 | 适用                        |
| :----------- | :------- | :--- | :-------------------------- |
| **AES-128**  | 128bit   | 中   | 通用                        |
| **ChaCha20** | 256bit   | 高   | 软件实现                    |
| **ASCON**    | 128bit   | 很高 | IoT 专用（NIST 轻量级标准） |

## 4. 固件安全

### 4.1 安全启动

```
Boot ROM → 验证 Bootloader 签名 → 验证 OS 签名 → 验证应用签名
   │              │                    │               │
  信任根        签名验证             签名验证        签名验证
```

### 4.2 固件签名与验证

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, utils

def sign_firmware(firmware_path: str, private_key) -> bytes:
    """固件签名"""
    with open(firmware_path, "rb") as f:
        firmware = f.read()

    signature = private_key.sign(
        firmware,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_firmware(firmware_path: str, signature: bytes, public_key) -> bool:
    """固件验证"""
    with open(firmware_path, "rb") as f:
        firmware = f.read()

    try:
        public_key.verify(signature, firmware, ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False
```

### 4.3 固件加密

```python
# 固件加密保护知识产权
def encrypt_firmware(firmware: bytes, key: bytes) -> bytes:
    """加密固件"""
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    encrypted = iv + encryptor.update(firmware) + encryptor.finalize()
    return encrypted

# 设备端解密（在安全区域执行）
def decrypt_firmware(encrypted: bytes, key: bytes) -> bytes:
    """解密固件"""
    iv = encrypted[:16]
    ciphertext = encrypted[16:]
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()
```

## 5. OTA 更新安全

### 5.1 安全 OTA 流程

```
1. 构建固件 → 签名 → 加密 → 上传到 CDN
2. 通知设备有新版本（版本号 + 哈希 + 签名）
3. 设备下载固件
4. 验证签名 → 解密 → 校验哈希
5. 写入备份分区
6. 重启到新固件
7. 验证新固件运行正常
8. 确认更新 / 回滚
```

### 5.2 A/B 分区更新

```mermaid
flowchart LR
    A[分区A 当前固件 v1.0.0<br/>↑ 活跃] B[分区B 新固件 v1.1.0]
```

更新流程：写入 B → 切换启动 → 验证 → 确认/回滚

### 5.3 OTA 安全检查清单

| 检查项     | 描述                    |
| :--------- | :---------------------- |
| 传输加密   | 使用 HTTPS/TLS 下载固件 |
| 签名验证   | 验证固件来源可信        |
| 完整性校验 | SHA-256 校验固件完整    |
| 版本控制   | 防止降级攻击            |
| 回滚机制   | 更新失败自动回滚        |
| 灰度发布   | 逐步推送，降低风险      |
| 审计日志   | 记录所有更新操作        |

## 6. 隐私保护

### 6.1 数据最小化

| 原则           | 描述           | 实践                         |
| :------------- | :------------- | :--------------------------- |
| **目的限制**   | 只收集必要数据 | 不收集与功能无关的传感器数据 |
| **数据最小化** | 最小化数据粒度 | 降精度：25.5°C → 25°C        |
| **本地处理**   | 数据不出设备   | 边缘推理，只上传结果         |
| **匿名化**     | 去除个人标识   | 设备 ID 代替用户 ID          |
| **定期删除**   | 设定数据保留期 | 超期自动删除                 |

### 6.2 差分隐私

```python
import numpy as np

def add_laplace_noise(value: float, sensitivity: float, epsilon: float) -> float:
    """添加拉普拉斯噪声实现差分隐私"""
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)
    return value + noise

# 使用：上报温度时添加噪声
real_temp = 25.5
private_temp = add_laplace_noise(real_temp, sensitivity=1.0, epsilon=0.5)
# private_temp ≈ 25.5 ± 小量噪声
```

## 7. 合规标准

### 7.1 主要标准

| 标准                | 范围 | 核心要求                         |
| :------------------ | :--- | :------------------------------- |
| **GDPR**            | 欧盟 | 数据保护、用户同意、被遗忘权     |
| **等保 2.0**        | 中国 | 安全物理环境、通信传输、边界防护 |
| **NIST 8259A**      | 美国 | IoT 设备网络安全基线             |
| **ETSI EN 303 645** | 欧洲 | 消费 IoT 安全基线                |
| **GB/T 37044**      | 中国 | IoT 安全评估指南                 |

### 7.2 安全基线

| 基线要求         | 描述                 |
| :--------------- | :------------------- |
| **无默认密码**   | 每台设备唯一密码     |
| **漏洞披露机制** | 提供 CVE 报告渠道    |
| **最小权限**     | 仅开放必要端口和服务 |
| **安全更新**     | 支持自动安全更新     |
| **传输加密**     | 所有通信使用 TLS     |
| **数据保护**     | 个人数据加密存储     |

## 8. 安全最佳实践

### 8.1 纵深防御

```
物理安全 → 设备安全 → 网络安全 → 应用安全 → 数据安全
  │          │          │          │          │
  防拆       安全启动   防火墙     输入验证   加密存储
  TPM       固件签名   TLS       权限控制   差分隐私
  串口保护   证书认证   VPN       审计日志   数据最小化
```

### 8.2 安全开发生命周期

| 阶段     | 安全活动                 |
| :------- | :----------------------- |
| **需求** | 威胁建模、安全需求定义   |
| **设计** | 安全架构设计、密码学选型 |
| **开发** | 安全编码规范、代码审查   |
| **测试** | 渗透测试、模糊测试       |
| **部署** | 安全配置、证书管理       |
| **运维** | 安全监控、漏洞响应       |

## 9. 小结

IoT 安全是系统性的挑战：

1. **设备认证**是第一道防线，X.509 证书是生产环境推荐方案
2. **数据加密**需覆盖传输、存储和端到端三个层次
3. **固件安全**通过安全启动和签名验证防止篡改
4. **OTA 安全**需确保签名验证、完整性校验和回滚机制
5. **隐私保护**遵循数据最小化和本地处理原则
6. **合规标准**是产品上市的必要条件，需提前规划
7. 安全是**纵深防御**，不能依赖单一措施



<!-- ============ 文档分隔线：035-iot/008-PracticeProject.md ============ -->



## 1. 智能家居系统

### 1.1 系统架构

```mermaid
flowchart LR
    D[智能设备<br/>灯/空调 门锁/窗帘] <-->|Wi-Fi/BLE| G[家庭网关 ESP32] -->|MQTT| C[云平台]
    C --> M[手机 App]
```

### 1.2 设备端实现

```cpp
// ESP32 智能灯控制器
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* ssid = "HomeWiFi";
const char* password = "password";
const char* mqtt_server = "broker.emqx.io";

// 设备信息
const char* device_id = "light-living-001";
const char* device_type = "smart_light";

// 引脚
#define LED_R 25
#define LED_G 26
#define LED_B 27

WiFiClient espClient;
PubSubClient client(espClient);

// 当前状态
struct LightState {
    bool power = false;
    int brightness = 100;
    int color_r = 255, color_g = 255, color_b = 255;
} state;

void apply_state() {
    if (!state.power) {
        ledcWrite(0, 0); ledcWrite(1, 0); ledcWrite(2, 0);
        return;
    }
    float factor = state.brightness / 100.0;
    ledcWrite(0, (int)(state.color_r * factor));
    ledcWrite(1, (int)(state.color_g * factor));
    ledcWrite(2, (int)(state.color_b * factor));
}

void handle_command(char* topic, byte* payload, unsigned int length) {
    StaticJsonDocument<256> doc;
    deserializeJson(doc, payload, length);

    String cmd = doc["command"];
    if (cmd == "set_power") {
        state.power = doc["value"];
    } else if (cmd == "set_brightness") {
        state.brightness = doc["value"];
    } else if (cmd == "set_color") {
        state.color_r = doc["r"];
        state.color_g = doc["g"];
        state.color_b = doc["b"];
    }

    apply_state();
    report_state();
}

void report_state() {
    StaticJsonDocument<256> doc;
    doc["device_id"] = device_id;
    doc["power"] = state.power;
    doc["brightness"] = state.brightness;
    doc["color"]["r"] = state.color_r;
    doc["color"]["g"] = state.color_g;
    doc["color"]["b"] = state.color_b;

    char buffer[256];
    serializeJson(doc, buffer);
    client.publish("home/light/state", buffer);
}

void setup() {
    ledcSetup(0, 5000, 8); ledcAttachPin(LED_R, 0);
    ledcSetup(1, 5000, 8); ledcAttachPin(LED_G, 1);
    ledcSetup(2, 5000, 8); ledcAttachPin(LED_B, 2);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) delay(500);

    client.setServer(mqtt_server, 1883);
    client.setCallback(handle_command);
    client.connect(device_id);
    client.subscribe("home/light/command");
}

void loop() {
    client.loop();
}
```

### 1.3 规则引擎

```python
# 智能家居规则引擎
class SmartHomeRules:
    def __init__(self, mqtt_client):
        self.client = mqtt_client
        self.rules = []

    def add_rule(self, trigger, action):
        self.rules.append({"trigger": trigger, "action": action})

    def evaluate(self, event: dict):
        for rule in self.rules:
            if rule["trigger"](event):
                rule["action"](event)

# 定义规则
rules = SmartHomeRules(mqtt_client)

# 规则1：温度超过 28°C 自动开空调
rules.add_rule(
    trigger=lambda e: e.get("type") == "temperature" and e["value"] > 28,
    action=lambda e: mqtt_client.publish("home/ac/command",
        json.dumps({"command": "set_power", "value": True}))
)

# 规则2：人离开自动关灯
rules.add_rule(
    trigger=lambda e: e.get("type") == "presence" and e["value"] == "left",
    action=lambda e: mqtt_client.publish("home/light/command",
        json.dumps({"command": "set_power", "value": False}))
)

# 规则3：日落自动开灯
rules.add_rule(
    trigger=lambda e: e.get("type") == "sun_event" and e["value"] == "sunset",
    action=lambda e: mqtt_client.publish("home/light/command",
        json.dumps({"command": "set_power", "value": True, "brightness": 60}))
)
```

## 2. 环境监测站

### 2.1 系统架构

```
传感器集群 → LoRa 网关 → MQTT Broker → 时序数据库 → Grafana
  (野外)     (太阳能)    (EMQX)       (TDengine)    (可视化)
```

### 2.2 传感器节点

```cpp
// LoRa 环境监测节点
#include <LoRa.h>
#include <DHT.h>
#include <BH1750.h>
#include <Wire.h>

#define DHT_PIN 4
#define LORA_CS 18
#define LORA_RST 14
#define LORA_IRQ 26

DHT dht(DHT_PIN, DHT22);
BH1750 lightMeter;

struct SensorData {
    float temperature;
    float humidity;
    float light;
    float battery_voltage;
    uint32_t timestamp;
};

void setup() {
    dht.begin();
    Wire.begin();
    lightMeter.begin();

    LoRa.setPins(LORA_CS, LORA_RST, LORA_IRQ);
    LoRa.begin(470E6);  // 中国 LoRa 频段
    LoRa.setSpreadingFactor(10);
    LoRa.setCodingRate4(5);
    LoRa.setTxPower(17);
}

void loop() {
    SensorData data;
    data.temperature = dht.readTemperature();
    data.humidity = dht.readHumidity();
    data.light = lightMeter.readLightLevel();
    data.battery_voltage = readBattery();
    data.timestamp = millis();

    // 发送数据
    LoRa.beginPacket();
    LoRa.write((uint8_t*)&data, sizeof(data));
    LoRa.endPacket();

    // Deep Sleep 5分钟
    esp_sleep_enable_timer_wakeup(300 * 1000000);
    esp_deep_sleep_start();
}
```

### 2.3 数据后端

```python
# 环境监测数据后端
from influxdb_client import InfluxDBClient, Point
import paho.mqtt.client as mqtt
import json

# InfluxDB 写入
influx_client = InfluxDBClient(url="http://localhost:8086", token="token", org="org")
write_api = influx_client.write_api()

# MQTT 消费
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    point = Point("environment") \
        .tag("station_id", data["station_id"]) \
        .tag("location", data["location"]) \
        .field("temperature", data["temperature"]) \
        .field("humidity", data["humidity"]) \
        .field("pm25", data.get("pm25", 0)) \
        .field("light", data.get("light", 0)) \
        .field("battery", data.get("battery", 0))

    write_api.write(bucket="environment", record=point)

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("emqx", 1883)
mqtt_client.subscribe("env/+/data")
mqtt_client.loop_forever()
```

## 3. 工业预测维护

### 3.1 系统架构

```
振动/温度传感器 → 边缘网关 → 特征提取 → 异常检测 → 告警
                                    ↓
                              云端模型训练 → 模型下发
```

### 3.2 振动数据采集

```python
import numpy as np
from scipy import signal, fft

class VibrationAnalyzer:
    """振动数据分析"""
    def __init__(self, sample_rate=10000):
        self.sample_rate = sample_rate

    def extract_features(self, vibration_data: np.ndarray) -> dict:
        """提取振动特征"""
        # 时域特征
        rms = np.sqrt(np.mean(vibration_data ** 2))
        peak = np.max(np.abs(vibration_data))
        crest_factor = peak / rms if rms > 0 else 0
        kurtosis = self._kurtosis(vibration_data)

        # 频域特征
        freqs, psd = signal.welch(vibration_data, fs=self.sample_rate, nperseg=1024)
        dominant_freq = freqs[np.argmax(psd)]
        spectral_centroid = np.sum(freqs * psd) / np.sum(psd)

        return {
            "rms": float(rms),
            "peak": float(peak),
            "crest_factor": float(crest_factor),
            "kurtosis": float(kurtosis),
            "dominant_freq": float(dominant_freq),
            "spectral_centroid": float(spectral_centroid)
        }

    def _kurtosis(self, data: np.ndarray) -> float:
        n = len(data)
        mean = np.mean(data)
        std = np.std(data)
        if std == 0:
            return 0
        return float(np.sum(((data - mean) / std) ** 4) / n - 3)

    def detect_anomaly(self, features: dict, thresholds: dict) -> dict:
        """异常检测"""
        alerts = []
        for key, threshold in thresholds.items():
            if key in features and features[key] > threshold:
                alerts.append(f"{key} 超阈值: {features[key]:.2f} > {threshold}")
        return {"is_anomaly": len(alerts) > 0, "alerts": alerts}
```

### 3.3 预测模型

```python
# 剩余使用寿命（RUL）预测
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

class RULPredictor:
    """剩余使用寿命预测"""
    def __init__(self):
        self.model = GradientBoostingRegressor(
            n_estimators=200,
            max_depth=5,
            learning_rate=0.1
        )

    def train(self, features: np.ndarray, rul_labels: np.ndarray):
        self.model.fit(features, rul_labels)

    def predict(self, features: np.ndarray) -> dict:
        predicted_rul = self.model.predict(features.reshape(1, -1))[0]
        confidence = self._estimate_confidence(features)

        return {
            "predicted_rul_hours": float(predicted_rul),
            "confidence": float(confidence),
            "maintenance_needed": predicted_rul < 72  # 72小时阈值
        }

    def _estimate_confidence(self, features):
        # 简化的置信度估计
        predictions = []
        for estimator in self.model.estimators_:
            pred = estimator[0].predict(features.reshape(1, -1))
            predictions.append(pred[0])
        return 1.0 - np.std(predictions) / (np.mean(predictions) + 1e-6)
```

## 4. 智慧农业

### 4.1 系统架构

```
土壤/气象传感器 → NB-IoT → 云平台 → 农业决策引擎 → 自动灌溉
                                              ↓
                                         手机 App 通知
```

### 4.2 农业决策引擎

```python
class AgricultureDecisionEngine:
    """农业决策引擎"""
    def __init__(self, mqtt_client):
        self.client = mqtt_client
        self.crop_config = {
            "tomato": {
                "optimal_temp": (20, 30),
                "optimal_humidity": (60, 80),
                "optimal_soil_moisture": (40, 60),
                "water_per_irrigation_ml": 500
            }
        }

    def evaluate(self, sensor_data: dict, crop: str = "tomato"):
        config = self.crop_config.get(crop, {})
        decisions = []

        # 温度决策
        temp = sensor_data.get("temperature", 0)
        opt_temp = config.get("optimal_temp", (0, 100))
        if temp < opt_temp[0]:
            decisions.append({"action": "close_ventilation", "reason": f"温度过低: {temp}°C"})
        elif temp > opt_temp[1]:
            decisions.append({"action": "open_ventilation", "reason": f"温度过高: {temp}°C"})

        # 灌溉决策
        soil_moisture = sensor_data.get("soil_moisture", 50)
        opt_moisture = config.get("optimal_soil_moisture", (30, 70))
        if soil_moisture < opt_moisture[0]:
            water = config.get("water_per_irrigation_ml", 500)
            decisions.append({
                "action": "irrigate",
                "amount_ml": water,
                "reason": f"土壤湿度低: {soil_moisture}%"
            })

        # 执行决策
        for decision in decisions:
            self._execute(decision)

        return decisions

    def _execute(self, decision: dict):
        self.client.publish(
            "farm/actuator/command",
            json.dumps(decision)
        )
```

## 5. MQTT 数据采集完整链路

### 5.1 完整系统

```python
# 完整 IoT 数据采集系统
import json
import time
import threading
from datetime import datetime
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision

class IoTDataPipeline:
    """IoT 数据采集完整链路"""

    def __init__(self, config: dict):
        self.config = config
        self.mqtt_client = None
        self.influx_client = None
        self.running = False

    def start(self):
        self._init_mqtt()
        self._init_influxdb()
        self.running = True
        print("IoT 数据管道已启动")

    def _init_mqtt(self):
        self.mqtt_client = mqtt.Client(client_id="data-pipeline")
        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client.connect(
            self.config["mqtt"]["host"],
            self.config["mqtt"]["port"]
        )
        self.mqtt_client.loop_start()

    def _init_influxdb(self):
        self.influx_client = InfluxDBClient(
            url=self.config["influxdb"]["url"],
            token=self.config["influxdb"]["token"],
            org=self.config["influxdb"]["org"]
        )
        self.write_api = self.influx_client.write_api()

    def _on_connect(self, client, userdata, flags, rc):
        topics = self.config["mqtt"]["subscribe_topics"]
        for topic in topics:
            client.subscribe(topic, qos=1)
        print(f"已订阅: {topics}")

    def _on_message(self, client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            self._process_message(msg.topic, data)
        except Exception as e:
            print(f"处理消息失败: {e}")

    def _process_message(self, topic: str, data: dict):
        # 1. 数据验证
        if not self._validate(data):
            return

        # 2. 数据清洗
        cleaned = self._clean(data)

        # 3. 写入时序数据库
        self._write_to_influx(cleaned)

        # 4. 规则检查
        alerts = self._check_rules(cleaned)
        for alert in alerts:
            self._send_alert(alert)

    def _validate(self, data: dict) -> bool:
        required = ["device_id", "timestamp"]
        return all(k in data for k in required)

    def _clean(self, data: dict) -> dict:
        # 范围过滤
        if "temperature" in data:
            if not (-40 <= data["temperature"] <= 80):
                data["temperature"] = None
        return data

    def _write_to_influx(self, data: dict):
        point = Point("sensor_data") \
            .tag("device_id", data.get("device_id", "unknown"))

        for key, value in data.items():
            if key not in ["device_id", "timestamp"] and value is not None:
                if isinstance(value, (int, float)):
                    point = point.field(key, value)

        self.write_api.write(
            bucket=self.config["influxdb"]["bucket"],
            record=point
        )

    def _check_rules(self, data: dict) -> list:
        alerts = []
        if data.get("temperature", 0) > 35:
            alerts.append({"type": "high_temp", "device": data["device_id"], "value": data["temperature"]})
        return alerts

    def _send_alert(self, alert: dict):
        self.mqtt_client.publish("iot/alerts", json.dumps(alert))

# 配置与启动
config = {
    "mqtt": {
        "host": "broker.emqx.io",
        "port": 1883,
        "subscribe_topics": ["iot/+/data", "iot/+/event"]
    },
    "influxdb": {
        "url": "http://localhost:8086",
        "token": "my-token",
        "org": "my-org",
        "bucket": "iot-data"
    }
}

pipeline = IoTDataPipeline(config)
pipeline.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("停止中...")
```

## 6. 从传感器到云端完整链路

### 6.1 部署架构

```yaml
# docker-compose.yml - 完整 IoT 平台
version: '3.8'
services:
  # MQTT Broker
  emqx:
    image: emqx/emqx:5.7
    ports:
      - '1883:1883'
      - '18083:18083'

  # 时序数据库
  tdengine:
    image: tdengine/tdengine:3.3
    ports:
      - '6041:6041'
    volumes:
      - td-data:/var/lib/taos

  # 数据管道
  data-pipeline:
    build: ./pipeline
    depends_on:
      - emqx
      - tdengine
    environment:
      MQTT_HOST: emqx
      TDENGINE_HOST: tdengine

  # 规则引擎
  rule-engine:
    build: ./rules
    depends_on:
      - emqx
    environment:
      MQTT_HOST: emqx

  # Grafana 可视化
  grafana:
    image: grafana/grafana:11.0
    ports:
      - '3000:3000'
    depends_on:
      - tdengine

  # ThingsBoard
  thingsboard:
    image: thingsboard/tb-postgres:latest
    ports:
      - '9090:9090'
      - '1883:1883'

volumes:
  td-data:
```

### 6.2 关键配置

| 组件            | 配置要点                     |
| :-------------- | :--------------------------- |
| **EMQX**        | 认证方式、ACL 规则、集群     |
| **TDengine**    | 保留天数、缓存大小、副本数   |
| **数据管道**    | 批量大小、写入间隔、错误重试 |
| **Grafana**     | Dashboard 模板、告警通道     |
| **ThingsBoard** | 设备配置、规则链、OTA        |

## 7. 小结

实战项目是掌握 IoT 开发的最佳方式：

1. **智能家居**是最常见的消费 IoT 场景，核心是设备控制和规则引擎
2. **环境监测**适合学习 LoRa + 低功耗 + 时序数据库
3. **预测维护**是工业 IoT 的核心价值，需掌握振动分析和 ML 模型
4. **智慧农业**结合传感器和自动控制，体现 IoT 的闭环价值
5. **完整链路**从传感器到云端，涵盖采集、传输、存储、分析和可视化
6. Docker Compose 可快速搭建完整 IoT 平台，适合开发和测试



<!-- ============ 文档分隔线：035-iot/009-MQTT.md ============ -->


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



<!-- ============ 文档分隔线：035-iot/010-CoAP.md ============ -->



## 1. CoAP 概述

### 1.1 什么是 CoAP

CoAP（Constrained Application Protocol）是专为受限设备设计的 RESTful 协议，运行在 UDP 之上。

### 1.2 与 HTTP 对比

| 对比项   | CoAP                | HTTP      |
| -------- | ------------------- | --------- |
| 传输层   | UDP                 | TCP       |
| 头部大小 | 4 字节              | 数百字节  |
| 方法     | GET/POST/PUT/DELETE | 相同      |
| 数据格式 | CBOR/JSON           | JSON/HTML |
| 发现     | 内置                | 需外部    |
| 组播     | 支持                | 不支持    |
| 功耗     | 低                  | 高        |

### 1.3 协议栈

```mermaid
flowchart TD
    App[Application] --> CoAP[CoAP]
    CoAP --> DTLS[DTLS] --> UDP[UDP]
    UDP --> IP[IPv4/IPv6]
    IP --> WP[6LoWPAN]
```

## 2. 消息模型

### 2.1 消息类型

| 类型            | 缩写 | 描述      |
| --------------- | ---- | --------- |
| Confirmable     | CON  | 需要确认  |
| Non-confirmable | NON  | 不需确认  |
| Acknowledgement | ACK  | 确认响应  |
| Reset           | RST  | 拒绝/错误 |

### 2.2 消息格式

```mermaid
flowchart TD
    B0["Ver | T | TKL | Code | Message ID"]
    B1["Token (if any, TKL bytes) ..."]
    B0 --> B1
    B2["Options (if any) ..."]
    B1 --> B2
    B3["1 1 1 1 1 1 1 1 | Payload (if any) ..."]
    B2 --> B3
```

### 2.3 请求/响应模式

**CON 请求**：

```
Client → CON GET /temperature → Server
Client ← ACK 2.05 Content "25.5" ← Server
```

**NON 请求**：

```
Client → NON GET /temperature → Server
Client ← NON 2.05 Content "25.5" ← Server
```

**分离响应**（处理时间较长时）：

```
Client → CON GET /temperature → Server
Client ← ACK (空确认) ← Server
Client ← CON 2.05 Content "25.5" ← Server
Client → ACK → Server
```

## 3. RESTful 接口

### 3.1 方法

| 方法   | 描述      |
| ------ | --------- |
| GET    | 获取资源  |
| POST   | 创建/处理 |
| PUT    | 更新资源  |
| DELETE | 删除资源  |

### 3.2 响应码

| 码   | 含义                  |
| ---- | --------------------- |
| 2.01 | Created               |
| 2.02 | Deleted               |
| 2.03 | Valid                 |
| 2.04 | Changed               |
| 2.05 | Content               |
| 4.01 | Unauthorized          |
| 4.04 | Not Found             |
| 4.06 | Not Acceptable        |
| 5.00 | Internal Server Error |

### 3.3 资源发现

```
GET /.well-known/core

→ </sensors/temp>;rt="temperature";if="sensor",
   </sensors/humidity>;rt="humidity";if="sensor",
   </actuators/led>;rt="led";if="actuator"
```

## 4. 观察模式（Observe）

### 4.1 原理

客户端注册观察，服务器在资源变化时主动推送。

```
Client → GET /temperature (Observe=0) → Server
Client ← 2.05 Content "25.5" (Observe=10) ← Server
Client ← 2.05 Content "26.0" (Observe=11) ← Server
Client ← 2.05 Content "25.8" (Observe=12) ← Server
```

### 4.2 注册与取消

| Observe 值 | 描述     |
| ---------- | -------- |
| 0          | 注册观察 |
| 1          | 取消观察 |

## 5. 组播

### 5.1 组播地址

| 地址        | 描述                  |
| ----------- | --------------------- |
| FF02::FD    | CoAP 组播（链路本地） |
| FF03::FD    | CoAP 组播（站点本地） |
| 224.0.1.187 | IPv4 组播             |

### 5.2 组播场景

```
Client → MULTICAST GET /temperature → All Devices
Client ← 2.05 Content "25.5" ← Device 1
Client ← 2.05 Content "24.0" ← Device 2
Client ← 2.05 Content "26.2" ← Device 3
```

## 6. 安全机制

### 6.1 DTLS

CoAP 使用 DTLS（Datagram TLS）提供安全传输。

| 模式         | 描述           |
| ------------ | -------------- |
| NoSec        | 无安全（默认） |
| PreSharedKey | 预共享密钥     |
| RawPublicKey | 原始公钥       |
| Certificate  | X.509 证书     |

### 6.2 OSCORE

OSCORE（Object Security for Constrained RESTful Environments）提供端到端安全，是 CoAP 的推荐安全方案。

## 7. 代码示例

### 7.1 Python (aiocoap)

```python
import asyncio
from aiocoap import *

async def main():
    context = await Context.create_client_context()
    request = Message(code=GET, uri='coap://localhost/temperature')
    response = await context.request(request).response
    print(f"Temperature: {response.payload.decode()}")

asyncio.run(main())
```

### 7.2 CoAP Server

```python
import asyncio
from aiocoap import *

class TemperatureResource(resource.Resource):
    async def render_get(self, request):
        temp = read_sensor()
        return Message(payload=str(temp).encode())

async def main():
    root = resource.Site()
    root.add_resource(['temperature'], TemperatureResource())
    await Context.create_server_context(root)
    await asyncio.get_event_loop().create_future()

asyncio.run(main())
```



<!-- ============ 文档分隔线：035-iot/011-ArduinoDevelopment.md ============ -->


## 1. Arduino 概述

### 1.1 什么是 Arduino

Arduino 是开源电子原型平台，包含硬件（微控制器板）和软件（IDE），适合快速开发交互式电子项目。

### 1.2 常见开发板

| 开发板    | MCU        | 电压 | Flash | 特点     |
| --------- | ---------- | ---- | ----- | -------- |
| Uno R3    | ATmega328P | 5V   | 32KB  | 入门首选 |
| Nano      | ATmega328P | 5V   | 32KB  | 小型     |
| Mega 2560 | ATmega2560 | 5V   | 256KB | 引脚多   |
| Leonardo  | ATmega32U4 | 5V   | 32KB  | USB HID  |
| Due       | SAM3X8E    | 3.3V | 512KB | ARM      |

### 1.3 开发环境

- Arduino IDE 2.x
- PlatformIO (VS Code)
- Arduino Web Editor

## 2. 编程基础

### 2.1 程序结构

```cpp
void setup() {
  // 初始化代码，只执行一次
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // 主循环，重复执行
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

### 2.2 数字 I/O

```cpp
// 设置引脚模式
pinMode(7, OUTPUT);   // 输出
pinMode(8, INPUT);    // 输入
pinMode(9, INPUT_PULLUP); // 内部上拉

// 数字输出
digitalWrite(7, HIGH);
digitalWrite(7, LOW);

// 数字输入
int value = digitalRead(8);
```

### 2.3 模拟 I/O

```cpp
// 模拟读取（0-1023）
int sensorValue = analogRead(A0);

// 模拟输出（PWM，0-255）
analogWrite(9, 128);  // 50% 占空比

// 模拟参考电压
analogReference(INTERNAL);  // 1.1V
```

### 2.4 串口通信

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    Serial.print("Received: ");
    Serial.println(data);
  }
  Serial.println("Hello");
  delay(1000);
}
```

## 3. 传感器交互

### 3.1 温湿度传感器（DHT11/DHT22）

```cpp
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Sensor read failed!");
    return;
  }

  Serial.print("Temp: "); Serial.print(temperature);
  Serial.print("°C  Humidity: "); Serial.print(humidity);
  Serial.println("%");
  delay(2000);
}
```

### 3.2 超声波测距（HC-SR04）

```cpp
#define TRIG_PIN 9
#define ECHO_PIN 10

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

float getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2;  // cm
}

void loop() {
  float dist = getDistance();
  Serial.print("Distance: "); Serial.print(dist); Serial.println(" cm");
  delay(500);
}
```

### 3.3 光敏电阻

```cpp
#define LIGHT_PIN A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int lightValue = analogRead(LIGHT_PIN);
  Serial.print("Light: "); Serial.println(lightValue);
  delay(500);
}
```

## 4. 执行器控制

### 4.1 LED 控制

```cpp
// 呼吸灯
#define LED_PIN 9

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(LED_PIN, brightness);
    delay(5);
  }
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(LED_PIN, brightness);
    delay(5);
  }
}
```

### 4.2 舵机控制

```cpp
#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(9);
}

void loop() {
  myServo.write(0);     // 0度
  delay(1000);
  myServo.write(90);    // 90度
  delay(1000);
  myServo.write(180);   // 180度
  delay(1000);
}
```

### 4.3 电机控制（L298N）

```cpp
#define ENA 5
#define IN1 6
#define IN2 7

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void motorForward(int speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed);
}

void motorStop() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);
}
```

## 5. 通信模块

### 5.1 WiFi（ESP8266）

```cpp
#include <ESP8266WiFi.h>

const char* ssid = "YourWiFi";
const char* password = "YourPassword";

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
}
```

### 5.2 I2C 通信

```cpp
#include <Wire.h>

void setup() {
  Wire.begin();  // 加入 I2C 总线
  Serial.begin(9600);
}

void loop() {
  Wire.requestFrom(0x68, 6);  // 从地址 0x68 读取 6 字节
  while (Wire.available()) {
    char c = Wire.read();
    Serial.print(c);
  }
  delay(500);
}
```

## 6. 项目实战：智能温控器

```cpp
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 2
#define RELAY_PIN 3
#define BUTTON_PIN 4

DHT dht(DHTPIN, DHT11);
LiquidCrystal_I2C lcd(0x27, 16, 2);

float targetTemp = 25.0;

void setup() {
  dht.begin();
  lcd.init();
  lcd.backlight();
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  float temp = dht.readTemperature();

  lcd.setCursor(0, 0);
  lcd.print("Temp: "); lcd.print(temp); lcd.print("C");
  lcd.setCursor(0, 1);
  lcd.print("Target: "); lcd.print(targetTemp); lcd.print("C");

  // 温度控制
  if (temp < targetTemp) {
    digitalWrite(RELAY_PIN, HIGH);  // 开启加热
  } else {
    digitalWrite(RELAY_PIN, LOW);   // 关闭加热
  }

  // 按钮调节目标温度
  if (digitalRead(BUTTON_PIN) == LOW) {
    targetTemp += 0.5;
    if (targetTemp > 30) targetTemp = 20;
    delay(200);
  }

  delay(1000);
}
```
## 程序结构

**基本写法：setup 函数**
`void setup() { }`
```cpp
// 上电或复位时执行一次
void setup() {
  pinMode(13, OUTPUT);
}
```

---

**基本写法：loop 函数**
`void loop() { }`
```cpp
// setup 后不断循环执行
void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
}
```

---

**基本写法：包含头文件**
`#include <库>`
```cpp
// 引入标准库
#include <Wire.h>
```

---

**基本写法：包含本地文件**
`#include "文件.h"`
```cpp
// 引入项目内自定义头文件
#include "mylib.h"
```

---

## 变量与类型

**基本写法：定义整型变量**
`int <变量名> = <值>;`
```cpp
// 定义 16 位有符号整数
int ledPin = 13;
```

---

**基本写法：定义无符号长整型**
`unsigned long <变量名> = <值>;`
```cpp
// 用于 millis 微秒计数
unsigned long startTime = 0;
```

---

**基本写法：定义浮点型**
`float <变量名> = <值>;`
```cpp
// 定义单精度浮点数
float temperature = 23.5;
```

---

**基本写法：定义常量**
`const <类型> <变量名> = <值>;`
```cpp
// 编译期常量不占内存
const int LED_PIN = 13;
```

---

**基本写法：宏定义**
`#define <名称> <值>`
```cpp
// 预处理宏替换
#define LED_PIN 13
```

---

## 引脚模式

**基本写法：设置为输出**
`pinMode(<引脚>, OUTPUT);`
```cpp
// 配置为输出模式驱动 LED
pinMode(13, OUTPUT);
```

---

**基本写法：设置为输入**
`pinMode(<引脚>, INPUT);`
```cpp
// 配置为高阻态输入
pinMode(2, INPUT);
```

---

**基本写法：启用内部上拉**
`pinMode(<引脚>, INPUT_PULLUP);`
```cpp
// 启用内部上拉电阻免外接
pinMode(2, INPUT_PULLUP);
```

---

## 数字 IO

**基本写法：输出高电平**
`digitalWrite(<引脚>, HIGH);`
```cpp
// 点亮 LED
digitalWrite(13, HIGH);
```

---

**基本写法：输出低电平**
`digitalWrite(<引脚>, LOW);`
```cpp
// 熄灭 LED
digitalWrite(13, LOW);
```

---

**基本写法：读取数字输入**
`digitalRead(<引脚>)`
```cpp
// 读取按钮状态
int state = digitalRead(2);
```

---

## 模拟 IO

**基本写法：读取模拟值**
`analogRead(<引脚>)`
```cpp
// 读取 0-1023 的 ADC 值
int sensorValue = analogRead(A0);
```

---

**基本写法：PWM 输出**
`analogWrite(<引脚>, <值>);`
```cpp
// 输出 0-255 PWM 控制亮度
analogWrite(9, 128);
```

---

**基本写法：参考电压设置**
`analogReference(<类型>);`
```cpp
// 设置 ADC 参考电压为内部 1.1V
analogReference(INTERNAL);
```

---

## 时间函数

**基本写法：毫秒延时**
`delay(<毫秒>);`
```cpp
// 阻塞延时 1000 毫秒
delay(1000);
```

---

**基本写法：微秒延时**
`delayMicroseconds(<微秒>);`
```cpp
// 短时延时适合时序控制
delayMicroseconds(100);
```

---

**基本写法：获取运行毫秒数**
`millis()`
```cpp
// 获取上电至今毫秒数约 50 天溢出
unsigned long t = millis();
```

---

**基本写法：获取运行微秒数**
`micros()`
```cpp
// 获取上电至今微秒数约 70 分钟溢出
unsigned long t = micros();
```

---

**基本写法：非阻塞定时**
```cpp
// 通过 millis 实现非阻塞定时
if (millis() - previousMillis >= interval) {
  previousMillis = millis();
}
```

---

## 数学运算

**基本写法：映射范围**
`map(<值>, <源低>, <源高>, <目标低>, <目标高>)`
```cpp
// 将 0-1023 映射到 0-255
int pwm = map(sensor, 0, 1023, 0, 255);
```

---

**基本写法：取最小值**
`min(<a>, <b>)`
```cpp
// 返回较小值
int v = min(10, 20);
```

---

**基本写法：取最大值**
`max(<a>, <b>)`
```cpp
// 返回较大值
int v = max(10, 20);
```

---

**基本写法：约束范围**
`constrain(<值>, <最小>, <最大>)`
```cpp
// 限制值在 0-255 之间
int v = constrain(sensor, 0, 255);
```

---

## 随机数

**基本写法：设置随机种子**
`randomSeed(<种子>);`
```cpp
// 用模拟噪声作为种子
randomSeed(analogRead(0));
```

---

**基本写法：生成随机数**
`random(<最小>, <最大>)`
```cpp
// 生成 0-99 之间随机数
int r = random(0, 100);
```

---

## 中断

**基本写法：附加中断**
`attachInterrupt(<数字引脚>, <回调>, <触发模式>);`
```cpp
// 在引脚 2 下降沿触发 ISR
attachInterrupt(digitalPinToInterrupt(2), myISR, FALLING);
```

---

**基本写法：分离中断**
`detachInterrupt(<数字引脚>);`
```cpp
// 移除引脚中断
detachInterrupt(digitalPinToInterrupt(2));
```

---

**基本写法：volatile 变量**
`volatile <类型> <变量名>;`
```cpp
// 中断中修改的变量需声明为 volatile
volatile int counter = 0;
```

---

## 字节操作

**基本写法：读取低位字节**
`lowByte(<值>)`
```cpp
// 取 16 位值的低字节
uint8_t lo = lowByte(0x1234);
```

---

**基本写法：读取高位字节**
`highByte(<值>)`
```cpp
// 取 16 位值的高字节
uint8_t hi = highByte(0x1234);
```

---

**基本写法：读取指定字节**
`bitRead(<值>, <位>)`
```cpp
// 读取值的某一位
bool b = bitRead(0x0F, 3);
```



<!-- ============ 文档分隔线：035-iot/012-ESP32Development.md ============ -->



## 1. ESP32 概述

### 1.1 芯片特性

| 特性  | ESP32        | ESP32-S3     | ESP32-C3     |
| ----- | ------------ | ------------ | ------------ |
| 内核  | 双核 Xtensa  | 双核 Xtensa  | 单核 RISC-V  |
| 频率  | 240MHz       | 240MHz       | 160MHz       |
| WiFi  | 802.11 b/g/n | 802.11 b/g/n | 802.11 b/g/n |
| 蓝牙  | BT 4.2 + BLE | BT 5.0 + BLE | BT 5.0 + BLE |
| Flash | 4-16MB       | 8-32MB       | 4-16MB       |
| GPIO  | 34           | 45           | 22           |
| ADC   | 18 通道      | 20 通道      | 6 通道       |

### 1.2 开发框架

| 框架          | 语言   | 特点          |
| ------------- | ------ | ------------- |
| Arduino IDE   | C++    | 简单易用      |
| ESP-IDF       | C      | 官方、功能全  |
| MicroPython   | Python | 快速原型      |
| CircuitPython | Python | Adafruit 生态 |

## 2. WiFi 开发

### 2.1 STA 模式

```cpp
#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "PASSWORD");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.print("IP: "); Serial.println(WiFi.localIP());
}
```

### 2.2 AP 模式

```cpp
#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.softAP("ESP32-Hotspot", "password123");
  Serial.print("AP IP: "); Serial.println(WiFi.softAPIP());
}
```

### 2.3 HTTP 客户端

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("https://api.example.com/data");
    int code = http.GET();

    if (code > 0) {
      String payload = http.getString();
      Serial.println(payload);
    }
    http.end();
  }
  delay(10000);
}
```

### 2.4 MQTT 通信

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println("Message: " + message);
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("esp32-client")) {
      client.subscribe("home/control/#");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  WiFi.begin("SSID", "PASSWORD");
  client.setServer("broker.emqx.io", 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();
  client.publish("home/sensor/temp", "25.5");
  delay(5000);
}
```

## 3. BLE 开发

### 3.1 BLE Server

```cpp
#include <BLEDevice.h>
#include <BLEServer.h>

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

void setup() {
  BLEDevice::init("ESP32-BLE");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
    CHARACTERISTIC_UUID,
    BLECharacteristic::PROPERTY_READ |
    BLECharacteristic::PROPERTY_WRITE
  );
  pCharacteristic->setValue("Hello BLE");
  pService->start();
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  BLEDevice::startAdvertising();
}
```

## 4. FreeRTOS 多任务

### 4.1 双核任务

```cpp
TaskHandle_t Task1;
TaskHandle_t Task2;

void task1(void *pvParameters) {
  for (;;) {
    // 核心 0：传感器读取
    float temp = readTemperature();
    vTaskDelay(1000 / portTICK_PERIOD_MS);
  }
}

void task2(void *pvParameters) {
  for (;;) {
    // 核心 1：网络通信
    publishMQTT();
    vTaskDelay(5000 / portTICK_PERIOD_MS);
  }
}

void setup() {
  xTaskCreatePinnedToCore(task1, "Sensor", 4096, NULL, 1, &Task1, 0);
  xTaskCreatePinnedToCore(task2, "Network", 8192, NULL, 1, &Task2, 1);
}
```

### 4.2 任务间通信

```cpp
QueueHandle_t tempQueue;

void sensorTask(void *pvParameters) {
  for (;;) {
    float temp = readTemperature();
    xQueueSend(tempQueue, &temp, portMAX_DELAY);
    vTaskDelay(1000 / portTICK_PERIOD_MS);
  }
}

void networkTask(void *pvParameters) {
  float temp;
  for (;;) {
    if (xQueueReceive(tempQueue, &temp, portMAX_DELAY)) {
      publishMQTT(temp);
    }
  }
}

void setup() {
  tempQueue = xQueueCreate(10, sizeof(float));
  xTaskCreate(sensorTask, "Sensor", 4096, NULL, 1, NULL);
  xTaskCreate(networkTask, "Network", 8192, NULL, 1, NULL);
}
```

## 5. 低功耗模式

### 5.1 睡眠模式

| 模式        | 功耗   | 唤醒方式         |
| ----------- | ------ | ---------------- |
| Active      | ~240mA | -                |
| Modem Sleep | ~3mA   | 定时器           |
| Light Sleep | ~0.8mA | GPIO/定时器      |
| Deep Sleep  | ~10μA  | GPIO/定时器/触摸 |

### 5.2 Deep Sleep

```cpp
#define uS_TO_S_FACTOR 1000000ULL
#define TIME_TO_SLEEP  60

void setup() {
  Serial.begin(115200);

  // 读取传感器
  float temp = readTemperature();
  sendToServer(temp);

  // 进入深度睡眠 60 秒
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  esp_deep_sleep_start();
}

void loop() {
  // 不会执行（Deep Sleep 后重启）
}
```

## 6. 项目实战：WiFi 温湿度监控

```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHT22);
WiFiClient espClient;
PubSubClient client(espClient);

void sendSensorData() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  StaticJsonDocument<128> doc;
  doc["temperature"] = temp;
  doc["humidity"] = hum;
  doc["device"] = "esp32-001";

  char buffer[128];
  serializeJson(doc, buffer);
  client.publish("iot/sensor/data", buffer);
}

void setup() {
  dht.begin();
  WiFi.begin("SSID", "PASSWORD");
  client.setServer("broker.emqx.io", 1883);
}

void loop() {
  if (!client.connected()) {
    client.connect("esp32-sensor-001");
  }
  client.loop();
  sendSensorData();

  // Deep Sleep 5 分钟
  esp_sleep_enable_timer_wakeup(300 * 1000000ULL);
  esp_deep_sleep_start();
}
```



<!-- ============ 文档分隔线：035-iot/013-RTThread.md ============ -->



## 1. RT-Thread 概述

### 1.1 什么是 RT-Thread

RT-Thread 是国产开源实时操作系统（RTOS），适用于资源受限的嵌入式场景。

### 1.2 版本对比

| 版本     | RAM 需求 | Flash 需求 | 适用场景        |
| -------- | -------- | ---------- | --------------- |
| Nano     | 3KB      | 24KB       | 极小资源 MCU    |
| Standard | 10KB+    | 100KB+     | 通用嵌入式      |
| Smart    | 64KB+    | 512KB+     | 带 MMU 的处理器 |

### 1.3 架构

```mermaid
flowchart TD
    App[应用层] --> Comp[组件层 FinSH/DFS/Net/...]
    Comp --> Kern[内核层 线程/IPC/定时器/内存]
    Kern --> HW[硬件层 BSP/驱动]
```

## 2. 内核机制

### 2.1 线程管理

```c
// 静态线程
ALIGN(RT_ALIGN_SIZE)
static char thread_stack[512];
static struct rt_thread thread;

rt_thread_init(&thread,
    "my_thread",
    thread_entry, RT_NULL,
    &thread_stack[0], sizeof(thread_stack),
    10, 20);

rt_thread_startup(&thread);

// 动态线程
rt_thread_t tid = rt_thread_create("dynamic",
    thread_entry, RT_NULL,
    1024, 10, 20);
rt_thread_startup(tid);
```

### 2.2 线程调度

| 调度算法   | 描述                   |
| ---------- | ---------------------- |
| 优先级抢占 | 高优先级立即抢占       |
| 时间片轮转 | 同优先级轮流执行       |
| 优先级范围 | 0（最高）~ 255（最低） |

### 2.3 线程间通信

| IPC 机制 | 描述       |
| -------- | ---------- |
| 信号量   | 同步/互斥  |
| 互斥量   | 互斥访问   |
| 事件集   | 事件通知   |
| 邮箱     | 4 字节消息 |
| 消息队列 | 变长消息   |

**信号量示例**：

```c
static rt_sem_t sem;

void producer(void *parameter) {
    while (1) {
        produce_data();
        rt_sem_release(sem);
        rt_thread_delay(100);
    }
}

void consumer(void *parameter) {
    while (1) {
        rt_sem_take(sem, RT_WAITING_FOREVER);
        consume_data();
    }
}

// 初始化
sem = rt_sem_create("data_sem", 0, RT_IPC_FLAG_PRIO);
```

**消息队列示例**：

```c
static rt_mq_t msg_queue;

struct sensor_data {
    float temperature;
    float humidity;
};

void sender(void *parameter) {
    struct sensor_data data = {25.5, 60.0};
    rt_mq_send(msg_queue, &data, sizeof(data));
}

void receiver(void *parameter) {
    struct sensor_data data;
    while (1) {
        if (rt_mq_recv(msg_queue, &data, sizeof(data), RT_WAITING_FOREVER) == RT_EOK) {
            rt_kprintf("Temp: %.1f, Hum: %.1f\n", data.temperature, data.humidity);
        }
    }
}

msg_queue = rt_mq_create("sensor_mq", sizeof(struct sensor_data), 10, RT_IPC_FLAG_PRIO);
```

### 2.4 定时器

```c
// 硬件定时器（高精度）
rt_timer_t timer = rt_timer_create("my_timer",
    timeout_callback, RT_NULL,
    100,  // 100 个 tick
    RT_TIMER_FLAG_PERIODIC);
rt_timer_start(timer);

// 软件定时器（低精度）
rt_timer_t soft_timer = rt_timer_create("soft_timer",
    timeout_callback, RT_NULL,
    1000,
    RT_TIMER_FLAG_PERIODIC | RT_TIMER_FLAG_SOFT_TIMER);
rt_timer_start(soft_timer);
```

### 2.5 内存管理

| 算法       | 描述         | 适用场景  |
| ---------- | ------------ | --------- |
| 小内存算法 | 简单链表     | RAM < 2MB |
| SLAB       | 类 SLAB 分配 | 中等 RAM  |
| memheap    | 多内存池     | 多片 RAM  |

## 3. 设备驱动框架

### 3.1 I/O 设备模型

```c
// 打开设备
rt_device_t dev = rt_device_find("uart1");
rt_device_open(dev, RT_DEVICE_OFLAG_RDWR);

// 读取
char buffer[64];
rt_size_t size = rt_device_read(dev, 0, buffer, sizeof(buffer));

// 写入
rt_device_write(dev, 0, "Hello", 5);

// 关闭
rt_device_close(dev);
```

### 3.2 PIN 设备

```c
#define LED_PIN    GET_PIN(A, 5)
#define BUTTON_PIN GET_PIN(C, 13)

rt_pin_mode(LED_PIN, PIN_MODE_OUTPUT);
rt_pin_write(LED_PIN, PIN_HIGH);

rt_pin_mode(BUTTON_PIN, PIN_MODE_INPUT_PULLUP);
rt_pin_attach_irq(BUTTON_PIN, PIN_IRQ_MODE_FALLING, button_isr, RT_NULL);
rt_pin_irq_enable(BUTTON_PIN, PIN_IRQ_ENABLE);
```

### 3.3 ADC 设备

```c
rt_adc_device_t adc_dev = (rt_adc_device_t)rt_device_find("adc1");
rt_adc_enable(adc_dev, 0);  // 通道 0
rt_uint32_t value = rt_adc_read(adc_dev, 0);
float voltage = value * 3.3 / 4096;
rt_adc_disable(adc_dev, 0);
```

## 4. 组件框架

### 4.1 FinSH 控制台

```c
// 导出命令
MSH_CMD_EXPORT(hello, hello command);

// 带参数命令
int echo_args(int argc, char **argv) {
    rt_kprintf("argc=%d\n", argc);
    for (int i = 0; i < argc; i++) {
        rt_kprintf("argv[%d]=%s\n", i, argv[i]);
    }
    return 0;
}
MSH_CMD_EXPORT(echo_args, echo args command);
```

### 4.2 DFS 文件系统

```c
// 挂载文件系统
dfs_mount("flash", "/", "elm", 0, 0);

// 文件操作
int fd = open("/data/log.txt", O_WRONLY | O_CREAT);
write(fd, "Hello RT-Thread", 15);
close(fd);
```

### 4.3 网络框架

```c
// TCP 客户端
int sock = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in server_addr;
server_addr.sin_family = AF_INET;
server_addr.sin_port = htons(8080);
inet_pton(AF_INET, "192.168.1.100", &server_addr.sin_addr);
connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr));
send(sock, "Hello", 5, 0);
closesocket(sock);
```

## 5. 项目实战

### 5.1 智能网关

```
传感器 → RT-Thread → MQTT → 云平台
              ↓
         本地控制逻辑
```

### 5.2 开发流程

```
1. 选择 BSP → env 工具配置
2. menuconfig → 选择组件
3. scons → 编译
4. 烧录 → 调试
5. FinSH → 测试
```



<!-- ============ 文档分隔线：035-iot/014-AI.md ============ -->



## 1. 边缘 AI 概述

### 1.1 什么是边缘 AI

边缘 AI 是将 AI 推理部署在边缘设备上，实现本地数据处理和决策，减少对云端的依赖。

### 1.2 边缘 vs 云端

| 对比项   | 云端 AI        | 边缘 AI        |
| -------- | -------------- | -------------- |
| 延迟     | 高（网络延迟） | 低（本地推理） |
| 带宽     | 需上传数据     | 无需上传       |
| 隐私     | 数据离开设备   | 数据本地处理   |
| 可用性   | 依赖网络       | 离线可用       |
| 算力     | 强             | 有限           |
| 模型大小 | 无限制         | 严格限制       |

### 1.3 应用场景

| 场景     | 描述               |
| -------- | ------------------ |
| 智能家居 | 语音唤醒、人脸识别 |
| 工业检测 | 缺陷检测、预测维护 |
| 自动驾驶 | 实时感知、决策     |
| 医疗设备 | 生命体征监测       |
| 安防监控 | 异常行为检测       |

## 2. TinyML

### 2.1 概述

TinyML 是在微控制器（MCU）上运行机器学习的技术，目标是在功耗 < 1mW 的设备上实现 AI 推理。

### 2.2 资源约束

| 约束  | 典型值       |
| ----- | ------------ |
| RAM   | 16-512 KB    |
| Flash | 64 KB - 2 MB |
| 功耗  | < 1 mW       |
| 算力  | 10-100 DMIPS |

### 2.3 典型任务

| 任务       | 模型        | RAM    | Flash  |
| ---------- | ----------- | ------ | ------ |
| 唤醒词检测 | DSCNN       | ~20KB  | ~50KB  |
| 图像分类   | MobileNet   | ~200KB | ~500KB |
| 异常检测   | AutoEncoder | ~10KB  | ~30KB  |
| 手势识别   | LSTM        | ~50KB  | ~100KB |

## 3. 模型压缩技术

### 3.1 量化

| 类型                | 描述           | 压缩比 |
| ------------------- | -------------- | ------ |
| 训练后量化（PTQ）   | 训练后直接量化 | 2-4x   |
| 量化感知训练（QAT） | 训练时模拟量化 | 2-4x   |
| INT8 量化           | FP32 → INT8    | 4x     |
| 二值量化            | 权重 ±1        | 32x    |

**INT8 量化原理**：

$$q = \text{round}\left(\frac{r}{S} + Z\right)$$

其中 $r$ 为浮点值，$S$ 为缩放因子，$Z$ 为零点。

### 3.2 剪枝

| 类型         | 描述           | 压缩比 |
| ------------ | -------------- | ------ |
| 非结构化剪枝 | 删除单个权重   | 5-10x  |
| 结构化剪枝   | 删除整个通道   | 2-4x   |
| 自动剪枝     | 自动搜索剪枝率 | 可变   |

### 3.3 知识蒸馏

```
教师模型（大）→ 软标签 → 学生模型（小）
```

学生模型同时学习硬标签（真实标签）和软标签（教师输出），获得更好的性能。

### 3.4 架构搜索（NAS）

自动搜索适合边缘设备的网络架构，如 MobileNet、EfficientNet-Lite。

## 4. 边缘推理框架

### 4.1 TensorFlow Lite Micro

```cpp
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"

// 模型
const tflite::Model* model = tflite::GetModel(g_model_data);

// 操作解析器
tflite::MicroMutableOpResolver<10> resolver;
resolver.AddConv2D();
resolver.AddDepthwiseConv2D();
resolver.AddFullyConnected();
resolver.AddSoftmax();

// 解释器
constexpr int kTensorArenaSize = 60 * 1024;
uint8_t tensor_arena[kTensorArenaSize];

tflite::MicroInterpreter interpreter(model, resolver, tensor_arena, kTensorArenaSize);
interpreter.AllocateTensors();

// 推理
float* input = interpreter.input(0)->data.f;
// 填充输入数据
interpreter.Invoke();
float* output = interpreter.output(0)->data.f;
```

### 4.2 框架对比

| 框架         | 平台     | 特点             |
| ------------ | -------- | ---------------- |
| TFLite Micro | MCU      | Google 官方      |
| ONNX Runtime | 边缘设备 | 微软，跨平台     |
| NCNN         | ARM/边缘 | 腾讯，高性能     |
| MNN          | ARM/边缘 | 阿里，全功能     |
| PaddleLite   | ARM/边缘 | 百度             |
| MicroTVM     | MCU      | Apache，编译优化 |

### 4.3 硬件加速

| 硬件 | 类型         | 特点         |
| ---- | ------------ | ------------ |
| NPU  | 神经网络专用 | 高效、低功耗 |
| GPU  | 图形处理     | 并行计算     |
| DSP  | 数字信号     | 定点运算     |
| FPGA | 可编程逻辑   | 灵活、低延迟 |

## 5. 端侧智能应用

### 5.1 语音唤醒

```
麦克风 → 预处理 → MFCC 特征 → DSCNN → 唤醒词判断
```

### 5.2 视觉检测

```
摄像头 → 图像预处理 → MobileNet → 分类/检测
```

### 5.3 异常检测

```
传感器 → 特征提取 → AutoEncoder → 重构误差 → 异常判断
```

## 6. 开发流程

```
1. 数据采集与标注
2. 模型训练（云端）
3. 模型压缩（量化+剪枝）
4. 模型转换（TFLite/ONNX）
5. 边缘部署与优化
6. 持续学习（可选）
```

### 6.1 模型转换

```bash
# TensorFlow → TFLite
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model('model')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# 生成 C 数组
xxd -i model.tflite > model_data.cc
```

### 6.2 性能优化

| 优化     | 描述           |
| -------- | -------------- |
| 算子融合 | 减少内存访问   |
| 内存复用 | 减少峰值内存   |
| 定点运算 | 替代浮点运算   |
| 模型分区 | 按硬件能力分配 |



<!-- ============ 文档分隔线：035-iot/015-LwM2MManagement.md ============ -->



## 1. LwM2M 概述

### 1.1 协议架构

协议架构是LwM2M设备管理的重要组成部分。本节详细介绍协议架构的核心概念、工作原理和实际应用。

**关键要点**：

- 协议架构的定义与核心原理
- 协议架构的实现方式与技术细节
- 协议架构在实际场景中的应用与最佳实践
- 协议架构的常见问题与解决方案

协议架构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 对象模型

对象模型是LwM2M设备管理的重要组成部分。本节详细介绍对象模型的核心概念、工作原理和实际应用。

**关键要点**：

- 对象模型的定义与核心原理
- 对象模型的实现方式与技术细节
- 对象模型在实际场景中的应用与最佳实践
- 对象模型的常见问题与解决方案

对象模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 引导启动

### 2.1 Factory Bootstrap

Factory Bootstrap是LwM2M设备管理的重要组成部分。本节详细介绍Factory Bootstrap的核心概念、工作原理和实际应用。

**关键要点**：

- Factory Bootstrap的定义与核心原理
- Factory Bootstrap的实现方式与技术细节
- Factory Bootstrap在实际场景中的应用与最佳实践
- Factory Bootstrap的常见问题与解决方案

Factory Bootstrap在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Smart Bootstrap

Smart Bootstrap是LwM2M设备管理的重要组成部分。本节详细介绍Smart Bootstrap的核心概念、工作原理和实际应用。

**关键要点**：

- Smart Bootstrap的定义与核心原理
- Smart Bootstrap的实现方式与技术细节
- Smart Bootstrap在实际场景中的应用与最佳实践
- Smart Bootstrap的常见问题与解决方案

Smart Bootstrap在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 LwM2M Bootstrap Server

LwM2M Bootstrap Server是LwM2M设备管理的重要组成部分。本节详细介绍LwM2M Bootstrap Server的核心概念、工作原理和实际应用。

**关键要点**：

- LwM2M Bootstrap Server的定义与核心原理
- LwM2M Bootstrap Server的实现方式与技术细节
- LwM2M Bootstrap Server在实际场景中的应用与最佳实践
- LwM2M Bootstrap Server的常见问题与解决方案

LwM2M Bootstrap Server在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 设备管理

### 3.1 注册与注销

注册与注销是LwM2M设备管理的重要组成部分。本节详细介绍注册与注销的核心概念、工作原理和实际应用。

**关键要点**：

- 注册与注销的定义与核心原理
- 注册与注销的实现方式与技术细节
- 注册与注销在实际场景中的应用与最佳实践
- 注册与注销的常见问题与解决方案

注册与注销在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 读取/写入/执行

读取/写入/执行是LwM2M设备管理的重要组成部分。本节详细介绍读取/写入/执行的核心概念、工作原理和实际应用。

**关键要点**：

- 读取/写入/执行的定义与核心原理
- 读取/写入/执行的实现方式与技术细节
- 读取/写入/执行在实际场景中的应用与最佳实践
- 读取/写入/执行的常见问题与解决方案

读取/写入/执行在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 观察与通知

观察与通知是LwM2M设备管理的重要组成部分。本节详细介绍观察与通知的核心概念、工作原理和实际应用。

**关键要点**：

- 观察与通知的定义与核心原理
- 观察与通知的实现方式与技术细节
- 观察与通知在实际场景中的应用与最佳实践
- 观察与通知的常见问题与解决方案

观察与通知在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 固件更新

### 4.1 FOTA 流程

FOTA 流程是LwM2M设备管理的重要组成部分。本节详细介绍FOTA 流程的核心概念、工作原理和实际应用。

**关键要点**：

- FOTA 流程的定义与核心原理
- FOTA 流程的实现方式与技术细节
- FOTA 流程在实际场景中的应用与最佳实践
- FOTA 流程的常见问题与解决方案

FOTA 流程在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 固件对象（Object 5）

固件对象（Object 5）是LwM2M设备管理的重要组成部分。本节详细介绍固件对象（Object 5）的核心概念、工作原理和实际应用。

**关键要点**：

- 固件对象（Object 5）的定义与核心原理
- 固件对象（Object 5）的实现方式与技术细节
- 固件对象（Object 5）在实际场景中的应用与最佳实践
- 固件对象（Object 5）的常见问题与解决方案

固件对象（Object 5）在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：035-iot/016-TimeSeriesDatabase.md ============ -->



## 1. 时序数据特征

### 1.1 数据模型

数据模型是时序数据库的重要组成部分。本节详细介绍数据模型的核心概念、工作原理和实际应用。

**关键要点**：

- 数据模型的定义与核心原理
- 数据模型的实现方式与技术细节
- 数据模型在实际场景中的应用与最佳实践
- 数据模型的常见问题与解决方案

数据模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 降采样与保留策略

降采样与保留策略是时序数据库的重要组成部分。本节详细介绍降采样与保留策略的核心概念、工作原理和实际应用。

**关键要点**：

- 降采样与保留策略的定义与核心原理
- 降采样与保留策略的实现方式与技术细节
- 降采样与保留策略在实际场景中的应用与最佳实践
- 降采样与保留策略的常见问题与解决方案

降采样与保留策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. InfluxDB

### 2.1 Line Protocol

Line Protocol是时序数据库的重要组成部分。本节详细介绍Line Protocol的核心概念、工作原理和实际应用。

**关键要点**：

- Line Protocol的定义与核心原理
- Line Protocol的实现方式与技术细节
- Line Protocol在实际场景中的应用与最佳实践
- Line Protocol的常见问题与解决方案

Line Protocol在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Flux 查询

Flux 查询是时序数据库的重要组成部分。本节详细介绍Flux 查询的核心概念、工作原理和实际应用。

**关键要点**：

- Flux 查询的定义与核心原理
- Flux 查询的实现方式与技术细节
- Flux 查询在实际场景中的应用与最佳实践
- Flux 查询的常见问题与解决方案

Flux 查询在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 连续查询

连续查询是时序数据库的重要组成部分。本节详细介绍连续查询的核心概念、工作原理和实际应用。

**关键要点**：

- 连续查询的定义与核心原理
- 连续查询的实现方式与技术细节
- 连续查询在实际场景中的应用与最佳实践
- 连续查询的常见问题与解决方案

连续查询在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. TDengine

### 3.1 超级表与子表

超级表与子表是时序数据库的重要组成部分。本节详细介绍超级表与子表的核心概念、工作原理和实际应用。

**关键要点**：

- 超级表与子表的定义与核心原理
- 超级表与子表的实现方式与技术细节
- 超级表与子表在实际场景中的应用与最佳实践
- 超级表与子表的常见问题与解决方案

超级表与子表在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 SQL 查询

SQL 查询是时序数据库的重要组成部分。本节详细介绍SQL 查询的核心概念、工作原理和实际应用。

**关键要点**：

- SQL 查询的定义与核心原理
- SQL 查询的实现方式与技术细节
- SQL 查询在实际场景中的应用与最佳实践
- SQL 查询的常见问题与解决方案

SQL 查询在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 集群部署

集群部署是时序数据库的重要组成部分。本节详细介绍集群部署的核心概念、工作原理和实际应用。

**关键要点**：

- 集群部署的定义与核心原理
- 集群部署的实现方式与技术细节
- 集群部署在实际场景中的应用与最佳实践
- 集群部署的常见问题与解决方案

集群部署在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 对比与选型

### 4.1 写入性能

写入性能是时序数据库的重要组成部分。本节详细介绍写入性能的核心概念、工作原理和实际应用。

**关键要点**：

- 写入性能的定义与核心原理
- 写入性能的实现方式与技术细节
- 写入性能在实际场景中的应用与最佳实践
- 写入性能的常见问题与解决方案

写入性能在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 查询性能

查询性能是时序数据库的重要组成部分。本节详细介绍查询性能的核心概念、工作原理和实际应用。

**关键要点**：

- 查询性能的定义与核心原理
- 查询性能的实现方式与技术细节
- 查询性能在实际场景中的应用与最佳实践
- 查询性能的常见问题与解决方案

查询性能在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 压缩率

压缩率是时序数据库的重要组成部分。本节详细介绍压缩率的核心概念、工作原理和实际应用。

**关键要点**：

- 压缩率的定义与核心原理
- 压缩率的实现方式与技术细节
- 压缩率在实际场景中的应用与最佳实践
- 压缩率的常见问题与解决方案

压缩率在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：035-iot/017-IoTSecurity.md ============ -->



## 1. 设备认证

### 1.1 证书认证

证书认证是物联网安全的重要组成部分。本节详细介绍证书认证的核心概念、工作原理和实际应用。

**关键要点**：

- 证书认证的定义与核心原理
- 证书认证的实现方式与技术细节
- 证书认证在实际场景中的应用与最佳实践
- 证书认证的常见问题与解决方案

证书认证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Token 认证

Token 认证是物联网安全的重要组成部分。本节详细介绍Token 认证的核心概念、工作原理和实际应用。

**关键要点**：

- Token 认证的定义与核心原理
- Token 认证的实现方式与技术细节
- Token 认证在实际场景中的应用与最佳实践
- Token 认证的常见问题与解决方案

Token 认证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 硬件安全模块

硬件安全模块是物联网安全的重要组成部分。本节详细介绍硬件安全模块的核心概念、工作原理和实际应用。

**关键要点**：

- 硬件安全模块的定义与核心原理
- 硬件安全模块的实现方式与技术细节
- 硬件安全模块在实际场景中的应用与最佳实践
- 硬件安全模块的常见问题与解决方案

硬件安全模块在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 通信安全

### 2.1 TLS 1.3

TLS 1.3是物联网安全的重要组成部分。本节详细介绍TLS 1.3的核心概念、工作原理和实际应用。

**关键要点**：

- TLS 1.3的定义与核心原理
- TLS 1.3的实现方式与技术细节
- TLS 1.3在实际场景中的应用与最佳实践
- TLS 1.3的常见问题与解决方案

TLS 1.3在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 DTLS

DTLS是物联网安全的重要组成部分。本节详细介绍DTLS的核心概念、工作原理和实际应用。

**关键要点**：

- DTLS的定义与核心原理
- DTLS的实现方式与技术细节
- DTLS在实际场景中的应用与最佳实践
- DTLS的常见问题与解决方案

DTLS在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 PSK 与证书

PSK 与证书是物联网安全的重要组成部分。本节详细介绍PSK 与证书的核心概念、工作原理和实际应用。

**关键要点**：

- PSK 与证书的定义与核心原理
- PSK 与证书的实现方式与技术细节
- PSK 与证书在实际场景中的应用与最佳实践
- PSK 与证书的常见问题与解决方案

PSK 与证书在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 固件安全

### 3.1 固件签名

固件签名是物联网安全的重要组成部分。本节详细介绍固件签名的核心概念、工作原理和实际应用。

**关键要点**：

- 固件签名的定义与核心原理
- 固件签名的实现方式与技术细节
- 固件签名在实际场景中的应用与最佳实践
- 固件签名的常见问题与解决方案

固件签名在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 安全启动

安全启动是物联网安全的重要组成部分。本节详细介绍安全启动的核心概念、工作原理和实际应用。

**关键要点**：

- 安全启动的定义与核心原理
- 安全启动的实现方式与技术细节
- 安全启动在实际场景中的应用与最佳实践
- 安全启动的常见问题与解决方案

安全启动在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 OTA 安全更新

OTA 安全更新是物联网安全的重要组成部分。本节详细介绍OTA 安全更新的核心概念、工作原理和实际应用。

**关键要点**：

- OTA 安全更新的定义与核心原理
- OTA 安全更新的实现方式与技术细节
- OTA 安全更新在实际场景中的应用与最佳实践
- OTA 安全更新的常见问题与解决方案

OTA 安全更新在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 安全框架

### 4.1 NIST IoT 安全

NIST IoT 安全是物联网安全的重要组成部分。本节详细介绍NIST IoT 安全的核心概念、工作原理和实际应用。

**关键要点**：

- NIST IoT 安全的定义与核心原理
- NIST IoT 安全的实现方式与技术细节
- NIST IoT 安全在实际场景中的应用与最佳实践
- NIST IoT 安全的常见问题与解决方案

NIST IoT 安全在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 IEC 62443

IEC 62443是物联网安全的重要组成部分。本节详细介绍IEC 62443的核心概念、工作原理和实际应用。

**关键要点**：

- IEC 62443的定义与核心原理
- IEC 62443的实现方式与技术细节
- IEC 62443在实际场景中的应用与最佳实践
- IEC 62443的常见问题与解决方案

IEC 62443在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：035-iot/018-MainstreamIoTPlatforms.md ============ -->



## 1. AWS IoT Core

### 1.1 Device Gateway

Device Gateway是主流IoT平台的重要组成部分。本节详细介绍Device Gateway的核心概念、工作原理和实际应用。

**关键要点**：

- Device Gateway的定义与核心原理
- Device Gateway的实现方式与技术细节
- Device Gateway在实际场景中的应用与最佳实践
- Device Gateway的常见问题与解决方案

Device Gateway在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Rules Engine

Rules Engine是主流IoT平台的重要组成部分。本节详细介绍Rules Engine的核心概念、工作原理和实际应用。

**关键要点**：

- Rules Engine的定义与核心原理
- Rules Engine的实现方式与技术细节
- Rules Engine在实际场景中的应用与最佳实践
- Rules Engine的常见问题与解决方案

Rules Engine在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 Device Shadow

Device Shadow是主流IoT平台的重要组成部分。本节详细介绍Device Shadow的核心概念、工作原理和实际应用。

**关键要点**：

- Device Shadow的定义与核心原理
- Device Shadow的实现方式与技术细节
- Device Shadow在实际场景中的应用与最佳实践
- Device Shadow的常见问题与解决方案

Device Shadow在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Azure IoT Hub

### 2.1 设备孪生

设备孪生是主流IoT平台的重要组成部分。本节详细介绍设备孪生的核心概念、工作原理和实际应用。

**关键要点**：

- 设备孪生的定义与核心原理
- 设备孪生的实现方式与技术细节
- 设备孪生在实际场景中的应用与最佳实践
- 设备孪生的常见问题与解决方案

设备孪生在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 消息路由

消息路由是主流IoT平台的重要组成部分。本节详细介绍消息路由的核心概念、工作原理和实际应用。

**关键要点**：

- 消息路由的定义与核心原理
- 消息路由的实现方式与技术细节
- 消息路由在实际场景中的应用与最佳实践
- 消息路由的常见问题与解决方案

消息路由在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 IoT Edge

IoT Edge是主流IoT平台的重要组成部分。本节详细介绍IoT Edge的核心概念、工作原理和实际应用。

**关键要点**：

- IoT Edge的定义与核心原理
- IoT Edge的实现方式与技术细节
- IoT Edge在实际场景中的应用与最佳实践
- IoT Edge的常见问题与解决方案

IoT Edge在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 阿里云 IoT

### 3.1 物模型

物模型是主流IoT平台的重要组成部分。本节详细介绍物模型的核心概念、工作原理和实际应用。

**关键要点**：

- 物模型的定义与核心原理
- 物模型的实现方式与技术细节
- 物模型在实际场景中的应用与最佳实践
- 物模型的常见问题与解决方案

物模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 规则引擎

规则引擎是主流IoT平台的重要组成部分。本节详细介绍规则引擎的核心概念、工作原理和实际应用。

**关键要点**：

- 规则引擎的定义与核心原理
- 规则引擎的实现方式与技术细节
- 规则引擎在实际场景中的应用与最佳实践
- 规则引擎的常见问题与解决方案

规则引擎在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 设备认证

设备认证是主流IoT平台的重要组成部分。本节详细介绍设备认证的核心概念、工作原理和实际应用。

**关键要点**：

- 设备认证的定义与核心原理
- 设备认证的实现方式与技术细节
- 设备认证在实际场景中的应用与最佳实践
- 设备认证的常见问题与解决方案

设备认证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 平台对比

### 4.1 功能对比

功能对比是主流IoT平台的重要组成部分。本节详细介绍功能对比的核心概念、工作原理和实际应用。

**关键要点**：

- 功能对比的定义与核心原理
- 功能对比的实现方式与技术细节
- 功能对比在实际场景中的应用与最佳实践
- 功能对比的常见问题与解决方案

功能对比在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 定价模型

定价模型是主流IoT平台的重要组成部分。本节详细介绍定价模型的核心概念、工作原理和实际应用。

**关键要点**：

- 定价模型的定义与核心原理
- 定价模型的实现方式与技术细节
- 定价模型在实际场景中的应用与最佳实践
- 定价模型的常见问题与解决方案

定价模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 选型建议

选型建议是主流IoT平台的重要组成部分。本节详细介绍选型建议的核心概念、工作原理和实际应用。

**关键要点**：

- 选型建议的定义与核心原理
- 选型建议的实现方式与技术细节
- 选型建议在实际场景中的应用与最佳实践
- 选型建议的常见问题与解决方案

选型建议在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：035-iot/019-DigitalTwin.md ============ -->



## 1. 数字孪生概念

### 1.1 定义与层次

定义与层次是数字孪生的重要组成部分。本节详细介绍定义与层次的核心概念、工作原理和实际应用。

**关键要点**：

- 定义与层次的定义与核心原理
- 定义与层次的实现方式与技术细节
- 定义与层次在实际场景中的应用与最佳实践
- 定义与层次的常见问题与解决方案

定义与层次在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 核心能力

核心能力是数字孪生的重要组成部分。本节详细介绍核心能力的核心概念、工作原理和实际应用。

**关键要点**：

- 核心能力的定义与核心原理
- 核心能力的实现方式与技术细节
- 核心能力在实际场景中的应用与最佳实践
- 核心能力的常见问题与解决方案

核心能力在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Azure Digital Twins

### 2.1 DTDL 模型

DTDL 模型是数字孪生的重要组成部分。本节详细介绍DTDL 模型的核心概念、工作原理和实际应用。

**关键要点**：

- DTDL 模型的定义与核心原理
- DTDL 模型的实现方式与技术细节
- DTDL 模型在实际场景中的应用与最佳实践
- DTDL 模型的常见问题与解决方案

DTDL 模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 孪生图

孪生图是数字孪生的重要组成部分。本节详细介绍孪生图的核心概念、工作原理和实际应用。

**关键要点**：

- 孪生图的定义与核心原理
- 孪生图的实现方式与技术细节
- 孪生图在实际场景中的应用与最佳实践
- 孪生图的常见问题与解决方案

孪生图在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 事件路由

事件路由是数字孪生的重要组成部分。本节详细介绍事件路由的核心概念、工作原理和实际应用。

**关键要点**：

- 事件路由的定义与核心原理
- 事件路由的实现方式与技术细节
- 事件路由在实际场景中的应用与最佳实践
- 事件路由的常见问题与解决方案

事件路由在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. ThingWorx

### 3.1 模型与实体

模型与实体是数字孪生的重要组成部分。本节详细介绍模型与实体的核心概念、工作原理和实际应用。

**关键要点**：

- 模型与实体的定义与核心原理
- 模型与实体的实现方式与技术细节
- 模型与实体在实际场景中的应用与最佳实践
- 模型与实体的常见问题与解决方案

模型与实体在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 可视化仪表盘

可视化仪表盘是数字孪生的重要组成部分。本节详细介绍可视化仪表盘的核心概念、工作原理和实际应用。

**关键要点**：

- 可视化仪表盘的定义与核心原理
- 可视化仪表盘的实现方式与技术细节
- 可视化仪表盘在实际场景中的应用与最佳实践
- 可视化仪表盘的常见问题与解决方案

可视化仪表盘在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 应用场景

### 4.1 智能制造

智能制造是数字孪生的重要组成部分。本节详细介绍智能制造的核心概念、工作原理和实际应用。

**关键要点**：

- 智能制造的定义与核心原理
- 智能制造的实现方式与技术细节
- 智能制造在实际场景中的应用与最佳实践
- 智能制造的常见问题与解决方案

智能制造在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 智慧城市

智慧城市是数字孪生的重要组成部分。本节详细介绍智慧城市的核心概念、工作原理和实际应用。

**关键要点**：

- 智慧城市的定义与核心原理
- 智慧城市的实现方式与技术细节
- 智慧城市在实际场景中的应用与最佳实践
- 智慧城市的常见问题与解决方案

智慧城市在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 预测性维护

预测性维护是数字孪生的重要组成部分。本节详细介绍预测性维护的核心概念、工作原理和实际应用。

**关键要点**：

- 预测性维护的定义与核心原理
- 预测性维护的实现方式与技术细节
- 预测性维护在实际场景中的应用与最佳实践
- 预测性维护的常见问题与解决方案

预测性维护在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：035-iot/020-MosquittoBrokerManage.md ============ -->


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



<!-- ============ 文档分隔线：035-iot/021-MosquittoPub.md ============ -->


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



<!-- ============ 文档分隔线：035-iot/022-MosquittoSub.md ============ -->


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



<!-- ============ 文档分隔线：035-iot/023-ESP32Setup.md ============ -->


## Arduino IDE 配置

**基本写法：添加 ESP32 板支持 URL**
`https://dl.espressif.com/dl/package_esp32_index.json`
```bash
# 在首选项附加开发板管理器 URL 添加
https://dl.espressif.com/dl/package_esp32_index.json
```

---

**基本写法：通过 Boards Manager 安装**
`esp32 by Espressif Systems`
```bash
# 在开发板管理器搜索 esp32 并安装
esp32 by Espressif Systems
```

---

**基本写法：指定 ESP32 板型号**
`Tools -> Board -> ESP32 Arduino -> <板型>`
```bash
# 选择对应的 ESP32 开发板型号
ESP32 Dev Module
```

---

**基本写法：选择端口**
`Tools -> Port -> <COM 端口>`
```bash
# 选择连接的串口
COM3
```

---

## arduino-cli 命令

**基本写法：安装 arduino-cli**
`go install github.com/arduino/arduino-cli@latest`
```bash
# 通过 Go 安装 arduino-cli
go install github.com/arduino/arduino-cli@latest
```

---

**基本写法：更新核心索引**
`arduino-cli core update-index`
```bash
# 更新所有板支持索引
arduino-cli core update-index
```

---

**基本写法：添加 ESP32 索引**
`arduino-cli core update-index --additional-urls <URL>`
```bash
# 通过命令行添加 ESP32 URL
arduino-cli core update-index --additional-urls "https://dl.espressif.com/dl/package_esp32_index.json"
```

---

**基本写法：搜索 ESP32 核心**
`arduino-cli core search esp32`
```bash
# 搜索可用的 ESP32 板包
arduino-cli core search esp32
```

---

**基本写法：安装 ESP32 核心**
`arduino-cli core install esp32:esp32`
```bash
# 安装 ESP32 板支持包
arduino-cli core install esp32:esp32
```

---

**基本写法：列出已安装核心**
`arduino-cli core list`
```bash
# 查看所有已安装板支持包
arduino-cli core list
```

---

## 板与端口管理

**基本写法：列出已连接板**
`arduino-cli board list`
```bash
# 列出所有连接的开发板
arduino-cli board list
```

---

**基本写法：列出所有板型号**
`arduino-cli board listall esp32`
```bash
# 列出所有 ESP32 系列 board ID
arduino-cli board listall esp32
```

---

**基本写法：编译 sketch**
`arduino-cli compile --fqbn esp32:esp32:esp32 <sketch 目录>`
```bash
# 编译 ESP32 项目
arduino-cli compile --fqbn esp32:esp32:esp32 my-sketch
```

---

**基本写法：上传 sketch**
`arduino-cli upload -p <端口> --fqbn esp32:esp32:esp32 <sketch 目录>`
```bash
# 上传到 ESP32 板
arduino-cli upload -p COM3 --fqbn esp32:esp32:esp32 my-sketch
```

---

## 库管理

**基本写法：搜索库**
`arduino-cli lib search <关键词>`
```bash
# 搜索 MQTT 相关库
arduino-cli lib search "PubSubClient"
```

---

**基本写法：安装库**
`arduino-cli lib install "<库名>"`
```bash
# 安装 PubSubClient MQTT 库
arduino-cli lib install "PubSubClient"
```

---

**基本写法：列出已安装库**
`arduino-cli lib list`
```bash
# 查看所有已安装库
arduino-cli lib list
```

---

**基本写法：升级库**
`arduino-cli lib upgrade [<库名>]`
```bash
# 升级所有库到最新
arduino-cli lib upgrade
```

---

**基本写法：卸载库**
`arduino-cli lib uninstall "<库名>"`
```bash
# 卸载不再需要的库
arduino-cli lib uninstall "PubSubClient"
```

---

## ESP-IDF 环境

**基本写法：安装 ESP-IDF 依赖**
`sudo apt-get install gcc git make ncurses flex bison gperf`
```bash
# 在 Linux 安装 ESP-IDF 必需工具
sudo apt-get install gcc git make ncurses flex bison gperf
```

---

**基本写法：克隆 ESP-IDF**
`git clone --recursive https://github.com/espressif/esp-idf.git`
```bash
# 克隆 ESP-IDF 仓库含子模块
git clone --recursive https://github.com/espressif/esp-idf.git
```

---

**基本写法：安装 ESP-IDF 工具链**
`./install.sh esp32`
```bash
# 在 esp-idf 目录执行安装脚本
./install.sh esp32
```

---

**基本写法：激活 ESP-IDF 环境**
`. ./export.sh`
```bash
# 在新终端激活 ESP-IDF 环境变量
. ./export.sh
```

---

## idf.py 命令

**基本写法：创建项目**
`idf.py create-project <项目名>`
```bash
# 从模板创建 ESP-IDF 项目
idf.py create-project my-project
```

---

**基本写法：设置目标芯片**
`idf.py set-target esp32`
```bash
# 设置目标芯片为 ESP32
idf.py set-target esp32
```

---

**基本写法：编译项目**
`idf.py build`
```bash
# 编译 ESP-IDF 项目
idf.py build
```

---

**基本写法：烧录固件**
`idf.py -p <端口> flash`
```bash
# 烧录到 ESP32
idf.py -p /dev/ttyUSB0 flash
```

---

**基本写法：监视串口**
`idf.py -p <端口> monitor`
```bash
# 监视 ESP32 串口输出
idf.py -p /dev/ttyUSB0 monitor
```

---

**基本写法：编译烧录监视一条命令**
`idf.py -p <端口> build flash monitor`
```bash
# 编译烧录并自动监视
idf.py -p /dev/ttyUSB0 build flash monitor
```

---

**基本写法：清除构建**
`idf.py fullclean`
```bash
# 完全清除构建目录
idf.py fullclean
```

---

## esptool 工具

**基本写法：查看芯片信息**
`esptool.py --port <端口> chip_id`
```bash
# 读取 ESP32 芯片 ID
esptool.py --port /dev/ttyUSB0 chip_id
```

---

**基本写法：擦除整个 Flash**
`esptool.py --port <端口> erase_flash`
```bash
# 擦除 ESP32 整个 flash
esptool.py --port /dev/ttyUSB0 erase_flash
```

---

**基本写法：写入固件**
`esptool.py --port <端口> --baud <波特率> write_flash 0x10000 <固件.bin>`
```bash
# 烧录编译好的 bin 固件
esptool.py --port /dev/ttyUSB0 --baud 921600 write_flash 0x10000 firmware.bin
```



<!-- ============ 文档分隔线：035-iot/024-ESP32GPIOPinout.md ============ -->


## 引脚模式

**基本写法：设置为输出**
`pinMode(<引脚>, OUTPUT);`
```cpp
// 配置 GPIO2 为输出驱动 LED
pinMode(2, OUTPUT);
```

---

**基本写法：设置为输入**
`pinMode(<引脚>, INPUT);`
```cpp
// 配置 GPIO4 为输入读取按钮
pinMode(4, INPUT);
```

---

**基本写法：启用内部上拉**
`pinMode(<引脚>, INPUT_PULLUP);`
```cpp
// 启用内部上拉电阻
pinMode(4, INPUT_PULLUP);
```

---

**基本写法：启用内部下拉**
`pinMode(<引脚>, INPUT_PULLDOWN);`
```cpp
// 启用内部下拉电阻
pinMode(4, INPUT_PULLDOWN);
```

---

## 数字 IO

**基本写法：数字写**
`digitalWrite(<引脚>, <电平>);`
```cpp
// 点亮 GPIO2 上的 LED
digitalWrite(2, HIGH);
```

---

**基本写法：数字读**
`digitalRead(<引脚>)`
```cpp
// 读取 GPIO4 的电平
int v = digitalRead(4);
```

---

## ADC 模拟输入

**基本写法：读取 ADC 值**
`analogRead(<引脚>)`
```cpp
// 读取 GPIO32 的模拟值
int v = analogRead(32);
```

---

**基本写法：设置 ADC 分辨率**
`analogReadResolution(<位数>);`
```cpp
// 设置 12 位分辨率 0-4095
analogReadResolution(12);
```

---

**基本写法：设置 ADC 衰减**
`analogSetPinAttenuation(<引脚>, <衰减>);`
```cpp
// 设置 ADC_11db 扩展量程到 3.3V
analogSetPinAttenuation(32, ADC_11db);
```

---

**基本写法：ADC 引脚对应**
```cpp
// ESP32 ADC1 通道与 GPIO 映射
// ADC1_CH0 = GPIO36
// ADC1_CH3 = GPIO39
// ADC1_CH4 = GPIO32
// ADC1_CH5 = GPIO33
// ADC1_CH6 = GPIO34
// ADC1_CH7 = GPIO35
```

---

## DAC 输出

**基本写法：DAC 输出**
`dacWrite(<引脚>, <值>);`
```cpp
// GPIO25 输出 8 位模拟值
dacWrite(25, 128);
```

---

**基本写法：关闭 DAC**
`dacWrite(<引脚>, 0);`
```cpp
// 设置为 0 等同关闭 DAC
dacWrite(25, 0);
```

---

**基本写法：DAC 引脚**
```cpp
// ESP32 内置 2 路 DAC
// DAC1 = GPIO25
// DAC2 = GPIO26
```

---

## PWM 输出

**基本写法：配置 LEDC 通道**
`ledcSetup(<通道>, <频率>, <分辨率>);`
```cpp
// 配置通道 0 频率 5000Hz 8 位分辨率
ledcSetup(0, 5000, 8);
```

---

**基本写法：附加引脚到通道**
`ledcAttachPin(<引脚>, <通道>);`
```cpp
// 将 GPIO2 附加到通道 0
ledcAttachPin(2, 0);
```

---

**基本写法：输出 PWM**
`ledcWrite(<通道>, <占空比>);`
```cpp
// 通道 0 输出占空比 128
ledcWrite(0, 128);
```

---

**基本写法：分离引脚**
`ledcDetachPin(<引脚>);`
```cpp
// 释放 GPIO2
ledcDetachPin(2);
```

---

## 触摸传感

**基本写法：读取触摸值**
`touchRead(<引脚>)`
```cpp
// 读取 GPIO4 触摸传感值
int v = touchRead(4);
```

---

**基本写法：触摸引脚映射**
```cpp
// ESP32 触摸引脚与 GPIO 对应
// T0 = GPIO4
// T1 = GPIO0
// T2 = GPIO2
// T3 = GPIO15
// T4 = GPIO13
// T5 = GPIO12
// T6 = GPIO14
// T7 = GPIO27
```

---

**基本写法：设置触摸阈值**
`touchSetCycles(<设定值>, <测量值>);`
```cpp
// 调整触摸灵敏度
touchSetCycles(0x1000, 0x1000);
```

---

## 中断

**基本写法：附加中断**
`attachInterrupt(<引脚>, <回调>, <模式>);`
```cpp
// GPIO4 下降沿触发 ISR
attachInterrupt(4, myISR, FALLING);
```

---

**基本写法：分离中断**
`detachInterrupt(<引脚>);`
```cpp
// 移除 GPIO4 中断
detachInterrupt(4);
```

---

**基本写法：volatile 变量**
`volatile <类型> <变量名>;`
```cpp
// 中断与主循环共享变量必须 volatile
volatile bool flag = false;
```

---

## 引脚约束

**基本写法：安全输入输出引脚**
```cpp
// ESP32 推荐安全使用的 GPIO
// GPIO 2 4 5 12 13 14 15 16 17 18 19 21 22 23 25 26 27 32 33
```

---

**基本写法：仅输入引脚**
```cpp
// GPIO 34 35 36 39 仅能作为输入
// 无内部上拉下拉电阻
int v = analogRead(34);
```

---

**基本写法：禁用引脚**
```cpp
// GPIO 6-11 连接 SPI Flash 不可使用
// GPIO 0 1 3 5 14 15 启动时需注意状态
```

---

**基本写法：启动引脚约束**
```cpp
// 启动时必须为特定状态的引脚
// GPIO0 高进入运行模式低进入下载模式
// GPIO2 上电时必须为低电平
// GPIO12 启动时低电平否则启动失败
```

---

## RTC GPIO

**基本写法：RTC GPIO 唤醒**
`esp_sleep_enable_ext0_wakeup(<引脚>, <电平>);`
```cpp
// 配置 GPIO13 高电平唤醒
esp_sleep_enable_ext0_wakeup(GPIO_NUM_13, 1);
```

---

**基本写法：进入深度睡眠**
`esp_deep_sleep_start();`
```cpp
// 进入深度睡眠等待唤醒
esp_deep_sleep_start();
```

---

**基本写法：定时唤醒**
`esp_sleep_enable_timer_wakeup(<微秒>);`
```cpp
// 10 秒后唤醒
esp_sleep_enable_timer_wakeup(10 * 1000000);
```

---

## 引脚重映射

**基本写法：使用宏定义引脚**
```cpp
// 使用宏便于引脚重映射
#define LED_PIN 2
#define BUTTON_PIN 4
void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}
```



<!-- ============ 文档分隔线：035-iot/025-ESP32I2C.md ============ -->


## I2C 初始化

**基本写法：包含 Wire 库**
`#include <Wire.h>`
```cpp
// 引入 Arduino 标准的 Wire 库
#include <Wire.h>
```

---

**基本写法：以默认引脚初始化**
`Wire.begin();`
```cpp
// 主模式使用默认 SDA=21 SCL=22
Wire.begin();
```

---

**基本写法：指定引脚初始化**
`Wire.begin(<SDA>, <SCL>);`
```cpp
// 自定义 SDA=GPIO26 SCL=GPIO27
Wire.begin(26, 27);
```

---

**基本写法：从机模式初始化**
`Wire.begin(<从机地址>);`
```cpp
// 作为 I2C 从机地址 0x08
Wire.begin(0x08);
```

---

**基本写法：设置时钟频率**
`Wire.setClock(<频率>);`
```cpp
// 设置 I2C 时钟为 400kHz 快速模式
Wire.setClock(400000);
```

---

**基本写法：设置超时**
`Wire.setTimeOut(<毫秒>);`
```cpp
// 设置总线超时 100ms
Wire.setTimeOut(100);
```

---

## 主机写操作

**基本写法：开始传输**
`Wire.beginTransmission(<地址>);`
```cpp
// 向地址 0x68 开始传输
Wire.beginTransmission(0x68);
```

---

**基本写法：写入单字节**
`Wire.write(<字节>);`
```cpp
// 写入寄存器地址 0x3B
Wire.write(0x3B);
```

---

**基本写法：写入多字节**
`Wire.write(<缓冲区>, <长度>);`
```cpp
// 写入字节数组
Wire.write(data, sizeof(data));
```

---

**基本写法：结束传输**
`Wire.endTransmission();`
```cpp
// 结束并发送数据返回状态码
int status = Wire.endTransmission();
```

---

**基本写法：结束保持连接**
`Wire.endTransmission(false);`
```cpp
// 发送重复起始位不发送停止位
Wire.endTransmission(false);
```

---

## 主机读操作

**基本写法：请求读取**
`Wire.requestFrom(<地址>, <字节数>);`
```cpp
// 从地址 0x68 请求 6 字节
Wire.requestFrom(0x68, 6);
```

---

**基本写法：检查可读字节**
`Wire.available()`
```cpp
// 返回缓冲区可读字节数
int n = Wire.available();
```

---

**基本写法：读取单字节**
`Wire.read()`
```cpp
// 读取一个字节
int b = Wire.read();
```

---

**基本写法：读取多字节**
```cpp
// 循环读取所有可用字节
while (Wire.available()) {
  byte b = Wire.read();
}
```

---

## 寄存器读写

**基本写法：写入寄存器**
```cpp
// 向指定寄存器写入一个字节
Wire.beginTransmission(0x68);
Wire.write(0x6B);
Wire.write(0x00);
Wire.endTransmission();
```

---

**基本写法：读取寄存器**
```cpp
// 从指定寄存器读取一个字节
Wire.beginTransmission(0x68);
Wire.write(0x75);
Wire.endTransmission(false);
Wire.requestFrom(0x68, 1);
uint8_t whoami = Wire.read();
```

---

**基本写法：读取多字节寄存器**
```cpp
// 连续读取多个寄存器值
Wire.beginTransmission(0x68);
Wire.write(0x3B);
Wire.endTransmission(false);
Wire.requestFrom(0x68, 6);
for (int i = 0; i < 6; i++) {
  data[i] = Wire.read();
}
```

---

## 从机模式

**基本写法：注册接收事件**
`Wire.onReceive(<回调>);`
```cpp
// 主机写入时触发回调
Wire.onReceive(receiveEvent);
```

---

**基本写法：注册请求事件**
`Wire.onRequest(<回调>);`
```cpp
// 主机请求读取时触发
Wire.onRequest(requestEvent);
```

---

**基本写法：接收事件回调**
```cpp
// 主机写入数据时被调用
void receiveEvent(int howMany) {
  while (Wire.available()) {
    byte b = Wire.read();
  }
}
```

---

**基本写法：请求事件回调**
```cpp
// 主机请求时返回数据
void requestEvent() {
  Wire.write("hello");
}
```

---

## 扫描设备

**基本写法：扫描 I2C 设备**
```cpp
// 扫描 1-127 地址查找连接设备
for (byte addr = 1; addr < 127; addr++) {
  Wire.beginTransmission(addr);
  if (Wire.endTransmission() == 0) {
    Serial.print("Found: 0x");
    Serial.println(addr, HEX);
  }
}
```

---

**基本写法：检测设备存在**
```cpp
// 检测指定地址设备是否响应
bool deviceExists(uint8_t addr) {
  Wire.beginTransmission(addr);
  return Wire.endTransmission() == 0;
}
```

---

## 常见传感器

**基本写法：BME280 读取**
```cpp
// 通过 I2C 读取 BME280 温湿度气压
#include <Adafruit_BME280.h>
Adafruit_BME280 bme;
bool ok = bme.begin(0x76);
float temp = bme.readTemperature();
```

---

**基本写法：MPU6050 加速度计**
```cpp
// 读取 MPU6050 加速度陀螺仪数据
Wire.beginTransmission(0x68);
Wire.write(0x3B);
Wire.endTransmission(false);
Wire.requestFrom(0x68, 14);
int16_t ax = (Wire.read() << 8) | Wire.read();
```

---

**基本写法：OLED 显示屏初始化**
```cpp
// 初始化 SSD1306 0.96 OLED 显示
#include <Adafruit_SSD1306.h>
Adafruit_SSD1306 display(128, 64, &Wire, -1);
display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
```

---

## 错误处理

**基本写法：检查传输状态码**
```cpp
// 检查 endTransmission 返回值
int status = Wire.endTransmission();
// 0 成功 1 数据太长 2 收到 NACK 地址 3 收到 NACK 数据 4 其他错误
```

---

**基本写法：读取超时保护**
```cpp
// 防止 I2C 阻塞的超时保护
unsigned long start = millis();
while (Wire.available() < 6) {
  if (millis() - start > 1000) return false;
  delay(1);
}
```

---

## 多路 I2C 总线

**基本写法：创建第二路 I2C**
```cpp
// ESP32 使用第二路 I2C 总线
TwoWire I2C2 = TwoWire(1);
I2C2.begin(SDA2, SCL2, 400000);
```

---

**基本写法：分别使用两路 I2C**
```cpp
// 主总线读取传感器
Wire.beginTransmission(0x68);
// 副总线读取另一组传感器
I2C2.beginTransmission(0x76);
```



<!-- ============ 文档分隔线：035-iot/026-ESP32SPIUART.md ============ -->


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



<!-- ============ 文档分隔线：035-iot/027-ESP32WiFiConfig.md ============ -->


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



<!-- ============ 文档分隔线：035-iot/028-ESP32OTA.md ============ -->


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
