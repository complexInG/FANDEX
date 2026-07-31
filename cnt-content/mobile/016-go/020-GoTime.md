# Go time 包 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 当前时间

**基本写法：获取当前时间**
`time.Now() time.Time`
```go
// 返回当前本地时间
now := time.Now()
```

**基本写法：获取当前 Unix 时间戳**
`time.Now().Unix() int64`
```go
// 返回自 1970-01-01 起的秒数
sec := time.Now().Unix()
```

**基本写法：获取纳秒时间戳**
`time.Now().UnixNano() int64`
```go
// 返回纳秒级时间戳，用于高精度计时
nano := time.Now().UnixNano()
```

**基本写法：获取 Unix 毫秒**
`time.Now().UnixMilli() int64`
```go
// 返回毫秒时间戳（Go 1.17+）
ms := time.Now().UnixMilli()
```

---

## 时间创建

**基本写法：构造指定时间**
`time.Date(<年>, <月>, <日>, <时>, <分>, <秒>, <纳秒>, <时区>) time.Time`
```go
// 构造 2024 年 1 月 1 日 0 点 UTC 时间
t := time.Date(2024, time.January, 1, 0, 0, 0, 0, time.UTC)
```

**基本写法：从 Unix 秒创建**
`time.Unix(<秒>, <纳秒>) time.Time`
```go
// 从时间戳还原时间
t := time.Unix(1700000000, 0)
```

**基本写法：解析字符串为时间**
`time.Parse(<布局>, <字符串>) (time.Time, error)`
```go
// 按 RFC3339 布局解析
t, err := time.Parse("2006-01-02 15:04:05", "2024-01-01 12:00:00")
```

**基本写法：按本地时区解析**
`time.ParseInLocation(<布局>, <字符串>, <时区>) (time.Time, error)`
```go
// 按上海时区解析字符串
loc, _ := time.LoadLocation("Asia/Shanghai")
t, _ := time.ParseInLocation("2006-01-02 15:04:05", "2024-01-01 12:00:00", loc)
```

---

## 格式化布局

**基本写法：格式化为字符串**
`<时间>.Format(<布局>) string`
```go
// Go 使用参考时间 2006-01-02 15:04:05 作为布局
s := time.Now().Format("2006-01-02 15:04:05")
```

**基本写法：RFC3339 格式**
`<时间>.Format(time.RFC3339) string`
```go
// 输出 2024-01-01T12:00:00Z 格式
s := time.Now().Format(time.RFC3339)
```

**基本写法：自定义布局**
`<时间>.Format("<布局串>") string`
```go
// 常用占位：年 2006 月 01 日 02 时 15 分 04 秒 05
s := time.Now().Format("2006/01/02 15:04")
```

**基本写法：格式化为 RFC3339Nano**
`<时间>.Format(time.RFC3339Nano) string`
```go
// 带纳秒精度的 ISO 格式
s := time.Now().Format(time.RFC3339Nano)
```

---

## 时间运算

**基本写法：增加时间**
`<时间>.Add(<时长>) time.Time`
```go
// 当前时间加 2 小时
later := time.Now().Add(2 * time.Hour)
```

**基本写法：增加年月日**
`<时间>.AddDate(<年>, <月>, <日>) time.Time`
```go
// 当前时间加 1 年 2 个月 3 天
t := time.Now().AddDate(1, 2, 3)
```

**基本写法：计算时间差**
`<时间>.Sub(<另一时间>) time.Duration`
```go
// 计算两个时间间隔
diff := end.Sub(start)
```

**基本写法：比较时间先后**
`<时间>.Before(<另一时间>) bool`
```go
// 判断 t1 是否早于 t2
if t1.Before(t2) { }
```

**基本写法：比较时间相等**
`<时间>.Equal(<另一时间>) bool`
```go
// 判断两时间是否相等（推荐用 Equal 而非 ==）
if t1.Equal(t2) { }
```

**基本写法：判断之后**
`<时间>.After(<另一时间>) bool`
```go
// 判断 t1 是否晚于 t2
if t1.After(t2) { }
```

---

## 时长 Duration

**基本写法：定义时长**
`<数值> * time.<单位>`
```go
// 常见单位：ns、us、ms、s、m、h
d := 500 * time.Millisecond
```

**基本写法：时长转秒**
`<时长>.Seconds() float64`
```go
// 将时长转为浮点秒
sec := d.Seconds()
```

**基本写法：时长转字符串**
`<时长>.String() string`
```go
// 输出如 500ms、2h30m 的可读形式
s := d.String()
```

**基本写法：解析时长字符串**
`time.ParseDuration(<字符串>) (time.Duration, error)`
```go
// 解析 1h30m 形式时长
d, err := time.ParseDuration("1h30m")
```

---

## 定时器

**基本写法：一次性定时器**
`time.NewTimer(<时长>) *time.Timer`
```go
// 2 秒后触发
timer := time.NewTimer(2 * time.Second)
<-timer.C
```

**基本写法：重置定时器**
`<timer>.Reset(<时长>) bool`
```go
// 重新计时（Go 1.23+ 仅在未停止且未触发时返回 true）
timer.Reset(3 * time.Second)
```

**基本写法：停止定时器**
`<timer>.Stop() bool`
```go
// 停止定时器，返回是否成功停止
timer.Stop()
```

**基本写法：周期触发**
`time.NewTicker(<时长>) *time.Ticker`
```go
// 每 1 秒触发一次
ticker := time.NewTicker(time.Second)
defer ticker.Stop()
for t := range ticker.C {
    fmt.Println(t)
}
```

**基本写法：阻塞等待**
`time.Sleep(<时长>)`
```go
// 暂停当前 goroutine 100 毫秒
time.Sleep(100 * time.Millisecond)
```

**基本写法：After 延迟通道**
`time.After(<时长>) <-chan time.Time`
```go
// 返回到时发送一次的通道
select {
case <-time.After(time.Second):
}
```

---

## 时区

**基本写法：获取时区**
`time.LoadLocation(<名称>) (*time.Location, error)`
```go
// 加载上海时区
loc, err := time.LoadLocation("Asia/Shanghai")
```

**基本写法：UTC 时区**
`time.UTC *time.Location`
```go
// 使用 UTC 时区
t := time.Now().In(time.UTC)
```

**基本写法：转换时区**
`<时间>.In(<时区>) time.Time`
```go
// 将时间转换为指定时区表示
t := time.Now().In(loc)
```

**基本写法：固定偏移时区**
`time.FixedZone(<名称>, <秒偏移>) *time.Location`
```go
// 东八区固定偏移
loc := time.FixedZone("CST", 8*3600)
```

---

## 时间戳与组件

**基本写法：获取年月日**
`<时间>.Date() (<年>, <月>, <日>)`
```go
// 返回年月日三个值
y, m, d := time.Now().Date()
```

**基本写法：获取时分秒**
`<时间>.Clock() (<时>, <分>, <秒>)`
```go
// 返回时分秒三个值
h, mi, s := time.Now().Clock()
```

**基本写法：获取星期几**
`<时间>.Weekday() time.Weekday`
```go
// 返回星期，0 是 Sunday
w := time.Now().Weekday()
```

**基本写法：获取年内天数**
`<时间>.YearDay() int`
```go
// 返回当年第几天（1-366）
day := time.Now().YearDay()
```

---

## 性能计时

**基本写法：高精度计时**
`time.Since(<起始时间>) time.Duration`
```go
// 测量代码执行耗时
start := time.Now()
doWork()
fmt.Println(time.Since(start))
```

**基本写法：单调时钟计时**
`time.Now() time.Time`
```go
// Now 内含单调时钟读数，Sub/Before/After 仅比较单调部分
// 不受系统时间回拨影响
```