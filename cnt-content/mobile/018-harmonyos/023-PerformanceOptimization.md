# 性能优化 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 构建优化

**基本写法：并行构建**
`hvigorw assembleHap --parallel --daemon`
```bash
# 启用并行构建与守护进程加速
hvigorw --mode module -p module=entry@default assembleHap --parallel --daemon --incremental
```

---

**基本写法：增量构建**
`hvigorw assembleHap --incremental`
```bash
# 仅编译变更部分
hvigorw assembleHap --incremental
```

---

**基本写法：分析构建性能**
`hvigorw assembleHap --analyze=normal`
```bash
# 输出构建分析报告
hvigorw --mode module -p module=entry@default assembleHap --analyze=normal
```

---

## LazyForEach 懒加载

**基本写法：LazyForEach 替代 ForEach**
`LazyForEach(<数据源>, (<item>) => <组件>, (<item>) => <键>)`
```typescript
// 大数据列表懒加载，仅渲染可视区域
LazyForEach(this.dataSource, (item: string) => {
  ListItem() {
    Text(item).fontSize(16)
  }
}, (item: string) => item)
```

---

**基本写法：实现 IDataSource**
`class <名> implements IDataSource { totalCount(): number { } getData(<index>): <T> { } }`
```typescript
// 自定义懒加载数据源
class MyDataSource implements IDataSource {
  private data: string[] = []
  totalCount(): number { return this.data.length }
  getData(index: number): string { return this.data[index] }
  registerDataChangeListener(listener: DataChangeListener): void { }
  unregisterDataChangeListener(listener: DataChangeListener): void { }
}
```

---

## 组件复用

**基本写法：@Reusable 标记可复用组件**
`@Reusable @Component struct <组件名> { aboutToReuse(<params>): void { } }`
```typescript
// 标记组件可复用，减少重复创建开销
@Reusable
@Component
struct MyItem {
  @State title: string = ''
  aboutToReuse(params: Record<string, object>): void {
    this.title = params.title as string
  }
  build() { Text(this.title) }
}
```

---

**基本写法：使用复用组件**
`<复用组件>({ <参数>: <值> })`
```typescript
// 在列表中使用可复用组件
ForEach(this.items, (item: string) => {
  MyItem({ title: item })
}, (item: string) => item)
```

---

## 状态管理优化

**基本写法：@ObjectLink 嵌套对象**
`@ObjectLink <var>: <Class>;`
```typescript
// 嵌套对象响应式更新
@Observed
class ItemData {
  name: string = ''
  count: number = 0
}

@Component
struct ItemView {
  @ObjectLink item: ItemData
  build() { Text(`${this.item.name}: ${this.item.count}`) }
}
```

---

**基本写法：@Observed 标记可观察类**
`@Observed class <类名> { }`
```typescript
// 标记类为可观察对象
@Observed
class User {
  name: string
  age: number
  constructor(name: string, age: number) {
    this.name = name
    this.age = age
  }
}
```

---

**基本写法：AppStorage 全局状态**
`AppStorage.setOrCreate('<键>', <值>);`
```typescript
// 全局共享状态，避免逐层传递
AppStorage.setOrCreate('userInfo', { name: 'Tom', age: 18 })
// 获取全局状态
let user = AppStorage.get('userInfo')
```

---

**基本写法：@StorageLink 双向绑定全局状态**
`@StorageLink('<键>') <var>: <类型>;`
```typescript
// 组件内双向绑定 AppStorage
@StorageLink('count') count: number = 0
build() {
  Button(`count: ${this.count}`).onClick(() => this.count++)
}
```

---

## 条件渲染优化

**基本写法：if/else 替代 Visibility 隐藏**
`if (<条件>) { <组件A> } else { <组件B> }`
```typescript
// 条件渲染仅创建需要的组件
if (this.isLoading) {
  LoadingProgress()
} else {
  Text(this.content)
}
```

---

**基本写法：避免频繁 if 切换**
`// 使用 Visibility.None 保留组件结构`
```typescript
// 高频切换场景用 Visibility 避免重建
Text(this.text)
  .visibility(this.show ? Visibility.Visible : Visibility.None)
```

---

## 任务调度

**基本写法：TaskPool 子线程执行**
`taskpool.execute(<函数>).then(<回调>)`
```typescript
// 将耗时任务放入 TaskPool 子线程
import { taskpool } from '@kit.ArkTS'

@Concurrent
function heavyCompute(input: number): number {
  return input * input
}

taskpool.execute(heavyCompute, 42).then((result) => {
  console.info(`结果: ${result}`)
})
```

---

**基本写法：Worker 子线程**
`const <worker> = new worker.ThreadWorker('<脚本路径>')`
```typescript
// 创建 Worker 线程处理耗时任务
import { worker } from '@kit.ArkTS'

const w = new worker.ThreadWorker('entry/ets/workers/MyWorker.ets')
w.postMessage({ data: 'hello' })
w.onmessage = (e) => { console.info(`收到: ${e.data}`) }
```

---

**基本写法：Worker 发送消息**
`postMessage(<数据>);`
```typescript
// Worker 线程内向主线程发送数据
// MyWorker.ets
const w: worker.ThreadWorker = worker.workerPort
w.onmessage = (e) => {
  w.postMessage(`处理完成: ${e.data}`)
}
```

---

## 图片优化

**基本写法：Image 组件加载资源**
`Image($r('app.media.<资源>')).objectFit(ImageFit.Cover)`
```typescript
// 指定图片适配模式
Image($r('app.media.background'))
  .objectFit(ImageFit.Cover)
  .width('100%')
  .height(200)
```

---

**基本写法：异步加载网络图片**
`Image('<url>').alt($r('app.media.placeholder'))`
```typescript
// 设置占位图避免闪烁
Image('https://example.com/image.jpg')
  .alt($r('app.media.placeholder'))
  .objectFit(ImageFit.Contain)
```
