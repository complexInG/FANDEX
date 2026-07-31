# 物联网 Mosquitto Broker 管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
