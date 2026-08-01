---
order: 250
title: Jest 异步测试
module: 036-software-testing
category: '036-software-testing'
difficulty: beginner
description: Jest 异步测试 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Jest 异步测试

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## async / await 测试

**换行写法：使用 async/await 测试异步**
`test(<名称>, async () => { await <异步调用>; expect(...); })`

```javascript
# 使用 async/await 测试异步函数
test("异步获取用户", async () => {
  const user = await fetchUser(1);
  expect(user).toHaveProperty("name");
});
```

---

## Promise return 测试

**基本写法：返回 Promise 进行断言**
`test(<名称>, () => { return <Promise>.then(<回调>); })`

```javascript
# 返回 Promise 让 Jest 等待
test("Promise 解析", () => {
  return fetchUser(1).then((user) => {
    expect(user.id).toBe(1);
  });
});
```

---

## resolves 匹配器

**基本写法：断言 Promise 成功解析**
`expect(<Promise>).resolves.<匹配器>(<期望>)`

```javascript
# 使用 resolves 断言 Promise 结果
test("resolves 断言", () => {
  return expect(Promise.resolve(42)).resolves.toBe(42);
});
```

---

## rejects 匹配器

**基本写法：断言 Promise 被拒绝**
`expect(<Promise>).rejects.<匹配器>(<期望>)`

```javascript
# 使用 rejects 断言 Promise 抛错
test("rejects 断言", () => {
  return expect(Promise.reject(new Error("失败"))).rejects.toThrow("失败");
});
```

---

## async resolves

**换行写法：async 配合 resolves**
`test(<名称>, async () => { await expect(<Promise>).resolves.<匹配器>(<期望>); })`

```javascript
# async/await 配合 resolves
test("async resolves", async () => {
  await expect(Promise.resolve("ok")).resolves.toBe("ok");
});
```

---

## async rejects

**换行写法：async 配合 rejects**
`test(<名称>, async () => { await expect(<Promise>).rejects.<匹配器>(<期望>); })`

```javascript
# async/await 配合 rejects
test("async rejects", async () => {
  await expect(Promise.reject(new Error("err"))).rejects.toThrow("err");
});
```

---

## 回调函数测试

**换行写法：测试回调函数**
`test(<名称>, (<done>) => { <异步操作>; <done>; })`

```javascript
# 使用 done 回调测试异步
test("回调完成", (done) => {
  fetchData((data) => {
    expect(data).toBe("result");
    done();
  });
});
```

---

## 测试超时设置

**基本写法：设置测试超时时间**
`test(<名称>, <回调>, <超时毫秒>)`
`jest.setTimeout(<毫秒>)`

```javascript
# 设置单个测试与全局超时
test("长时间操作", async () => {
  await longTask();
}, 10000);

jest.setTimeout(15000);
```

---

## fetch 模拟

**换行写法：Mock fetch 请求**
`global.fetch = jest.fn(() => Promise.resolve({ json: () => Promise.resolve(<数据>) }))`

```javascript
# Mock 全局 fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ id: 1, name: "Alice" }),
  })
);
```

---

## axios 模拟

**换行写法：Mock axios 模块**
`jest.mock('axios');`
`axios.get.mockResolvedValue({ data: <数据> });`

```javascript
# Mock axios 请求
import axios from "axios";
jest.mock("axios");
axios.get.mockResolvedValue({ data: { id: 1 } });
```

---

## 并发测试 test.concurrent

**换行写法：并发执行测试**
`test.concurrent(<名称>, <回调>, [<超时>])`

```javascript
# 并发执行多个测试用例
test.concurrent("并发测试1", async () => {
  expect(await fetchData()).toBeDefined();
});
```

---

## 异步错误捕获

**换行写法：断言异步函数抛错**
`await expect(<异步函数>()).rejects.toThrow(<错误>)`

```javascript
# 断言异步函数抛出指定错误
await expect(asyncFail()).rejects.toThrow("失败原因");
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
| Jest 异步测试 | 025-JestAsync | 本文自身 |
| Jest 配置与快照 | 026-JestConfig | 本文的并列主题 |
| Mockito 模拟 | 027-Mockito | 本文的并列主题 |
| E2E 端到端测试 | 028-E2ETest | 本文的并列主题 |
| 断言库 | 029-AssertionLibrary | 本文的并列主题 |
