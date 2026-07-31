# Java 日期时间 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## LocalDate 本地日期

**基本写法：创建本地日期**
`LocalDate.of(<年>, <月>, <日>);`
```java
// 创建指定日期
LocalDate d = LocalDate.of(2025, 7, 31);
```

---

**基本写法：当前日期**
`LocalDate.now();`
```java
// 获取当前日期
LocalDate today = LocalDate.now();
```

---

**基本写法：解析日期**
`LocalDate.parse("<字符串>");`
```java
// 按默认格式解析
LocalDate d = LocalDate.parse("2025-07-31");
```

---

**基本写法：日期加减**
`<date>.plusDays(<天数>);`
```java
// 加 1 天
LocalDate tmw = today.plusDays(1);
```

---

**基本写法：日期减**
`<date>.minusMonths(<月数>);`
```java
// 减 1 个月
LocalDate last = today.minusMonths(1);
```

---

## LocalTime 本地时间

**基本写法：创建本地时间**
`LocalTime.of(<时>, <分>, <秒>);`
```java
// 创建指定时间
LocalTime t = LocalTime.of(10, 30, 0);
```

---

**基本写法：当前时间**
`LocalTime.now();`
```java
// 获取当前时间
LocalTime now = LocalTime.now();
```

---

## LocalDateTime 日期时间

**基本写法：创建日期时间**
`LocalDateTime.of(<日期>, <时间>);`
```java
// 组合日期和时间
LocalDateTime dt = LocalDateTime.of(LocalDate.now(), LocalTime.now());
```

---

**基本写法：当前日期时间**
`LocalDateTime.now();`
```java
// 获取当前日期时间
LocalDateTime now = LocalDateTime.now();
```

---

**基本写法：解析日期时间**
`LocalDateTime.parse("<字符串>");`
```java
// 解析 ISO 格式
LocalDateTime dt = LocalDateTime.parse("2025-07-31T10:30:00");
```

---

## ZonedDateTime 时区日期时间

**基本写法：指定时区**
`ZonedDateTime.now(ZoneId.of("<时区>"));`
```java
// 获取指定时区的当前时间
ZonedDateTime z = ZonedDateTime.now(ZoneId.of("Asia/Shanghai"));
```

---

**基本写法：转换为另一时区**
`<zonedDateTime>.withZoneSameInstant(ZoneId.of("<时区>"));`
```java
// 同一时刻转换时区
ZonedDateTime utc = z.withZoneSameInstant(ZoneId.of("UTC"));
```

---

## Instant 时间戳

**基本写法：当前 Instant**
`Instant.now();`
```java
// 获取 UTC 时间戳
Instant now = Instant.now();
```

---

**基本写法：从纪元创建**
`Instant.ofEpochSecond(<秒>);`
```java
// 从 Unix 时间戳创建
Instant i = Instant.ofEpochSecond(1700000000);
```

---

**基本写法：获取秒数**
`<instant>.getEpochSecond();`
```java
// 获取 Unix 秒数
long sec = now.getEpochSecond();
```

---

**基本写法：获取毫秒**
`<instant>.toEpochMilli();`
```java
// 获取 Unix 毫秒
long ms = now.toEpochMilli();
```

---

## Duration 时长

**基本写法：创建时长**
`Duration.ofMinutes(<分钟>);`
```java
// 创建 30 分钟时长
Duration d = Duration.ofMinutes(30);
```

---

**基本写法：计算两个时间差**
`Duration.between(<开始>, <结束>);`
```java
// 计算时长
Duration d = Duration.between(t1, t2);
```

---

**基本写法：获取秒数**
`<duration>.toSeconds();`
```java
// 转换为秒
long s = d.toSeconds();
```

---

## Period 日期段

**基本写法：创建日期段**
`Period.of(<年>, <月>, <日>);`
```java
// 创建 1 年 2 月 3 天
Period p = Period.of(1, 2, 3);
```

---

**基本写法：计算日期差**
`Period.between(<开始>, <结束>);`
```java
// 计算两个日期间隔
Period p = Period.between(d1, d2);
```

---

## DateTimeFormatter 格式化

**基本写法：自定义格式**
`DateTimeFormatter.ofPattern("<模式>");`
```java
// 定义格式化模式
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
```

---

**基本写法：格式化输出**
`<datetime>.format(<formatter>);`
```java
// 格式化为字符串
String s = now.format(fmt);
```

---

**基本写法：解析字符串**
`LocalDateTime.parse("<字符串>", <formatter>);`
```java
// 按指定格式解析
LocalDateTime dt = LocalDateTime.parse("2025-07-31 10:30:00", fmt);
```

---

**基本写法：内置格式**
`DateTimeFormatter.ISO_LOCAL_DATE;`
```java
// 使用内置 ISO 格式
String s = today.format(DateTimeFormatter.ISO_LOCAL_DATE);
```

---

## 时区与转换

**基本写法：LocalDateTime 转 Instant**
`<datetime>.atZone(ZoneId.of("<时区>")).toInstant();`
```java
// 本地时间转时间戳
Instant i = dt.atZone(ZoneId.of("Asia/Shanghai")).toInstant();
```

---

**基本写法：Instant 转 LocalDateTime**
`<instant>.atZone(ZoneId.of("<时区>")).toLocalDateTime();`
```java
// 时间戳转本地时间
LocalDateTime dt = i.atZone(ZoneId.of("Asia/Shanghai")).toLocalDateTime();
```

---

## Date 旧 API 转换

**基本写法：Date 转 Instant**
`<date>.toInstant();`
```java
// 旧 Date 转新 API
Instant i = new Date().toInstant();
```

---

**基本写法：Instant 转 Date**
`Date.from(<instant>);`
```java
// 新 API 转旧 Date
Date d = Date.from(Instant.now());
```

---

## ChronoUnit 计算差值

**基本写法：计算天数差**
`ChronoUnit.DAYS.between(<开始>, <结束>);`
```java
// 计算两个日期相差天数
long days = ChronoUnit.DAYS.between(d1, d2);
```

---

**基本写法：计算小时差**
`ChronoUnit.HOURS.between(<开始>, <结束>);`
```java
// 计算两个时间相差小时
long hours = ChronoUnit.HOURS.between(t1, t2);
```

---

## TemporalAdjusters 调整器

**基本写法：获取下周一**
`<date>.with(TemporalAdjusters.next(DayOfWeek.MONDAY));`
```java
// 调整到下一个周一
LocalDate next = today.with(TemporalAdjusters.next(DayOfWeek.MONDAY));
```

---

**基本写法：当月最后一天**
`<date>.with(TemporalAdjusters.lastDayOfMonth());`
```java
// 获取本月最后一天
LocalDate last = today.with(TemporalAdjusters.lastDayOfMonth());
```
