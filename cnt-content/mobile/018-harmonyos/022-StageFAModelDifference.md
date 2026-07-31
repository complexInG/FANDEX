# Stage 与 FA 模型差异 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模型概述

**基本写法：Stage 模型（API 9+ 主推）**
`export default class <Ability名> extends UIAbility { }`
```typescript
// Stage 模型 UIAbility 入口
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want, launchParam) { }
  onWindowStageCreate(windowStage) { }
}
```

---

**基本写法：FA 模型（API 8 及以前 旧模型）**
`export default { onCreate(want) { }, onActive() { } }`
```typescript
// FA 模型 PageAbility 匿名对象导出
export default {
  onCreate(want) { console.info('onCreate') },
  onActive() { console.info('onActive') },
  onDestroy() { console.info('onDestroy') }
}
```

---

## 配置文件差异

**基本写法：Stage 模型 module.json5**
`{ "module": { "type": "entry", "abilities": [{ "name": "<Ability名>", "srcEntry": "<路径>", "startWindowIcon": "<资源>" }] } }`
```json5
// Stage 模型使用 module.json5
{
  "module": {
    "name": "entry",
    "type": "entry",
    "deviceTypes": ["phone", "tablet"],
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background"
      }
    ]
  }
}
```

---

**基本写法：FA 模型 config.json**
`{ "module": { "abilities": [{ "name": "<Ability名>", "type": "page" }] } }`
```json5
// FA 模型使用 config.json
{
  "app": { "bundleName": "com.example.app" },
  "module": {
    "name": "entry",
    "type": "entry",
    "abilities": [
      { "name": "MainAbility", "type": "page", "visible": true }
    ]
  }
}
```

---

## 组件类型对比

**基本写法：Stage UIAbility**
`export default class <名> extends UIAbility { onWindowStageCreate(<stage>) { <stage>.loadContent('<页面>') } }`
```typescript
// Stage UIAbility 加载页面
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage) {
    windowStage.loadContent('pages/Index', (err) => {
      if (err) console.error('加载失败');
    });
  }
}
```

---

**基本写法：Stage ExtensionAbility**
`export default class <名> extends FormExtensionAbility { onAddForm(<want>) { } }`
```typescript
// Stage 卡片扩展能力
import { FormExtensionAbility } from '@kit.FormKit';

export default class CardAbility extends FormExtensionAbility {
  onAddForm(want) {
    return { formData: { title: '卡片标题' } };
  }
}
```

---

**基本写法：FA PageAbility**
`export default { onCreate(<want>) { this.context.setDisplayedContent('<页面>') } }`
```typescript
// FA 模型 PageAbility
export default {
  onCreate(want) {
    this.context.setDisplayedContent('pages/index', {});
  }
}
```

---

## 生命周期对比

**基本写法：Stage UIAbility 生命周期**
`onCreate -> onWindowStageCreate -> onForeground -> onBackground -> onWindowStageDestroy -> onDestroy`
```typescript
// Stage 生命周期回调
export default class EntryAbility extends UIAbility {
  onCreate(want, launchParam) { }
  onWindowStageCreate(windowStage) { }
  onForeground() { }
  onBackground() { }
  onWindowStageDestroy() { }
  onDestroy() { }
}
```

---

**基本写法：FA PageAbility 生命周期**
`onCreate -> onStart -> onActive -> onInactive -> onBackground -> onForeground -> onDestroy`
```typescript
// FA 生命周期回调
export default {
  onCreate(want) { },
  onStart() { },
  onActive() { },
  onInactive() { },
  onBackground() { },
  onForeground() { },
  onDestroy() { }
}
```

---

## 进程与引擎

**基本写法：Stage 共享 ArkTS 引擎**
`// 同进程多个 UIAbility 共享引擎实例`
```typescript
// Stage 模型：同一 HAP 中的 UIAbility 共享 ArkTS 引擎
// 内存占用更低，组件间可直接共享对象
```

---

**基本写法：FA 独享引擎实例**
`// 每个 Ability 独享 ArkTS 引擎实例`
```typescript
// FA 模型：每个 PageAbility 独立引擎实例
// 内存占用更高，组件间通过 IPC 通信
```

---

## 页面加载方式

**基本写法：Stage 通过 WindowStage 加载**
`<windowStage>.loadContent('<页面路径>', <回调>);`
```typescript
// Stage 模型在 onWindowStageCreate 中加载页面
onWindowStageCreate(windowStage) {
  windowStage.loadContent('pages/Index');
}
```

---

**基本写法：FA 通过 context 加载**
`this.context.setDisplayedContent('<页面路径>', <参数>);`
```typescript
// FA 模型在 onCreate 中加载页面
onCreate(want) {
  this.context.setDisplayedContent('pages/index', {});
}
```

---

## 工程结构对比

**基本写法：Stage 工程结构**
`entry/src/main/ets/entryability/ + entry/src/main/ets/pages/`
```text
// Stage 模型目录
entry/src/main/
  ets/
    entryability/EntryAbility.ets
    pages/Index.ets
  resources/
  module.json5
```

---

**基本写法：FA 工程结构**
`entry/src/main/js/default/pages/ + entry/src/main/config.json`
```text
// FA 模型目录
entry/src/main/
  js/default/
    pages/index/index.js
    pages/index/index.hml
  config.json
```

---

## AbilityStage 应用级回调

**基本写法：Stage AbilityStage**
`export default class <名> extends AbilityStage { onCreate() { } }`
```typescript
// Stage 模型应用级生命周期
import { AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    console.info('应用启动');
  }
}
```

---

**基本写法：注册 AbilityStage**
`// 在 module.json5 中配置 srcEntry`
```json5
// module.json5 注册 AbilityStage
{
  "module": {
    "name": "entry",
    "srcEntry": "./ets/myabilitystage/MyAbilityStage.ets",
    "abilities": []
  }
}
```
