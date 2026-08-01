---
order: 52
title: Arduino开发
module: iot
category: 'eng-infra'
difficulty: beginner
description: Arduino入门：开发环境、编程基础、传感器交互与项目实战详解。
author: fanquanpp
updated: '2026-08-01'
related:
  - iot/MQTT协议
  - iot/CoAP协议
  - iot/ESP32开发
  - 'iot/RT-Thread实时系统'
prerequisites:
  - iot/概述与架构
---
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
| Arduino开发 | 011-ArduinoDevelopment | 本文自身 |
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
| 物联网 ESP32 OTA 更新 | 028-ESP32OTA | 本文的并列主题 |
