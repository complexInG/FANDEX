---
order: 54
title: 导航与路由
module: harmonyos
category: HarmonyOS
difficulty: intermediate
description: Navigation与Router
author: fanquanpp
updated: '2026-08-01'
related:
  - harmonyos/自定义组件
  - harmonyos/列表与网格
  - harmonyos/网络请求
  - harmonyos/数据持久化
prerequisites:
  - harmonyos/概述与环境搭建
---

# 导航与路由 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 概述

HarmonyOS 提供了两套路由导航方案：Navigation 组件和 Router 模块。Navigation 是声明式的导航容器，支持 NavDestination 子页面管理、导航栏定制和路由栈操作，适合复杂的单页面应用架构。Router 是命令式的页面路由，通过 API 调用实现页面跳转和返回，适合简单的多页面应用。在实际开发中，推荐优先使用 Navigation，它提供了更丰富的导航能力和更好的类型安全。

## 基础概念

**Navigation**：导航容器组件，内部管理一个路由栈，每个栈元素对应一个 NavDestination 页面。支持 pushPath（入栈）、pop（出栈）、replacePath（替换）等操作。

**NavDestination**：Navigation 的子页面组件，每个 NavDestination 代表一个可导航的目标页面。通过 title 设置导航栏标题，通过 hideBackButton 控制返回按钮显示。

**NavPathStack**：Navigation 的路由栈对象，提供了完整的栈操作 API，包括 push、pop、replace、clear、moveToTop 等。支持获取栈信息、监听栈变化。

**Router**：全局路由模块，通过 router.pushUrl 和 router.back 等方法实现页面跳转。每个页面需要在 main_pages.json 中注册路径。

**页面参数传递**：两种方案都支持页面间参数传递。Navigation 通过 NavPathStack 的参数机制传递，Router 通过 params 字段传递。

## 快速上手

### Navigation 基本用法

```typescript
// 创建路由栈
@Entry
@Component
struct NavigationDemo {
  // 创建导航栈
  navStack: NavPathStack = new NavPathStack()

  build() {
    // Navigation 容器
    Navigation(this.navStack) {
      // 首页内容
      Column() {
        Text('首页')
          .fontSize(24)
          .margin({ bottom: 20 })

        Button('跳转到详情页')
          .onClick(() => {
            // 将页面路径压入导航栈
            this.navStack.pushPath({ name: 'Detail' })
          })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .title('应用首页')
    // 注册 NavDestination 页面
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'Detail') {
      DetailPage({ navStack: this.navStack })
    }
  }
}

// 详情页组件
@Component
struct DetailPage {
  navStack: NavPathStack = new NavPathStack()

  build() {
    NavDestination() {
      Column() {
        Text('详情页内容')
          .fontSize(20)
        Button('返回')
          .onClick(() => {
            this.navStack.pop()
          })
      }
    }
    .title('详情页')
  }
}
```

### Router 基本用法

```typescript
import router from '@ohos.router'

@Entry
@Component
struct RouterDemo {
  build() {
    Column() {
      Button('跳转到详情页')
        .onClick(() => {
          // 使用 Router 跳转，传递参数
          router.pushUrl({
            url: 'pages/DetailPage',
            params: {
              id: 42,
              name: '测试数据'
            }
          })
        })

      Button('替换当前页')
        .onClick(() => {
          // 替换当前页面，无法返回
          router.replaceUrl({
            url: 'pages/LoginPage'
          })
        })
    }
  }
}

// 详情页接收参数
@Entry
@Component
struct DetailPage {
  build() {
    Column() {
      // 获取路由传递的参数
      Text(`参数: ${JSON.stringify(router.getParams())}`)
        .fontSize(16)

      Button('返回上一页')
        .onClick(() => {
          router.back()
        })
    }
  }
}
```

## 详细用法

### Navigation 带参数跳转

```typescript
// 定义页面参数类型
interface DetailParams {
  itemId: number
  title: string
}

@Entry
@Component
struct NavWithParamsDemo {
  navStack: NavPathStack = new NavPathStack()

  build() {
    Navigation(this.navStack) {
      Column({ space: 10 }) {
        Button('查看商品1')
          .onClick(() => {
            this.navStack.pushPath({
              name: 'ProductDetail',
              param: { itemId: 1, title: '商品一' } as DetailParams
            })
          })

        Button('查看商品2')
          .onClick(() => {
            this.navStack.pushPath({
              name: 'ProductDetail',
              param: { itemId: 2, title: '商品二' } as DetailParams
            })
          })
      }
    }
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'ProductDetail') {
      ProductDetailPage({ navStack: this.navStack })
    }
  }
}

@Component
struct ProductDetailPage {
  navStack: NavPathStack = new NavPathStack()
  // 从导航栈获取参数
  @State params: DetailParams = this.navStack.getParamByName('ProductDetail')[0] as DetailParams

  build() {
    NavDestination() {
      Column() {
        Text(`商品ID: ${this.params.itemId}`)
        Text(`商品名称: ${this.params.title}`)
        Button('返回')
          .onClick(() => this.navStack.pop())
      }
    }
    .title(this.params.title)
  }
}
```

### Navigation 路由栈操作

```typescript
@Entry
@Component
struct NavStackOpsDemo {
  navStack: NavPathStack = new NavPathStack()

  build() {
    Navigation(this.navStack) {
      Column({ space: 10 }) {
        Text(`当前栈深度: ${this.navStack.size()}`)
          .fontSize(14)

        Button('压入页面A')
          .onClick(() => this.navStack.pushPath({ name: 'PageA' }))

        Button('压入页面B')
          .onClick(() => this.navStack.pushPath({ name: 'PageB' }))

        Button('弹出当前页')
          .onClick(() => this.navStack.pop())

        Button('弹出到指定页面')
          .onClick(() => this.navStack.popToName('PageA'))

        Button('清空栈')
          .onClick(() => this.navStack.clear())

        Button('移动到栈顶')
          .onClick(() => this.navStack.moveToTop('PageA'))
      }
      .padding(20)
    }
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'PageA') {
      PageA({ navStack: this.navStack })
    } else if (name === 'PageB') {
      PageB({ navStack: this.navStack })
    }
  }
}
```

### 自定义导航栏

```typescript
@Entry
@Component
struct CustomNavBarDemo {
  navStack: NavPathStack = new NavPathStack()

  build() {
    Navigation(this.navStack) {
      Column() {
        Text('首页内容')
      }
    }
    // 隐藏默认导航栏
    .hideToolBar(true)
    // 自定义导航栏
    .customNavContentTransition(() => {
      // 返回自定义导航栏内容
      return undefined
    })
    .titleMode(NavigationTitleMode.Mini)
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    // 空实现
  }
}
```

## 常见场景

### Tab 页签与导航结合

```typescript
@Entry
@Component
struct TabNavDemo {
  navStack: NavPathStack = new NavPathStack()
  @State currentTab: number = 0

  build() {
    Navigation(this.navStack) {
      Tabs({ index: this.currentTab }) {
        TabContent() {
          Column() {
            Text('首页')
            Button('查看详情')
              .onClick(() => this.navStack.pushPath({ name: 'Detail' }))
          }
        }.tabBar('首页')

        TabContent() {
          Column() {
            Text('我的')
            Button('设置')
              .onClick(() => this.navStack.pushPath({ name: 'Settings' }))
          }
        }.tabBar('我的')
      }
    }
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'Detail') {
      DetailPage({ navStack: this.navStack })
    } else if (name === 'Settings') {
      SettingsPage({ navStack: this.navStack })
    }
  }
}
```

### 带返回结果的页面跳转

```typescript
import { CommonDataSource } from '@ohos.base'

@Entry
@Component
struct ResultNavDemo {
  navStack: NavPathStack = new NavPathStack()
  @State selectedCity: string = '未选择'

  build() {
    Navigation(this.navStack) {
      Column({ space: 10 }) {
        Text(`当前城市: ${this.selectedCity}`)
          .fontSize(18)

        Button('选择城市')
          .onClick(() => {
            this.navStack.pushPath({ name: 'CityPicker' })
          })
      }
      .padding(20)
    }
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'CityPicker') {
      CityPickerPage({
        navStack: this.navStack,
        onCitySelected: (city: string) => {
          this.selectedCity = city
        }
      })
    }
  }
}

@Component
struct CityPickerPage {
  navStack: NavPathStack = new NavPathStack()
  onCitySelected: (city: string) => void = () => {}
  @State cities: string[] = ['北京', '上海', '广州', '深圳', '杭州']

  build() {
    NavDestination() {
      List() {
        ForEach(this.cities, (city: string) => {
          ListItem() {
            Text(city)
              .width('100%')
              .padding(16)
              .onClick(() => {
                this.onCitySelected(city)
                this.navStack.pop()
              })
          }
        }, (city: string) => city)
      }
    }
    .title('选择城市')
  }
}
```

## 注意事项

- **Navigation vs Router**：Navigation 是推荐方案，支持类型安全的参数传递和声明式路由管理。Router 适合简单场景或从旧项目迁移。不要在同一页面中混用两种方案。
- **NavPathStack 传递**：NavPathStack 需要通过组件参数传递给子页面，确保每个 NavDestination 都能访问到同一个栈实例。
- **页面注册**：Router 方案需要在 main_pages.json 中注册页面路径，未注册的路径无法跳转。Navigation 方案通过 navDestination 构建器动态注册。
- **路由栈大小**：注意控制路由栈深度，过深的栈会占用大量内存。适时使用 replacePath 替代 pushPath，或使用 clear 清空栈。
- **生命周期**：NavDestination 拥有独立的生命周期回调（onShown、onHidden、aboutToAppear、aboutToDisappear），适合在此处管理页面级资源。

## 进阶用法

### 导航转场动画

```typescript
@Entry
@Component
struct TransitionNavDemo {
  navStack: NavPathStack = new NavPathStack()

  build() {
    Navigation(this.navStack) {
      Column() {
        Button('跳转')
          .onClick(() => this.navStack.pushPath({ name: 'AnimatedPage' }))
      }
    }
    // 自定义导航转场动画
    .navTransition({
      // 入场动画
      onTransitionEnter: (transition: NavigationTransition) => {
        // 从右侧滑入
        transition.to.translate({ x: 0 })
        transition.from.translate({ x: '100%' })
      },
      // 出场动画
      onTransitionExit: (transition: NavigationTransition) => {
        transition.to.translate({ x: '-30%' })
        transition.from.translate({ x: 0 })
      }
    })
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'AnimatedPage') {
      AnimatedPage({ navStack: this.navStack })
    }
  }
}
```

### 路由拦截与守卫

```typescript
@Entry
@Component
struct GuardNavDemo {
  navStack: NavPathStack = new NavPathStack()
  @State isLoggedIn: boolean = false

  build() {
    Navigation(this.navStack) {
      Column({ space: 10 }) {
        Button('查看个人中心')
          .onClick(() => {
            // 路由守卫：未登录时跳转到登录页
            if (!this.isLoggedIn) {
              this.navStack.pushPath({ name: 'Login' })
            } else {
              this.navStack.pushPath({ name: 'Profile' })
            }
          })

        Button(this.isLoggedIn ? '退出登录' : '模拟登录')
          .onClick(() => {
            this.isLoggedIn = !this.isLoggedIn
          })
      }
      .padding(20)
    }
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    if (name === 'Login') {
      LoginPage({
        navStack: this.navStack,
        onLoginSuccess: () => {
          this.isLoggedIn = true
          this.navStack.replacePath({ name: 'Profile' })
        }
      })
    } else if (name === 'Profile') {
      ProfilePage({ navStack: this.navStack })
    }
  }
}
```

### 深度链接与路由恢复

```typescript
@Entry
@Component
struct DeepLinkDemo {
  navStack: NavPathStack = new NavPathStack()

  aboutToAppear() {
    // 处理深度链接，恢复路由状态
    const deepLink = this.getDeepLink()
    if (deepLink) {
      // 根据深度链接构建路由栈
      this.navStack.pushPath({ name: 'Home' })
      if (deepLink.page === 'Detail') {
        this.navStack.pushPath({
          name: 'Detail',
          param: { id: deepLink.id }
        })
      }
    }
  }

  private getDeepLink(): object | null {
    // 从意图中获取深度链接信息
    return null
  }

  build() {
    Navigation(this.navStack) {
      Column() {
        Text('首页')
      }
    }
    .navDestination(this.buildNavDestination)
  }

  @Builder
  buildNavDestination(name: string) {
    // 路由页面注册
  }
}
```
## Navigation 导航组件

**Navigation 容器**
`Navigation([<pathStack>?]: NavPathStack) { ... }`
```typescript
@Component
struct Index {
  private pathStack: NavPathStack = new NavPathStack()

  build() {
    Navigation(this.pathStack) {
      Column() {
        Button('Go Detail').onClick(() => {
          this.pathStack.pushPath({ name: 'detail' })
        })
      }
    }
    .title('Home')
    .titleMode(NavigationTitleMode.Mini)
  }
}
```

**NavDestination 目标页**
`NavDestination() { ... }`
```typescript
@Component
struct DetailPage {
  build() {
    NavDestination() {
      Column() {
        Text('Detail Page')
      }
    }
    .title('Detail')
    .onShown(() => {})
    .onHidden(() => {})
  }
}
```

**NavPathStack 路由栈**
`new NavPathStack(): NavPathStack`
```typescript
private pathStack: NavPathStack = new NavPathStack()

// 路由跳转
pathStack.pushPath({ name: 'detail', param: { id: 1 } })
pathStack.pushPath({ name: 'detail' }, (popInfo: PopInfo) => {})
pathStack.replacePath({ name: 'detail' })
pathStack.replacePathByName('detail', { id: 1 })

// 路由返回
pathStack.pop()
pathStack.pop({ result: 'success' })
pathStack.popToName('home')
pathStack.popToIndex(0)
pathStack.clear()
```

**NavPathStack 路由信息**
```typescript
// 获取栈大小
const size = pathStack.size()

// 获取所有路由信息
const allPaths = pathStack.getAllPathName()

// 获取参数
const param = pathStack.getParamByName('detail')
const paramByIndex = pathStack.getParamByIndex(0)
```

---

## NavRouter 路由组件

**NavRouter 路由容器**
`NavRouter() { ... }.navDestination(() => { ... })`
```typescript
@Component
struct Index {
  @State list: Array<string> = ['A', 'B', 'C']

  build() {
    Navigation() {
      List() {
        ForEach(this.list, (item: string) => {
          ListItem() {
            NavRouter() {
              Text(item).padding(16)
            }
            .navDestination(() => {
              DetailPage({ title: item })
            })
          }
        })
      }
    }
  }
}
```

---

## router 路由 API

**router.pushUrl 推入页面**
`router.pushUrl(<options>: RouterOptions, [<mode>?: RouterMode]): Promise<void>`
```typescript
import { router } from '@kit.ArkUI'

router.pushUrl({
  url: 'pages/Detail',
  params: { id: 1, name: 'Tom' }
}).then(() => {
  console.info('跳转成功')
}).catch((err) => {
  console.error(`跳转失败: ${JSON.stringify(err)}`)
})
```

**router.pushUrl 指定模式**
`router.pushUrl(<options>, <mode>: RouterMode)`
```typescript
router.pushUrl({ url: 'pages/Detail' }, router.RouterMode.Standard)
router.pushUrl({ url: 'pages/Detail' }, router.RouterMode.Single)
```

**router.replaceUrl 替换页面**
`router.replaceUrl(<options>: RouterOptions, [<mode>?: RouterMode]): Promise<void>`
```typescript
router.replaceUrl({
  url: 'pages/Home',
  params: {}
})
```

**router.back 返回**
`router.back([<options>?]: RouterOptions | string])`
```typescript
router.back()                              // 返回上一页
router.back({ url: 'pages/Home' })         // 返回到指定页
router.back({ url: 'pages/Home', params: { ok: true } })
```

**router.clear 清空栈**
`router.clear(): void`
```typescript
router.clear()
```

---

## router 路由信息

**router.getState 获取状态**
`router.getState(): RouterState`
```typescript
const state = router.getState()
console.info(`index: ${state.index}`)
console.info(`name: ${state.name}`)
console.info(`path: ${state.path}`)
```

**router.getLength 栈长度**
`router.getLength(): number`
```typescript
const length = router.getLength()
console.info(`栈深度: ${length}`)
```

**router.getParams 获取参数**
`router.getParams(): Object`
```typescript
const params = router.getParams() as DetailParams
console.info(`id: ${params.id}`)
```

---

## router 路由模式

**RouterMode 路由模式**
```typescript
router.RouterMode.Standard  // 标准模式,允许多个相同页面
router.RouterMode.Single    // 单例模式,相同页面只保留一个
```

---

## router 事件

**router.enableAlertBeforeBackPage 返回拦截**
`router.enableAlertBeforeBackPage(<options>): Promise<void>`
```typescript
router.enableAlertBeforeBackPage({
  message: '确定要退出吗?'
}).then(() => {
  console.info('已注册返回拦截')
})
```

**router.disableAlertBeforeBackPage 取消拦截**
`router.disableAlertBeforeBackPage(): void`
```typescript
router.disableAlertBeforeBackPage()
```

---

## 页面路由配置

**main_pages.json 路由配置**
```json5
{
  "src": [
    "pages/Index",
    "pages/Detail",
    "pages/Profile",
    "pages/Settings"
  ]
}
```

---

## 页面间通信

**pushUrl 传参**
```typescript
// 发送方
router.pushUrl({
  url: 'pages/Detail',
  params: { id: 1, name: 'Tom' }
})

// 接收方
@Entry
@Component
struct Detail {
  private params: DetailParams = router.getParams() as DetailParams

  build() {
    Column() {
      Text(`ID: ${this.params.id}`)
      Text(`Name: ${this.params.name}`)
    }
  }
}
```

**back 返回数据**
```typescript
// 接收方
router.pushUrl({
  url: 'pages/Editor'
}).then(() => {})

// 编辑页返回时传递数据
router.back({ url: 'pages/Home', params: { saved: true } })

// 主页接收返回数据
// 通过 onBackPress 或 aboutToAppear 中读取参数
```

---

## Navigation 路由模式

**Navigation 模式**
```typescript
Navigation(this.pathStack) { ... }
  .mode(NavigationMode.Stack)     // 栈模式
  .mode(NavigationMode.Split)     // 分栏模式
  .mode(NavigationMode.Auto)      // 自适应模式
```

**titleMode 标题模式**
```typescript
Navigation() { ... }
  .titleMode(NavigationTitleMode.Mini)    // 迷你标题
  .titleMode(NavigationTitleMode.Full)    // 完整标题
  .titleMode(NavigationTitleMode.Free)    // 自由模式
```

---

## NavDestination 事件

**onShown 显示**
`NavDestination().onShown(() => { ... })`
```typescript
NavDestination() { ... }
  .onShown(() => {
    console.info('页面显示')
  })
```

**onHidden 隐藏**
`NavDestination().onHidden(() => { ... })`
```typescript
NavDestination() { ... }
  .onHidden(() => {
    console.info('页面隐藏')
  })
```

**onBackPressed 返回拦截**
`NavDestination().onBackPressed((): boolean => { ... })`
```typescript
NavDestination() { ... }
  .onBackPressed((): boolean => {
    return this.handleBack()
  })
```

**onNavBarStateChange 标题栏变化**
`NavDestination().onNavBarStateChange((state: NavBarState) => { ... })`
```typescript
NavDestination() { ... }
  .onNavBarStateChange((state: NavBarState) => {
    console.info(`state: ${state}`)
  })
```

---

## 动态路由

**NavPathStack 动态注册**
```typescript
@Entry
@Component
struct Index {
  private pathStack: NavPathStack = new NavPathStack()

  @Builder pageMap(name: string) {
    if (name === 'detail') {
      DetailPage()
    } else if (name === 'profile') {
      ProfilePage()
    }
  }

  build() {
    Navigation(this.pathStack) {
      Column() {
        Button('Detail').onClick(() => {
          this.pathStack.pushPath({ name: 'detail' })
        })
      }
    }
    .navDestination(this.pageMap)
  }
}
```

---

## 转场动画

**customNavContentTransition 自定义转场**
`Navigation().customNavContentTransition((from, to, op) => { ... })`
```typescript
Navigation(this.pathStack) { ... }
  .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, op: NavigationOperation) => {
    return {
      timeout: 300,
      transition: (proxy) => {
        // 自定义转场动画
      }
    }
  })
```

---

## 路由守卫

**页面拦截示例**
```typescript
@Component
struct Index {
  private pathStack: NavPathStack = new NavPathStack()

  private checkLogin(): boolean {
    return AppStorage.get<string>('token') !== undefined
  }

  build() {
    Navigation(this.pathStack) {
      Button('Profile').onClick(() => {
        if (this.checkLogin()) {
          this.pathStack.pushPath({ name: 'profile' })
        } else {
          this.pathStack.pushPath({ name: 'login' })
        }
      })
    }
  }
}
```

## 参考文献



华为开发者联盟 HarmonyOS 文档：https://developer.huawei.com/consumer/cn/harmonyos
ArkTS 语言规范：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-overview
ArkUI 组件参考：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/
DevEco Studio：https://developer.huawei.com/consumer/cn/deveco-studio/

## 延伸阅读



TypeScript 基础（ArkTS 语言底座），见 009-typescript 模块。
声明式 UI 概念与 React/Vue 对比，见 011-react/010-vue3 模块。
移动端应用架构，见 018-harmonyos 模块文档。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供鸿蒙开发课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与环境搭建 | 001-OverviewSetup | 本文的前置基础 |
| ArkTS与ArkUI | 002-ArkTSArkUI | 本文的并列主题 |
| UI组件与动画 | 003-UIComponentAnimation | 本文的并列主题 |
| 网络与数据持久化 | 004-NetworkAndPersistence | 本文的并列主题 |
| 多媒体与设备能力 | 005-MultimediaDeviceCapability | 本文的并列主题 |
| ArkTS语言特性 | 006-ArkTSLanguageFeature | 本文的并列主题 |
| 状态管理 | 007-StateManagement | 本文的并列主题 |
| 自定义组件 | 008-CustomComponent | 本文的并列主题 |
| 列表与网格 | 009-ListGrid | 本文的并列主题 |
| 导航与路由 | 010-NavigationRoute | 本文自身 |
| 网络请求 | 011-NetworkRequest | 本文的并列主题 |
| 数据持久化 | 012-DataPersistence | 本文的并列主题 |
| 动画系统 | 013-AnimationSystem | 本文的并列主题 |
| 手势与交互 | 014-GestureInteraction | 本文的并列主题 |
| 通知与权限 | 015-NotificationPermission | 本文的安全延伸 |
| 多媒体能力 | 016-MultimediaCapability | 本文的并列主题 |
| 传感器与位置 | 017-SensorLocation | 本文的并列主题 |
| 卡片开发 | 018-CardDevelopment | 本文的并列主题 |
| 分布式能力 | 019-DistributedCapability | 本文的并列主题 |
| 性能优化 | 020-PerformanceOptimization | 本文的性能延伸 |
| 国际化与无障碍 | 021-I18nAccessibility | 本文的并列主题 |
| 测试与调试 | 022-TestDebug | 本文的并列主题 |
| 应用签名与发布 | 023-AppSignaturePublish | 本文的并列主题 |
| Stage模型与FA模型区别 | 024-StageFAModelDifference | 本文的并列主题 |
| ArkTS与TypeScript差异 | 025-ArkTSTypeScriptDifference | 本文的并列主题 |
| ArkUI声明式语法 | 026-ArkUIDeclarativeSyntax | 本文的并列主题 |
| 组件生命周期详解 | 027-ComponentLifecycleDetailed | 本文的并列主题 |
| 路由跳转与路由栈 | 028-RouteJumpStack | 本文的并列主题 |
| 权限申请 | 029-PermissionRequest | 本文的安全延伸 |
| 分布式数据管理 | 030-DistributedDataManagement | 本文的并列主题 |
| 跨设备调用 | 031-CrossDeviceCall | 本文的并列主题 |
| 元服务开发与发布 | 032-AtomicServiceDevPublish | 本文的并列主题 |
| DevEco-Studio调试器 | 033-DevEcoStudioDebugger | 本文的并列主题 |
