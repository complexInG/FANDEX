---
order: 270
title: Mockito 模拟
module: 036-software-testing
category: '036-software-testing'
difficulty: beginner
description: Mockito 模拟 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Mockito 模拟

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## mock 创建模拟对象

**基本写法：创建 Mock 对象**
`mock(<类>.class)`
`@Mock <类型> <字段>;`

```java
# 创建 Mock 对象
import static org.mockito.Mockito.*;

List<String> mockList = mock(List.class);
mockList.add("item");
verify(mockList).add("item");
```

---

## @Mock 注解

**换行写法：使用注解创建 Mock**
`@ExtendWith(MockitoExtension.class)`
`class <测试类> {`
`    @Mock <类型> <字段>;`
`}`

```java
# 使用 @Mock 注解
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.Mock;

@ExtendWith(MockitoExtension.class)
class ServiceTest {
    @Mock
    private Database db;
}
```

---

## when 打桩返回值

**换行写法：设置方法返回值**
`when(<mock>.<方法>(<参数>)).thenReturn(<值>)`
`when(<mock>.<方法>(<参数>)).thenThrow(<异常>)`

```java
# 设置 Mock 方法返回值或抛异常
when(mockList.size()).thenReturn(10);
when(mockList.get(0)).thenReturn("first");
when(mockList.get(1)).thenThrow(new RuntimeException("不存在"));
```

---

## thenReturn 多次返回

**换行写法：连续调用返回不同值**
`when(<mock>.<方法>()).thenReturn(<值1>, <值2>, <值3>)`

```java
# 同一方法多次调用返回不同值
when(mockIterator.next()).thenReturn("A", "B", "C");
```

---

## thenAnswer 自定义实现

**基本写法：自定义方法实现**
`when(<mock>.<方法>()).thenAnswer(<Answer>)`
`when(<mock>.<方法>()).then(invocation -> <实现>)`

```java
# 使用 lambda 自定义方法行为
when(mockList.get(anyInt())).thenAnswer(invocation -> {
    int index = invocation.getArgument(0);
    return "item-" + index;
});
```

---

## verify 调用验证

**基本写法：验证方法调用**
`verify(<mock>).<方法>(<参数>)`
`verify(<mock>, <times>).<方法>(<参数>)`

```java
# 验证 Mock 方法调用次数与参数
verify(mockList).add("item");
verify(mockList, times(2)).add(anyString());
verify(mockList, never()).clear();
verify(mockList, atLeast(1)).size();
```

---

## 参数匹配器

**基本写法：使用参数匹配器**
`any()` | `anyInt()` | `anyString()` | `eq(<值>)` | `argThat(<断言>)`

```java
# 使用匹配器匹配参数
when(mockList.get(anyInt())).thenReturn("ok");
when(mockMap.get(eq("key"))).thenReturn("value");

verify(mockList).add(argThat(s -> s.length() > 3));
```

---

## ArgumentCaptor 参数捕获

**换行写法：捕获参数进行断言**
`ArgumentCaptor<<类型>> captor = ArgumentCaptor.forClass(<类>.class);`
`verify(<mock>).<方法>(captor.capture());`
`captor.getValue()`

```java
# 捕获方法调用参数
import org.mockito.ArgumentCaptor;

ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
verify(mockList).add(captor.capture());
assertEquals("item", captor.getValue());

# 多次调用的所有参数
List<String> all = captor.getAllValues();
```

---

## spy 间谍对象

**基本写法：创建间谍保留真实实现**
`spy(<对象>)`
`@Spy <类型> <字段> = new <类>();`

```java
# spy 保留真实方法实现，可部分打桩
List<String> realList = new ArrayList<>();
List<String> spyList = spy(realList);

spyList.add("real");
when(spyList.size()).thenReturn(100);
assertEquals(100, spyList.size());
```

---

## doReturn / doThrow

**基本写法：对 spy 使用 doReturn**
`doReturn(<值>).when(<spy>).<方法>()`
`doThrow(<异常>).when(<spy>).<方法>()`

```java
# 对 spy 对象应使用 doReturn 而非 when
List<String> spyList = spy(new ArrayList<>());
doReturn(100).when(spyList).size();
doThrow(new RuntimeException()).when(spyList).clear();
```

---

## verifyNoInteractions

**基本写法：验证无交互**
`verifyNoInteractions(<mock>)`
`verifyNoMoreInteractions(<mock>)`

```java
# 验证 Mock 没有发生交互
verifyNoInteractions(mockList);
verify(mockList).add("a");
verifyNoMoreInteractions(mockList);
```

---

## @InjectMocks 注入

**换行写法：自动注入 Mock 到被测对象**
`@InjectMocks`
`<类型> <字段>;`

```java
# 自动将 @Mock 字段注入到 @InjectMocks 对象
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
    @Mock
    private PaymentGateway gateway;
    @InjectMocks
    private OrderService service;

    @Test
    void testPay() {
        when(gateway.charge(any())).thenReturn(true);
        assertTrue(service.placeOrder());
    }
}
```

---

## timeout 超时验证

**基本写法：验证在超时内调用**
`verify(<mock>, timeout(<毫秒>)).<方法>()`

```java
# 验证方法在指定时间内被调用
verify(mockService, timeout(1000)).process(any());
verify(mockService, timeout(1000).times(2)).process(any());
```

---

## Mockito 静态方法模拟

**换行写法：模拟静态方法**
`try (MockedStatic<<类>> mocked = mockStatic(<类>.class)) {`
`    mocked.when(() -> <类>.<方法>()).thenReturn(<值>);`
`}`

```java
# 模拟静态方法（Mockito 3.4+）
try (MockedStatic<Utility> mocked = mockStatic(Utility.class)) {
    mocked.when(() -> Utility.now()).thenReturn(0L);
    assertEquals(0L, Service.getTime());
}
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
| Mockito 模拟 | 027-Mockito | 本文自身 |
| E2E 端到端测试 | 028-E2ETest | 本文的并列主题 |
| 断言库 | 029-AssertionLibrary | 本文的并列主题 |
