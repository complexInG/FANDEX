# 元服务开发与发布 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 元服务概述

**基本写法：元服务与普通应用差异**
`// module.json5 中 type 配置为 "atomicService"`
```json5
// 元服务配置（无需安装即用）
{
  "module": {
    "name": "entry",
    "type": "atomicService",
    "deviceTypes": ["phone", "tablet"]
  }
}
```

---

**基本写法：创建元服务模板**
`// DevEco Studio → File → New → Module → Atomic Service`
```text
// 在 DevEco Studio 中创建元服务模块
// 模块类型选 Atomic Service
// 会自动配置 type 为 atomicService
```

---

## 工程配置

**基本写法：module.json5 完整配置**
`{ "module": { "type": "atomicService", "abilities": [{ "name": "<Ability>", "srcEntry": "<路径>" }] } }`
```json5
// 元服务 module.json5 配置
{
  "module": {
    "name": "entry",
    "type": "atomicService",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": ["phone", "tablet"],
    "deliveryWithInstall": true,
    "installationFree": true,
    "pages": "$profile:main_pages",
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background"
      }
    ]
  }
}
```

---

**基本写法：安装即用属性**
`"installationFree": true`
```json5
// 配置免安装运行
{
  "module": {
    "type": "atomicService",
    "installationFree": true
  }
}
```

---

## 卡片集成

**基本写法：元服务携带卡片**
`"extensionAbilities": [{ "name": "<名>", "type": "form" }]`
```json5
// 元服务中声明卡片扩展能力
{
  "module": {
    "extensionAbilities": [
      {
        "name": "ServiceCardAbility",
        "type": "form",
        "srcEntry": "./ets/servicecardability/ServiceCardAbility.ets",
        "metadata": [
          { "name": "ohos.extension.form", "resource": "$profile:form_config" }
        ]
      }
    ]
  }
}
```

---

**基本写法：卡片配置**
`{ "forms": [{ "name": "<名>", "src": "<页面>", "defaultDimension": "2*2" }] }`
```json5
// form_config.json 元服务卡片配置
{
  "forms": [
    {
      "name": "service_widget",
      "displayName": "元服务卡片",
      "src": "./ets/servicecardability/pages/WidgetPage.ets",
      "window": { "designWidth": 720 },
      "isDefault": true,
      "colorMode": "auto",
      "supportDimensions": ["2*2", "2*4"],
      "defaultDimension": "2*2"
    }
  ]
}
```

---

## 服务直达

**基本写法：通过 URI 拉起元服务**
`this.context.startAbility({ uri: '<URI>', type: '<类型>' })`
```typescript
// 通过 deeplink 拉起元服务
import { Want } from '@kit.AbilityKit'

let want: Want = {
  uri: 'store://appgallery.com/atomic/detail?id=123456',
  action: 'ohos.want.action.viewData'
}
this.context.startAbility(want)
```

---

**基本写法：通过 bundleName 拉起**
`this.context.startAbility({ bundleName: '<包名>', abilityName: '<Ability>' })`
```typescript
// 直接拉起指定元服务
let want: Want = {
  bundleName: 'com.example.myservice',
  abilityName: 'EntryAbility'
}
this.context.startAbility(want)
```

---

## 构建与发布

**基本写法：构建元服务 HAP**
`hvigorw --mode module -p module=entry@default assembleHap`
```bash
# 构建元服务 HAP 包
hvigorw --mode module -p module=entry@default -p product=default assembleHap --parallel --daemon
```

---

**基本写法：构建 APP**
`hvigorw --mode project -p product=default assembleApp`
```bash
# 构建元服务 APP 包
hvigorw --mode project -p product=default assembleApp
```

---

**基本写法：元服务签名配置**
`"signingConfigs": [{ "name": "release", "type": "HarmonyOS" }]`
```json5
// build-profile.json5 元服务签名
{
  "app": {
    "signingConfigs": [
      {
        "name": "release",
        "type": "HarmonyOS",
        "material": {
          "cert": { "file": "service.cer" },
          "store": { "file": "service.p12", "password": "123456" },
          "key": { "alias": "service", "password": "123456" },
          "profile": { "file": "service.p7b" }
        }
      }
    ]
  }
}
```

---

**基本写法：上传至 AppGallery**
`// AppGallery Connect → 我的应用 → 元服务 → 上传`
```text
// 上传元服务流程
// 1. 登录 AppGallery Connect
// 2. 选择「元服务」分类
// 3. 创建元服务 → 填写信息
// 4. 上传已签名的 APP 包
// 5. 提交审核
```

---

## 元服务 API 限制

**基本写法：可用 API 范围**
`// 使用 @kit 引入支持的 Kit`
```typescript
// 元服务支持的 Kit（部分受限）
import { UIAbility } from '@kit.AbilityKit'
import { relationalStore } from '@kit.ArkData'
import { http } from '@kit.NetworkKit'

// 不支持：部分后台能力、系统级权限
```

---

**基本写法：获取元服务信息**
`this.context.applicationInfo.name`
```typescript
// 获取当前元服务信息
onCreate() {
  let info = this.context.applicationInfo
  console.info(`名称: ${info.name}`)
  console.info(`包名: ${info.bundleName}`)
}
```

---

## 数据共享

**基本写法：元服务间数据传递**
`AppStorage.setOrCreate('<键>', <值>)`
```typescript
// 通过 AppStorage 在元服务内共享数据
AppStorage.setOrCreate('service_data', { id: 1, name: 'test' })

// 另一处获取
let data = AppStorage.get('service_data')
```

---

**基本写法：通过 Want 参数传递**
`want.parameters['<键>'] = <值>`
```typescript
// 启动元服务时传递参数
let want: Want = {
  bundleName: 'com.example.myservice',
  abilityName: 'EntryAbility',
  parameters: { userId: 1001, action: 'start' }
}
```
