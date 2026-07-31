# C++ 格式化输出

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## std::format 基础

**基本写法：格式化字符串**
`std::format(<格式串>, <参数>...);`
```cpp
// 返回格式化后的字符串
std::string s = std::format("x = {}, y = {}", 1, 2);
```

---

**基本写法：占位符位置**
`std::format("{<索引>}", <参数>...)`
```cpp
// 通过索引指定参数顺序
std::string s = std::format("{1} before {0}", "B", "A");
```

---

## 格式说明

**基本写法：填充与对齐**
`{:[<填充>]<对齐><宽度>}`
```cpp
// 居中对齐宽度 10 填充 *
std::string s = std::format("{:*^10}", "hi");
```

---

**基本写法：整数进制**
`{:<进制>}`
```cpp
// 二进制与十六进制输出
std::string b = std::format("{:b}", 42);
std::string h = std::format("{:x}", 255);
```

---

**基本写法：显示前缀**
`{:<#进制>}`
```cpp
// 显示 0x 0b 前缀
std::string s = std::format("{:#x}", 255);  // 0xff
```

---

**基本写法：浮点精度**
`{:<宽度>.<精度>f}`
```cpp
// 保留两位小数
std::string s = std::format("{:.2f}", 3.14159);
```

---

**基本写法：科学计数法**
`{:<宽度>.<精度>e}`
```cpp
// 科学计数法输出
std::string s = std::format("{:.3e}", 12345.6);
```

---

**基本写法：正负号**
`{:+<格式>}`
```cpp
// 总是显示正负号
std::string s = std::format("{:+}", 42);
```

---

**基本写法：零填充**
`{:0<宽度>}`
```cpp
// 前导零填充
std::string s = std::format("{:05}", 42);  // 00042
```

---

## format_to 输出

**基本写法：输出到迭代器**
`std::format_to(<迭代器>, <格式串>, <参数>...);`
```cpp
// 写入容器避免临时字符串
std::string out;
std::format_to(std::back_inserter(out), "x={}", 1);
```

---

**基本写法：限定输出数量**
`std::format_to_n(<迭代器>, <数量>, <格式串>, <参数>...);`
```cpp
// 限制输出字符数
char buf[16];
auto r = std::format_to_n(buf, 15, "{}", 12345);
*r.out = '\0';
```

---

**基本写法：计算所需大小**
`std::formatted_size(<格式串>, <参数>...);`
```cpp
// 预先获取输出长度
size_t n = std::formatted_size("{}", value);
```

---

## format_to_n 结果

**基本写法：获取结果信息**
`auto <r> = std::format_to_n(...); <r>.out; <r>.size;`
```cpp
// 结果包含输出迭代器与字符数
auto r = std::format_to_n(buf, n, "{}", x);
size_t written = r.size;
```

---

## 自定义类型格式化

**基本写法：特化 formatter**
`template <> struct std::formatter<<类型>> { };`
```cpp
// 为自定义类型支持 format
template <>
struct std::formatter<Point> {
    constexpr auto parse(format_parse_context& ctx) { return ctx.begin(); }
    auto format(const Point& p, format_context& ctx) const {
        return std::format_to(ctx.out(), "({}, {})", p.x, p.y);
    }
};
```

---

**基本写法：使用自定义格式化**
`std::format("{}", <对象>);`
```cpp
// 自定义类型可直接格式化
Point p{1, 2};
std::string s = std::format("{}", p);
```

---

## std::print C++23

**基本写法：打印输出**
`std::print(<格式串>, <参数>...);`
```cpp
// 直接输出到标准输出
std::print("value = {}\n", x);
```

---

**基本写法：自动换行**
`std::println(<格式串>, <参数>...);`
```cpp
// C++23 自动追加换行
std::println("sum = {}", total);
```

---

**基本写法：输出到文件流**
`std::print(<流>, <格式串>, <参数>...);`
```cpp
// 输出到指定流
std::print(std::cerr, "error: {}\n", msg);
```

---

## 常用格式速查

**基本写法：字符与字符串**
`{:s}` 或 `{}`
```cpp
// 字符串直接输出
std::format("name={}, ch={}", "Tom", 'A');
```

---

**基本写法：布尔值**
`{}`
```cpp
// 布尔输出为 0/1 或 true/false
std::format("{}", true);  // 1 或 true
```

---

**基本写法：指针**
`{:p}`
```cpp
// 指针地址输出
std::format("{:p}", (void*)ptr);
```
