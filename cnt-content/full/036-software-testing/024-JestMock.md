---
order: 240
title: Jest Mock 模拟
module: 036-software-testing
category: '036-software-testing'
difficulty: beginner
description: Jest Mock 模拟 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Jest Mock 模拟

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## jest.fn 创建 Mock 函数

**基本写法：创建模拟函数**
`jest.fn([<实现>])`

```javascript
# 创建 Mock 函数
const mockFn = jest.fn();
mockFn("a");
expect(mockFn).toHaveBeenCalledWith("a");
```

---

## Mock 函数返回值

**基本写法：设置 Mock 返回值**
`<mock>.mockReturnValue(<值>)`
`<mock>.mockReturnValueOnce(<值>)`
`<mock>.mockResolvedValue(<Promise值>)`
`<mock>.mockRejectedValue(<错误>)`

```javascript
# 设置 Mock 函数返回值
const fn = jest.fn();
fn.mockReturnValue(42);
fn.mockReturnValueOnce(1).mockReturnValueOnce(2);
fn.mockResolvedValue("async value");
fn.mockRejectedValue(new Error("失败"));
```

---

## Mock 函数实现

**基本写法：自定义 Mock 实现**
`<mock>.mockImplementation(<函数>)`
`<mock>.mockImplementationOnce(<函数>)`

```javascript
# 自定义 Mock 实现
const fn = jest.fn();
fn.mockImplementation((x) => x * 2);
fn.mockImplementationOnce((x) => x + 1);
```

---

## jest.mock 模块模拟

**基本写法：自动 Mock 整个模块**
`jest.mock(<模块路径>)`

```javascript
# 自动 Mock 整个模块
jest.mock("./utils");
const { add } = require("./utils");
add.mockReturnValue(10);
```

---

## jest.mock 工厂函数

**换行写法：使用工厂函数自定义 Mock**
`jest.mock(<模块路径>, () => { <工厂实现> })`

```javascript
# 使用工厂函数自定义 Mock
jest.mock("./api", () => ({
  fetchData: jest.fn(() => Promise.resolve({ data: "mocked" })),
}));
```

---

## jest.requireActual 真实模块

**基本写法：获取真实模块**
`jest.requireActual(<模块路径>)`

```javascript
# 部分模拟时保留真实模块
jest.mock("./utils", () => ({
  ...jest.requireActual("./utils"),
  onlyMocked: jest.fn(),
}));
```

---

## jest.spyOn 监视方法

**基本写法：监听对象方法**
`jest.spyOn(<对象>, <方法名>)`

```javascript
# 监视对象方法调用
const obj = { method: (x) => x + 1 };
const spy = jest.spyOn(obj, "method");
obj.method(5);
expect(spy).toHaveBeenCalledWith(5);
```

---

## spyOn 模拟实现

**基本写法：监听并替换实现**
`jest.spyOn(<对象>, <方法>).mockImplementation(<函数>)`

```javascript
# 监听并替换方法实现
const spy = jest.spyOn(console, "log").mockImplementation(() => {});
console.log("不会输出");
expect(spy).toHaveBeenCalled();
```

---

## jest.mocked 类型安全 Mock

**基本写法：将导入转为 Mock 类型**
`jest.mocked(<导入函数>)`

```javascript
# 类型安全地访问 Mock 属性
import { fetchData } from "./api";
jest.mock("./api");
jest.mocked(fetchData).mockResolvedValue({ data: "ok" });
```

---

## Mock 调用记录

**基本写法：访问 Mock 调用信息**
`<mock>.mock.calls`
`<mock>.mock.results`
`<mock>.mock.instances`

```javascript
# 访问 Mock 调用记录
const fn = jest.fn();
fn("a", "b");
expect(fn.mock.calls[0]).toEqual(["a", "b"]);
expect(fn.mock.results[0].value).toBeUndefined();
```

---

## mockReset 重置 Mock

**基本写法：重置 Mock 状态**
`<mock>.mockReset()`
`<mock>.mockClear()`
`<mock>.mockRestore()`

```javascript
# 重置 Mock 不同级别
fn.mockClear();   # 清除调用记录
fn.mockReset();   # 清除记录并移除实现
fn.mockRestore(); # 恢复 spyOn 的原始实现
```

---

## jest.useFakeTimers 模拟定时器

**基本写法：使用假定时器**
`jest.useFakeTimers()`
`jest.useRealTimers()`
`jest.runAllTimers()`
`jest.advanceTimersByTime(<毫秒>)`

```javascript
# 模拟定时器执行
jest.useFakeTimers();
const fn = jest.fn();
setTimeout(fn, 1000);
jest.advanceTimersByTime(1000);
expect(fn).toHaveBeenCalled();
```

---

## jest.fn 链式调用

**换行写法：Mock 链式调用**
`jest.fn().mockReturnThis().mockReturnValue(<值>)`

```javascript
# Mock 链式 API 调用
const chainable = jest.fn().mockReturnThis();
chainable().method().value();
```

---

## mockImplementation async

**换行写法：Mock 异步函数**
`jest.fn().mockImplementation(async (<参数>) => { <异步逻辑> })`

```javascript
# Mock 异步函数实现
const asyncFn = jest.fn().mockImplementation(async (id) => {
  return { id, name: "mocked" };
});
await asyncFn(1);
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
| Jest Mock 模拟 | 024-JestMock | 本文自身 |
| Jest 异步测试 | 025-JestAsync | 本文的并列主题 |
| Jest 配置与快照 | 026-JestConfig | 本文的并列主题 |
| Mockito 模拟 | 027-Mockito | 本文的并列主题 |
| E2E 端到端测试 | 028-E2ETest | 本文的并列主题 |
| 断言库 | 029-AssertionLibrary | 本文的并列主题 |
