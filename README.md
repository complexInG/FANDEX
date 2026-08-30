# FANDEX

**FANDEX 是一套「代码语法速查伴侣」体系**：为已具备基础的开发者提供 50+ 技术模块、
1900+ 篇语法速查文档，全部内容离线可用。

本体系托管在**单一 Git 仓库（monorepo）**中：根目录是唯一的仓库根（全仓库只有一个
`.git`），网站、桌面端、双端 Android 应用与共享内容层全部是根仓库下的普通子目录，
不存在任何子仓库、submodule 或嵌套 Git 配置。四端应用共享同一内容体系——内容单一
来源为 `cnt-content/full`，模块元数据唯一来源为 `shd-shared/metadata/modules.json`，
任何一端不维护独立内容副本。

## 仓库结构

```
FANDEX/                        # 仓库根（唯一 .git 所在）
├── README.md  AGENTS.md  CHANGELOG.md  LICENSE   # 根级信息文件
├── app-web/            # 官网（Astro 7 + React 19 + Tailwind CSS 4），GitHub Pages 部署
├── app-desktop/        # 桌面端占位（Tauri 2，规划中）
├── app-Android-new/    # Android 应用 · 新技术栈主线（Kotlin + Jetpack Compose）
├── app-Android-old/    # Android 应用 · 旧技术栈归档线（历史版本，功能完整可构建）
├── cnt-content/        # 内容层：full/ 全量文档、syntax/ 语法速览素材、mobile/ 历史遗留
├── shd-shared/         # 共享层：设计令牌、模块元数据（metadata/modules.json）、图标资产
├── tls-tools/          # 工具链：文档 ID 分配、内容审计、manifest 签名分发
├── thd-third-party/    # 第三方组件 / 插件 / 适配器
└── tools/              # 根目录辅助工具
```

各目录的工程规范详见 [AGENTS.md](AGENTS.md)，版本变更历史见
[CHANGELOG.md](CHANGELOG.md)。

## 应用端说明

双端 Android 应用共享同一套内容体系，`applicationId` 不同，可并存安装：

| | app-Android-new（主线） | app-Android-old（归档线） |
| --- | --- | --- |
| 包名 | `com.fandexpp.fandex` | `com.fandex.app` |
| 技术栈 | Kotlin + Jetpack Compose + Material 3 | Kotlin + Jetpack Compose + Material 3 |
| 内容源 | `cnt-content`（generate-content.mjs） | `cnt-content`（generate-legacy-content.mjs） |
| 文档规模 | 54 模块 / 1900+ 篇 | 54 模块 / 1900+ 篇 |
| 特性 | 语法速览、学习路线、全文搜索、mermaid 图表 | 离线速查、数学公式渲染、更新自检 |

文档内容全部内置于 APK（assets），安装后完全离线可用；内容源统一锚定
`cnt-content/full`，任何一端不做独立内容维护。

## 快速开始

### 环境

- Node.js >= 22 与 pnpm >= 10（`package.json` 声明 `packageManager`）
- JDK 21、Android SDK（compileSdk 37）
- 网站部署于 `/FANDEX/` 基础路径（GitHub Pages 项目站点）

### 网站（app-web）

```bash
pnpm install --frozen-lockfile
pnpm build:web        # 构建（含内容统计、语法索引、Astro 静态构建、pagefind）
pnpm dev:web          # 本地开发服务器
```

### Android 双端

```bash
# 新技术栈主线（构建前先同步内容资产）
node app-Android-new/scripts/generate-content.mjs
cd app-Android-new && ./gradlew :app:assembleDebug

# 旧技术栈归档线
node app-Android-old/scripts/generate-legacy-content.mjs
cd app-Android-old && ./gradlew :app:assembleDebug
```

两个工程均已配置 Gradle wrapper（腾讯镜像分发），首次构建自动下载。

## 内容管线

内容单一来源为 `cnt-content/full/<编号-模块>/<编号-标题>.md`，frontmatter
携带 `order / title / module / category / difficulty / description` 等元数据：

- **网站**：Astro Content Collections 构建期校验（`app-web/src/content.config.ts`）；
- **Android new**：`app-Android-new/scripts/generate-content.mjs` 生成
  `assets/docs`、`assets/metadata`、语法数据与学习路径数据；
- **Android old**：`app-Android-old/scripts/generate-legacy-content.mjs` 生成
  `assets/dist-mobile`（frontmatter 剥离 + `index.json` 索引）。

模块与分类元数据唯一来源为 `shd-shared/metadata/modules.json`
（模块 id / 标题 / 分类 / 配色），修改模块结构前请先阅读
[AGENTS.md](AGENTS.md) 中的文档 frontmatter 规范与 ID 分配流程。

## 构建与发布（CI）

`.github/workflows/android-release.yml` 提供双端 Android 自动化：

- **push 到 main**：双端并行构建校验，上传 APK 构建产物（不发布）；
- **push `v*` 标签**：双端构建签名 APK 并创建 GitHub Release，附带
  `FANDEX-<tag>.apk` 与 `FANDEX-Legacy-<tag>.apk`；发布说明自动提取
  `CHANGELOG.md` 对应版本段落；
- 签名采用个人分发策略：未注入正式 keystore 时回退 debug 签名，
  两个安装包包名不同，可并存安装。

网站部署由 `deploy.yml` 负责：push 到 main 后构建并发布至 GitHub Pages。

## 贡献

- 代码与文档规范、frontmatter 字段约束、校验入口见 [AGENTS.md](AGENTS.md)；
- 新增 / 修改文档请保持 frontmatter 规范并通过内容审计脚本；
- 提交信息遵循 Conventional Commits，版本发布走 `v*` 标签。

## 许可

MIT License，全文见 [LICENSE](LICENSE)；`thd-third-party/licenses/` 存放
第三方组件的许可文本。
