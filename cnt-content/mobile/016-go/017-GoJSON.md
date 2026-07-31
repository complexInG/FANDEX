# Go JSON 编解码

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 编码与解码

**基本写法：序列化为 JSON**
`json.Marshal(<值>)`
```go
// 将 Go 数据结构序列化为 JSON
data, err := json.Marshal(map[string]int{"a": 1, "b": 2})
fmt.Println(string(data))
```

**基本写法：带缩进序列化**
`json.MarshalIndent(<值>, <前缀>, <缩进>)`
```go
// 生成格式化的 JSON
data, _ := json.MarshalIndent(user, "", "  ")
fmt.Println(string(data))
```

**基本写法：反序列化 JSON**
`json.Unmarshal(<数据>, &<变量>)`
```go
// 将 JSON 解析为 Go 数据结构
var u User
err := json.Unmarshal([]byte(`{"name":"Go"}`), &u)
```

**基本写法：编码到 Writer**
`json.NewEncoder(<writer>).Encode(<值>)`
```go
// 直接编码输出到 Writer
json.NewEncoder(os.Stdout).Encode(user)
```

**基本写法：从 Reader 解码**
`json.NewDecoder(<reader>).Decode(&<变量>)`
```go
// 从 Reader 直接解码
var u User
json.NewDecoder(strings.NewReader(jsonStr)).Decode(&u)
```

---

## 结构体标签

**基本写法：字段映射标签**
`` `json:"<字段名>"` ``
```go
// 使用标签控制 JSON 字段名
type User struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
}
```

**基本写法：忽略字段**
`` `json:"-"` ``
```go
// 序列化时忽略该字段
type User struct {
    Password string `json:"-"`
    Name     string `json:"name"`
}
```

**基本写法：omitempty 省略空值**
`` `json:"<字段名>,omitempty"` ``
```go
// 字段为零值时不输出
type User struct {
    Name  string `json:"name"`
    Email string `json:"email,omitempty"`
}
```

**基本写法：字符串化字段**
`` `json:"<字段名>,string"` ``
```go
// 将数值序列化为字符串
type Config struct {
    Port int `json:"port,string"`
}
```

---

## 流式处理

**基本写法：流式编码多对象**
`enc := json.NewEncoder(<writer>)`
```go
// 连续编码多个 JSON 对象
enc := json.NewEncoder(os.Stdout)
enc.Encode(obj1)
enc.Encode(obj2)
```

**基本写法：流式解码多对象**
`dec := json.NewDecoder(<reader>)`
```go
// 循环解码多个 JSON 对象
dec := json.NewDecoder(file)
for dec.More() {
    var u User
    dec.Decode(&u)
    fmt.Println(u)
}
```

**基本写法：解码 JSON 数组流**
`dec.Token()`
```go
// 逐个解码数组元素
dec := json.NewDecoder(file)
dec.Token() // 读取开始的 [
for dec.More() {
    var item Item
    dec.Decode(&item)
}
dec.Token() // 读取结束的 ]
```

---

## 动态 JSON

**基本写法：解析到 map**
`var m map[string]interface{}`
```go
// 不确定结构时解析到 map
var m map[string]interface{}
json.Unmarshal(data, &m)
name := m["name"].(string)
```

**基本写法：解析到 interface{}**
`var v interface{}`
```go
// 完全动态解析
var v interface{}
json.Unmarshal(data, &v)
m := v.(map[string]interface{})
```

**基本写法：类型断言访问**
`v.(<类型>)`
```go
// 动态访问 JSON 字段
m := v.(map[string]interface{})
for key, val := range m {
    switch t := val.(type) {
    case string:
        fmt.Println(key, "is string:", t)
    case float64:
        fmt.Println(key, "is number:", t)
    }
}
```

---

## json.RawMessage

**基本写法：延迟解码**
`json.RawMessage`
```go
// 保留原始 JSON 字节，延迟解析
type Envelope struct {
    Type string          `json:"type"`
    Data json.RawMessage `json:"data"`
}
var env Envelope
json.Unmarshal(data, &env)
// 根据 Type 决定如何解析 Data
```

**基本写法：合并 RawMessage**
`json.RawMessage(<字节>)`
```go
// 构造原始 JSON 片段
raw := json.RawMessage(`{"key":"value"}`)
result, _ := json.Marshal(struct {
    Wrap json.RawMessage `json:"wrap"`
}{Wrap: raw})
```

---

## 自定义序列化

**换行写法：实现 MarshalJSON**
`func (<类型>) MarshalJSON() ([]byte, error)`
```go
// 自定义序列化逻辑
type Temperature float64
func (t Temperature) MarshalJSON() ([]byte, error) {
    return json.Marshal(fmt.Sprintf("%.1fC", t))
}
```

**换行写法：实现 UnmarshalJSON**
`func (<接收者>) UnmarshalJSON([]byte) error`
```go
// 自定义反序列化逻辑
func (t *Temperature) UnmarshalJSON(data []byte) error {
    var s string
    if err := json.Unmarshal(data, &s); err != nil {
        return err
    }
    val, _ := strconv.ParseFloat(strings.TrimSuffix(s, "C"), 64)
    *t = Temperature(val)
    return nil
}
```

---

## 错误处理

**基本写法：获取字段错误**
`json.UnmarshalTypeError`
```go
// 捕获类型不匹配错误
var u User
err := json.Unmarshal(data, &u)
if typeErr, ok := err.(*json.UnmarshalTypeError); ok {
    fmt.Printf("字段 %s 类型错误\n", typeErr.Field)
}
```

**基本写法：UnknownFields 检测**
`dec.DisallowUnknownFields()`
```go
// 禁止 JSON 中出现未知字段
dec := json.NewDecoder(r)
dec.DisallowUnknownFields()
var u User
err := dec.Decode(&u)
```

---

## Go 1.24+ JSON 增强

**基本写法：jsontext 严格 JSON 处理**
`import "encoding/json/v2"`
```go
// Go 1.24+ 实验性 JSON v2 API（需启用实验特性）
// 提供更严格的类型系统和更高效的编解码
var js jsonv2.Value
js.Unmarshal(data)
```

**基本写法：json v2 序列化**
`jsonv2.Marshal(<值>)`
```go
// Go 1.24+ 实验性 v2 序列化
// data, err := jsonv2.Marshal(user)
```
