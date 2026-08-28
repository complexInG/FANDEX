---
order: 240
title: 物联网 ESP32 GPIO 与引脚
module: 'iot'
category: 云与基础设施
difficulty: beginner
description: 物联网 ESP32 GPIO 与引脚 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

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
