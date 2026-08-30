---
order: 50
title: 包装类缓存陷阱救急锦囊
module: 'java'
category: 后端技术
difficulty: beginner
description: Integer 缓存池 -128~127：为什么 100==100 是 true，200==200 是 false。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'java/004-DataTypeConversion'
  - 'java/007-OperatorExpression'
prerequisites:
  - 'java/004-DataTypeConversion'
---

## 一句话定调

**包装类比较内容，只用 `equals()`**。`==` 比较的是引用，而 Java 对部分包装类做了"缓存池"，结果时真时假，不能用来判断数值。

## 极简代码（看懂这 20 行就够了）

```java
Integer a = 100;
Integer b = 100;
System.out.println(a == b);    // true：-128~127 在缓存池内，是同一个对象

Integer c = 200;
Integer d = 200;
System.out.println(c == d);    // false：超出缓存范围，各自 new 了一个对象

System.out.println(c.equals(d)); // true：比较内容，永远正确
```

缓存池范围（自动装箱时生效）：

| 类型 | 缓存范围 |
| --- | --- |
| `Boolean` | `true` / `false` |
| `Byte` | 全部（-128~127） |
| `Short` / `Integer` / `Long` | -128~127 |
| `Character` | 0~127 |
| `Float` / `Double` | 无缓存 |

## 如果报这个错，看这里

**现象：两个 `Integer` 明明相等，`==` 却是 false（或项目里偶发 true/false 不一致）**

原因：数值超出缓存池后 `==` 比较的是对象引用。

对策：包装类一律用 `equals()` 比较；需要比较大小用 `compareTo()`。遇到 `List<Integer>.contains()`、`Set` 去重等场景，集合内部已经正确使用 `equals`，不用自己担心。

**现象：`int` 与 `Integer` 比较时偶尔出现 `NullPointerException`**

原因：`Integer` 为 null 时自动拆箱（`null.intValue()`）直接抛 NPE。

对策：拆箱前先判空，或使用 `Optional` 与 `Objects.equals` 规避。

## 记住

> 包装类比较内容，只用 `equals()`；判空后再拆箱，别让 null 偷偷触发 NPE。
