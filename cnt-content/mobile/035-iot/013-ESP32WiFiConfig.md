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
