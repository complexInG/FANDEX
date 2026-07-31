# C++20 Ranges 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 视图基础

**基本写法：filter 过滤**
`<range> | std::views::filter(<谓词>);`
```cpp
// 过滤出偶数
auto evens = v | std::views::filter([](int x) { return x % 2 == 0; });
```

---

**基本写法：transform 转换**
`<range> | std::views::transform(<函数>);`
```cpp
// 每个元素乘以 2
auto doubled = v | std::views::transform([](int x) { return x * 2; });
```

---

**基本写法：take 取前 N 个**
`<range> | std::views::take(<数量>);`
```cpp
// 取前 5 个元素
auto first5 = v | std::views::take(5);
```

---

**基本写法：drop 跳过前 N 个**
`<range> | std::views::drop(<数量>);`
```cpp
// 跳过前 3 个元素
auto rest = v | std::views::drop(3);
```

---

**基本写法：reverse 反转**
`<range> | std::views::reverse;`
```cpp
// 反转顺序
auto reversed = v | std::views::reverse;
```

---

## 链式组合

**基本写法：管道操作符组合**
`<range> | std::views::filter(<谓词>) | std::views::transform(<函数>);`
```cpp
// 过滤偶数并乘以 10
auto result = v
    | std::views::filter([](int x) { return x % 2 == 0; })
    | std::views::transform([](int x) { return x * 10; });
```

---

**基本写法：取前 N 个并反转**
`<range> | std::views::take(<数量>) | std::views::reverse;`
```cpp
// 取前 3 个并反转
auto result = v | std::views::take(3) | std::views::reverse;
```

---

## 生成视图

**基本写法：iota 递增序列**
`std::views::iota(<起始> [, <结束>]);`
```cpp
// 生成 0 到 9
auto nums = std::views::iota(0, 10);

// 生成无限序列（配合 take）
auto infinite = std::views::iota(0) | std::views::take(100);
```

---

**基本写法：repeat 重复**
`std::views::repeat(<值> [, <次数>]);`
```cpp
// 重复 5 五次（无限需配合 take）
auto fives = std::views::repeat(5, 3);
```

---

**基本写法：empty 单元素视图**
`std::views::single(<值>);`
```cpp
// 包含单个元素的视图
auto one = std::views::single(42);
```

---

## 元素访问

**基本写法：遍历 range**
`for (auto&& <元素> : <range>) { ... }`
```cpp
// 遍历过滤后的视图
for (int x : v | std::views::filter([](int n) { return n > 0; })) {
    std::cout << x;
}
```

---

## 常用算法

**基本写法：ranges::sort 排序**
`std::ranges::sort(<range> [, <比较器>]);`
```cpp
// 对容器排序
std::ranges::sort(v);
// 降序
std::ranges::sort(v, std::greater<int>());
```

---

**基本写法：ranges::find 查找**
`std::ranges::find(<range>, <值>);`
```cpp
// 查找值为 5 的元素
auto it = std::ranges::find(v, 5);
```

---

**基本写法：ranges::min_element 最小值**
`std::ranges::min_element(<range>);`
```cpp
// 查找最小元素
auto it = std::ranges::min_element(v);
```

---

**基本写法：ranges::count 计数**
`std::ranges::count(<range>, <值>);`
```cpp
// 统计值为 3 的个数
auto n = std::ranges::count(v, 3);
```

---

**基本写法：ranges::transform 转换**
`std::ranges::transform(<range>, <输出迭代器>, <函数>);`
```cpp
// 转换并存入另一容器
std::ranges::transform(v, std::back_inserter(dest), [](int x) { return x * 2; });
```
