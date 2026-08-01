---
order: 2
title: ArkTS与ArkUI
module: harmonyos
category: 鸿蒙开发
difficulty: beginner
description: 'ArkTS 语言基础、ArkUI 方舟开发框架、声明式 UI 范式、组件化开发、装饰器与状态管理。'
author: fanquanpp
updated: '2026-08-01'
related:
  - harmonyos/概述与环境搭建
  - harmonyos/UI组件与动画
  - harmonyos/网络与数据持久化
prerequisites: []
---
## 1. ArkTS 语言基础

### 1.1 ArkTS 概述

ArkTS 是基于 **TypeScript 扩展**的编程语言，专为 HarmonyOS 应用开发设计。它在 TypeScript 基础上进行了如下扩展和约束：

| 特性         | 说明                                       |
| :----------- | :----------------------------------------- |
| **类型系统** | 基于 TypeScript 静态类型，更严格的类型检查 |
| **UI 语法**  | 扩展了声明式 UI 构建语法                   |
| **状态管理** | 内置响应式状态管理装饰器                   |
| **性能优化** | 静态编译，AOT 优化                         |
| **安全约束** | 禁止部分动态特性（如 eval、with）          |

### 1.2 基础数据类型

```typescript
// 基本类型
let isDone: boolean = false;
let count: number = 42;
let name: string = 'HarmonyOS';

// 数组
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ['a', 'b', 'c'];

// 元组
let tuple: [string, number] = ['age', 25];

// 枚举
enum Direction {
  Up = 'UP',
  Down = 'DOWN',
  Left = 'LEFT',
  Right = 'RIGHT',
}
let dir: Direction = Direction.Up;

// 联合类型
let value: string | number = 'hello';
value = 100;

// 类型别名
type NullableString = string | null;
let name2: NullableString = null;
```

### 1.3 函数与箭头函数

```typescript
// 普通函数
function add(a: number, b: number): number {
  return a + b;
}

// 可选参数与默认值
function greet(name: string, greeting?: string): string {
  return `${greeting || '你好'}, ${name}!`;
}

// 箭头函数
const multiply = (a: number, b: number): number => a * b;

// 回调函数类型
type Callback = (result: string) => void;

function fetchData(url: string, callback: Callback): void {
  // 模拟异步操作
  callback('data loaded');
}
```

### 1.4 类与接口

```typescript
// 接口定义
interface IUser {
  id: number;
  name: string;
  email?: string;
  getDisplayName(): string;
}

// 类实现
class User implements IUser {
  id: number;
  name: string;
  email?: string;

  constructor(id: number, name: string, email?: string) {
    this.id = id;
    this.name = name;
    this.email = email;
  }

  getDisplayName(): string {
    return this.email ? `${this.name} <${this.email}>` : this.name;
  }
}

// 泛型类
class DataStore<T> {
  private items: T[] = [];

  add(item: T): void {
    this.items.push(item);
  }

  getAll(): T[] {
    return [...this.items];
  }
}

const store = new DataStore<string>();
store.add('item1');
```

### 1.5 ArkTS 与 TypeScript 差异

| 特性           | TypeScript | ArkTS                 |
| :------------- | :--------- | :-------------------- |
| **eval**       | 支持       | 禁止                  |
| **with**       | 支持       | 禁止                  |
| **动态属性**   | 支持       | 限制使用              |
| **原型链修改** | 支持       | 禁止                  |
| **any 类型**   | 支持       | 不推荐，严格限制      |
| **装饰器**     | 实验性支持 | 原生支持（UI 装饰器） |

## 2. ArkUI 方舟开发框架

### 2.1 ArkUI 概述

ArkUI 是 HarmonyOS 的**声明式 UI 开发框架**，提供一套统一的开发范式：

| 特性          | 说明                           |
| :------------ | :----------------------------- |
| **声明式 UI** | 描述 UI 应该是什么，而非怎么做 |
| **组件化**    | 一切皆组件，可组合嵌套         |
| **状态驱动**  | UI 自动响应状态变化            |
| **跨设备**    | 一套代码适配多种设备           |

### 2.2 声明式 UI 范式

```typescript
// 命令式 UI（传统方式）
// textView.setText("Hello");
// textView.setTextColor(Color.BLUE);

// 声明式 UI（ArkUI 方式）
@Entry
@Component
struct HelloPage {
  @State message: string = 'Hello';

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontColor(Color.Blue)
    }
  }
}
```

### 2.3 UI 渲染流程

```
状态变化 → 框架检测变化 → 重新执行 build() → 虚拟 DOM Diff → 最小化更新真实 DOM
```

## 3. 装饰器体系

### 3.1 @Entry 装饰器

标记页面入口组件，一个页面只能有一个 `@Entry` 组件：

```typescript
@Entry
@Component
struct MainPage {
  build() {
    Column() {
      Text('这是页面入口')
    }
  }
}
```

### 3.2 @Component 装饰器

将 struct 声明为 UI 组件，每个组件必须包含 `build()` 方法：

```typescript
@Component
export struct GreetingCard {
  @Prop name: string = '';

  build() {
    Row() {
      Text(`你好, ${this.name}!`)
        .fontSize(20)
    }
    .padding(16)
    .backgroundColor('#f5f5f5')
    .borderRadius(8)
  }
}
```

### 3.3 @Builder 装饰器

定义轻量级 UI 构建函数，用于复用 UI 片段：

```typescript
@Entry
@Component
struct BuilderDemo {
  @State items: string[] = ['首页', '发现', '我的'];

  // 定义 Builder
  @Builder
  TabItem(title: string, index: number) {
    Column() {
      Text(title)
        .fontSize(14)
        .fontColor(index === 0 ? '#1a73e8' : '#999999')
      Divider()
        .color(index === 0 ? '#1a73e8' : 'transparent')
        .width(20)
    }
    .padding({ left: 12, right: 12 })
  }

  build() {
    Row() {
      ForEach(this.items, (item: string, index?: number) => {
        this.TabItem(item, index ?? 0)
      })
    }
  }
}
```

### 3.4 @BuilderParam 与 @WrapBuilder

用于插槽式组件设计：

```typescript
// 子组件定义插槽
@Component
struct Card {
  @BuilderParam contentBuilder: () => void;

  build() {
    Column() {
      // 渲染插槽内容
      this.contentBuilder()
    }
    .padding(16)
    .backgroundColor('#ffffff')
    .borderRadius(12)
    .shadow({ radius: 4, color: '#1a000000', offsetY: 2 })
  }
}

// 父组件传入内容
@Entry
@Component
struct CardDemo {
  @Builder
  cardContent() {
    Text('这是卡片内容')
      .fontSize(16)
  }

  build() {
    Column() {
      Card({ contentBuilder: this.cardContent })
    }
    .padding(20)
  }
}
```

## 4. 状态管理

### 4.1 状态管理总览

```mermaid
flowchart LR
    State[@State] --> Prop[@Prop --> 子组件]
    State --> Link[@Link <--> 子组件（双向）]
    State --> Provide[@Provide --> @Consume（跨层级）]
```

### 4.2 @State 装饰器

组件内部状态，变化会触发 UI 刷新：

```typescript
@Entry
@Component
struct StateDemo {
  @State count: number = 0;
  @State user: User = { name: '张三', age: 25 };

  build() {
    Column() {
      Text(`计数: ${this.count}`)
        .fontSize(24)

      Button('增加')
        .onClick(() => {
          this.count += 1;  // 触发 UI 刷新
        })

      Button('修改用户')
        .onClick(() => {
          this.user.name = '李四';  // 嵌套属性变化也触发刷新
        })
    }
  }
}
```

> **注意**：@State 支持观察 Object 和 Array 的嵌套属性变化（一级嵌套）。

### 4.3 @Prop 装饰器

父组件向子组件**单向传递**数据，子组件本地可修改但不影响父组件：

```typescript
@Component
struct ChildComponent {
  @Prop title: string = '';
  @Prop count: number = 0;

  build() {
    Column() {
      Text(this.title)
        .fontSize(20)
      Text(`数量: ${this.count}`)
        .fontSize(16)
    }
  }
}

@Entry
@Component
struct ParentComponent {
  @State message: string = '标题';
  @State num: number = 5;

  build() {
    Column() {
      ChildComponent({ title: this.message, count: this.num })
      Button('修改')
        .onClick(() => {
          this.num += 1;  // 父组件修改会同步到子组件
        })
    }
  }
}
```

### 4.4 @Link 装饰器

父子组件**双向绑定**，子组件修改会同步回父组件：

```typescript
@Component
struct Counter {
  @Link value: number;

  build() {
    Row() {
      Button('-')
        .onClick(() => {
          this.value -= 1;  // 修改会同步到父组件
        })
      Text(`${this.value}`)
        .fontSize(24)
        .margin({ left: 16, right: 16 })
      Button('+')
        .onClick(() => {
          this.value += 1;
        })
    }
  }
}

@Entry
@Component
struct LinkDemo {
  @State count: number = 0;

  build() {
    Column() {
      Text(`父组件计数: ${this.count}`)
        .fontSize(20)
      // 使用 $ 语法传递引用
      Counter({ value: $count })
    }
  }
}
```

### 4.5 @Provide 与 @Consume

跨层级组件通信，无需逐层传递：

```typescript
@Entry
@Component
struct GrandParent {
  @Provide theme: string = 'light';

  build() {
    Column() {
      Text(`主题: ${this.theme}`)
      Parent()
      Button('切换主题')
        .onClick(() => {
          this.theme = this.theme === 'light' ? 'dark' : 'light';
        })
    }
  }
}

@Component
struct Parent {
  build() {
    Column() {
      Child()  // 无需传递 theme
    }
  }
}

@Component
struct Child {
  @Consume theme: string;  // 自动匹配同名的 @Provide

  build() {
    Text(`当前主题: ${this.theme}`)
      .fontColor(this.theme === 'dark' ? '#ffffff' : '#000000')
  }
}
```

### 4.6 状态管理对比

| 装饰器        | 方向      | 嵌套层级 | 典型场景         |
| :------------ | :-------- | :------- | :--------------- |
| **@State**    | 组件内部  | -        | 组件私有状态     |
| **@Prop**     | 父→子     | 1 层     | 只读展示数据     |
| **@Link**     | 父↔子     | 1 层     | 表单双向绑定     |
| **@Provide**  | 祖先→后代 | N 层     | 主题、全局配置   |
| **@Consume**  | 后代←祖先 | N 层     | 消费全局配置     |
| **@Watch**    | 监听变化  | -        | 状态变化回调     |
| **@Observed** | 类装饰器  | -        | 深度观察嵌套对象 |

### 4.7 @Watch 装饰器

监听状态变化并执行回调：

```typescript
@Entry
@Component
struct WatchDemo {
  @State @Watch('onPriceChange') price: number = 100;

  onPriceChange(newValue: number, oldValue: number) {
    console.info(`价格从 ${oldValue} 变为 ${newValue}`);
  }

  build() {
    Column() {
      Text(`价格: ${this.price}`)
      Button('涨价')
        .onClick(() => {
          this.price += 10;
        })
    }
  }
}
```

## 5. 条件渲染与循环渲染

### 5.1 条件渲染

```typescript
@Entry
@Component
struct ConditionalDemo {
  @State isLoggedIn: boolean = false;

  build() {
    Column() {
      if (this.isLoggedIn) {
        Text('欢迎回来！')
          .fontSize(20)
          .fontColor('#1a73e8')
      } else {
        Text('请先登录')
          .fontSize(20)
          .fontColor('#999999')
      }

      Button(this.isLoggedIn ? '退出' : '登录')
        .onClick(() => {
          this.isLoggedIn = !this.isLoggedIn;
        })
    }
  }
}
```

### 5.2 循环渲染（ForEach）

```typescript
@Entry
@Component
struct ForEachDemo {
  @State fruits: string[] = ['苹果', '香蕉', '橘子'];

  build() {
    Column() {
      ForEach(
        this.fruits,
        (item: string, index?: number) => {
          Row() {
            Text(`${(index ?? 0) + 1}. ${item}`)
              .fontSize(18)
          }
          .width('100%')
          .padding(12)
        },
        (item: string) => item  // 键值生成器
      )

      Button('添加水果')
        .onClick(() => {
          this.fruits.push('葡萄');
        })
    }
  }
}
```

### 5.3 LazyForEach 懒加载

适用于大数据量列表，按需加载：

```typescript
// 数据源需要实现 IDataSource 接口
class MyDataSource implements IDataSource {
  private data: string[] = [];

  totalCount(): number {
    return this.data.length;
  }

  getData(index: number): string {
    return this.data[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {}
  unregisterDataChangeListener(listener: DataChangeListener): void {}
}

@Entry
@Component
struct LazyForEachDemo {
  private dataSource: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i < 1000; i++) {
      this.dataSource.data.push(`Item ${i}`);
    }
  }

  build() {
    List() {
      LazyForEach(
        this.dataSource,
        (item: string) => {
          ListItem() {
            Text(item).fontSize(16)
          }
          .height(60)
        },
        (item: string) => item
      )
    }
    .width('100%')
    .height('100%')
  }
}
```

## 6. 组件生命周期

### 6.1 UIAbility 生命周期

```
onCreate → onWindowStageCreate → onForeground ↔ onBackground → onWindowStageDestroy → onDestroy
```

### 6.2 组件生命周期

```typescript
@Entry
@Component
struct LifecycleDemo {
  @State message: string = 'Hello';

  // 组件即将出现
  aboutToAppear() {
    console.info('组件即将出现，可初始化数据');
  }

  // 组件即将销毁
  aboutToDisappear() {
    console.info('组件即将销毁，可清理资源');
  }

  // 页面显示
  onPageShow() {
    console.info('页面显示');
  }

  // 页面隐藏
  onPageHide() {
    console.info('页面隐藏');
  }

  // 返回键按下
  onBackPress(): boolean {
    console.info('返回键按下');
    return false;  // false 表示不拦截，true 表示拦截
  }

  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

| 回调                 | 触发时机             | 用途               |
| :------------------- | :------------------- | :----------------- |
| **aboutToAppear**    | 组件创建后、build 前 | 初始化数据         |
| **aboutToDisappear** | 组件销毁前           | 清理定时器、监听器 |
| **onPageShow**       | 页面显示时           | 刷新数据           |
| **onPageHide**       | 页面隐藏时           | 暂停操作           |
| **onBackPress**      | 返回键按下时         | 拦截返回行为       |
## 尺寸属性

**width / height 宽高**
`.width(<Length>): void / .height(<Length>): void`
```typescript
Text('Hello')
  .width(120)
  .height(40)
```

**size 同时设置宽高**
`.size({ width: <Length>, height: <Length> }): void`
```typescript
Text('Hello').size({ width: 120, height: 40 })
```

**constraintSize 约束尺寸**
`.constraintSize({ minWidth?, maxWidth?, minHeight?, maxHeight? }): void`
```typescript
Text('Hello').constraintSize({ minWidth: 100, maxWidth: 200 })
```

**aspectRatio 宽高比**
`.aspectRatio(<ratio>: number): void`
```typescript
Image($r('app.media.icon')).aspectRatio(1.5)
```

**layoutWeight 权重**
`.layoutWeight(<weight>: number): void`
```typescript
Row() {
  Text('Left').layoutWeight(1)
  Text('Right').layoutWeight(2)
}
```

---

## 位置属性

**position 绝对定位**
`.position({ x: <Length>, y: <Length> }): void`
```typescript
Text('Hello').position({ x: 100, y: 100 })
```

**markAnchor 锚点**
`.markAnchor({ x: <Length>, y: <Length> }): void`
```typescript
Text('Hello').markAnchor({ x: 0, y: 0 })
```

**offset 相对偏移**
`.offset({ x: <Length>, y: <Length> }): void`
```typescript
Text('Hello').offset({ x: 10, y: 10 })
```

**zIndex 层级**
`.zIndex(<number>): void`
```typescript
Text('Hello').zIndex(10)
```

---

## 边距与边框

**margin 外边距**
`.margin({ top?, right?, bottom?, left? } | <Length>): void`
```typescript
Text('Hello').margin({ top: 8, right: 8, bottom: 8, left: 8 })
Text('Hello').margin(8)
```

**padding 内边距**
`.padding({ top?, right?, bottom?, left? } | <Length>): void`
```typescript
Text('Hello').padding({ top: 8, right: 8, bottom: 8, left: 8 })
```

**border 边框**
`.border({ width, color, radius, style }): void`
```typescript
Text('Hello').border({
  width: 1,
  color: '#ccc',
  radius: 8,
  style: BorderStyle.Solid
})
```

**borderRadius 圆角**
`.borderRadius(<Length> | { topLeft?, topRight?, bottomLeft?, bottomRight? }): void`
```typescript
Text('Hello').borderRadius(8)
```

---

## 背景与前景

**backgroundColor 背景色**
`.backgroundColor(<ResourceColor>): void`
```typescript
Text('Hello').backgroundColor('#1a73e8')
```

**backgroundImage 背景图**
`.backgroundImage(<ResourceStr>): void`
```typescript
Text('Hello').backgroundImage($r('app.media.bg'))
```

**backgroundImageSize 背景图尺寸**
`.backgroundImageSize(<ImageSize> | { width, height }): void`
```typescript
Text('Hello').backgroundImageSize(ImageSize.Cover)
```

**opacity 透明度**
`.opacity(<number>): void`
```typescript
Text('Hello').opacity(0.8)
```

**foregroundColor 前景色**
`.foregroundColor(<ResourceColor>): void`
```typescript
Text('Hello').foregroundColor(Color.White)
```

---

## 可见性

**visibility 可见性**
`.visibility(<Visibility>): void`
```typescript
Column().visibility(Visibility.Hidden)  // Visible | Hidden | None
```

**enabled 是否启用**
`.enabled(<boolean>): void`
```typescript
Button('Submit').enabled(false)
```

---

## 点击事件

**onClick 点击**
`<Component>.onClick((event: ClickEvent) => { ... }): void`
```typescript
Button('Click').onClick((event: ClickEvent) => {
  console.info(`x: ${event.x}, y: ${event.y}`)
})
```

---

## 触摸事件

**onTouch 触摸**
`<Component>.onTouch((event: TouchEvent) => { ... }): void`
```typescript
Column().onTouch((event: TouchEvent) => {
  if (event.type === TouchType.Down) {
    console.info('按下')
  } else if (event.type === TouchType.Up) {
    console.info('抬起')
  }
})
```

**TouchType 枚举**
```typescript
enum TouchType {
  Down = 0,
  Up = 1,
  Move = 2,
  Cancel = 3
}
```

---

## 挂载事件

**onAppear 显示**
`<Component>.onAppear(() => { ... }): void`
```typescript
Column().onAppear(() => {
  console.info('显示')
})
```

**onDisappear 隐藏**
`<Component>.onDisappear(() => { ... }): void`
```typescript
Column().onDisappear(() => {
  console.info('隐藏')
})
```

---

## 区域变化事件

**onAreaChange 区域变化**
`<Component>.onAreaChange((oldValue: Area, newValue: Area) => { ... }): void`
```typescript
Column().onAreaChange((oldValue: Area, newValue: Area) => {
  console.info(`width: ${newValue.width}`)
})
```

**onVisibleAreaChange 可见区域变化**
`<Component>.onVisibleAreaChange([<ratios>], (isDetect: boolean, ratio: number) => { ... }): void`
```typescript
Column().onVisibleAreaChange([0.5, 1.0], (isDetect: boolean, ratio: number) => {
  console.info(`可见比例: ${ratio}`)
})
```

---

## 按键与鼠标事件

**onKeyEvent 按键**
`<Component>.onKeyEvent((event: KeyEvent) => { ... }): void`
```typescript
TextInput({ placeholder: '请输入' })
  .onKeyEvent((event: KeyEvent) => {
    if (event.type === KeyType.Down) {
      console.info(`按下键: ${event.keyCode}`)
    }
  })
```

**onMouse 鼠标**
`<Component>.onMouse((event: MouseEvent) => { ... }): void`
```typescript
Text('鼠标区域').onMouse((event: MouseEvent) => {
  console.info(`鼠标事件: ${event.action}`)
})
```

**onHover 悬停**
`<Component>.onHover((isHover: boolean) => { ... }): void`
```typescript
Text('鼠标区域').onHover((isHover: boolean) => {
  console.info(`悬停状态: ${isHover}`)
})
```

---

## 焦点事件

**onFocus 获得焦点**
`<Component>.onFocus(() => { ... }): void`
```typescript
TextInput().onFocus(() => console.info('获得焦点'))
```

**onBlur 失去焦点**
`<Component>.onBlur(() => { ... }): void`
```typescript
TextInput().onBlur(() => console.info('失去焦点'))
```

---

## 动画属性绑定

**animation 属性动画绑定**
`.animation(value: AnimateParam): void`
```typescript
Image($r('app.media.icon'))
  .width(100).height(100)
  .scale({ x: this.scale, y: this.scale })
  .opacity(this.opacity)
  .animation({
    duration: 300,
    curve: Curve.EaseInOut,
    delay: 0,
    iterations: 1,
    playMode: PlayMode.Normal,
    onFinish: () => {}
  })
```

**AnimateParam 参数**
```typescript
interface AnimateParam {
  duration: number
  tempo?: number
  curve?: Curve | ICurve
  delay?: number
  iterations?: number
  playMode?: PlayMode
  onFinish?: () => void
  onStart?: () => void
}
```

---

## 变换属性

**scale 缩放**
`.scale(value: ScaleOptions): void`
```typescript
.scale({ x: 1.5, y: 1.5, centerX: 0, centerY: 0 })
```

**translate 平移**
`.translate(value: TranslateOptions): void`
```typescript
.translate({ x: 100, y: 50 })
```

**rotate 旋转**
`.rotate(value: RotateOptions): void`
```typescript
.rotate({ angle: 45, centerX: 0, centerY: 0 })
```

**ScaleOptions**
```typescript
interface ScaleOptions {
  x?: number
  y?: number
  z?: number
  centerX?: number | string
  centerY?: number | string
}
```

**TranslateOptions**
```typescript
interface TranslateOptions {
  x?: number | string
  y?: number | string
  z?: number | string
}
```

**RotateOptions**
```typescript
interface RotateOptions {
  angle: number | string
  centerX?: number | string
  centerY?: number | string
  centerZ?: number | string
  perspective?: number
}
```

---

## 图像效果

**brightness 亮度**
`.brightness(<number>): void`
```typescript
Image($r('app.media.icon')).brightness(1.5)
```

**saturate 饱和度**
`.saturate(<number>): void`
```typescript
Image($r('app.media.icon')).saturate(2.0)
```

**contrast 对比度**
`.contrast(<number>): void`
```typescript
Image($r('app.media.icon')).contrast(1.2)
```

---

## 转场动画

**transition 转场**
`.transition(value: TransitionOptions | TransitionOptions[]): void`
```typescript
Column() {
  Text('展开内容')
}
.transition({
  type: TransitionType.Insert,
  opacity: 0,
  translate: { y: -20 }
})
.transition({
  type: TransitionType.Delete,
  opacity: 0,
  translate: { y: -20 }
})
```

**TransitionType 枚举**
```typescript
enum TransitionType {
  All = 'all',
  Insert = 'insert',
  Delete = 'delete'
}
```

**TransitionOptions 配置**
```typescript
interface TransitionOptions {
  type?: TransitionType
  opacity?: number
  translate?: TranslateOptions
  scale?: ScaleOptions
  rotate?: RotateOptions
}
```

---

## 共享元素转场

**geometryTransition 共享元素**
`.geometryTransition(id: string): void`
```typescript
Image($r('app.media.photo'))
  .geometryTransition('shared_image_id')
  .width(100).height(100)
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
