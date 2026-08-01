---
order: 290
title: 断言库
module: 036-software-testing
category: '036-software-testing'
difficulty: beginner
description: 断言库 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 断言库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Chai BDD 风格

**基本写法：expect 风格断言**
`expect(<值>).to.<断言>(<期望>)`

```javascript
# Chai expect 风格断言
import { expect } from "chai";

expect(5).to.equal(5);
expect("hello").to.be.a("string");
expect([1, 2, 3]).to.include(2);
expect({ a: 1 }).to.deep.equal({ a: 1 });
```

---

## Chai should 风格

**基本写法：should 风格断言**
`<值>.should.<断言>(<期望>)`

```javascript
# Chai should 风格断言
import "chai/register-should";

(5).should.equal(5);
"hello".should.be.a("string");
[1, 2, 3].should.include(2);
```

---

## Chai assert 风格

**基本写法：TDD 风格断言**
`assert.<方法>(<实际>, <期望>[, <消息>])`

```javascript
# Chai assert 风格断言
import { assert } from "chai";

assert.equal(5, 5);
assert.typeOf("hello", "string");
assert.include([1, 2, 3], 2);
assert.deepEqual({ a: 1 }, { a: 1 });
```

---

## Chai 链式断言

**基本写法：链式修饰符**
`expect(<值>).to.<修饰符>.<断言>(<期望>)`

```javascript
# Chai 链式修饰符增强可读性
expect(5).to.not.equal(6);
expect(null).to.not.exist;
expect([]).to.be.empty;
expect(10).to.be.at.most(10);
expect("hello").to.have.lengthOf(5);
```

---

## Chai 数字断言

**基本写法：数值比较**
`expect(<值>).to.be.<比较>(<n>)`

```javascript
# Chai 数字比较断言
expect(5).to.be.above(3);
expect(5).to.be.at.least(5);
expect(5).to.be.below(10);
expect(5).to.be.at.most(5);
expect(5).to.be.within(1, 10);
```

---

## Chai 字符串断言

**基本写法：字符串匹配**
`expect(<字符串>).to.<包含|匹配>(<值>)`

```javascript
# Chai 字符串断言
expect("hello world").to.include("world");
expect("hello").to.startWith("he");
expect("world").to.endWith("ld");
expect("hello").to.match(/^he/);
expect("hello").to.have.lengthOf(5);
```

---

## Chai 对象断言

**基本写法：对象属性断言**
`expect(<对象>).to.have.<属性>(<值>)`

```javascript
# Chai 对象属性断言
expect({ a: 1, b: 2 }).to.have.property("a");
expect({ a: 1 }).to.have.property("a", 1);
expect({ a: 1, b: 2 }).to.have.all.keys("a", "b");
expect({ a: 1 }).to.include({ a: 1 });
```

---

## Chai 数组断言

**基本写法：数组断言**
`expect(<数组>).to.<包含|长度>(<值>)`

```javascript
# Chai 数组断言
expect([1, 2, 3]).to.include(2);
expect([1, 2, 3]).to.have.lengthOf(3);
expect([1, 2, 3]).to.have.ordered.members([1, 2, 3]);
expect([1, 2, 3]).to.deep.equal([1, 2, 3]);
```

---

## Chai 异常断言

**基本写法：断言抛出异常**
`expect(() => <调用>).to.throw([<错误类型>][, <消息>])`

```javascript
# Chai 异常断言
expect(() => { throw new Error("失败"); }).to.throw("失败");
expect(() => { throw new TypeError(); }).to.throw(TypeError);
expect(() => { throw new Error(); }).to.throw(/失败/);
```

---

## Hamcrest Java 断言

**基本写法：Hamcrest 匹配器断言**
`assertThat(<实际>, <matcher>)`

```java
# Hamcrest 断言库
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

assertThat(5, is(5));
assertThat("hello", containsString("ell"));
assertThat(5, greaterThan(3));
assertThat("hello", notNullValue());
```

---

## Hamcrest 集合匹配器

**基本写法：集合相关匹配器**
`assertThat(<集合>, hasItem(<元素>))`
`assertThat(<集合>, contains(<元素>))`

```java
# Hamcrest 集合匹配器
assertThat(List.of(1, 2, 3), hasItem(2));
assertThat(List.of(1, 2, 3), contains(1, 2, 3));
assert assertThat(List.of(1, 2, 3), hasSize(3));
assertThat(List.of(1, 2, 3), everyItem(lessThan(10)));
```

---

## Hamcrest 字符串匹配器

**基本写法：字符串匹配器**
`assertThat(<字符串>, <匹配器>)`

```java
# Hamcrest 字符串匹配器
assertThat("hello world", containsString("world"));
assertThat("hello", startsWith("he"));
assertThat("world", endsWith("ld"));
assertThat("hello", equalTo("hello"));
assertThat("  hello  ", is(equalToIgnoringWhiteSpace("hello")));
```

---

## AssertJ 流式断言

**基本写法：AssertJ 流式 API**
`assertThat(<值>).<断言>().<断言>()`

```java
# AssertJ 流式断言库
import static org.assertj.core.api.Assertions.*;

assertThat("hello")
    .isNotNull()
    .startsWith("he")
    .hasSize(5)
    .contains("ell");

assertThat(5).isPositive().isGreaterThan(3);
assertThat(List.of(1, 2, 3)).hasSize(3).contains(2);
```

---

## AssertJ 异常断言

**换行写法：AssertJ 异常断言**
`assertThatThrownBy(() -> <调用>).isInstanceOf(<异常类>).hasMessage("<消息>")`

```java
# AssertJ 异常断言
assertThatThrownBy(() -> { throw new IllegalArgumentException("无效"); })
    .isInstanceOf(IllegalArgumentException.class)
    .hasMessageContaining("无效");
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
| Jest 配置与快照 | 026-JestConfig | 本文的并列主题 |
| Mockito 模拟 | 027-Mockito | 本文的并列主题 |
| E2E 端到端测试 | 028-E2ETest | 本文的并列主题 |
| 断言库 | 029-AssertionLibrary | 本文自身 |
