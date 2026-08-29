> **重要通知** · 2026 年 7 月 24 日
>
> 为推进 FANDEX 体系的长期演进,整体项目正进行**整合与重构**,后续将以全新仓库([fanquanpp/FANDEX](https://github.com/fanquanpp/FANDEX))作为唯一维护主体重新发布,预计 **2026 年 8 月下旬**正式完成。
>
> 据此,本仓库内容及站内文档自即日起**暂停更新**,但仍会围绕美术风格、交互体验(UI/UX)等方向持续探索。新仓库正式发布后,本仓库将进入**只读归档状态**,现有源码与历史 Release 仍可自由获取与使用;如有 fork 或二次开发需求,请遵循 **MIT 许可证**条款自行处理,作者不再对使用过程中的任何问题提供支持。
>
> 敬请留意后续公告,感谢您的理解与支持。 —— FANDEX 维护者

---

<div align="center">

# FANDEX-App

**代码语法速查伴侣** · Android 原生离线应用

为已具备基础的开发者打造的移动端语法速查工具:实践中遗忘写法、需要确认函数签名、查阅使用公式时,打开 App 即查即用。22 个模块、313 篇速查文档全部内置,飞行模式下正常工作。

[![下载 APK](https://img.shields.io/badge/APK-GitHub_Releases-2088FF?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fanquanpp/FANDEX-App/releases)
[![首页](https://img.shields.io/badge/GitHub_Pages-访问首页-2088FF?style=for-the-badge&logo=github&logoColor=white)](https://fanquanpp.github.io/FANDEX-App/)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.4.10-7F52FF?style=flat-square&logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![Jetpack Compose](https://img.shields.io/badge/Compose-Material_3_Expressive-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white)](https://developer.android.com/compose)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](./LICENSE)

</div>

## 核心特性

- **即查即用**:22 个模块、313 篇速查文档全部内置,完全离线工作,无网络依赖
- **公式化速查**:统一模板(语法签名 + 代码示例),跨模块查阅体验一致
- **原生渲染**:纯 Kotlin + Jetpack Compose 实现,commonmark-java AST 直接映射为 Compose 组件树,无 WebView
- **代码高亮**:支持 20+ 语言语法高亮、公式预处理、代码一键复制
- **双主题过渡**:DataStore 持久化用户偏好,主题切换带 400ms 颜色过渡动画
- **几何背景装饰**:基于 Compose Canvas 原生绘制,四种视图变体 + 十一种装饰元素

## 内容矩阵

22 个模块按五大分类组织,所有速查文档由本仓库针对移动端查阅场景独立编撰与特色重写。

| 分类 | 模块 |
| :--- | :--- |
| 编程语言 | C · C++ · C# · Go · Java · JavaScript · Kotlin · Lua · Python · TypeScript · HarmonyOS |
| 前端技术 | CSS · HTML5 · SVG · React · Vue3 |
| 数据库 | MySQL · PostgreSQL · Redis · SQL |
| 工具链 | Git |
| 标记语言 | Markdown · HTML5 · SVG |

## 快速开始

环境要求:Android Studio(最新稳定版本)、JDK 21、Android SDK 37。

```bash
# Debug 构建
cd android && ./gradlew assembleDebug

# Release 构建(启用混淆 + 签名)
cd android && ./gradlew assembleRelease
```

APK 输出路径:`android/app/build/outputs/apk/{debug|release}/FANDEX-v{version}.apk`

> 安装前请在系统设置中允许"安装未知来源应用"权限。最低支持 Android 8.0(API 26),目标平台 Android 16(API 37)。

## 技术栈

| 层级 | 技术 | 版本 |
| :--- | :--- | :--- |
| 开发语言 | Kotlin | 2.4.10 |
| UI 框架 | Jetpack Compose + Material 3 | BOM 2026.06.01 |
| 导航 | Navigation Compose | 2.9.8 |
| Markdown 解析 | commonmark-java + GFM 扩展 | 0.29.0 |
| 偏好持久化 | DataStore Preferences | 1.2.1 |
| 网络请求 | OkHttp(仅用于更新自检) | 5.4.0 |
| 构建工具 | Android Gradle Plugin | 9.3.0 |
| 编译目标 | JVM 21 / Android SDK 37 | 最低 SDK 26 |

## 许可证

基于 [MIT 许可证](./LICENSE) 完全开源。任何个人或机构均可自由获取、使用、修改和分发,但须保留原始版权声明与许可声明。

## 免责声明

本仓库所有内容均由人工与人工智能技术协同编撰,受限于编撰方式及知识更新周期,内容可能存在遗漏、过时或错误之处。使用者应结合官方文档与权威资料进行独立验证与核实,因使用或引用本仓库内容所产生的一切直接或间接后果,均由使用者自行承担。
