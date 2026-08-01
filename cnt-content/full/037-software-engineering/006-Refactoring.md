---
order: 15
title: 代码重构
module: 'software-engineering'
category: 'eng-infra'
difficulty: intermediate
description: 代码重构原则、常用重构手法与代码坏味道识别。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'software-engineering/UML图详解'
  - 'software-engineering/设计模式详解'
  - 'software-engineering/软件测试方法'
  - 'software-engineering/软件度量'
prerequisites: []
---

## 1. 重构原则

### 1.1 什么是重构

重构是在**不改变代码外在行为**的前提下，对代码内部结构进行调整，使其更易理解和修改。

### 1.2 重构时机

| 时机          | 说明                   |
| :------------ | :--------------------- |
| 三次法则      | 第三次做类似的事时重构 |
| 添加功能时    | 先重构使添加更容易     |
| 修复Bug时     | 使代码更易理解         |
| Code Review时 | 团队共同改进           |

### 1.3 重构与测试

```
重构循环:
1. 确保有测试覆盖
2. 小步重构
3. 每步后运行测试
4. 测试通过则继续，失败则回退
```

## 2. 代码坏味道

### 2.1 常见坏味道

| 坏味道       | 症状                       | 重构手法                       |
| :----------- | :------------------------- | :----------------------------- |
| 重复代码     | 相同/相似代码多处出现      | 提取方法、上移方法             |
| 过长方法     | 方法超过20行               | 提取方法、以查询替代临时变量   |
| 过大类       | 类承担过多职责             | 提取类、提取子类               |
| 过长参数列表 | 参数超过4个                | 引入参数对象、保持对象完整     |
| 发散式变化   | 一个类因多种原因变化       | 提取类                         |
| 霰弹式修改   | 一个变化需改多个类         | 移动方法/字段、内联类          |
| 依恋情结     | 方法过度使用其他类数据     | 移动方法、提取方法             |
| 数据泥团     | 多个字段总是一起出现       | 提取类                         |
| 基本类型偏执 | 用基本类型代替小对象       | 引入参数对象、以对象替代数据值 |
| switch语句   | 重复的switch/case          | 以多态替代条件表达式           |
| 临时字段     | 某些字段只在特定情况下使用 | 提取类                         |
| 消息链       | a.b().c().d()              | 隐藏委托、提取方法             |
| 中间人       | 类只是委托给其他类         | 移除中间人、内联方法           |

## 3. 常用重构手法

### 3.1 提取方法

```java
// 重构前
void printOwing() {
    // 打印横幅
    System.out.println("***********");
    System.out.println("** Owing **");
    System.out.println("***********");
    // 计算并打印金额
    double outstanding = 0.0;
    for (Order o : orders) {
        outstanding += o.getAmount();
    }
    System.out.println("name: " + name);
    System.out.println("amount: " + outstanding);
}

// 重构后
void printOwing() {
    printBanner();
    double outstanding = getOutstanding();
    printDetails(outstanding);
}
```

### 3.2 以查询替代临时变量

```java
// 重构前
double getPrice() {
    double basePrice = quantity * itemPrice;
    if (basePrice > 1000) {
        return basePrice * 0.95;
    }
    return basePrice * 0.98;
}

// 重构后
double getPrice() {
    if (basePrice() > 1000) {
        return basePrice() * 0.95;
    }
    return basePrice() * 0.98;
}
double basePrice() { return quantity * itemPrice; }
```

### 3.3 以多态替代条件表达式

```java
// 重构前
double getSpeed() {
    switch (type) {
        case EUROPEAN: return getBaseSpeed();
        case AFRICAN: return getBaseSpeed() - getLoadFactor() * numberOfCoconuts;
        case NORWEGIAN_BLUE: return isNailed ? 0 : getBaseSpeed(voltage);
    }
}

// 重构后
abstract class Bird {
    abstract double getSpeed();
}
class EuropeanBird extends Bird {
    double getSpeed() { return getBaseSpeed(); }
}
class AfricanBird extends Bird {
    double getSpeed() { return getBaseSpeed() - getLoadFactor() * numberOfCoconuts; }
}
```

### 3.4 其他常用手法

| 手法                   | 说明                                  |
| :--------------------- | :------------------------------------ |
| 重命名方法/变量        | 使名称表达意图                        |
| 内联方法               | 方法体比方法名更清晰时                |
| 移动方法               | 将方法移到更合适的类                  |
| 提取接口               | 从类中提取公共接口                    |
| 以工厂方法替代构造函数 | 更灵活的对象创建                      |
| 封装字段               | 将public字段改为private+getter/setter |
| 分解条件表达式         | 提取条件判断为独立方法                |

## 4. 重构安全策略

### 4.1 小步重构

```
每次只做一种重构 → 运行测试 → 确认通过 → 下一步
```

### 4.2 重构检查清单

| 检查项   | 说明               |
| :------- | :----------------- |
| 测试覆盖 | 重构前确保有测试   |
| 行为不变 | 重构不改变外部行为 |
| 版本控制 | 每步重构单独提交   |
| 持续集成 | 每步后CI通过       |
| 代码审查 | 重构后进行Review   |

## 参考文献

IEEE Software 期刊：https://www.computer.org/csdl/magazine/so
Martin Fowler 网站：https://martinfowler.com/
敏捷宣言：https://agilemanifesto.org/iso/zhchs/manifesto.html
12 因素应用：https://12factor.net/zh_cn/

## 延伸阅读

软件架构设计，见 038-software-architecture 模块。
工程实践（Git/CI），见 003-git/031-devops 模块。
测试工程，见 036-software-testing 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供软件工程课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 敏捷落地实践

Scrum：Sprint（1-4 周）、三会议（计划/每日站会/回顾）、三工件（Backlog/Sprint Backlog/增量）。
看板：可视化流程、WIP 限制、流动效率。
用户故事：As a / I want / so that + 验收标准。
常见失败：仪式化、缺乏自组织、需求仍大爆炸。

### 13.2 代码评审最佳实践

评审范围：小 PR（<400 行）、明确描述、自动化前置。
关注点：正确性、可读性、测试、边界、安全。
沟通：提问式评论、代码建议、避免人身化。
机制：必过门禁、多 Reviewer 轮换、评审 SLA。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 软件工程概述 | 001-SoftwareEngineeringOverview | 本文的前置基础 |
| 敏捷开发 | 002-AgileDevelopment | 本文的并列主题 |
| 需求分析方法 | 003-RequirementAnalysisMethod | 本文的并列主题 |
| UML图详解 | 004-UMLGraphDetailed | 本文的并列主题 |
| 设计模式详解 | 005-DesignPatternDetailed | 本文的并列主题 |
| 代码重构 | 006-Refactoring | 本文自身 |
| 软件测试方法 | 007-SoftwareTestMethod | 本文的并列主题 |
| 软件度量 | 008-SoftwareMetrics | 本文的并列主题 |
| 技术债务管理 | 009-TechDebtManagement | 本文的并列主题 |
| DevOps与CICD集成 | 010-DevOpsCICDIntegration | 本文的并列主题 |
