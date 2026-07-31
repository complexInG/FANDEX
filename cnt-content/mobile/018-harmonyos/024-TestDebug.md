# 测试与调试 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 日志输出

**基本写法：console 日志**
`console.info('<消息>')`
```typescript
// 输出 info 级别日志
console.info('应用启动完成')
console.error('加载失败')
console.warn('资源缺失')
```

---

**基本写法：hilog 结构化日志**
`hilog.info(<域ID>, '<标签>', '<消息>')`
```typescript
// 使用 hilog 输出结构化日志
import { hilog } from '@kit.PerformanceAnalysisKit'

const DOMAIN = 0x0001
hilog.info(DOMAIN, 'MyTag', '应用启动')
hilog.error(DOMAXIN, 'MyTag', '错误: %{public}s', '网络超时')
```

---

**基本写法：格式化日志参数**
`hilog.info(<域ID>, '<标签>', '<格式>', <参数>)`
```typescript
// 使用格式化占位符
hilog.info(DOMAIN, 'MyTag', '用户: %{public}s, 年龄: %{public}d', name, age)
// private 表示参数不在日志中明文显示
hilog.info(DOMAIN, 'MyTag', '密码: %{private}s', password)
```

---

## hdc 调试命令

**基本写法：查看日志**
`hdc shell hilog`
```bash
# 实时查看设备日志
hdc shell hilog
# 过滤标签
hdc shell hilog -T MyTag
# 过滤级别（D/I/W/E/F）
hdc shell hilog -L I
```

---

**基本写法：清除日志缓冲**
`hdc shell hilog -r`
```bash
# 清空日志缓冲区
hdc shell hilog -r
```

---

**基本写法：进入设备 shell**
`hdc shell`
```bash
# 进入设备终端
hdc shell
# 执行单条命令
hdc shell ls /data/local/tmp
```

---

**基本写法：文件推送与拉取**
`hdc file send <本地路径> <设备路径>`
```bash
# 推送文件到设备
hdc file send ./test.txt /data/local/tmp/
# 从设备拉取文件
hdc file recv /data/local/tmp/log.txt ./
```

---

**基本写法：截屏**
`hdc shell snapshot_display -f <文件路径>`
```bash
# 截图保存到设备
hdc shell snapshot_display -f /data/local/tmp/screenshot.png
# 拉取到本地
hdc file recv /data/local/tmp/screenshot.png ./
```

---

## 断点调试

**基本写法：DevEco Studio 断点**
`// 在代码行号旁点击设置断点`
```typescript
// 在 DevEco Studio 中点击行号旁空白设置断点
// 按 F9 (Resume) 继续执行
// F8 (Step Over) 单步跳过
// F7 (Step Into) 单步进入
```

---

**基本写法：条件断点**
`// 右键断点设置条件表达式`
```typescript
// 右键断点 → Condition → 输入条件
// 如 i === 100 仅在 i 为 100 时暂停
for (let i = 0; i < 1000; i++) {
  // 条件断点: i === 500
  this.process(i)
}
```

---

**基本写法：日志断点**
`// 右键断点 → More → 取消勾选 Suspend → 填写 Log`
```typescript
// 日志断点不暂停执行，仅输出日志
// 适用于无法加 console.log 的库代码
```

---

## 性能分析

**基本写法：Profiler 启动**
`// DevEco Studio → View → Tool Windows → Profiler`
```text
// 打开 Profiler 面板
// 选择 Session → 选择设备与应用
// 可监控 CPU、内存、帧率、能耗
```

---

**基本写法：CPU 性能分析**
`// Profiler → CPU → Record`
```text
// 录制 CPU 使用情况
// 查看函数调用栈与耗时占比
// 识别热点函数
```

---

**基本写法：内存分析**
`// Profiler → Memory → Heap Dump`
```text
// 捕获堆快照分析内存泄漏
// 查看对象分布与引用链
```

---

## 单元测试

**基本写法：创建测试类**
`@TestSuite class <测试类> { @Test <方法名>() { } }`
```typescript
// ArkTS 单元测试
import { describe, it, expect } from '@ohos/hypium'

export default function abilityTest() {
  describe('abilityTest', () => {
    it('assertContain', 0, () => {
      let a = 'abc'
      let b = 'b'
      expect(a).assertContain(b)
    })
  })
}
```

---

**基本写法：断言**
`expect(<实际>).assertEqual(<期望>)`
```typescript
// 常用断言方法
expect(1 + 1).assertEqual(2)
expect('hello').assertContain('ell')
expect(true).assertTrue()
expect(null).assertNull()
```

---

**基本写法：异步测试**
`it('<描述>', 0, async (done: Function) => { done() })`
```typescript
// 异步测试用例
it('asyncTest', 0, async (done: Function) => {
  let result = await fetchData()
  expect(result).assertEqual('ok')
  done()
})
```

---

**基本写法：运行测试**
`hvigorw test`
```bash
# 运行所有单元测试
hvigorw test
# 运行指定模块测试
hvigorw --mode module -p module=entry@default test
```

---

## UI 测试

**基本写法：UiTest 驱动**
`import { UiDriver } from '@kit.TestKit'`
```typescript
// 自动化 UI 测试
import { UiDriver, UiComponent, BY } from '@kit.TestKit'

async function uiTest() {
  let driver = new UiDriver()
  let btn = await driver.findComponent(BY.text('确定'))
  await btn.click()
}
```

---

**基本写法：查找组件**
`driver.findComponent(BY.text('<文本>'))`
```typescript
// 按文本查找按钮并点击
let btn = await driver.findComponent(BY.text('登录'))
await btn.click()
// 按 ID 查找
let input = await driver.findComponent(BY.id('username'))
await input.inputText('admin')
```
