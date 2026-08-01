---
order: 260
title: Jest 配置与快照
module: 036-software-testing
category: '036-software-testing'
difficulty: beginner
description: Jest 配置与快照 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Jest 配置与快照

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## jest.config.js 配置

**换行写法：Jest 配置文件**
`module.exports = { <配置项> };`

```javascript
# Jest 配置文件示例
module.exports = {
  testEnvironment: "node",
  testMatch: ["**/*.test.js"],
  collectCoverageFrom: ["src/**/*.js"],
  coverageDirectory: "coverage",
  moduleNameMapper: { "^@/(.*)$": "<rootDir>/src/$1" },
};
```

---

## testEnvironment 环境

**基本写法：设置测试环境**
`testEnvironment: "<node|jsdom>"`

```javascript
# Node 环境与浏览器环境
testEnvironment: "node";    # Node.js 环境
testEnvironment: "jsdom";   # 浏览器 DOM 环境
```

---

## preset 预设

**基本写法：使用预设配置**
`preset: "<预设名>"`

```javascript
# 使用 ts-jest 或其他预设
preset: "ts-jest";
preset: "@testing-library/react";
```

---

## moduleNameMapper 路径映射

**基本写法：模块路径别名**
`moduleNameMapper: { "<别名正则>": "<真实路径>" }`

```javascript
# 路径别名映射
moduleNameMapper: {
  "^@/(.*)$": "<rootDir>/src/$1",
  "\\.(css|less)$": "identity-obj-proxy",
};
```

---

## 命令行选项

**基本写法：常用 Jest 命令**
`jest [<测试路径>] [--watch] [--coverage] [--verbose]`

```bash
# Jest 常用命令
jest                          # 运行所有测试
jest path/to/test             # 运行指定测试
jest --watch                  # 监视模式
jest --coverage               # 生成覆盖率报告
jest --verbose                # 显示详细输出
jest --bail                   # 失败时停止
```

---

## toMatchSnapshot 快照测试

**基本写法：生成并对比快照**
`expect(<值>).toMatchSnapshot([<属性匹配>, [<提示>]])`

```javascript
# 快照测试序列化对象
expect({ id: 1, name: "Alice" }).toMatchSnapshot();
```

---

## toMatchInlineSnapshot 内联快照

**基本写法：内联快照存储在测试文件中**
`expect(<值>).toMatchInlineSnapshot([<属性匹配>,] "<快照>")`

```javascript
# 内联快照首次运行自动写入
expect(config).toMatchInlineSnapshot();
```

---

## 更新快照

**基本写法：更新过时快照**
`jest --updateSnapshot`

```bash
# 更新所有快照
jest --updateSnapshot
jest -u   # 简写
```

---

## toThrowErrorMatchingSnapshot

**基本写法：异常快照**
`expect(() => <调用>).toThrowErrorMatchingSnapshot()`

```javascript
# 异常信息快照
expect(() => riskyCall()).toThrowErrorMatchingSnapshot();
```

---

## setup 文件

**基本写法：全局设置文件**
`setupFiles: ["<路径>"]`
`setupFilesAfterEnv: ["<路径>"]`

```javascript
# 配置全局 setup 文件
setupFiles: ["<rootDir>/jest.setup.js"];
setupFilesAfterEnv: ["@testing-library/jest-dom"];
```

---

## coverageThreshold 覆盖率阈值

**换行写法：设置覆盖率阈值**
`coverageThreshold: { global: { branches: <n>, functions: <n>, lines: <n>, statements: <n> } }`

```javascript
# 强制覆盖率达标
coverageThreshold: {
  global: {
    branches: 80,
    functions: 80,
    lines: 80,
    statements: 80,
  },
};
```

---

## transform 转换

**基本写法：配置代码转换**
`transform: { "<文件正则>": "<转换器>" }`

```javascript
# 使用 babel 或 ts-jest 转换
transform: {
  "^.+\\.tsx?$": "ts-jest",
  "^.+\\.jsx?$": "babel-jest",
};
```

---

## 全局配置 setup 与 teardown

**换行写法：全局 setup/teardown**
`globalSetup: "<模块路径>"`
`globalTeardown: "<模块路径>"`

```javascript
# 全局 setup 与 teardown 模块
module.exports = {
  globalSetup: "<rootDir>/setup.js",
  globalTeardown: "<rootDir>/teardown.js",
};
```

## 参考文献



ISTQB 官方资源：https://www.istqb.org/
Testing Library：https://testing-library.com/
Playwright：https://playwright.dev/
Martin Fowler 测试专题：https://martinfowler.com/testing/

## 延伸阅读



测试分层与用例设计，见 036-software-testing 模块文档。
CI 集成测试，见 031-devops 模块。
代码质量与评审，见 037-software-engineering 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供测试课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 测试替身与依赖隔离

替身类型：dummy、stub、spy、mock、fake；按意图选择。
mock 验证交互（调用次数/参数），stub 返回数据；过度验证交互导致脆测试。
依赖注入与端口适配器（hexagonal）提升可测性。
Testcontainers 起真实依赖（数据库/消息）兼顾真实与隔离。

### 13.2 测试金字塔落地

单元：纯函数与领域逻辑，毫秒级。
集成：Repository/API/外部服务，秒级。
E2E：关键用户旅程，分钟级；冒烟集在发布前。
度量与治理：失败分类、flake 治理、覆盖率趋势看板。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 测试基础与方法 | 001-TestBasicsMethod | 本文的前置基础 |
| 功能与自动化测试 | 002-FunctionalAndAutomatedTest | 本文的并列主题 |
| 性能与接口测试 | 003-PerformanceInterfaceTest | 本文的性能延伸 |
| 安全与移动测试 | 004-SecurityAndMobileTest | 本文的安全延伸 |
| 测试概念与原则 | 005-TestConceptPrinciple | 本文的并列主题 |
| 测试层级 | 006-TestLevels | 本文的并列主题 |
| 测试类型 | 007-TestType | 本文的并列主题 |
| 等价类划分 | 008-EquivalenceClassPartition | 本文的并列主题 |
| 边界值分析 | 009-BoundaryValueAnalysis | 本文的并列主题 |
| Selenium | 010-Selenium | 本文的并列主题 |
| pytest | 011-Pytest | 本文的并列主题 |
| JUnit5 | 012-JUnit5 | 本文的并列主题 |
| API自动化测试 | 013-APIAutomationTest | 本文的并列主题 |
| JMeter | 014-JMeter | 本文的并列主题 |
| 白盒测试覆盖度 | 015-WhiteBoxTestCoverage | 本文的并列主题 |
| 自动化测试框架对比 | 016-AutomationTestFrameworkComparison | 本文的并列主题 |
| API自动化测试详解 | 017-APIAutomationTestDetailed | 本文的并列主题 |
| 压力测试与稳定性测试 | 018-StressAndStabilityTest | 本文的并列主题 |
| 安全测试 | 019-SecurityTesting | 本文的安全延伸 |
| 测试双 | 020-TestDouble | 本文的并列主题 |
| TDD与BDD | 021-TDDBDD | 本文的并列主题 |
| CI-CD测试门禁 | 022-CICDTest | 本文的并列主题 |
| Jest 基础 API | 023-JestBasics | 本文的前置基础 |
| Jest Mock 模拟 | 024-JestMock | 本文的并列主题 |
| Jest 异步测试 | 025-JestAsync | 本文的并列主题 |
| Jest 配置与快照 | 026-JestConfig | 本文自身 |
| Mockito 模拟 | 027-Mockito | 本文的并列主题 |
| E2E 端到端测试 | 028-E2ETest | 本文的并列主题 |
| 断言库 | 029-AssertionLibrary | 本文的并列主题 |
