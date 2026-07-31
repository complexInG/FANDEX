# 跨设备调用 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## continuationManager 设备选择

**基本写法：注册 continuation**
`continuationManager.register(<选项>, <回调>)`
```typescript
// 注册跨设备迁移管理器
import { continuationManager } from '@kit.DistributedServiceKit'

let token = -1
continuationManager.registerContinuation({
  deviceId: '',
  type: continuationManager.ContinuationDeviceTypes.CONNECTED_SAME_ACCOUNT
}, (err, data) => {
  if (err) { console.error('注册失败'); return }
  token = data
  console.info(`注册成功 token: ${token}`)
})
```

---

**基本写法：拉起设备选择面板**
`continuationManager.startContinuationDeviceManager(<token>, <选项>, <回调>)`
```typescript
// 弹出设备选择 UI
let options: continuationManager.ContinuationExtraOptions = {
  continuationMode: continuationManager.ContinuationMode.COLLABORATION_MUTABLE
}
continuationManager.startContinuationDeviceManager(token, options, (err, data) => {
  if (err) { console.error('取消选择'); return }
  console.info(`已选设备: ${data.deviceId}`)
})
```

---

**基本写法：取消注册**
`continuationManager.unregisterContinuation(<token>)`
```typescript
// 注销迁移管理器
continuationManager.unregisterContinuation(token, (err) => {
  console.info('已注销')
})
```

---

**基本写法：更新连接状态**
`continuationManager.updateContinuationState(<token>, '<设备ID>', <状态>, <回调>)`
```typescript
// 更新设备连接状态
continuationManager.updateContinuationState(token, 'device_id', 1, (err) => {
  console.info('状态已更新')
})
```

---

## 启动远程 Ability

**基本写法：启动远程 UIAbility**
`this.context.startAbility({ deviceId: '<设备ID>', bundleName: '<包名>', abilityName: '<Ability名>' })`
```typescript
// 通过 UIAbility context 拉起远程页面
import { Want } from '@kit.AbilityKit'

let want: Want = {
  deviceId: 'remote_device_id',
  bundleName: 'com.example.myapp',
  abilityName: 'EntryAbility',
  parameters: { action: 'remote_start' }
}
this.context.startAbility(want).then(() => {
  console.info('远程启动成功')
}).catch((err) => {
  console.error(`启动失败: ${err}`)
})
```

---

**基本写法：带返回值启动**
`this.context.startAbilityForResult(<want>)`
```typescript
// 启动远程 Ability 并获取返回结果
let want: Want = {
  deviceId: 'remote_device_id',
  bundleName: 'com.example.myapp',
  abilityName: 'EntryAbility'
}
let result = await this.context.startAbilityForResult(want)
if (result.resultCode === 0) {
  let data = result.want.parameters['result']
  console.info(`返回数据: ${data}`)
}
```

---

**基本写法：处理返回数据**
`onRemoteRequest(<code>, <data>, <reply>, <option>)`
```typescript
// 远程 Ability 返回数据
onActive() {
  let result = AppStorage.get('remoteResult')
  console.info(`远程返回: ${result}`)
}
```

---

## RPC 远程调用

**基本写法：创建 RemoteObject**
`class <名> extends rpc.RemoteObject { asObject() { return this } }`
```typescript
// ServiceAbility 暴露远程接口
import { rpc } from '@kit.IPCKit'

class MyServiceStub extends rpc.RemoteObject {
  onRemoteRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): boolean {
    if (code === 1) {
      let param = data.readString()
      reply.writeString(`处理: ${param}`)
      return true
    }
    return false
  }
}
```

---

**基本写法：ServiceAbility 返回代理**
`onConnect(<want>) { return new <Stub>() }`
```typescript
// ServiceAbility onConnect 返回 RemoteObject
export default class ServiceAbilityExt extends Ability {
  onConnect(want: Want): rpc.RemoteObject {
    return new MyServiceStub('MyService')
  }
}
```

---

**基本写法：获取远程代理**
`this.context.connectServiceExtensionAbility(<want>, <连接选项>)`
```typescript
// 连接远程 Service
import { Want } from '@kit.AbilityKit'
import { rpc } from '@kit.IPCKit'

let connectionId = -1
let remoteProxy: rpc.IRemoteObject | null = null

let want: Want = {
  deviceId: 'remote_device_id',
  bundleName: 'com.example.myapp',
  abilityName: 'ServiceAbilityExt'
}

connectionId = this.context.connectServiceExtensionAbility(want, {
  onConnect: (elementName, remoteObject) => {
    remoteProxy = remoteObject
    console.info('远程服务已连接')
  },
  onDisconnect: (elementName) => {
    console.info('远程服务已断开')
  }
})
```

---

**基本写法：发送远程请求**
`remoteProxy.sendMessageRequest(<code>, <data>, <reply>, <option>)`
```typescript
// 通过代理调用远程方法
let option = new rpc.MessageOption()
let data = rpc.MessageSequence.create()
data.writeString('hello from client')
let reply = rpc.MessageSequence.create()

remoteProxy.sendMessageRequest(1, data, reply, option).then((result) => {
  let response = result.reply.readString()
  console.info(`远程响应: ${response}`)
})
```

---

**基本写法：断开远程连接**
`this.context.disconnectServiceExtensionAbility(<connectionId>)`
```typescript
// 断开远程 Service 连接
this.context.disconnectServiceExtensionAbility(connectionId, (err) => {
  console.info('已断开')
})
```

---

## Want 传参

**基本写法：通过 Want 传递参数**
`let want: Want = { parameters: { '<键>': <值> } }`
```typescript
// 使用 Want.parameters 传递自定义参数
let want: Want = {
  deviceId: 'remote_device_id',
  bundleName: 'com.example.myapp',
  abilityName: 'EntryAbility',
  parameters: {
    userId: 1001,
    userName: 'Alice',
    action: 'view_detail'
  }
}
```

---

**基本写法：接收 Want 参数**
`onCreate(<want>) { let <值> = want.parameters['<键>'] }`
```typescript
// 在目标 Ability 中读取参数
onCreate(want: Want) {
  let userId = want.parameters['userId'] as number
  let userName = want.parameters['userName'] as string
  console.info(`用户: ${userName} (ID: ${userId})`)
}
```
