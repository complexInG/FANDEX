# 物联网 ESP32 开发环境

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
