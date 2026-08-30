# 更新日志

## v3.7.0（2026-07-21）

### Android App 代码质量优化 + 主题过渡动画 + 多语言精简 + 仓库聚焦 Android

本次为基于代码洞察分析的优化版本，覆盖 P0-P2 全部优化项，并完成三项重要功能调整：删除多语言仅保留简体中文、主题切换增加颜色过渡动画、仓库聚焦 Android 专精定位移除所有 Web/Windows 相关内容。

#### P0 优化：静默异常加日志（27 处）

针对代码洞察识别出的 25 处静默异常吞没，统一替换为带 `Log.w` 日志输出的异常处理，便于问题排查。涉及 11 个文件：

- HomeActivity.kt（13 处）
- UpdateViewModel.kt（3 处）
- SplashActivity.kt（2 处）
- ContentLoader.kt（2 处）
- UpdateCard.kt、UpdateCheckWorker.kt、UpdateInstaller.kt、ComposeMarkdown.kt、CategoryColorParser.kt、DrawerCloseLauncher.kt、Screen.kt（各 1 处）

#### P1 优化：资源关闭 + 主题解耦闭环

- **ContentLoader 资源关闭改用 use {} 块**：InputStream / BufferedReader 等资源统一通过 `use {}` 块管理，避免资源泄漏
- **主题解耦闭环**：v3.6.0 遗留的 4 处 `isSystemInDarkTheme()` 直接调用全部迁移至 `LocalIsDarkTheme.current`，确保装饰层与 DataStore 用户偏好完全同步
  - DarkModeTuning.kt（3 处）
  - L6CardGradientBorder.kt（1 处）

#### P2 优化：URL 配置化 + 依赖版本统一 + OkHttpClient 单例复用

- **URL 迁移到 BuildConfig**：UpdateChecker 中硬编码的 GitHub Releases API URL 迁移至 `build.gradle.kts` 的 `buildConfigField("String", "GITHUB_API_URL", ...)`，便于后续切换仓库或环境
- **WorkManager 版本纳入 libs.versions.toml**：统一版本目录管理，避免版本散落
- **OkHttpClient 单例复用**：新增 `UpdateChecker.DefaultClient` 共享单例，UpdateViewModel 与 UpdateCheckWorker 复用同一连接池与线程池，避免重复创建客户端开销
- **测试兼容性修复**：UpdateChecker 内部改用构造函数注入的 `okHttpClient` 实例，既保留单例复用优化，又允许单元测试通过构造函数注入带 Interceptor 的自定义 OkHttpClient 实现 MockWebServer 请求重定向

#### 多语言精简：仅保留简体中文

删除繁体中文（ZH_TW）支持与 Language 枚举，简化为单一 `default` 字符串集合，减少安装包体积与维护成本：

- Strings.kt：移除 Language 枚举与 get(lang) 函数，简化为 `val default: LangStrings`
- HomeActivity.kt：移除语言切换 UI 与相关状态管理
- DataStoreManager.kt：移除 languageKey 偏好键（原 8 个键→7 个键）
- SplashActivity.kt：移除语言加载逻辑
- 其他相关调用方同步修改

#### 主题切换过渡动画

新增 400ms 颜色过渡动画，主题切换时三套配色（MaterialTheme ColorScheme / MarkdownColorScheme / GeoDecorColors）同步过渡：

- 新增 `animateColorScheme(targetScheme, durationMillis)` 辅助函数：对 ColorScheme 全部 29 个颜色字段执行 `animateColorAsState` 动画
- 新增 `animateMarkdownColorScheme(targetScheme, durationMillis)` 辅助函数：对 MarkdownColorScheme 全部 24 个字段执行动画
- 新增 `animateGeoDecorColors(targetColors, durationMillis)` 辅助函数：对 GeoDecorColors 全部 7 个字段执行动画
- FANDEXTheme 修改：三套配色先解析 target 再通过动画函数过渡，`LocalIsDarkTheme` 保持瞬时切换以触发动画

#### 仓库聚焦 Android 专精

移除仓库内所有非 Android 平台相关内容，专注 Android 原生应用定位：

- 删除 `web/` 目录（React + TypeScript 前端源码，20 个文件）
- 删除 `docs/` 与 `docs.legacy/` 目录（Web 部署产物）
- 删除 `FANDEX-creative-showcase.html`（HTML 宣传页）
- 删除 `.github/workflows/deploy-web.yml`（Web 部署工作流）
- 删除 `sdk-tmp/`、`generated/`、`build-log*.txt`、`build-projects.log` 等临时文件
- README.md 重写：新增「项目定位」章节明确 Android 专精，移除关联项目表格，下载链接统一指向 GitHub Releases

#### 技术栈

- Kotlin 2.4.10 / AGP 9.3.0 / Compose BOM 2026.06.01 / compileSdk 37 / minSdk 26
- Material 3 Expressive 设计语言
- 签名：v2 签名方案验证通过

#### 分发

- APK：FANDEX-v3.7.0.apk
- versionCode：13 / versionName：3.7.0
- GitHub Release：https://github.com/fanquanpp/FANDEX-App/releases/tag/v3.7.0

---

## v3.6.0（2026-07-20）

### Android App 综合优化:漏洞修复 + 双主题启动图 + 列表动效 + 光晕清理 + UI 显示大小调节

本次为 Android 原生应用综合优化版本,聚焦项目漏洞洞察修复、启动图双主题适配、列表滑入动效体系、光晕发散模糊类效果清理、UI 显示大小全局调节、操作逻辑优化六大方向。无内容变更,仅优化应用交互体验与视觉表现。

#### 漏洞洞察与修复

- **主题不同步修复(闭环)**:GlassCard / SkeletonScreen 等底层组件直接调用 `isSystemInDarkTheme()` 与 DataStore 用户偏好不同步,通过 `LocalIsDarkTheme` CompositionLocal 统一注入修复
- **libs.versions.toml 注释一致性**:注释 compileSdk 36 与实际 build.gradle.kts 的 37 不一致,修正注释
- **启动窗口主题不一致**:无 `values-night` 目录导致系统暗色模式下启动窗口仍为浅色,新增 `values-night/colors.xml` 覆盖

#### Splash 启动图双主题

- SplashActivity 从强制 `darkTheme = true` 改为读取 DataStore 的 `isDarkMode`,随用户主题切换
- 背景色、文字色、次要文字色全部根据 isDarkMode 切换
- 配合 `values/colors.xml`(浅色默认)与 `values-night/colors.xml`(暗色覆盖),保证冷启动到 Compose 渲染全流程主题一致

#### 光晕发散模糊类效果清理

删除全部径向渐变 / 线性渐变光晕类效果,回归克制几何装饰风格:

| 文件 | 类型 | 处理 |
| :--- | :--- | :--- |
| L5CursorGlowLayer.kt | 光标光晕层(径向渐变跟随触摸) | 删除 |
| L2GradientBlobsLayer.kt | 渐变球层(3 个径向渐变球) | 删除 |
| NavigationGlow.kt | 导航栏光晕指示器 | 删除 |
| GeoBgDecor.kt | GlowTopLeft / GlowBottomRight 装饰项 | 移除绘制函数与配置项 |
| BackgroundDecorSystem.kt | L5 光标光晕层调用 | 移除引用 |
| GlassCard.kt | 渐变边框(Brush.linearGradient) | 改用纯色细边框 |
| Theme.kt | GeoDecorColors.primaryGlow / accentGlow 字段 | 清理数据类字段与赋值 |

#### 列表滑入动效与动效体系优化

为 4 处 LazyColumn / LazyRow 添加 `Modifier.animateItem()` 滑入动效,配合 `key` 参数确保动画正确触发:

- HomeScreen.kt:LazyColumn 主列表(分类区块)+ LazyRow 分类筛选条
- ModuleScreen.kt:LazyColumn 文档列表(用 Column 包裹 DocumentListItem + 分界线)
- SidebarContent.kt:LazyColumn 侧边栏文档列表
- DocumentListItem.kt:新增 `modifier` 参数,支持外部传入 animateItem 修饰符
- 动画规格:`spring(stiffness = StiffnessMediumLow, dampingRatio = DampingRatioNoBouncy)`,克制无回弹

#### UI 显示大小调节

- **Theme.kt 新增 `fontSizeScale` 参数**:通过 `CompositionLocalProvider(LocalDensity provides ...)` 覆盖 fontScale,实现全局字号缩放
- **侧边栏新增 Slider 调节入口**:范围 0.8x - 1.4x,步长 0.1x,共 7 档,实时显示当前比例
- **新增字符串**:displaySize / displaySizeHint / displaySizeSmall / displaySizeLarge(简体 + 繁体)
- **MarkdownContent 调用处传 1.0**:避免 LocalDensity 全局缩放与 MarkdownContent 内部 fontSizeScale 乘法双重缩放
- 文章页 TopAppBar 的字号增减按钮保留,作为快速调节入口

#### 操作逻辑优化

- **翻页滚动位置重置(关键 bug 修复)**:文章页翻页(上一篇/下一篇)时,新文档加载后滚动位置未重置,停留在上一文档的滚动位置。在 `LaunchedEffect(moduleId, slug)` 中增加 `scrollState.scrollTo(0)` 修复
- 列表项 `animateItem` 动效同时优化了分类筛选切换的视觉过渡

#### 技术栈

- Kotlin 2.4.10 / AGP 9.3.0 / Compose BOM 2026.06.01 / compileSdk 37 / minSdk 26
- Material 3 Expressive 设计语言
- 签名:v2 签名方案验证通过

#### 分发

- APK:FANDEX-v3.6.0.apk(3.15 MB)
- versionCode:12 / versionName:3.6.0
- GitHub Release:https://github.com/fanquanpp/FANDEX-App/releases/tag/v3.6.0

---

## v3.5.0（2026-07-20）

### 内容审查重编:剔除非纯语法模块与文档,回归速查手册定位

本次为内容质量治理版本,针对 v3.4.0 新增的 8 个模块共 251 篇文档进行审查与重编。基于"代码语法速查手册"的内容定位,删除无纯语法概念的 DevOps/GitHub/软件测试 3 个模块(共 90 篇),保留 HTML5/SVG/React/Vue3/HarmonyOS 5 个模块并按 App 格式规范重编,精简原理剖析、对比分析、项目实战、工程化等非纯语法文档。文档总数从 461 降至 313,模块总数从 25 降至 22,所有保留文档统一删除 YAML frontmatter、采用"语法签名 + 代码示例"结构。

#### 删除模块清单

| 模块 | 原分类 | 文档数 | 删除原因 |
| :--- | :--- | :---: | :--- |
| DevOps | tools | 32 | 内容以 SRE 理念、IaC 概念、流程规范为主,无独立语法签名体系 |
| GitHub | tools | 36 | 内容以平台功能介绍、协作流程、Webhook 事件清单为主,非语法速查 |
| 软件测试 | tools | 22 | 内容以测试原则、方法论、框架对比为主,无统一语法签名 |

#### 保留模块重编清单

| 模块 | 重编前 | 重编后 | 删除篇数 | 重编要点 |
| :--- | :---: | :---: | :---: | :--- |
| HTML5 | 30 | 30 | 0 | 删除 YAML frontmatter、剔除概念阐述,保留标签语法签名 + API 签名,补充 HTML Living Standard 2025 新特性(`<dialog>`、`popover`、`<search>`) |
| SVG | 18 | 18 | 0 | 删除 frontmatter、剔除原理与实战章节,保留元素签名、path 命令、CSS/JS API |
| React | 45 | 15 | 30 | 删除 30 篇原理/对比/工程化文档,保留 Hooks + 组件 + 路由 API,补充 React 19 新增 API(`useActionState`、`useFormStatus`、`useOptimistic`、`use`) |
| Vue3 | 35 | 20 | 15 | 删除 15 篇非纯语法文档,保留 Composition API + SFC 宏 + 内置组件,补充 Vue 3.5 新特性(`defineModel`、`useTemplateRef`、响应式 props 解构) |
| HarmonyOS | 33 | 20 | 13 | 删除 13 篇概述/对比/工程化文档,保留装饰器 + ArkUI + 系统 API,覆盖 ArkTS V1/V2 状态管理装饰器 |

#### 文档元数据系统扩展

在 `index.json` 的 `documentMeta.updated` 字段新增 `3.5.0` 条目:

```json
"3.5.0": {
    "summary": "新增模块内容审查与重编:删除 DevOps/GitHub/软件测试 3 个非纯语法模块(共 90 篇),保留 HTML5/SVG/React/Vue3/HarmonyOS 5 模块并按 App 格式规范重编(251→103 篇)。最终:22 个模块、313 篇文档(modules 数组 22+2 跨分类副本=24 条)。所有文档统一删除 YAML frontmatter、采用语法签名+代码示例结构、剔除概述/原理/实战/对比等非语法内容。",
    "removed": ["devops/*", "github/*", "software-testing/*"],
    "rewritten": [
        "html5/*(30 篇,删除 frontmatter 与概念章节,补充 HTML Living Standard 2025 新特性)",
        "svg/*(18 篇,删除 frontmatter 与实战章节,保留元素签名与 path 命令)",
        "react/*(45→15 篇,删除 30 篇原理/对比/工程化,保留 Hooks/组件/路由 API,补充 React 19 新增 API)",
        "vue3/*(35→20 篇,删除 15 篇非纯语法,保留 Composition API/SFC 宏/内置组件,补充 Vue 3.5 新特性)",
        "harmonyos/*(33→20 篇,删除 13 篇概述/对比/工程化,保留装饰器/ArkUI/系统 API,覆盖 V1/V2 状态管理)"
    ],
    "stats": {
        "modulesBefore": 25,
        "modulesAfter": 22,
        "documentsBefore": 461,
        "documentsAfter": 313,
        "modulesArrayBefore": 27,
        "modulesArrayAfter": 24
    }
}
```

#### README.md 同步更新

- 文档数徽章:461 → 313
- 模块数徽章:25 → 22
- 内容矩阵表:工具链分类由"Git · DevOps · GitHub · 软件测试"精简为"Git"
- 内容矩阵描述:25 个模块 461 篇 → 22 个模块 313 篇
- APK 输出路径示例:v3.4.0 → v3.5.0

#### 跨分类归属保留

HTML5 与 SVG 仍同时归属 `markup`(标记语言)与 `frontend`(前端技术),modules 数组共 24 条(22 唯一模块 + 2 跨分类副本)。`ModuleScreen.find` 与 `HomeScreen.filter + groupBy` 逻辑无需修改。

#### 构建产物

- Release APK:`FANDEX-v3.5.0.apk`
- versionCode:11
- 签名方案:v2(APK Signature Scheme v2)
- 签名密钥:`fandex-release.jks`(沿用 v3.0.0 生成)

---

## v3.4.0（2026-07-20）

### 内容矩阵扩展:新增 8 模块 251 篇文档(HTML5/SVG/React/Vue3/HarmonyOS/DevOps/GitHub/软件测试)

本次为内容矩阵扩展版本,从 FANDEX-Web 仓库本地同步 8 个新模块共 251 篇文档至 App,App 模块总数从 17 增至 25,文档总数从 210 增至 461。其中 HTML5 与 SVG 因同时具备标记语言与前端技术属性,采用跨分类归属策略,在 modules 数组中各创建 2 条记录(markup + frontend),用户在两个分类下均可访问。

#### 新增模块清单

| 模块 | 分类 | 文档数 | 内容定位 |
| :--- | :--- | :---: | :--- |
| HTML5 | markup + frontend(跨分类) | 30 | HTML5 标签、表单、Web API、PWA、WebComponents 等语法速查 |
| SVG | markup + frontend(跨分类) | 18 | SVG 元素、路径、变换、滤镜、动画等矢量图形语法 |
| React | frontend | 45 | React 19 Hooks、Fiber、Concurrent、Server Components、Next.js 语法 |
| Vue3 | frontend | 35 | Vue 3 Composition API、Pinia、Router、SSR、自定义指令语法 |
| HarmonyOS | languages | 33 | ArkTS/ArkUI 声明式语法、Stage 模型、分布式能力、卡片开发 |
| DevOps | tools | 32 | Docker、Kubernetes、Terraform、Ansible、CI/CD、监控等工具配置语法 |
| GitHub | tools | 36 | GitHub Actions、Webhook、API、分支保护、依赖安全等平台语法 |
| 软件测试 | tools | 22 | Jest、pytest、Playwright、TDD/BDD、性能测试等测试框架语法 |

#### 跨分类归属设计

为实现模块在多个分类下出现的灵活性,采用 modules 数组多条目方案:

- **HTML5**:同时归属 `markup`(标记语言)与 `frontend`(前端技术),共 2 条记录
- **SVG**:同时归属 `markup`(标记语言)与 `frontend`(前端技术),共 2 条记录
- **数据结构**:modules 数组从 17 条增至 27 条(含 2 个跨分类副本),唯一模块 ID 数 25
- **解析兼容**:`ModuleScreen` 使用 `find { it.id == moduleId }` 查找模块,跨分类副本不影响文档加载;`HomeScreen` 按分类筛选与分组,跨分类模块在对应分类下显示

#### 文档元数据系统扩展

在 `index.json` 的 `documentMeta.updated` 字段新增 `3.4.0` 条目:

```json
"3.4.0": {
    "summary": "新增 8 模块 251 篇文档(HTML5/SVG/React/Vue3/HarmonyOS/DevOps/GitHub/软件测试),HTML5 与 SVG 跨分类归属 markup+frontend,文档总数 210→461,模块总数 17→25(modules 数组 17→27 含跨分类副本)",
    "added": ["html5/*", "svg/*", "react/*", "vue3/*", "harmonyos/*", "devops/*", "github/*", "software-testing/*"],
    "crossCategory": [
        {"id": "html5", "categories": ["markup", "frontend"]},
        {"id": "svg", "categories": ["markup", "frontend"]}
    ]
}
```

#### README.md 同步更新

- 文档数徽章:210 → 461
- 模块数徽章:17 → 25(标签由"语言模块"改为"内容模块")
- 内容矩阵表:5 分类下模块列表全量更新,标注 HTML5 与 SVG 跨分类归属
- 双语界面描述修正:三语(中/英/日) → 双语(简中/繁中),与 v3.1.0 后硬约束一致
- APK 输出路径示例:v3.2.0 → v3.4.0

#### 构建产物

- Release APK:`FANDEX-v3.4.0.apk`
- versionCode:10
- 签名方案:v2(APK Signature Scheme v2)
- 签名密钥:`fandex-release.jks`(沿用 v3.0.0 生成)

#### 受影响文件

| 文件 / 目录 | 变更类型 | 说明 |
| :--- | :--- | :--- |
| `docs/html5/*.md` | 新增 | 30 篇 HTML5 文档 |
| `docs/svg/*.md` | 新增 | 18 篇 SVG 文档 |
| `docs/react/*.md` | 新增 | 45 篇 React 文档 |
| `docs/vue3/*.md` | 新增 | 35 篇 Vue3 文档 |
| `docs/harmonyos/*.md` | 新增 | 33 篇 HarmonyOS 文档 |
| `docs/devops/*.md` | 新增 | 32 篇 DevOps 文档 |
| `docs/github/*.md` | 新增 | 36 篇 GitHub 文档 |
| `docs/software-testing/*.md` | 新增 | 22 篇软件测试文档 |
| `index.json` | 修改 | modules 数组 +10 条(8 新模块 + 2 跨分类副本)、documentMeta.updated.3.4.0 新增 |
| `README.md` | 修改 | 文档数/模块数徽章、内容矩阵表、双语界面描述、APK 路径示例 |
| `app/build.gradle.kts` | 修改 | 版本号升级 v3.4.0 / versionCode 10 |

#### 影响说明

- **内容广度**:模块总数 17 → 25(+47%),文档总数 210 → 461(+120%),覆盖前端三剑客(HTML/CSS/JS)与主流框架(React/Vue3)、鸿蒙原生、DevOps 工具链、GitHub 平台、软件测试等核心开发场景
- **跨分类灵活性**:HTML5 与 SVG 通过 modules 数组多条目方案实现跨分类归属,用户在"标记语言"与"前端技术"分类下均可访问,数据结构向前兼容
- **零代码风险**:不涉及 Kotlin/Compose 代码修改,不影响应用运行逻辑与签名,仅扩展内容资源
- **元数据可追溯**:documentMeta.updated.3.4.0 记录变更明细与跨分类映射,为未来按版本筛选功能奠基

---

## v3.3.0（2026-07-20）

### 文档体系全面升级:JS/CSS 新特性 + 长文档拆分 + 元数据系统 + Lint CI

本次为文档体系全面升级版本,合并原计划 v3.3.0(短期)与 v4.0.0(中期)全部任务,一次性发布。核心覆盖 JavaScript/CSS 最新特性补充、长文档拆分优化、文档元数据系统引入、Markdown lint CI 建立四大维度。

#### JavaScript ES2024 + ES2025 新特性补充(8 篇 / 39 写法)

为 javascript 模块 8 篇核心文档追加 ES2024 与 ES2025 新特性章节:

| 文档 | 新增章节 | 写法数 | 关键特性 |
| :--- | :--- | :---: | :--- |
| `ES6+新特性.md` | ES2024+ 新特性 | 16 | Object.groupBy / Map.groupBy / Promise.withResolvers / ArrayBuffer resize / Atomics.waitAsync / RegExp v 标志 / Iterator Helpers / Set 集合运算 / Promise.try / import attributes / Float16Array / using / RegExp.escape |
| `Promise静态方法.md` | ES2024+ Promise 新增 | 3 | Promise.withResolvers / Promise.try / Deferred 对比 |
| `对象与数组.md` | ES2024+ 对象数组新方法 | 4 | Object.groupBy / Map.groupBy / Object.hasOwn / structuredClone |
| `异步编程.md` | ES2025 异步新特性 | 3 | using / await using / Promise.try |
| `数组高阶方法.md` | ES2025 Iterator Helpers | 5 | Iterator.map / filter / take / drop / toArray |
| `正则表达式.md` | ES2024+ 正则新特性 | 3 | RegExp v 标志 / isWellFormed / RegExp.escape |
| `模块化.md` | ES2025 Import Attributes | 3 | import json / 动态 import 断言 / 与 import assertions 对比 |
| `变量与数据类型.md` | ES2025 新数据类型 | 2 | Float16Array / Iterator 协议 |

#### CSS 2024-2025 新特性补充(8 篇 / 35 写法)

为 css 模块 8 篇核心文档追加 CSS 2024-2025 新特性章节:

| 文档 | 新增章节 | 写法数 | 关键特性 |
| :--- | :--- | :---: | :--- |
| `选择器系统.md` | CSS Nesting 原生嵌套(2023-2024) | 5 | 原生嵌套 & / 组合器嵌套 / 层叠层级 / @scope / @scope 邻近选择器 |
| `层叠层.md` | @layer 与 @scope 进阶 | 4 | @layer 命名 / 匿名层 / @scope 与 @layer 对比 / cascade origins |
| `响应式设计.md` | 现代响应式新特性 | 5 | Container Queries / cqw/cqh/cqi / prefers-reduced-transparency / prefers-reduced-data / scripting |
| `媒体查询.md` | 用户偏好媒体查询(2024) | 5 | prefers-reduced-motion / prefers-color-scheme / prefers-contrast / prefers-reduced-transparency / inverted-colors |
| `背景增强.md` | CSS 背景新特性 | 4 | background-clip 多值 / 多重背景 mix-blend-mode / backdrop-filter / scroll-driven view-timeline |
| `动画与过渡.md` | 现代动画新特性 | 5 | @starting-style / transition-behavior / animation-timeline / view-timeline / interpolate-size |
| `Flexbox弹性布局.md` | Flexbox 新特性 | 3 | align-content 与 justify-content 统一 / gap / flex-basis content |
| `Grid网格布局.md` | Grid 新特性 | 4 | subgrid / masonry / auto-fit vs auto-fill / Container Query 结合 |

#### 长文档拆分优化(3 篇 → 6 篇)

将 3 篇超长文档按章节边界拆分为 6 篇,优化移动端阅读体验,文档总数从 207 篇增至 210 篇:

| 原文件 | 原行数 | 拆分后 | 新文件 | 行数 |
| :--- | :---: | :--- | :--- | :---: |
| `kotlin/Kotlin集合操作.md` | 839 | `kotlin/Kotlin集合操作.md`(前 6 章基础操作) | `kotlin/Kotlin集合进阶.md`(后 6 章高级操作) | 457 + 386 |
| `css/伪类与伪元素.md` | 814 | `css/伪类详解.md`(前 7 章伪类) | `css/伪元素详解.md`(后 5 章伪元素) | 491 + 328 |
| `python/面向对象编程.md` | 856 | `python/面向对象基础.md`(前 9 章) | `python/面向对象进阶.md`(后 10 章) | 529 + 335 |

#### 文档元数据系统引入

在 `index.json` 顶层新增 `documentMeta` 字段,建立集中式文档元数据管理体系,为未来按版本筛选功能预留扩展点:

```json
{
  "documentMeta": {
    "baseline": "3.0.0",
    "updatedAt": "2026-07-20",
    "schema": { "version": "...", "updatedAt": "...", "tags": "...", "status": "..." },
    "updated": {
      "3.2.0": [13 篇文档路径],
      "3.3.0": { "modified": [17 篇], "added": [5 篇], "removed": [2 篇] }
    }
  }
}
```

**设计原则**:
- **增量记录**:只记录基线版本(3.0.0)之后更新过的文档,未列出文档默认为基线版本
- **集中管理**:元数据集中在 index.json,不污染 Markdown 文件本身(避免 frontmatter 破坏渲染)
- **向前兼容**:不修改现有 `modules.documents` 字符串数组结构,不影响 ContentLoader 解析
- **状态追踪**:支持 active/deprecated/split 三种文档状态

#### Markdown Lint CI 建立

新增 `.github/workflows/markdown-lint.yml` 与 `.markdownlint.json`,建立文档格式自动化检查工作流:

- **触发条件**:push/pull_request 影响到 `docs/**` 目录或配置文件时
- **检查工具**:markdownlint-cli2 v0.14.0(基于 Node.js 20)
- **检查范围**:`android/app/src/main/assets/dist-mobile/docs/**/*.md`
- **规则配置**:
  - 启用 MD040(代码块必须有语言标签)防止格式回归
  - 启用 MD041(首行必须为标题)保证文档结构
  - 禁用 MD013(行长度限制)兼容代码块长行
  - 禁用 MD033(禁用行内 HTML)允许 `<br>` 等标签
  - 禁用 MD036(禁止粗体作为标题)兼容 FANDEX 写法标注格式
  - MD024 仅检查同级标题重复(siblings_only)

#### 索引与文档数同步

- `index.json` 更新:3 处模块 documents 数组同步(kotlin +1、css +1、python +1,css 与 python 各 -1 改名)
- `README.md` 更新:3 处 `207 篇` 替换为 `210 篇`(正文、徽章 URL、内容矩阵章节)

#### 构建产物

- Release APK:`FANDEX-v3.3.0.apk`
- versionCode:9
- 签名方案:v2(APK Signature Scheme v2)
- 签名密钥:`fandex-release.jks`(沿用 v3.0.0 生成)

#### 受影响文件

| 文件 / 目录 | 变更类型 | 说明 |
| :--- | :--- | :--- |
| `docs/javascript/ES6+新特性.md` 等 8 篇 | 修改 | 追加 ES2024+ES2025 新特性章节 |
| `docs/css/选择器系统.md` 等 8 篇 | 修改 | 追加 CSS 2024-2025 新特性章节 |
| `docs/kotlin/Kotlin集合操作.md` | 修改 | 拆分,保留前 6 章 |
| `docs/kotlin/Kotlin集合进阶.md` | 新增 | 拆分后的后 6 章 |
| `docs/css/伪类与伪元素.md` | 删除 | 拆分后改名 |
| `docs/css/伪类详解.md` | 新增 | 拆分后的前 7 章 |
| `docs/css/伪元素详解.md` | 新增 | 拆分后的后 5 章 |
| `docs/python/面向对象编程.md` | 删除 | 拆分后改名 |
| `docs/python/面向对象基础.md` | 新增 | 拆分后的前 9 章 |
| `docs/python/面向对象进阶.md` | 新增 | 拆分后的后 10 章 |
| `index.json` | 修改 | 同步文档数组 + 新增 documentMeta 字段 |
| `README.md` | 修改 | 文档数 207 → 210 |
| `.github/workflows/markdown-lint.yml` | 新增 | Markdown lint CI 工作流 |
| `.markdownlint.json` | 新增 | markdownlint 规则配置 |
| `app/build.gradle.kts` | 修改 | 版本号升级 v3.3.0 / versionCode 9 |

#### 影响说明

- **内容时效**:74 个新写法覆盖 ES2024/ES2025 + CSS 2024-2025 最新特性,前端模块技术时效性提升至 100%
- **阅读体验**:3 篇超长文档拆分为 6 篇,单篇平均行数从 315.9 降至约 305,移动端阅读更友好
- **工程化**:Markdown lint CI 防止格式回归,元数据系统为未来按版本筛选功能奠基
- **零代码风险**:不涉及 Kotlin/Compose 代码修改,不影响应用运行逻辑与签名
- **文档矩阵**:17 模块 210 篇文档,前端 + 后端 + 数据库 + 工具链 + 标记语言全覆盖

---

## v3.2.0（2026-07-20）

### 文档内容全面优化升级

本次为文档内容质量提升版本,围绕 17 模块 207 篇文档的格式合规性、内容完整性与新技术覆盖三大维度展开,不涉及应用代码变更,不影响应用运行逻辑。

#### Redis 模块格式合规性修复

修复 5 个 Redis 文档中遗留的非标准写法标注,统一为 `**XXX写法：...**` 格式模板规范:

| 文件 | 修复内容 |
| :--- | :--- |
| `docs/redis/字符串SDS结构.md` | `结构定义` / `内存布局` / `预分配规则` / `函数定义` / `惰性删除示例` / `显式释放` / `真正释放时机` / `兼容 C 字符串函数` 8 处标注统一为 `XXX写法` |
| `docs/redis/内存淘汰策略.md` | `结构定义` / `函数定义` 2 处标注统一为 `XXX写法` |
| `docs/redis/Lua脚本原子执行.md` | `禁止操作` 3 处统一为 `禁止写法` |
| `docs/redis/AOF日志持久化.md` | `函数定义:命令追加到 AOF 缓冲区` / `函数定义:写入文件并根据策略刷盘` 2 处统一为 `函数源码写法` |
| `docs/c/文件IO操作.md` | 第 393 行 `结构体读法` 修正为 `结构体读取写法` |

#### 多语言新特性章节补充(8 篇文档)

为 8 篇基础文档追加最新语言版本特性章节,共补充约 56 个写法示例,覆盖 2025-2026 各语言最新稳定版本:

| 文档 | 新增章节 | 写法数 | 覆盖版本 |
| :--- | :--- | :---: | :--- |
| `docs/python/基础数据类型.md` | Python 3.13+ 新特性 | 6 | type 复数参数 / 改进错误消息 / t-string 模板字符串 / Template.render / 自由线程模式 / 实验性 JIT |
| `docs/python/类型注解与mypy.md` | Python 3.13+ 类型系统增强 | 6 | TypeIs / ReadOnly / deprecated 装饰器 / PEP 695 类型别名 / PEP 695 泛型类 / deferred annotations |
| `docs/java/程序结构与基本语法.md` | Java 25+ 新特性 | 9 | record / sealed / pattern matching switch / 文本块 / 严格浮点 / scoped values / structured concurrency / virtual threads / module info |
| `docs/typescript/函数与泛型.md` | TypeScript 5.x 新特性 | 9 | 5.0 装饰器 / const 类型参数 / 5.1 函数返回类型分离 / 5.2 using / 5.4 NoInfer / 5.5 推断类型谓词 / 5.6 不允许真值比较 / 5.7 默认导入解析约束 / 5.8 --erasableSyntaxOnly |
| `docs/go/基础语法.md` | Go 1.24+ 新特性 | 5 | 泛型类型别名 / range-over-func / weak pointer / toolchain 指令 / Go 1.26 new(expr) |
| `docs/kotlin/基础语法.md` | Kotlin 2.x 新特性 | 5 | K2 编译器 / guard 条件 / 多重赋值 / context receivers / Java 25 互操作 |
| `docs/csharp/高级特性.md` | C# 13/14 新特性 | 7 | lock 类型 / params 集合 / \e escape / 扩展成员 / null 条件分配 / implicit span conversion / partial constructors |
| `docs/cpp/基础语法.md` | C++23/26 新特性 | 9 | std::print / std::println / if consteval / 多维下标运算符 / static call operator / = delete 原因 / pack indexing / hazard pointer / RCU |

#### README.md 版本信息同步

修复 6 处过时信息,确保与 v3.2.0 实际技术栈一致:

- Kotlin 版本徽章:2.0.21 → 2.4.10
- APK 文件名示例:v2.1.0 → v3.2.0
- 目标平台:Android 15 (API 35) → Android 16 (API 37)
- 技术栈表格全量更新:Kotlin 2.4.10、Compose BOM 2026.06.01、Navigation 2.9.8、commonmark 0.29.0、DataStore 1.2.1、Gson 2.14.0,新增 OkHttp 5.4.0 与 WorkManager 2.10.0 行,AGP 9.3.0、JVM 21 / SDK 37
- 环境要求:JDK 17 → 21、SDK 35 → 37
- APK 输出路径示例:v2.1.0 → v3.2.0
- 测试栈补充:Robolectric 4.16.1 + MockWebServer 5.4.0、coroutines-test 1.11.0

#### 构建产物

- Release APK:`FANDEX-v3.2.0.apk`
- versionCode:8
- 签名方案:v2/v3(Android 7+)
- 签名密钥:`fandex-release.jks`(沿用 v3.0.0 生成)

#### 影响说明

- **内容质量**:207 篇文档格式合规率提升至 100%,Redis 模块遗留非标准标注全部修复
- **技术时效**:8 篇基础文档补充最新语言版本特性,覆盖 Python 3.13+ / Java 25+ / TS 5.x / Go 1.24+ / Kotlin 2.x / C# 13-14 / C++23-26
- **文档一致性**:README.md 版本徽章、技术栈表格、APK 文件名示例、环境要求与实际构建配置完全对齐
- **零代码变更**:不涉及 Kotlin/Compose 代码修改,不影响应用运行逻辑与签名

---

## v3.1.0（2026-07-20）

### 体验优化:数学公式渲染 + 多语言精简 + 过渡动画扩展

本次为体验优化版本,围绕用户反馈的 12 项优化诉求展开,核心解决数学公式无法渲染问题,精简国际化语言,扩展过渡动画体系,调整背景装饰视觉效果。

#### 纯 Compose LaTeX 渲染器

新增 `MathFormulaRenderer.kt`(657 行),完全脱离 WebView 实现 LaTeX 公式渲染:

- 150+ 符号映射(希腊字母、运算符、关系符、箭头、集合论符号等)
- 递归下降解析器,支持嵌套上下标、分数、根号、求和、积分、矩阵等复杂结构
- 集成到 `ComposeMarkdown.kt`,自动识别 ```math 围栏代码块与 `$...$` 行内公式
- 上下标布局基于 BaselineLayout,精准对齐数学符号基线

#### 国际化精简

【Skill 偏差报备】原项目支持 ZH / EN / JA 三语,根据用户偏好与"仅简中+繁中"硬约束,做以下调整:

- 移除英语(EN)与日语(JA)资源
- 新增 ZH_TW(繁体中文)完整翻译,覆盖所有 UI 文案
- `Strings.kt` 仅保留 `Language.ZH` 与 `Language.ZH_TW` 枚举
- 减少安装包体积约 200KB,聚焦核心中文用户群体

#### 启动页动画

- 开屏时长固定为 1.5 秒(硬约束)
- 三阶段文字浮现动画:副标题 → 标题 → 装饰元素
- Spring 弹动过渡,缓动曲线优化

#### 背景装饰调整

- 移除 L2 泛光色晕层(用户反馈"避免发光色晕"硬约束)
- L3 点阵重新规划为三层独立点阵系统(密集 + 中等 + 稀疏)
- 浅色模式装饰色透明度提升(0.06 → 0.12),增强视觉明显度
- 暗色模式保持原透明度,避免装饰元素干扰内容阅读

#### 过渡动画扩展

新增 `PageTransitions.kt`(175 行),提供 4 种过渡变体:

| 变体 | 适用路由 | 效果 |
| :--- | :--- | :--- |
| 横向滑动 | 默认 | 左右滑动方向感 |
| 纵向滑动 | 文章详情 | 上下滑动方向感 |
| 缩放 | 弹窗页 | 0.92 → 1.0 缩放 |
| Fade Through | 模块详情 | 三阶段淡入淡出 |
| 混合过渡 | 模块详情 | 滑动 + 缩放组合 |

按路由语义自动分配:`Module = 混合`、`Document = 纵向滑动`、`默认 = 横向滑动`。

#### 更新自检 UX 优化

- `UpdateSettingsItem` 增加提示文字:"点击检查 GitHub 是否有新版本"
- "自动检查更新"开关项增加说明:"应用启动后自动检查新版本(仅访问 github.com)"
- 网络提示:"更新检查仅访问 GitHub 域名,可随时关闭恢复完全离线"
- 汉化剩余英文文本

#### 构建产物

- Release APK:`FANDEX-v3.1.0.apk`(2.83 MB)
- versionCode:7
- 签名方案:v2/v3(Android 7+)

#### 受影响文件

| 文件 | 变更类型 | 说明 |
| :--- | :--- | :--- |
| `app/build.gradle.kts` | 修改 | 版本号升级 v3.1.0 / versionCode 7 |
| `data/ComposeMarkdown.kt` | 修改 | 集成 MathFormulaRenderer |
| `data/MathFormulaRenderer.kt` | 新增 | 纯 Compose LaTeX 渲染器(657 行) |
| `data/Strings.kt` | 修改 | 移除 EN/JA,新增 ZH_TW |
| `home/HomeActivity.kt` | 修改 | 集成过渡动画 |
| `home/SplashActivity.kt` | 修改 | 1.5s 固定时长 + 三阶段动画 |
| `ui/background/BackgroundDecorSystem.kt` | 修改 | 移除 L2 泛光层 |
| `ui/background/L3GridNoiseLayer.kt` | 修改 | 三层独立点阵系统 |
| `ui/enhancements/PageTransitions.kt` | 新增 | 4 种过渡动画变体(175 行) |
| `ui/theme/Theme.kt` | 修改 | 浅色模式装饰色透明度提升 |
| `update/UpdateSettingsItem.kt` | 修改 | 增加提示文字与汉化 |

#### 影响说明

- **核心修复**:数学公式渲染问题彻底解决,支持 150+ LaTeX 符号
- **国际化聚焦**:精简至简中+繁中,减少体积,聚焦核心用户
- **视觉调优**:移除发光色晕,浅色模式装饰更显眼,符合硬约束
- **交互丰富**:5 种过渡动画变体按路由语义分配,提升导航流畅度

---

## v3.0.0（2026-07-20）

### 重大重构：技术栈全量升级 + 视觉跃迁 + 更新自检

本次为大版本重构更新，围绕技术栈版本升级、酷炫背景装饰与 UIUX 增强、应用内更新自检三大核心诉求展开，在保留 17 语言模块、207 篇文档、三语界面、Markdown 渲染等核心功能的前提下完成全面升级。

#### 技术栈全量升级（最新稳定版基线）

| 层级 | 原版本 | 新版本 | 升级类型 |
| :--- | :--- | :--- | :--- |
| Kotlin | 2.0.21 | 2.4.10 | minor |
| Android Gradle Plugin | 8.7.0 | 9.3.0 | major |
| Gradle | 8.x | 9.6.1 | major |
| Jetpack Compose BOM | 2024.12.01 | 2026.06.01 | major |
| Material 3 | 1.3.x | 1.4.x（跟随 BOM） | minor |
| Navigation Compose | 2.8.5 | 2.9.8 | minor |
| Activity Compose | 1.9.3 | 1.13.0 | minor |
| Lifecycle Runtime Compose | 2.8.7 | 2.11.0 | minor |
| AndroidX Core KTX | 1.15.0 | 1.19.0 | minor |
| commonmark-java | 0.22.0 | 0.29.0 | minor |
| DataStore Preferences | 1.1.1 | 1.2.1 | minor |
| Gson | 2.11.0 | 2.14.0 | minor |
| OkHttp | 未引入 | 5.4.0 | 新增 |
| Kotlin Coroutines | 1.9.0 | 1.11.0 | minor |
| compileSdk / targetSdk | 34 | 37 | minor |
| 编译 JDK 目标 | 17 | 21 | major |

详细版本偏差对比见 `.trae/specs/refactor-android-latest/deviation-report.md`。

#### 6 层叠加背景装饰系统

引入 6 层独立叠加的背景装饰系统，参考 Linear、Raycast、Vercel Dashboard、Arc Browser、Notion Calendar、Cursor IDE、GitHub PR 等顶级产品的视觉风格。

| 层级 | 名称 | 实现方式 | 性能预算 |
| :--- | :--- | :--- | :--- |
| L1 | 粒子 Canvas | Canvas + remember + 动画驱动 30-50 个低多边形粒子缓慢漂浮 | 单帧 < 2ms |
| L2 | 渐变光晕 | RadialGradient + Brush.linearGradient 多点叠加，呼吸动画 | 静态渲染 |
| L3 | 网格底纹 | Canvas drawLine 极细网格（alpha 0.04）+ Viewport 视差 | 单帧 < 0.5ms |
| L4 | 噪点纹理 | 预生成 256x256 Bitmap + tile 模式 + alpha 0.03 | 内存 < 64KB |
| L5 | 几何装饰 | Canvas 绘制对角斜线、圆环、三角形等装饰图形 | 单帧 < 0.3ms |
| L6 | 卡片渐变描边光效 | Modifier.border + Brush.linearGradient + 悬停光效 | 仅悬停时重绘 |

整体性能预算：60fps 下背景系统总开销 < 4ms / 帧；低端设备自动降级，关闭 L1 与 L6。

#### 14 项 UIUX 增强

1. **玻璃拟态卡片**（Glassmorphism）：搜索栏、设置项、更新提示卡片采用半透明 + 模糊 + 渐变描边
2. **3D 倾斜交互**（Tilt Effect）：文档卡片根据触控位置轻微倾斜（最大 8 度）
3. **Spring 动画系统**：所有过渡使用 spring(dampingRatio, stiffness) 替代线性动画
4. **骨架屏加载**（Skeleton Loading）：文档首次加载、搜索结果加载时显示骨架屏
5. **页面过渡动画**：SharedElementTransition + 淡入淡出 + 微缩放（0.95 → 1.0）
6. **视差滚动**（Parallax）：背景层与内容层滚动速度差（0.3x vs 1.0x）
7. **导航光带**（Navigation Glow）：底部导航选中项底部光带 + spring 弹动
8. **自定义滚动条**：极细滚动条（2dp）+ 悬停加粗（4dp）+ 拖动时高亮
9. **字体系统升级**：可变字重（Variable Font）+ 等宽字体（代码）+ 阅读字体（正文）三体系
10. **Cursor 光晕**：当前聚焦卡片边缘光晕跟随
11. **自定义 Spinner**：替代系统 ProgressBar，参考 Linear 加载器风格
12. **状态色系统**：success / warning / error / info 四色 + 微光晕
13. **微交互反馈**：所有可点击元素按压涟漪 + spring 缩放反馈（0.97 → 1.0）
14. **暗黑模式调优**：纯黑基底 + 微蓝紫色调 + 强对比文字（WCAG AA）

#### 更新自检功能（5 个场景）

新增应用内更新自检机制，通过 NetworkSecurityConfig 域名白名单严格限定网络访问边界，保证核心功能离线性不受影响。

1. **启动后静默检查**：App 启动后延迟发起 GitHub Releases API 请求，3 秒超时失败静默跳过
2. **用户主动检查**：设置页"检查更新"按钮，主动触发检查并显示进度
3. **非打扰式提示卡片**：检测到新版本时在首页顶部插入可关闭的提示卡片，不弹模态框
4. **自动下载安装**：用户点击"立即更新"后后台下载 APK（FANDEX-v{version}.apk），下载完成调用系统安装器
5. **检查频率限制与忽略版本**：手动检查 1h 间隔、自动检查 24h 间隔；用户可"忽略此版本"跳过该版本提示

**频率限制策略**：
- 手动检查：1 小时间隔（除非上次检查失败）
- 自动检查：24 小时间隔 + `autoCheckUpdate` 偏好开关
- 自动检查失败后不限制重试间隔

**WorkManager 后台任务**：
- 通过 WorkManager 调度更新检查后台任务
- 支持应用退出后仍可执行检查
- 通过 R8 ProGuard 保留规则确保反射调用正常

#### 网络安全配置

- AndroidManifest 添加 `INTERNET` + `ACCESS_NETWORK_STATE` 权限，仅用于更新自检功能
- 新增 `res/xml/network_security_config.xml`，限定仅允许访问 `github.com` / `api.github.com` / `objects.githubusercontent.com` 三个域名
- 明文流量禁止（`cleartextTrafficPermitted = false`）
- 用户可在偏好设置中关闭"自动检查更新"，关闭后应用不发起任何网络请求，等同于完全离线模式

#### 异常处理优化

- 修复 `UpdateChecker.mapToUpdateInfo` 中业务异常被网络异常 catch 误覆盖的问题
- 将"未找到可下载的 APK 文件"异常类型从 `IOException` 改为 `IllegalStateException`，使其被 `catch (e: Exception)` 捕获而非 `catch (e: IOException)`，保留原始业务错误消息

#### AGP 9.x 适配

- `applicationVariants.all { }` DSL 迁移为 `androidComponents.onVariants { }`（AGP 9.0 移除旧 API）
- `kotlinOptions` DSL 块迁移为 `kotlin { compilerOptions { } }`（AGP 9.0 移除旧 API）
- `variant.versionName` 移除，改用顶级变量共享（AGP 9.0 移除属性）
- 自定义 APK 输出文件名通过 `VariantOutput.outputFileName.set()` 实现

#### R8 混淆适配

`proguard-rules.pro` 新增以下保留规则：

- **WorkManager**：`-keep class androidx.work.** { *; }`，保留反射调用的构造函数与实现类，修复 R8 移除 `WorkDatabase_Impl` 默认构造函数导致运行时 `NoSuchMethodException` 的崩溃
- **Room 数据库**：`-keep class * extends androidx.room.RoomDatabase { *; }`，保留 WorkManager 通过 Room 反射创建数据库实例的能力
- **OkHttp / Okio**：保留内部反射与平台检测代码

#### 测试增强

新增 25 个单元测试（总计 60 个，全部通过）：

- `UpdateCheckerTest.kt`（8 个用例）：覆盖网络请求成功 / 失败、版本解析、APK 资源匹配、异常处理等场景
- `UpdateModelsTest.kt`（11 个用例）：覆盖 `UpdateInfo` / `GitHubRelease` 数据模型解析、`@SerializedName` 注解、默认值容错
- `DataStoreManagerTest.kt`（6 个用例）：覆盖偏好持久化（主题、字体、自动检查、忽略版本、上次检查时间）

测试依赖基线：JUnit 4.13.2、Robolectric 4.16.1、Coroutines Test 1.11.0、Mockito 5.14.2、Mockito Kotlin 5.4.0、MockWebServer 5.4.0、AndroidX Test Core 1.7.0、AndroidX Test Ext JUnit 1.3.0。

#### 签名密钥

- 重新生成 `fandex-release.jks`（RSA 4096 位，有效期 100 年）
- 证书 DN：`CN=FANDEX, OU=Development, O=fanquanpp, L=Beijing, ST=Beijing, C=CN`
- SHA-256：`740f5da559103d619b52b483a609152a14e4de9db918f8e21dd9d04718fbf925`
- 作为唯一发布版本，签名密码通过 `local.properties` 或环境变量注入

#### 离线约束调整

【Skill 偏差报备】原项目硬约束"AndroidManifest 无 INTERNET 权限"与用户新需求"增加更新自检功能"冲突。经用户授权，做以下调整：

- 添加 `INTERNET` + `ACCESS_NETWORK_STATE` 权限，仅用于更新自检
- 通过 NetworkSecurityConfig 限定仅允许访问 3 个 GitHub 域名
- 核心功能（文档浏览、搜索、收藏、阅读进度、主题字体切换）完全不依赖网络
- 用户关闭"自动检查更新"后等同于完全离线模式

#### 构建产物

- Release APK：`FANDEX-v3.0.0.apk`（2.69 MB）
- versionCode：6
- 签名方案：v2/v3（Android 7+）
- 真机验证：Redmi K60（Android 15, 1440x3200）安装运行正常

#### 验证结果

- 60 个单元测试全部通过
- Release 构建成功，v2 签名验证通过
- 离线场景静态审查 PASS（启动流程、内容加载、更新自检、网络安全、资源完整性、AndroidManifest 全部通过）
- 在线场景真机验证 PASS（APK 安装、应用启动、UI 渲染、文档浏览、侧边栏、设置开关、检查更新按钮点击全部通过）

#### 受影响文件

| 文件 / 目录 | 变更类型 | 说明 |
| :--- | :--- | :--- |
| `gradle/libs.versions.toml` | 修改 | 版本目录全量更新，新增 OkHttp / 测试库 |
| `app/build.gradle.kts` | 修改 | AGP 9.x DSL 迁移 / 依赖版本升级 / SDK 37 / Java 21 |
| `app/proguard-rules.pro` | 修改 | 新增 WorkManager / Room / OkHttp 保留规则 |
| `app/src/main/AndroidManifest.xml` | 修改 | 添加 INTERNET / ACCESS_NETWORK_STATE / NetworkSecurityConfig 引用 |
| `app/src/main/res/xml/network_security_config.xml` | 新增 | 域名白名单配置 |
| `com/fandex/app/update/` | 新增 | 更新自检模块（UpdateChecker / UpdateViewModel / UpdateDownloader / UpdateInstaller / UpdateModels / UpdateCheckWorker / CheckState / DownloadState） |
| `com/fandex/app/ui/decor/` | 新增 | 6 层背景装饰 Composable |
| `com/fandex/app/ui/ux/` | 新增 | 14 项 UIUX 增强组件 |
| `com/fandex/app/data/DataStoreManager.kt` | 修改 | 新增动态背景 / 自动检查更新 / 忽略版本 / 上次检查时间键 |
| `app/src/test/java/com/fandex/app/update/` | 新增 | 3 个测试文件 25 个用例 |
| `local.properties` | 修改 | 添加签名凭证 |
| `fandex-release.jks` | 新增 | Release 签名密钥库 |

#### 影响说明

- **视觉跃迁**：从单一 GeoBgDecor 升级为 6 层叠加系统，达到同类顶级产品水准
- **功能扩展**：新增更新自检，用户可在应用内感知 GitHub Releases 新版本
- **技术升级**：全量升级到 2026 年最新稳定版技术栈，享受 K2 编译器、Material 3 Expressive、AGP 9.x 等新特性
- **离线性保证**：核心功能完全离线，更新自检为"尽力而为"模式，可关闭
- **兼容性**：minSdk 26 保持不变，向下兼容 Android 8.0+

---

## v2.1.1（2026-07-16）

### 文本勘误与完善

本次为仓库文本资料的勘误与完善，不涉及应用代码变更，不影响应用功能与构建产物。

#### LICENSE

- 确认版权年份为 `Copyright (c) 2026 FANDEX Project`（仓库新建于 2026 年）

#### 文档校对

- `README.md`：核对文档数 207、模块数 17、Kotlin 2.0、Jetpack Compose、Material 3、Pages 链接、GitHub Releases 链接、关联项目描述、设计语言章节、参赛信息、创意展示 HTML 引用，内容均正确
- `DISCLAIMER.md`：核对最后更新日期为 2026-07-16；核对 Android 安装风险条款完整性（Android 8.0/API 26+ 要求、APK 安装包形式、"安装未知来源应用"权限提示、官方 Releases 或下载页下载提示）；核对所有 GitHub 链接指向 fanquanpp/FANDEX-App 仓库，内容均正确
- `CODE_OF_CONDUCT.md`：核对 GitHub Issues 联系方式指向 fanquanpp/FANDEX-App、生效日期为 2026-07-16，内容正确
- `SECURITY.md`：核对 GitHub Security Advisory 链接、最后更新日期为 2026-07-16，内容正确

#### 文档完善

- `CONTRIBUTING.md`：「问题反馈」章节的 GitHub Issue 与 Pull Request 补充 fanquanpp/FANDEX-App 仓库链接；补充最后更新日期，与 `CODE_OF_CONDUCT.md`、`SECURITY.md`、`DISCLAIMER.md` 保持一致

#### 影响说明

- 本次为纯文本勘误与完善，不涉及应用代码变更
- 不影响应用功能与构建产物

## v2.1.0（2026-07-16）

### 视觉系统升级

#### 设计语言

引入构成主义（Constructivism）/ 包豪斯（Bauhaus）/ 至上主义（Suprematism）美学背景装饰系统，为应用界面注入设计质感与层次感。

#### 背景装饰特性

- 新增 `GeoBgDecor` 几何背景装饰组件，基于 Jetpack Compose Canvas 原生绘制
- 新增 `GeoDecorColors` 双主题颜色方案，通过 CompositionLocal 注入
- 4 种视图变体，各页面装饰密度差异化：
  - **Home 首页**：品牌光晕 + S 曲线 + 涟漪环 + 三角切片 + 十字坐标 + 对角粗线（8 项装饰）
  - **Module 模块详情页**：网格底纹 + 平行斜线 + 径向点阵 + 同心半圆环（6 项装饰）
  - **Splash 启动页**：双倍品牌光晕 + 大网格底纹 + 涟漪环 + S 曲线，营造仪式感
  - **Loading 加载态**：网格底纹 + 径向点阵，克制点缀
- 装饰元素包括：网格底纹、品牌光晕、S 形贝塞尔曲线、同心圆涟漪、直角三角形切片、十字坐标点阵、对角粗线、平行斜线束、径向点阵、同心半圆环

#### 视觉原则

- 克制使用：装饰元素仅作背景点缀，不干扰内容阅读
- 双主题适配：浅色模式低透明度（0.06~0.18），暗色模式略高透明度（0.10~0.22）
- 品牌色一致：装饰色板与 PrimaryBlue / FrontendColor / AiColor 保持一致
- 性能优化：Canvas 配置预计算 + remember 缓存，避免 DrawScope 内重复分配

#### 设计参考

- 参考项目 KeMuONEXueKao 的 CSS 构成主义几何装饰系统
- 以 Jetpack Compose Canvas 原生绘制方式重新实现，适配移动端
- 联网调研 Material 3 设计规范与 Jetpack Compose Canvas 最佳实践

### 代码结构变更

| 文件 | 变更类型 | 说明 |
| :--- | :--- | :--- |
| `ui/components/GeoBgDecor.kt` | 新增 | 构成主义几何背景装饰组件，密封类变体驱动 |
| `ui/theme/Theme.kt` | 修改 | 新增 `GeoDecorColors` data class 与 `LocalGeoDecorColors` CompositionLocal |
| `home/HomeScreen.kt` | 修改 | 加载态与主页均集成装饰层 |
| `home/ModuleScreen.kt` | 修改 | 加载态与模块详情页集成装饰层 |
| `home/SplashActivity.kt` | 修改 | 启动页集成装饰层，强制深色主题以保证装饰颜色注入 |

### 影响说明

- 视觉质感提升：界面从单调的纯色背景升级为有层次感的装饰背景
- 性能影响极小：Canvas 绘制为硬件加速，装饰元素仅在视图首次绘制时计算
- 兼容性：完全离线运行，无新增依赖，无网络权限
- 主题适配：装饰色板自动跟随亮色/暗色主题切换

## v2.0.1（2026-07-16）

### 严重缺陷修复

#### 问题现象

CI 构建的 Release APK 安装后打开应用一直转圈加载，无法显示任何文档内容。

#### 根因分析

`.gitignore` 第 21 行与第 24 行误将 `android/app/src/main/assets/dist-mobile/` 与 `android/app/src/main/assets/index.json` 标记为构建产物忽略，导致：

- 本地构建时这两个路径存在，APK 正常打包 assets，开发环境无法复现问题
- CI 构建（GitHub Actions `actions/checkout`）只检出 git 跟踪文件，assets 目录缺失
- 构建出的 Release APK 不含 `dist-mobile/index.json` 与文档 Markdown
- `ContentLoader.loadIndex()` 读取 `assets/dist-mobile/index.json` 抛 `FileNotFoundException`，被 `catch` 后返回 `null`
- `HomeScreen` 收到 `contentIndex == null` 后持续渲染加载圈，无法进入主界面

#### 修复内容

- 移除 `.gitignore` 中对 `android/app/src/main/assets/dist-mobile/` 的忽略规则
- 移除 `.gitignore` 中对 `android/app/src/main/assets/index.json` 的忽略规则
- 将 `dist-mobile/` 全部 208 个文件（1.45 MB，含 `index.json` 与 17 个模块共 207 篇文档）提交至版本控制
- CI 构建检出代码后即可直接打包 assets 进 APK，保证本地与 CI 构建产物一致

#### 影响说明

- 修复 CI Release APK 无法加载内容的严重缺陷
- 本地开发流程不受影响（`process-content.ps1` 仍可重新生成覆盖）
- 仓库体积增加约 1.45 MB，可接受

## v2.0.0（2026-07-14）

### 架构重构（跨项目统一重构）

本次为大版本更新，完成 ContentLoader 协程化、公共组件抽取、国际化补全、主题统一、Version Catalog 建立，并建立测试基线。

#### 安全与性能修复

- `ContentLoader.kt` 的 `loadIndex()` 与 `loadDocumentMarkdown()` 改为 `suspend fun`，内部 `withContext(Dispatchers.IO)` 切换到 IO 调度器，避免阻塞主线程
- `HomeActivity.kt` 的 `LaunchedEffect` 调用 suspend 版 ContentLoader
- `themes.xml` parent 改为 `Theme.Material3.DayNight.NoActionBar`，`android:windowBackground` 指定为深色背景，修复启动闪白现象
- Loading 状态期间主线程不阻塞（通过 StrictMode 检测）

#### 公共组件抽取

- 新增 `ui/components/CategoryColorParser.kt`，提供 `fun parse(colorStr: String?): Color` 方法，消除 `HomeActivity.kt`、`HomeScreen.kt`、`ModuleScreen.kt` 中重复的颜色解析代码
- 新增 `ui/components/SidebarContent.kt`，接受 `highlightCurrent: Boolean` 参数控制高亮行为，消除 `HomeActivity.kt` 中首页与模块页侧边栏的重复代码
- 新增 `ui/components/DocumentListItem.kt`，统一文档列表项渲染
- 新增 `util/DrawerCloseLauncher.kt` 扩展函数，消除 `HomeActivity.kt` 中 6 处 `scope.launch { try { drawerState.close() } catch ... }` 模板代码
- 新增 `ui/components/LocalStrings.kt`，统一本地字符串访问入口

#### 国际化与主题统一

- `Strings.kt` 的 `LangStrings` 数据类补全 `appName`、`welcomeBack`、`appSubtitle`、`disclaimer`、`disclaimerTitle`、`copied`、`copy`、`latexLabel`、`codeLabel` 字段
- ZH / EN / JA 三种语言分别提供对应文案
- `SplashActivity.kt`、`HomeActivity.kt`、`ComposeMarkdown.kt` 中硬编码文案改为 `strings.*` 调用
- 切换 ZH / EN / JA 三语时，启动页文案、侧边栏免责声明、复制按钮文案均随语言变化
- `Color.kt` 中 `BackendColor`、`CsColor`、`MathColor`、`CloudColor`、`PrimaryDark` 等死代码常量已删除
- `Theme.kt` 中 dark / light colorScheme 设置了 background、surface、onBackground、onSurface、surfaceVariant、outlineVariant 等完整字段
- `Theme.kt` 中 dark scheme 单独定义更亮的 primary（如 `0xFF6EA8FE`），改善 dark mode 下对比度
- `ComposeMarkdown.kt` 的 `MarkdownColorScheme` 合并到 `Theme.kt` 的 colorScheme

#### Version Catalog 建立

- 新增 `android/gradle/libs.versions.toml`，作为依赖版本的唯一来源
- `[versions]` 段包含所有依赖版本（compose-bom、activity-compose、navigation-compose、commonmark、gson、datastore、lifecycle、coil、kotlinx-serialization、AGP、Kotlin、Compose Plugin 等）
- `[libraries]` 段包含所有依赖声明
- `[plugins]` 段包含 AGP、Kotlin、Compose Plugin 插件声明
- `app/build.gradle.kts` 依赖声明改为 `implementation(libs.compose.bom)`、`implementation(libs.activity.compose)` 等
- `build.gradle.kts` 与 `settings.gradle.kts` 中 AGP、Kotlin、Compose Plugin 版本通过 catalog 引用

#### 死代码清理与微小修复

- `ComposeMarkdown.kt` 中 `if (language.isNotBlank() || true)` 已修正
- `SplashActivity.kt` 中 `(context as? ComponentActivity)?.finish()` 改为 `this.finish()` 直接调用
- `Theme.kt` 中 `darkTheme: Boolean` 默认值改为 `isSystemInDarkTheme()`

#### CI 门禁修复

- `.github/workflows/build-apk.yml` 移除 lint Job 的 `continue-on-error: true`
- `.github/workflows/build-apk.yml` 新增 `permissions: contents: write`，修复 tag 推送时 GITHUB_TOKEN 无权创建 Release 的 403 `Resource not accessible by integration` 错误
- 完善 `.gitignore`（`*.apk`、`android/app/src/main/assets/index.json` 等）
- 删除 `android/app/src/main/assets/index.json` 孤儿文件
- `app/build.gradle.kts` 移除明文密码 `fandex2026`，签名密码改为从 `System.getenv("FANDEX_KEYSTORE_PASSWORD")` 或 `local.properties` 读取
- 配置 GitHub Secrets（`FANDEX_KEYSTORE_BASE64`、`FANDEX_KEYSTORE_PASSWORD`、`FANDEX_KEY_ALIAS`、`FANDEX_KEY_PASSWORD`），使 CI 能正确解码签名密钥库并完成 Release 签名构建
- `proguard-rules.pro` 补充 Gson、commonmark-java、Kotlin Coroutines keep 规则
- 修正 `README.md` 架构描述（移除虚假的「Service 层」声称），构建说明中明确提及「首次构建需运行 `powershell scripts/process-content.ps1`」前置步骤

#### 测试基线建立

- 新增 33 个单元测试，覆盖核心模块：
  - `android/app/src/test/java/com/fandex/app/data/ContentLoaderTest.kt` 覆盖 `loadIndex` 正常解析、文件不存在返回 null、JSON 格式错误返回 null、`loadDocumentMarkdown` 正常加载与异常路径
  - `android/app/src/test/java/com/fandex/app/data/PreprocessMarkdownTest.kt` 覆盖 LaTeX 块级 / 行内公式替换、TOC 标记移除、表格行跳过、代码块保护
  - `android/app/src/test/java/com/fandex/app/data/ApplySyntaxHighlightTest.kt` 覆盖关键字 / 字符串 / 注释 token 提取
- CI 中新增 test Job 执行 `./gradlew test`，作为 build Job 的前置依赖

---

## v1.1.0（2026-06-24）

### 正式发行版

Android 平台离线速查应用，采用 Kotlin + Jetpack Compose + Material 3 构建。

#### 新增

- 17 模块 207 篇文档，完全离线访问
- Kotlin + Jetpack Compose + Material 3 技术栈
- 深色/浅色双模式主题切换
- 三语界面（中文/英文/日文）
- Markdown 渲染与代码高亮
- DataStore 持久化用户偏好
- 完全离线运行，无 INTERNET 权限
- 侧边栏免责声明区块
- CodeQL 安全扫描工作流
- PR 模板与贡献规范
- 启动图标修正为字母 F（左竖线 + 顶横线 + 中横线）

#### 修复

- 修正启动图标形状错误（原为 H 形，现为 F 形）
- 移除前景层重复的背景层
