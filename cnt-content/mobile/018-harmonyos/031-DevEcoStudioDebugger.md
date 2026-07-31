# DevEco Studio 调试器 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 工程构建

**基本写法：构建项目**
`hvigorw assembleHap`
```bash
# 命令行构建 HAP
hvigorw --mode module -p module=entry@default assembleHap --parallel --daemon
```

---

**基本写法：构建 Release 包**
`hvigorw --mode project -p product=default assembleApp --build-mode release`
```bash
# 构建 Release 模式的 APP 包
hvigorw --mode project -p product=default assembleApp --build-mode release
```

---

**基本写法：清理构建产物**
`hvigorw clean`
```bash
# 清理所有构建产物
hvigorw clean
```

---

**基本写法：构建多模块**
`hvigorw --mode project -p product=<产品> assembleHap`
```bash
# 构建所有模块
hvigorw --mode project -p product=default assembleHap
```

---

## 签名配置

**基本写法：DevEco Studio 图形化配置**
`// File → Project Structure → Signing Configs`
```text
// 自动签名流程
// 1. 打开 File → Project Structure
// 2. 选择 Signing Configs 标签
// 3. 勾选 Automatically sign
// 4. 选择或创建密钥库
// 5. 配置 Profile 和证书
```

---

**基本写法：手动签名**
`// Signing Configs → 添加 Release 配置`
```text
// 手动签名流程
// 1. Signing Configs → 点击 +
// 2. 名称填写 release
// 3. Store File 选择 .p12 文件
// 4. Store Password / Key Alias / Key Password
// 5. Sign Profile 选择 .p7b
// 6. Sign Cert 选择 .cer
// 7. Apply → OK
```

---

**基本写法：构建变体切换**
`// Build → Select Build Variant`
```text
// 切换构建变体
// 1. 左下角 Build Variants 面板
// 2. 或 Build → Select Build Variant
// 3. 选择 debug 或 release
// 4. 重新构建
```

---

## 断点调试

**基本写法：设置断点**
`// 点击代码行号左侧空白区域`
```text
// 断点操作
// 左键点击行号旁 → 设置断点（红点）
// 再次点击 → 取消断点
// 右键断点 → 更多选项（条件、日志断点）
```

---

**基本写法：条件断点**
`// 右键断点 → Condition: <表达式>`
```typescript
// 条件断点：仅当条件为真时暂停
for (let i = 0; i < 1000; i++) {
  // 断点条件: i === 500
  this.process(i)
}
```

---

**基本写法：调试快捷键**
`// F8: Step Over | F7: Step Into | F9: Resume`
```text
// 调试快捷键
// F9  / Resume Program    → 继续执行
// F8  / Step Over         → 单步跳过
// F7  / Step Into         → 单步进入
// Shift+F8 / Step Out     → 跳出当前函数
// Ctrl+F8 / Toggle        → 切换断点
```

---

**基本写法：变量监视**
`// Variables 面板 → 右键 Add to Watches`
```text
// 监视变量变化
// 1. 调试时打开 Variables 面板
// 2. 右键变量 → Add to Watches
// 3. 或在 Watches 面板手动输入表达式
```

---

**基本写法：表达式求值**
`// Alt+F8 / Evaluate Expression`
```typescript
// 调试时动态计算表达式
// 按 Alt+F8 打开求值窗口
// 输入表达式如: this.items.length
// 或: 1 + 2 * 3
```

---

## 日志调试

**基本写法：DevEco Studio 日志面板**
`// View → Tool Windows → Log`
```text
// 日志面板使用
// 1. View → Tool Windows → HiLog
// 2. 选择设备与应用进程
// 3. 日志级别筛选（D/I/W/E/F）
// 4. 关键词搜索过滤
// 5. 保存日志到文件
```

---

**基本写法：hilog 过滤**
`// 日志面板搜索栏输入过滤条件`
```text
// 日志过滤技巧
// 按标签过滤: tag:MyTag
// 按级别过滤: level:E
// 按内容过滤: 关键词
// 组合过滤: tag:MyTag level:E
```

---

**基本写法：代码中输出日志**
`hilog.info(<域>, '<标签>', '<消息>')`
```typescript
// 使用 hilog 输出日志
import { hilog } from '@kit.PerformanceAnalysisKit'

const DOMAIN = 0x0001
hilog.info(DOMAIN, 'MyApp', '页面加载完成')
hilog.error(DOMAIN, 'MyApp', '网络请求失败: %{public}s', err.message)
```

---

## hdc 命令

**基本写法：查看连接设备**
`hdc list targets`
```bash
# 列出所有已连接设备
hdc list targets
```

---

**基本写法：安装应用**
`hdc install <hap路径>`
```bash
# 安装 HAP 包到设备
hdc install entry-default-signed.hap
# 覆盖安装
hdc install -r entry-default-signed.hap
```

---

**基本写法：卸载应用**
`hdc uninstall <包名>`
```bash
# 卸载指定应用
hdc uninstall com.example.myapp
```

---

**基本写法：查看日志**
`hdc shell hilog`
```bash
# 实时查看设备日志
hdc shell hilog
# 过滤指定标签
hdc shell hilog -T MyApp
# 仅显示错误级别
hdc shell hilog -L E
```

---

**基本写法：文件操作**
`hdc file send <本地> <设备>`
```bash
# 推送文件到设备
hdc file send ./config.json /data/local/tmp/
# 从设备拉取文件
hdc file recv /data/local/tmp/log.txt ./
```

---

**基本写法：截屏**
`hdc shell snapshot_display -f <路径>`
```bash
# 设备截屏并拉取
hdc shell snapshot_display -f /data/local/tmp/screen.png
hdc file recv /data/local/tmp/screen.png ./
```

---

**基本写法：进入 shell**
`hdc shell`
```bash
# 进入设备终端
hdc shell
# 执行单条命令
hdc shell ps -ef | grep myapp
```

---

## 内存与性能分析

**基本写法：Profiler 面板**
`// View → Tool Windows → Profiler`
```text
// 性能分析流程
// 1. View → Tool Windows → Profiler
// 2. 选择设备与应用
// 3. 选择分析维度：
//    - CPU：函数调用栈与耗时
//    - Memory：内存分配与泄漏
//    - Energy：能耗分析
//    - Disk：磁盘 IO
//    - Network：网络请求
```

---

**基本写法：内存泄漏分析**
`// Profiler → Memory → Capture Heap Dump`
```text
// 内存泄漏排查步骤
// 1. Profiler → Memory 面板
// 2. 操作应用触发可疑场景
// 3. 点击 Capture Heap Dump
// 4. 分析对象分布与引用链
// 5. 定位未释放的对象
```

---

**基本写法：CPU 热点分析**
`// Profiler → CPU → Record → Stop → 查看火焰图`
```text
// CPU 性能分析
// 1. Profiler → CPU
// 2. 点击 Record 开始录制
// 3. 操作应用复现性能问题
// 4. Stop 停止录制
// 5. 查看 Call Chart / Flame Chart
// 6. 识别耗时最长的函数
```
