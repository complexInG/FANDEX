# Kotlin 时间 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Duration 时长

**基本写法：创建时长**
`<数字>.<单位>()`
```kotlin
// 不同单位创建 Duration
val d1 = 5.seconds
val d2 = 100.milliseconds
val d3 = 2.hours
```

---

**基本写法：字面量时长**
`<数字>.<单位>`
```kotlin
// Duration 字面量扩展属性
val d = 30.minutes
```

---

**基本写法：时长运算**
`<时长> + <时长> | <时长> * <倍数>`
```kotlin
// 时长加减乘除
val sum = 1.hours + 30.minutes
val half = 1.hours / 2
```

---

**基本写法：转换为单位**
`<duration>.inWholeSeconds | inWholeMilliseconds`
```kotlin
// 转换为整型单位
val s = (1.5.hours).inWholeSeconds
val ms = (1.minutes).inWholeMilliseconds
```

---

**基本写法：比较时长**
`<d1> > <d2> | <d>.compareTo(<d2>)`
```kotlin
// 比较时长大小
if (d1 > d2) { }
```

---

## TimeMark 与测量

**基本写法：获取时间标记**
`TimeSource.Monotonic.markNow()`
```kotlin
// 获取单调时钟标记
val mark = TimeSource.Monotonic.markNow()
```

---

**基本写法：测量经过时长**
`<mark>.elapsedNow()`
```kotlin
// 测量自标记以来的时长
val dur = mark.elapsedNow()
```

---

**基本写法：measureTime 测量代码**
`measureTime { <代码> }`
```kotlin
// 测量代码块耗时
val t = measureTime { doWork() }
println(t)
```

---

**基本写法：测量并返回结果**
`measureTimedValue { <代码> }`
```kotlin
// 同时返回结果与耗时
val (result, time) = measureTimedValue { compute() }
```

---

## kotlinx-datetime 跨平台

**基本写法：获取当前时刻**
`Clock.System.now()`
```kotlin
// 获取当前 Instant
val now = Clock.System.now()
```

---

**基本写法：当前本地日期**
`Clock.System.todayIn(<时区>)`
```kotlin
// 获取指定时区当前日期
val today = Clock.System.todayIn(TimeZone.currentSystemDefault())
```

---

**基本写法：创建 LocalDate**
`LocalDate(<年>, <月>, <日>)`
```kotlin
// 创建指定日期
val d = LocalDate(2025, 7, 31)
```

---

**基本写法：创建 LocalDateTime**
`LocalDateTime(<日期>, <时间>)`
```kotlin
// 创建本地日期时间
val dt = LocalDateTime(LocalDate(2025,7,31), LocalTime(10,30))
```

---

**基本写法：解析日期**
`LocalDate.parse("<字符串>")`
```kotlin
// 解析 ISO 日期字符串
val d = LocalDate.parse("2025-07-31")
```

---

## Instant 操作

**基本写法：加时长**
`<instant>.plus(<duration>)`
```kotlin
// Instant 加时长
val later = now.plus(1.hours)
```

---

**基本写法：计算差值**
`<i1>.minus(<i2>)`
```kotlin
// 两个 Instant 的时长差
val dur = i1.minus(i2)
```

---

**基本写法：转换为时区**
`<instant>.toLocalDateTime(<时区>)`
```kotlin
// 转为指定时区本地时间
val ldt = now.toLocalDateTime(TimeZone.of("Asia/Shanghai"))
```

---

## Instant 与 epoch

**基本写法：从 epoch 秒创建**
`Instant.fromEpochSeconds(<秒>)`
```kotlin
// Unix 秒转 Instant
val i = Instant.fromEpochSeconds(1700000000)
```

---

**基本写法：获取 epoch 秒**
`<instant>.epochSeconds`
```kotlin
// 获取 Unix 秒数
val s = now.epochSeconds
```

---

## DateTimePeriod 日期段

**基本写法：创建日期段**
`DateTimePeriod(years = <年>, months = <月>)`
```kotlin
// 创建年月日时段
val p = DateTimePeriod(years = 1, months = 2)
```

---

**基本写法：加日期段**
`<localDate>.plus(<period>, <时区>)`
```kotlin
// 日期加日期段
val next = d.plus(p, TimeZone.UTC)
```

---

## TimeZone 时区

**基本写法：系统默认时区**
`TimeZone.currentSystemDefault()`
```kotlin
// 获取系统默认时区
val tz = TimeZone.currentSystemDefault()
```

---

**基本写法：指定时区**
`TimeZone.of("<时区ID>")`
```kotlin
// 按名称获取时区
val tz = TimeZone.of("Asia/Shanghai")
```

---

**基本写法：UTC 时区**
`TimeZone.UTC`
```kotlin
// 直接引用 UTC 时区
val utc = TimeZone.UTC
```

---

## 格式化与解析

**基本写法：自定义格式化**
`LocalDate.Format { <配置> }`
```kotlin
// 自定义日期格式
val fmt = LocalDate.Format {
    year(); chars("-"); monthNumber(); chars("-"); dayOfMonth()
}
```

---

**基本写法：按格式解析**
`LocalDate.parse("<字符串>", <format>)`
```kotlin
// 按自定义格式解析
val d = LocalDate.parse("2025/07/31", fmt)
```

---

## DayOfWeek 与 Month

**基本写法：获取星期**
`<localDate>.dayOfWeek`
```kotlin
// 获取星期枚举值
val dow = d.dayOfWeek
```

---

**基本写法：获取月份**
`<localDate>.month`
```kotlin
// 获取月份枚举值
val m = d.month
```

---

## 协程中的延迟

**基本写法：Duration 延迟**
`delay(<duration>)`
```kotlin
// 协程中使用 Duration 延迟
delay(500.milliseconds)
```

---

## 日期比较

**基本写法：判断前/后**
`<d1> < <d2> | <d1>.until(<d2>)`
```kotlin
// 日期前后判断
if (d1 < d2) { }
val until = d1.until(d2)
```
