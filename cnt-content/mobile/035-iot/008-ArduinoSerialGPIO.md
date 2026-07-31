# 物联网 Arduino 串口与 GPIO

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 串口初始化

**基本写法：开启串口**
`Serial.begin(<波特率>);`
```cpp
// 初始化串口 9600 波特率
Serial.begin(9600);
```

---

**基本写法：高频波特率**
`Serial.begin(<波特率>);`
```cpp
// 调试输出使用 115200 波特率
Serial.begin(115200);
```

---

**基本写法：等待串口就绪**
`while (!Serial);`
```cpp
// 仅 Leonardo Micro 需要等待 USB CDC
while (!Serial) {
}
```

---

**基本写法：结束串口**
`Serial.end();`
```cpp
// 释放串口资源用于其他用途
Serial.end();
```

---

## 串口输出

**基本写法：打印字符串**
`Serial.print("<字符串>");`
```cpp
// 输出不换行
Serial.print("Hello");
```

---

**基本写法：打印并换行**
`Serial.println("<字符串>");`
```cpp
// 输出并换行
Serial.println("Hello, World!");
```

---

**基本写法：打印数字指定进制**
`Serial.print(<值>, <进制>);`
```cpp
// 以十六进制输出
Serial.print(255, HEX);
```

---

**基本写法：打印浮点数小数位**
`Serial.print(<值>, <位数>);`
```cpp
// 保留两位小数
Serial.print(23.5678, 2);
```

---

**基本写法：写入单字节**
`Serial.write(<字节>);`
```cpp
// 写入原始字节 0x41
Serial.write(0x41);
```

---

**基本写法：写入字节数组**
`Serial.write(<数组>, <长度>);`
```cpp
// 写入二进制数据
Serial.write(buffer, sizeof(buffer));
```

---

## 串口输入

**基本写法：检查可读字节数**
`Serial.available()`
```cpp
// 返回缓冲区字节数
int count = Serial.available();
```

---

**基本写法：读取单字节**
`Serial.read()`
```cpp
// 读取一个字节返回 -1 表示无数据
int c = Serial.read();
```

---

**基本写法：读取一行**
`Serial.readStringUntil('<终止符>')`
```cpp
// 读取到换行符为止
String line = Serial.readStringUntil('\n');
```

---

**基本写法：超时读取字符串**
`Serial.readString()`
```cpp
// 读取整个字符串受超时影响
String data = Serial.readString();
```

---

**基本写法：解析整数**
`Serial.parseInt()`
```cpp
// 从串口流解析整数
int value = Serial.parseInt();
```

---

**基本写法：解析浮点数**
`Serial.parseFloat()`
```cpp
// 从串口流解析浮点数
float value = Serial.parseFloat();
```

---

**基本写法：窥视下一字节**
`Serial.peek()`
```cpp
// 读取但不移除缓冲区首字节
int c = Serial.peek();
```

---

**基本写法：清空缓冲区**
`Serial.flush();`
```cpp
// 等待发送完成清空发送缓冲
Serial.flush();
```

---

## 软件串口

**基本写法：包含软件串口库**
`#include <SoftwareSerial.h>`
```cpp
// 引入软串口库
#include <SoftwareSerial.h>
```

---

**基本写法：创建软串口**
`SoftwareSerial <名称>(<RX>, <TX>);`
```cpp
// 在引脚 10 RX 11 TX 创建软串口
SoftwareSerial mySerial(10, 11);
```

---

**基本写法：初始化软串口**
`<名称>.begin(<波特率>);`
```cpp
// 软串口以 9600 波特率开始
mySerial.begin(9600);
```

---

**基本写法：软串口监听**
`<名称>.listen();`
```cpp
// 多软串口时启用当前串口
mySerial.listen();
```

---

## GPIO 数字操作

**基本写法：配置引脚模式**
`pinMode(<引脚>, <模式>);`
```cpp
// 设置引脚 7 为输出
pinMode(7, OUTPUT);
```

---

**基本写法：数字写**
`digitalWrite(<引脚>, <电平>);`
```cpp
// 引脚 7 输出高电平
digitalWrite(7, HIGH);
```

---

**基本写法：数字读**
`digitalRead(<引脚>)`
```cpp
// 读取引脚 2 的电平
int v = digitalRead(2);
```

---

**基本写法：引脚号转换**
`digitalPinToInterrupt(<引脚>)`
```cpp
// 将数字引脚转为中断号
int irq = digitalPinToInterrupt(2);
```

---

## 模拟输入

**基本写法：读取模拟值**
`analogRead(<引脚>)`
```cpp
// 读取 A0 上的模拟电压
int v = analogRead(A0);
```

---

**基本写法：多通道读取**
```cpp
// 依次读取多个模拟通道
for (int i = A0; i <= A3; i++) {
  int v = analogRead(i);
}
```

---

## PWM 输出

**基本写法：PWM 输出**
`analogWrite(<引脚>, <值>);`
```cpp
// 引脚 9 输出占空比 50%
analogWrite(9, 128);
```

---

**基本写法：PWM 呼吸灯**
```cpp
// 渐亮渐暗呼吸灯效果
for (int i = 0; i <= 255; i++) {
  analogWrite(9, i);
  delay(10);
}
```

---

**基本写法：关闭 PWM**
`analogWrite(<引脚>, 0);`
```cpp
// 占空比为 0 等同关闭
analogWrite(9, 0);
```

---

## 脉冲测量

**基本写法：测量脉冲宽度**
`pulseIn(<引脚>, <电平> [, <超时>])`
```cpp
// 测量高电平持续微秒数
unsigned long t = pulseIn(7, HIGH);
```

---

**基本写法：测量长脉冲带超时**
`pulseIn(<引脚>, <电平>, <超时>)`
```cpp
// 超时 100000 微秒即 100ms
unsigned long t = pulseIn(7, HIGH, 100000);
```

---

**基本写法：tone 输出**
`tone(<引脚>, <频率> [, <时长>])`
```cpp
// 在引脚 8 输出 440Hz 蜂鸣
tone(8, 440);
```

---

**基本写法：关闭 tone**
`noTone(<引脚>);`
```cpp
// 停止蜂鸣器输出
noTone(8);
```

---

## 移位寄存器

**基本写法：移位输出**
`shiftOut(<数据引脚>, <时钟引脚>, <顺序>, <数据>)`
```cpp
// 串行输出 8 位数据到 74HC595
shiftOut(dataPin, clockPin, MSBFIRST, 0xFF);
```

---

**基本写法：移位输入**
`shiftIn(<数据引脚>, <时钟引脚>, <顺序>)`
```cpp
// 串行读取 8 位数据
byte data = shiftIn(dataPin, clockPin, MSBFIRST);
```
