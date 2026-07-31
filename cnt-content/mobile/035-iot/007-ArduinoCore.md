# 物联网 Arduino 核心语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
