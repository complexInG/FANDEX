# 物联网 MQTT 主题与通配符

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
