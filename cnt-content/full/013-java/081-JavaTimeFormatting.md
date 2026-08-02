---
order: 810
title: Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册
module: 'java'
category: 后端技术
difficulty: beginner
description: Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## DateTimeFormatter 预定义

**基本写法：ISO 格式化**
`DateTimeFormatter.ISO_LOCAL_DATE;`
```java
// 使用预定义 ISO 格式
DateTimeFormatter f = DateTimeFormatter.ISO_LOCAL_DATE;
String s = f.format(LocalDate.now());
```

---

**基本写法：本地化格式**
`DateTimeFormatter.ofLocalizedDate(<FormatStyle>);`
```java
// 本地化日期格式
DateTimeFormatter f = DateTimeFormatter.ofLocalizedDate(FormatStyle.FULL);
String s = f.format(LocalDate.now());
```

---

## 自定义格式

**基本写法：自定义模式**
`DateTimeFormatter.ofPattern(<模式>);`
```java
// 自定义日期时间格式
DateTimeFormatter f = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String s = LocalDateTime.now().format(f);
```

---

**基本写法：带 Locale**
`DateTimeFormatter.ofPattern(<模式>, <Locale>);`
```java
// 指定地区与语言
DateTimeFormatter f = DateTimeFormatter.ofPattern("MMMM dd, yyyy", Locale.US);
String s = LocalDate.now().format(f);
```

---

## 格式化与解析

**基本写法：格式化**
`< temporal >.format(<formatter>);`
```java
// 把日期时间转为字符串
String s = LocalDateTime.now().format(f);
```

---

**基本写法：解析**
`<类型>.parse(<字符串>, <formatter>);`
```java
// 从字符串解析日期
LocalDate d = LocalDate.parse("2025-07-31", DateTimeFormatter.ISO_LOCAL_DATE);
```

---

**基本写法：解析为 LocalDateTime**
`LocalDateTime.parse(<字符串>, <formatter>);`
```java
// 解析为日期时间
LocalDateTime dt = LocalDateTime.parse("2025-07-31 10:15:30",
    DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
```

---

## ZoneId 时区

**基本写法：获取时区**
`ZoneId.of(<时区ID>);`
```java
// 创建时区对象
ZoneId sh = ZoneId.of("Asia/Shanghai");
```

---

**基本写法：系统默认时区**
`ZoneId.systemDefault();`
```java
// 获取系统默认时区
ZoneId z = ZoneId.systemDefault();
```

---

**基本写法：可用时区**
`ZoneId.getAvailableZoneIds();`
```java
// 列出所有可用时区 ID
Set<String> ids = ZoneId.getAvailableZoneIds();
```

---

## ZonedDateTime 带时区时间

**基本写法：创建带时区时间**
`ZonedDateTime.now(<ZoneId>);`
```java
// 获取指定时区的当前时间
ZonedDateTime sh = ZonedDateTime.now(ZoneId.of("Asia/Shanghai"));
```

---

**基本写法：时区转换**
`<zdt>.withZoneSameInstant(<ZoneId>);`
```java
// 把上海时间转换为纽约时间
ZonedDateTime ny = sh.withZoneSameInstant(ZoneId.of("America/New_York"));
```

---

## Instant 时间戳

**基本写法：当前时间戳**
`Instant.now();`
```java
// 获取 UTC 时间戳
Instant now = Instant.now();
```

---

**基本写法：从 epoch 创建**
`Instant.ofEpochSecond(<秒>);`
```java
// 从 Unix 时间戳创建
Instant t = Instant.ofEpochSecond(1700000000);
```

---

**基本写法：转 ZonedDateTime**
`<instant>.atZone(<ZoneId>);`
```java
// 时间戳转指定时区时间
ZonedDateTime sh = Instant.now().atZone(ZoneId.of("Asia/Shanghai"));
```

---

## Duration 与 Period

**基本写法：时间差**
`Duration.between(<起>, <止>);`
```java
// 计算两个时间点之间的时长
Duration d = Duration.between(t1, t2);
long seconds = d.getSeconds();
```

---

**基本写法：日期差**
`Period.between(<起>, <止>);`
```java
// 计算两个日期之间的差
Period p = Period.between(d1, d2);
int years = p.getYears();
```

---

**基本写法：创建 Duration**
`Duration.ofMinutes(<分钟>);`
```java
// 创建时长对象
Duration five = Duration.ofMinutes(5);
```

---

**基本写法：创建 Period**
`Period.ofDays(<天数>);`
```java
// 创建日期段对象
Period week = Period.ofDays(7);
```

---

## TemporalAdjusters 调整器

**基本写法：下周一**
`<date>.with(TemporalAdjusters.next(<DayOfWeek>));`
```java
// 获取下个周一
LocalDate next = LocalDate.now().with(TemporalAdjusters.next(DayOfWeek.MONDAY));
```

---

**基本写法：当月最后一天**
`<date>.with(TemporalAdjusters.lastDayOfMonth());`
```java
// 获取当月最后一天
LocalDate last = LocalDate.now().with(TemporalAdjusters.lastDayOfMonth());
```

---

## 延伸阅读
Java 并发与 JUC，见 013-java 模块并发文档。
JVM 内存与 GC 调优，见 013-java 模块 JVM 文档。
Spring Boot 微服务与 Kubernetes，见 013-java/041-JavaKubernetes 文档。
数据库访问（JDBC/JPA），见 019-sql 模块相关文档。
