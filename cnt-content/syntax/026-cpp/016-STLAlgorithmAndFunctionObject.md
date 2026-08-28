# C++ STL 算法与函数对象速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 非修改算法

**基本写法：for_each 遍历**
`std::for_each(<首迭代器>, <尾迭代器>, <函数>);`
```cpp
// 遍历输出每个元素
std::for_each(v.begin(), v.end(), [](int x) { std::cout << x; });
```

---

**基本写法：find 查找**
`std::find(<首迭代器>, <尾迭代器>, <值>);`
```cpp
// 查找值为 5 的元素
auto it = std::find(v.begin(), v.end(), 5);
```

---

**基本写法：find_if 条件查找**
`std::find_if(<首迭代器>, <尾迭代器>, <谓词>);`
```cpp
// 查找第一个大于 10 的元素
auto it = std::find_if(v.begin(), v.end(), [](int x) { return x > 10; });
```

---

**基本写法：count 计数**
`std::count(<首迭代器>, <尾迭代器>, <值>);`
```cpp
// 统计值为 3 的元素个数
auto n = std::count(v.begin(), v.end(), 3);
```

---

## 修改算法

**基本写法：transform 转换**
`std::transform(<首迭代器>, <尾迭代器>, <输出迭代器>, <函数>);`
```cpp
// 将每个元素乘以 2
std::transform(v.begin(), v.end(), v.begin(), [](int x) { return x * 2; });
```

---

**基本写法：copy 复制**
`std::copy(<首迭代器>, <尾迭代器>, <输出迭代器>);`
```cpp
// 复制到另一容器
std::copy(v.begin(), v.end(), std::back_inserter(dest));
```

---

**基本写法：remove_if 移除**
`std::remove_if(<首迭代器>, <尾迭代器>, <谓词>);`
```cpp
// 移除所有偶数（需配合 erase）
v.erase(std::remove_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; }), v.end());
```

---

**基本写法：replace 替换**
`std::replace(<首迭代器>, <尾迭代器>, <旧值>, <新值>);`
```cpp
// 将所有 0 替换为 -1
std::replace(v.begin(), v.end(), 0, -1);
```

---

**基本写法：fill 填充**
`std::fill(<首迭代器>, <尾迭代器>, <值>);`
```cpp
// 填充所有元素为 0
std::fill(v.begin(), v.end(), 0);
```

---

## 排序与分区

**基本写法：sort 排序**
`std::sort(<首迭代器>, <尾迭代器>);`
```cpp
// 默认升序排序
std::sort(v.begin(), v.end());
```

---

**基本写法：自定义排序**
`std::sort(<首迭代器>, <尾迭代器>, <比较器>);`
```cpp
// 降序排序
std::sort(v.begin(), v.end(), std::greater<int>());
```

---

**基本写法：stable_sort 稳定排序**
`std::stable_sort(<首迭代器>, <尾迭代器>);`
```cpp
// 保持相等元素的相对顺序
std::stable_sort(v.begin(), v.end());
```

---

**基本写法：partial_sort 部分排序**
`std::partial_sort(<首迭代器>, <中间迭代器>, <尾迭代器>);`
```cpp
// 前 10 个最小元素有序排列
std::partial_sort(v.begin(), v.begin() + 10, v.end());
```

---

**基本写法：nth_element 第 N 大**
`std::nth_element(<首迭代器>, <第n迭代器>, <尾迭代器>);`
```cpp
// 找第 5 小的元素
std::nth_element(v.begin(), v.begin() + 4, v.end());
```

---

## 二分查找

**基本写法：lower_bound 下界**
`std::lower_bound(<首迭代器>, <尾迭代器>, <值>);`
```cpp
// 查找第一个不小于 5 的位置
auto it = std::lower_bound(v.begin(), v.end(), 5);
```

---

**基本写法：upper_bound 上界**
`std::upper_bound(<首迭代器>, <尾迭代器>, <值>);`
```cpp
// 查找第一个大于 5 的位置
auto it = std::upper_bound(v.begin(), v.end(), 5);
```

---

**基本写法：binary_search 二分查找**
`std::binary_search(<首迭代器>, <尾迭代器>, <值>);`
```cpp
// 判断元素是否存在
bool found = std::binary_search(v.begin(), v.end(), 5);
```

---

## 数值算法

**基本写法：accumulate 累加**
`std::accumulate(<首迭代器>, <尾迭代器>, <初始值>);`
```cpp
// 求和
int sum = std::accumulate(v.begin(), v.end(), 0);
```

---

**基本写法：inner_product 内积**
`std::inner_product(<首1>, <尾1>, <首2>, <初始值>);`
```cpp
// 计算两向量内积
int product = std::inner_product(v1.begin(), v1.end(), v2.begin(), 0);
```

---

**基本写法：partial_sum 前缀和**
`std::partial_sum(<首迭代器>, <尾迭代器>, <输出迭代器>);`
```cpp
// 计算前缀和
std::partial_sum(v.begin(), v.end(), result.begin());
```

---

## 函数对象

**基本写法：std::plus 加法**
`std::plus<<类型>>()`
```cpp
// 加法函数对象
auto add = std::plus<int>();
int result = add(3, 5);
```

---

**基本写法：std::less 小于**
`std::less<<类型>>()`
```cpp
// 小于比较函数对象
auto cmp = std::less<int>();
bool result = cmp(3, 5);
```

---

**基本写法：std::greater 大于**
`std::greater<<类型>>()`
```cpp
// 用于降序排序
std::sort(v.begin(), v.end(), std::greater<int>());
```
