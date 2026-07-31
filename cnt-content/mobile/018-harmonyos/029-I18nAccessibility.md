# 国际化与无障碍 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 资源文件结构

**基本写法：多语言资源目录**
`resources/<语言>/element/string.json`
```text
// 多语言资源目录结构
resources/
  base/element/string.json          // 默认语言
  en_US/element/string.json         // 英语（美国）
  zh_CN/element/string.json         // 简体中文
  ja_JP/element/string.json        // 日语
```

---

**基本写法：字符串资源**
`{ "string": [{ "name": "<键>", "value": "<值>" }] }`
```json5
// resources/base/element/string.json
{
  "string": [
    { "name": "app_name", "value": "我的应用" },
    { "name": "welcome", "value": "欢迎" },
    { "name": "confirm", "value": "确定" }
  ]
}
```

---

**基本写法：英文资源**
`{ "string": [{ "name": "app_name", "value": "My App" }] }`
```json5
// resources/en_US/element/string.json
{
  "string": [
    { "name": "app_name", "value": "My App" },
    { "name": "welcome", "value": "Welcome" },
    { "name": "confirm", "value": "Confirm" }
  ]
}
```

---

## 引用资源

**基本写法：代码中引用字符串**
`$r('app.string.<键>')`
```typescript
// 引用字符串资源
Text($r('app.string.welcome'))
Button($r('app.string.confirm'))
```

---

**基本写法：引用颜色资源**
`$r('app.color.<键>')`
```typescript
// 引用颜色资源
Text('文本').fontColor($r('app.color.text_color'))
```

---

**基本写法：引用尺寸资源**
`$r('app.float.<键>')`
```typescript
// 引用尺寸资源
Text('文本').fontSize($r('app.float.title_size'))
```

---

**基本写法：引用图片资源**
`$r('app.media.<键>')`
```typescript
// 引用图片资源
Image($r('app.media.icon')).width(48).height(48)
```

---

## i18n 国际化

**基本写法：获取系统语言**
`i18n.getSystemLanguage()`
```typescript
// 获取当前系统语言
import { i18n } from '@kit.LocalizationKit'

let lang = i18n.getSystemLanguage()
console.info(`系统语言: ${lang}`)
// 如 zh-Hans-CN、en-US
```

---

**基本写法：获取系统区域**
`i18n.getSystemRegion()`
```typescript
// 获取系统区域设置
let region = i18n.getSystemRegion()
console.info(`区域: ${region}`)
// 如 CN、US
```

---

**基本写法：获取系统时区**
`i18n.getSystemTimeZone()`
```typescript
// 获取系统时区
let timezone = i18n.getSystemTimeZone()
console.info(`时区: ${timezone}`)
// 如 Asia/Shanghai
```

---

**基本写法：格式化日期**
`new Intl.DateTimeFormat(<locale>, <options>).format(<date>)`
```typescript
// 按地区格式化日期
let formatter = new Intl.DateTimeFormat('zh-CN', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit'
})
let dateStr = formatter.format(new Date())
console.info(dateStr)  // 2026/07/31
```

---

**基本写法：格式化数字**
`new Intl.NumberFormat(<locale>, <options>).format(<number>)`
```typescript
// 按地区格式化数字
let formatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD'
})
let price = formatter.format(99.99)
console.info(price)  // $99.99
```

---

**基本写法：格式化相对时间**
`new Intl.RelativeTimeFormat(<locale>, <options>).format(<值>, <单位>)`
```typescript
// 相对时间格式化
let rtf = new Intl.RelativeTimeFormat('zh-CN', { numeric: 'auto' })
rtf.format(-1, 'day')   // 昨天
rtf.format(2, 'hour')   // 2小时后
```

---

## 单复数处理

**基本写法：复数资源**
`{ "plural": [{ "name": "<键>", "value": [{ "quantity": "one", "value": "<单数>" }, { "quantity": "other", "value": "<复数>" }] }] }`
```json5
// resources/en_US/element/plural.json
{
  "plural": [
    {
      "name": "items_count",
      "value": [
        { "quantity": "one", "value": "%d item" },
        { "quantity": "other", "value": "%d items" }
      ]
    }
  ]
}
```

---

**基本写法：引用复数资源**
`$r('app.plural.<键>', <数量>)`
```typescript
// 根据数量自动选择单复数
Text($r('app.plural.items_count', count))
```

---

## 无障碍属性

**基本写法：设置无障碍文本**
`.accessibilityText('<描述>')`
```typescript
// 为无障碍模式提供文本描述
Image($r('app.media.icon'))
  .width(48).height(48)
  .accessibilityText('应用图标')
```

---

**基本写法：设置无障碍描述**
`.accessibilityDescription('<详细描述>')`
```typescript
// 提供更详细的无障碍描述
Button('提交')
  .accessibilityText('提交按钮')
  .accessibilityDescription('点击此按钮提交表单数据')
```

---

**基本写法：设置重要性级别**
`.accessibilityLevel(AccessibilityLevel.YES)`
```typescript
// 控制组件是否对无障碍服务可见
import { AccessibilityLevel } from '@kit.ArkUI'

Text('重要内容')
  .accessibilityLevel(AccessibilityLevel.YES)

Text('装饰内容')
  .accessibilityLevel(AccessibilityLevel.NO)
```

---

**基本写法：无障碍分组**
`.accessibilityGroup(true)`
```typescript
// 将子组件合并为无障碍单元
Row() {
  Text('姓名')
  Text('Alice')
}
.accessibilityGroup(true)
.accessibilityText('姓名：Alice')
```

---

**基本写法：无障碍操作**
`.accessibilityAction('<动作>', <回调>)`
```typescript
// 自定义无障碍操作
Text('自定义操作')
  .accessibilityAction('custom_action', () => {
    console.info('自定义操作触发')
  })
```
