---
order: 590
title: TypeScript 7 原生编译器
module: 'typescript'
category: 前端技术
difficulty: intermediate
description: TypeScript 7（typescript-go 原生端口）的定位、安装、兼容性与迁移要点。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'typescript/001-TypeScriptOverviewEnvSetup'
  - 'typescript/052-TscCompilerCommands'
  - 'typescript/043-TypeScriptCompilePerformanceOptimization'
prerequisites:
  - 'typescript/001-TypeScriptOverviewEnvSetup'
---

## 概述

TypeScript 7 是微软以 Go 语言重写的原生编译器，官方仓库 microsoft/typescript-go 的 README 直接以 "TypeScript 7" 作为标题，并将其定位为 TypeScript 的长期演进方向。npm 上的 `typescript` 包当前稳定版已进入 7.0.x，命令行工具仍然叫 `tsc`，因此对绝大多数项目而言，升级 TypeScript 7 只是更新依赖版本。本文从官方仓库与发布说明出发，梳理它的背景、安装方式、功能完成度与迁移注意点。

## 背景：为什么会有 TypeScript 7

TypeScript 从 2012 年发布以来一直运行在 JavaScript 运行时之上：编译器本身用 TypeScript 编写，先编译成 JavaScript 再执行。这种自举架构带来两个长期成本：类型检查器的启动与全量检查速度受限于 JS 引擎，以及内存占用随大型代码库增长。

微软在官方博客宣布了原生端口（native port）计划，microsoft/typescript-go 仓库作为开发暂存区推进这一工作，并计划长期合并回 microsoft/TypeScript。官方 README 明确：该仓库和议题跟踪器最终会关闭，内容并入主仓库。当前 npm `typescript` 的 7.0.x 稳定版即建立在这一原生实现之上。

## 安装与使用

安装方式与之前完全一致：

```bash
# 安装当前稳定版（7.x）
npm install -D typescript

# 查看版本
npx tsc --version
```

官方 README 说明：TypeScript 7.0 RC 及以后，命令名统一为 `tsc`，用法与 5.x/6.x 相同。仍想体验预览通道的团队可以使用 `@typescript/native-preview` 包，其中的命令为 `tsgo`：

```bash
npm install @typescript/native-preview
npx tsgo --version
```

VS Code 用户可以通过官方预览扩展启用原生语言服务：在设置中开启 `js/ts.experimental.useTsgo`。

## 功能完成度

官方 README 给出了相对 TypeScript 6.0 的逐项状态：

| 能力 | 状态 | 说明 |
| --- | --- | --- |
| 程序创建与模块解析 | 已完成 | 与 TS 6.0 相同 |
| 解析 / 扫描 | 已完成 | 与 TS 6.0 完全相同的语法错误 |
| tsconfig 解析 | 已完成 | 错误提示可能不如旧版详细 |
| 类型解析与类型检查 | 已完成 | 错误、位置、消息与 TS 6.0 一致 |
| JSX / 声明文件输出 / JS 输出 | 已完成 | |
| watch / build / 增量构建 | 已完成 | 项目引用与增量构建可用 |
| 语言服务（LSP） | 进行中 | 大部分功能已实现 |
| 编译器 API | 未就绪 | 依赖 `typescript` API 的构建工具需等待 |

所谓"已完成"表示官方未发现已知缺陷或重大剩余工作；"进行中"表示部分功能可能不可用。升级前应重点确认自己是否依赖编译器 API（例如自定义 transform、语言服务插件），这类工具需要等待官方 API 层完成。

## 兼容性与迁移要点

1. 类型与错误消息：官方以 TS 6.0 为对齐基线，类型结果与错误位置保持一致；错误中的类型打印格式可能略有不同。
2. 配置兼容：`tsconfig.json` 解析已完成，`strict` 家族、`moduleResolution`（node10/node16/nodenext/bundler）等选项沿用。
3. 工具链适配：`vue-tsc` 等包装工具声明 `typescript >= 5.0.0` 即可兼容 7.x；`@types` 包的版本策略不变。
4. 增量构建：`tsc --build` 与项目引用在 7.x 已完成，大型 monorepo 可以放心升级。
5. 有意变更：官方在仓库的 CHANGES.md 中列出了相对 TS 6.0 的有意行为变更，升级前建议通读，避免把"预期变更"当成回归。
6. 编译器 API 用户：自定义构建插件、代码生成工具等直接调用 `typescript` API 的项目，先确认依赖方是否已适配 7.x，再决定升级窗口。

## 与学习路线的衔接

本模块其余文档（基础类型、窄化、泛型、类型体操等）讲解的是语言与类型系统本身，这些能力在 TypeScript 7 中原样保留，学习路径不受影响。TypeScript 7 改变的是"编译器如何更快地执行这些规则"，而不是规则本身。

## 小结

TypeScript 7 = 原生编译器 + 相同的语言语义。安装命令不变、CLI 不变、类型行为以 6.0 为基线；真正需要关注的是语言服务与编译器 API 的完成度。对普通项目，执行 `npm install -D typescript` 并跑一遍 `tsc --noEmit` 即可验证。
