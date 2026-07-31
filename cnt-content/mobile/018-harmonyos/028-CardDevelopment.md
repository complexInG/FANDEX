# 卡片开发 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 卡片配置

**基本写法：module.json5 声明卡片**
`"extensionAbilities": [{ "name": "<名>", "type": "form", "srcEntry": "<路径>", "metadata": [{ "name": "ohos.extension.form", "resource": "$profile:form_config" }] }]`
```json5
// module.json5 中声明 FormExtensionAbility
{
  "extensionAbilities": [
    {
      "name": "CardAbility",
      "type": "form",
      "srcEntry": "./ets/cardability/CardAbility.ets",
      "metadata": [
        { "name": "ohos.extension.form", "resource": "$profile:form_config" }
      ]
    }
  ]
}
```

---

**基本写法：卡片配置文件**
`{ "forms": [{ "name": "<卡片名>", "displayName": "<显示名>", "src": "<页面>", "window": { "designWidth": 720 }, "isDefault": true }] }`
```json5
// resources/base/profile/form_config.json
{
  "forms": [
    {
      "name": "widget",
      "displayName": "我的卡片",
      "description": "示例卡片",
      "src": "./ets/cardability/pages/CardPage.ets",
      "window": { "designWidth": 720 },
      "isDefault": true,
      "colorMode": "auto",
      "supportDimensions": ["2*2", "2*4"],
      "defaultDimension": "2*2",
      "updateEnabled": true,
      "scheduledUpdateTime": "10:30"
    }
  ]
}
```

---

## FormExtensionAbility

**基本写法：创建卡片 Ability**
`export default class <名> extends FormExtensionAbility { onAddForm(<want>) { } }`
```typescript
// 卡片生命周期
import { FormExtensionAbility } from '@kit.FormKit'

export default class CardAbility extends FormExtensionAbility {
  onAddForm(want) {
    let formId = want.parameters['formId'] as string
    return { formData: { title: '卡片标题', content: '内容' } }
  }

  onCastToNormalForm(formId) {
    console.info(`转为普通卡片: ${formId}`)
  }

  onUpdateForm(formId) {
    // 定时刷新卡片
    let provider = this.context.formProvider
    provider.updateForm(formId, { formData: { time: new Date().toLocaleTimeString() } })
  }
}
```

---

**基本写法：卡片更新**
`formProvider.updateForm(<formId>, <formBindingData>)`
```typescript
// 主动更新卡片数据
import { formProvider } from '@kit.FormKit'
import { formBindingData } from '@kit.FormKit'

let obj: formBindingData.FormBindingData = {
  data: JSON.stringify({ title: '新标题', content: '新内容' })
}
formProvider.updateForm(formId, obj)
```

---

**基本写法：请求卡片刷新**
`formProvider.requestPublishForm(<formId>, <formBindingData>)`
```typescript
// 请求发布卡片刷新
formProvider.requestPublishForm(formId, { data: JSON.stringify({ update: true }) })
```

---

## 卡片页面

**基本写法：卡片 UI 页面**
`let <数据> = AppStateManager.get('<键>');`
```typescript
// CardPage.ets 卡片页面组件
let storage = new LocalStorage()

@Entry(storage)
@Component
struct CardPage {
  @LocalStorageProp('title') title: string = ''
  @LocalStorageProp('content') content: string = ''

  build() {
    Column() {
      Text(this.title).fontSize(16).fontWeight(FontWeight.Bold)
      Text(this.content).fontSize(14).margin({ top: 8 })
    }
    .padding(12)
    .height('100%')
    .width('100%')
  }
}
```

---

**基本写法：卡片点击跳转**
`.onClick(() => { postCardAction(this, { 'action': 'router', 'abilityName': '<Ability>', 'params': {} }) })`
```typescript
// 卡片点击事件触发跳转
import { postCardAction } from '@kit.FormKit'

Column() {
  Text(this.title)
}
.onClick(() => {
  postCardAction(this, {
    'action': 'router',
    'abilityName': 'EntryAbility',
    'params': { 'action': 'view_detail' }
  })
})
```

---

**基本写法：卡片消息刷新**
`postCardAction(this, { 'action': 'message', 'params': {} })`
```typescript
// 通过 message action 触发卡片 Ability
Column() {
  Button('刷新')
}.onClick(() => {
  postCardAction(this, {
    'action': 'message',
    'params': { 'action': 'refresh' }
  })
})
```

---

## 卡片数据交互

**基本写法：onAddForm 返回初始数据**
`return { formData: <数据> }`
```typescript
// 卡片添加时返回初始数据
onAddForm(want) {
  let formId = want.parameters['formId'] as string
  let formData = {
    title: '欢迎',
    content: '这是卡片内容',
    time: new Date().toLocaleTimeString()
  }
  return { formData: formData }
}
```

---

**基本写法：处理 message 事件**
`onFormEvent(<formId>, <message>)`
```typescript
// 接收卡片 message action
onFormEvent(formId: string, message: string) {
  let params = JSON.parse(message)
  if (params.action === 'refresh') {
    formProvider.updateForm(formId, {
      data: JSON.stringify({ time: new Date().toLocaleTimeString() })
    })
  }
}
```

---

**基本写法：卡片删除**
`onRemoveForm(<formId>)`
```typescript
// 卡片被删除时清理数据
onRemoveForm(formId: string) {
  console.info(`卡片已删除: ${formId}`)
  // 清理与该卡片关联的缓存数据
}
```

---

## 卡片尺寸适配

**基本写法：响应不同尺寸**
`if (this.dimension === '2*2') { } else { }`
```typescript
// 根据卡片尺寸渲染不同布局
@Entry
@Component
struct CardPage {
  @LocalStorageProp('dimension') dimension: string = '2*2'

  build() {
    if (this.dimension === '2*2') {
      Column() { Text('小卡片') }
    } else {
      Row() { Text('宽卡片') }
    }
  }
}
```

---

**基本写法：卡片资源配置**
`// resources/base/profile/form_config.json 中配置 supportDimensions`
```json5
// 支持的卡片尺寸规格
{
  "supportDimensions": ["2*2", "2*4", "4*4"],
  "defaultDimension": "2*2"
}
```
