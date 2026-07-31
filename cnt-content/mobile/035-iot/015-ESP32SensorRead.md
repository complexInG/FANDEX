# 物联网 ESP32 传感器读取

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
