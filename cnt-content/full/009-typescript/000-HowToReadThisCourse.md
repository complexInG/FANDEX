---
order: 10
title: 本课程使用指南（先读这里）
module: 'typescript'
category: 前端技术
difficulty: beginner
description: TypeScript 零基础学习路线：环境先行、跳过规则、分层阅读路径与验收标准。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'typescript/001-TypeScriptOverviewEnvSetup'
  - 'typescript/006-BasicTypeSystem'
  - 'typescript/007-InterfaceTypeAlias'
  - 'typescript/066-TypeScriptFAQ'
prerequisites: []
---

## 0. 这份资料怎么用

本模块有 67 篇文档，编号就是学习顺序：从 001 本指南开始，经 002 环境配置依次递进，到 067 的 FAQ 速查。**不要跳着读，也不要一次读完**。文档分三类：

**必读（零基础主线，约 2-3 周）**

1. `001-TypeScriptOverviewEnvSetup`：先装环境、跑通第一个 TypeScript 程序；
2. `002-TSBasicsVariablesAndTypes` 到 `005-TSBasicsGenerics`：变量、函数、类、泛型四篇前篇；
3. `006-BasicTypeSystem` 到 `010-LocalTypeInference`：类型系统核心；
4. `TypeCompatibility`、`TypeInferenceDeepDive`、`ConstAssertion`、`NeverTypeSemantics`：理解"为什么能赋值、为什么报错"；
5. `016-TypeGuardCustomGuard` 到 `023-ModuleResolutionInModernJavaScriptToolchains`：守卫、索引签名、声明文件与模块解析；
6. `048-TypeScriptEngineeringConfig`、`059-TypeScriptProjectExampleTypeSafeAPIClient`、`TypeScriptProjectExampleTodoApp`：工程化与实战收尾。

**按需查阅（遇到问题再回来看）**

- `TypeScriptFAQ`：高频疑问合集，先查这里再搜；
- `062-TscCompilerCommands`：tsc 命令速查；
- `063-TypeTestingAndAssertions`：类型测试与断言；
- `001-TypeScriptOverviewEnvSetup` 末尾的核心术语表与进阶新特性速览。

**进阶原理（有项目经验后再读）**

- 类型论与理论：`028-OnTheRoleOfSymbolicExecutionInTypeSystems` 到 `032-ConditionalTypeDistribute`、`061-ATheoryOfTypePolymorphismInProgramming`；
- 类型体操：`055-TypeGymnastics`、`051-ConditionalTypeInfer`、`054-TemplateLiteralType`；
- 编译器与性能：`052-TypeScriptCompilePerformanceOptimization`、`065-TypeScript7CompilerGuide`。

## 1. 为什么环境配置排在最前面

早期版本把"概述与环境配置"排在四篇前篇之后，零基础学习者会在前四篇里反复追问："我写的代码在哪里运行？tsc 是什么？"。本版已经调整：**第 01 课先装环境、跑通 `tsc`，再学语法**。语法学完立刻能在真实工程里验证，认知负担最小。

```mermaid
flowchart LR
    A["00 本指南"] --> B["01 环境配置<br/>跑通 tsc"]
    B --> C["02-05 前篇<br/>变量/函数/类/泛型"]
    C --> D["06-09 类型系统核心"]
    D --> E["10-13 兼容性/推断/const/never"]
    E --> F["14-24 类装饰器/声明文件/模块"]
    F --> G["49-61 工程化与项目实战"]
    G --> H["62-67 理论/命令/FAQ 按需查阅"]
```

## 2. 三条阅读规则

**规则一：环境先行。** 先读 `001-TypeScriptOverviewEnvSetup` 并完成安装；前四篇前篇里的每一段代码都建议放进自己的工程里跑一遍，而不是只读。

**规则二：看到公式直接跳过。** 少数进阶文档会使用类型论记号（如 `Γ ⊢ e : τ`）。零基础第一遍只读代码示例、表格和"动手试试"，公式一律跳过。正文不再出现这类记号，需要了解时再看各篇文末的"进阶附录"（如 `006-BasicTypeSystem` 附录 A）。

**规则三：新特性速览可跳过。** `001-TypeScriptOverviewEnvSetup` 末尾的 TS 5.x 新特性速览（const 类型参数、satisfies、using、NoInfer 等）是给有基础的人看的，第一遍读到正文"9. 总结"即可。`satisfies` 与 `as const` 都有独立成篇的系统讲解（`049-SatisfiesOperator`、`ConstAssertion`）。

## 3. 术语不认识怎么办

1. 先查 `001-TypeScriptOverviewEnvSetup` 末尾的"核心术语表"（零基础速查版）；
2. 再查 `TypeScriptFAQ` 的"概念对比"小节；
3. 进阶术语在各篇末尾的"术语表/附录"中查找。

## 4. 常见误区

| 误区 | 真相 |
| --- | --- |
| 把语法全部背下来 | 语法随用随查，重点是理解类型规则 |
| 跳过环境搭建直接看代码 | 没有运行环境，代码无法验证，学完就忘 |
| 一上来读类型体操 | 先会写业务类型，再学条件类型与体操 |
| 看到公式就觉得自己学不会 | 公式是进阶附录，跳过不影响主线 |
| 只读不敲 | 每段代码都亲手敲一遍，改一改看报错 |

## 5. 预期时间与验收标准

| 阶段 | 预期时间 | 验收标准 |
| --- | --- | --- |
| 第 1 周（01-09） | 6-8 小时 | 能独立初始化 tsconfig，写出带类型的变量、函数、类、泛型代码 |
| 第 2 周（10-18） | 6-8 小时 | 能解释"为什么这个赋值合法"，会用类型守卫和索引签名 |
| 第 3 周（19-24） | 5-7 小时 | 能读懂 .d.ts，正确使用 import type 与模块解析配置 |
| 第 4 周（49-61） | 8-10 小时 | 能独立完成 TODO 项目实战，并解释关键类型设计 |

## 6. 一句话记住

> 先跑通环境，再学语法；公式跳过、代码必敲；遇到问题先查 FAQ 和术语表。
