# 分布式能力 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 设备管理

**基本写法：获取设备管理器**
`const <dm> = deviceManager.createDeviceManager('<包名>')`
```typescript
// 创建分布式设备管理器
import { deviceManager } from '@kit.DistributedServiceKit'

let dm = deviceManager.createDeviceManager('com.example.myapp')
```

---

**基本写法：监听设备发现**
`<dm>.on('deviceFound', (<回调>))`
```typescript
// 监听设备发现事件
dm.on('deviceFound', (data) => {
  for (let i = 0; i < data.deviceCount; i++) {
    console.info(`发现设备: ${data.deviceInfos[i].deviceName}`)
  }
})
```

---

**基本写法：开始设备发现**
`<dm>.startDeviceDiscovery({ subscribeId: <ID> })`
```typescript
// 开始搜索附近的分布式设备
dm.startDeviceDiscovery({ subscribeId: 1001 })
```

---

**基本写法：停止设备发现**
`<dm>.stopDeviceDiscovery({ subscribeId: <ID> })`
```typescript
// 停止设备搜索
dm.stopDeviceDiscovery({ subscribeId: 1001 })
```

---

**基本写法：获取可信设备列表**
`<dm>.getTrustedDeviceList()`
```typescript
// 获取已建立信任关系的设备
let devices = dm.getTrustedDeviceList()
for (const device of devices) {
  console.info(`设备: ${device.deviceName}, ID: ${device.deviceId}`)
}
```

---

**基本写法：监听设备状态变化**
`<dm>.on('deviceStateChange', (<回调>))`
```typescript
// 监听设备上线/下线
dm.on('deviceStateChange', (data) => {
  if (data.action === 0) {
    console.info(`设备上线: ${data.device.deviceName}`)
  } else if (data.action === 1) {
    console.info(`设备下线: ${data.device.deviceName}`)
  }
})
```

---

## 跨设备迁移

**基本写法：UIAbility 可迁移配置**
`// 在 module.json5 中配置 continuable: true`
```json5
// module.json5 配置可迁移
{
  "abilities": [
    {
      "name": "EntryAbility",
      "continuable": true
    }
  ]
}
```

---

**基本写法：触发迁移**
`this.context.continueAbility('<设备ID>')`
```typescript
// 将 UIAbility 迁移到指定设备
import { AbilityConstant } from '@kit.AbilityKit'

export default class EntryAbility extends UIAbility {
  onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult {
    wantParam['data'] = '迁移数据'
    return AbilityConstant.OnContinueResult.AGREE
  }
}
```

---

**基本写法：接收迁移数据**
`onCreate(<want>, <launchParam>)`
```typescript
// 目标设备接收迁移数据
onCreate(want, launchParam) {
  if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
    let data = want.parameters['data']
    console.info(`收到迁移数据: ${data}`)
  }
}
```

---

**基本写法：恢复页面状态**
`onRestoreData(<wantParam>)`
```typescript
// 在目标设备恢复页面状态
onRestoreData(wantParam: Record<string, Object>): void {
  let savedData = wantParam['savedData']
  // 恢复 UI 状态
}
```

---

## 分布式任务调度

**基本写法：拉起远程 FA**
`FeatureAbility.startAbility({ deviceId: '<设备ID>', bundleName: '<包名>', abilityName: '<Ability名>' })`
```typescript
// 跨设备拉起指定 Ability
import { featureAbility } from '@kit.AbilityKit'

featureAbility.startAbility({
  deviceId: 'remote_device_id',
  bundleName: 'com.example.myapp',
  abilityName: 'EntryAbility'
}).then((data) => {
  console.info('远程启动成功')
})
```

---

**基本写法：连接远程 Service**
`FeatureAbility.connectAbility({ deviceId: '<设备ID>', bundleName: '<包名>', abilityName: '<Service名>' }, <回调>)`
```typescript
// 跨设备连接 Service
let connectionId = featureAbility.connectAbility({
  deviceId: 'remote_device_id',
  bundleName: 'com.example.myapp',
  abilityName: 'ServiceAbility'
}, {
  onConnect: (elementName, remoteProxy) => {
    console.info('远程服务已连接')
  },
  onDisconnect: (elementName) => {
    console.info('远程服务已断开')
  }
})
```

---

**基本写法：断开远程连接**
`featureAbility.disconnectAbility(<连接ID>)`
```typescript
// 断开远程 Service 连接
featureAbility.disconnectAbility(connectionId)
```

---

## 分布式认证

**基本写法：设备互信认证**
`<dm>.authenticateDevice(<设备信息>, <认证回调>)`
```typescript
// 发起设备间互信认证
dm.authenticateDevice(deviceInfo, {
  authType: 1,
  extraInfo: {},
  verify: (err, data) => {
    if (err) {
      console.error('认证失败')
      return
    }
    console.info('认证成功')
  }
})
```

---

**基本写法：取消认证**
`<dm>.unAuthenticateDevice(<设备信息>)`
```typescript
// 取消设备互信关系
dm.unAuthenticateDevice(deviceInfo)
```

---

## 同步调用

**基本写法：远程 RPC 调用**
`<remoteProxy>.sendMessageRequest(<请求>)`
```typescript
// 通过 RPC 代理发送远程请求
import { rpc } from '@kit.IPCKit'

let option = new rpc.MessageOption()
let data = rpc.MessageParcel.create()
data.writeString('hello')
let reply = rpc.MessageParcel.create()

remoteProxy.sendMessageRequest(1, data, reply, option).then((result) => {
  let response = result.reply.readString()
  console.info(`远程响应: ${response}`)
})
```

---

**基本写法：实现远程服务端**
`class <名> extends rpc.RemoteObject { onRemoteRequest(<code>, <data>, <reply>, <option>) { } }`
```typescript
// ServiceAbility 中实现远程接口
class ServiceStub extends rpc.RemoteObject {
  onRemoteRequest(code, data, reply, option): boolean {
    if (code === 1) {
      let msg = data.readString()
      reply.writeString(`echo: ${msg}`)
      return true
    }
    return false
  }
}
```
