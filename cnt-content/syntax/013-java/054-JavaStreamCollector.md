# Java Stream Collector 与分组语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Collectors.toList/toSet

**基本写法：收集为 List**
`<stream>.collect(Collectors.toList());`
```java
// 把流收集到 List
List<String> list = stream.collect(Collectors.toList());
```

---

**基本写法：收集为 Set**
`<stream>.collect(Collectors.toSet());`
```java
// 把流收集到 Set 自动去重
Set<String> set = stream.collect(Collectors.toSet());
```

---

**基本写法：收集为指定集合**
`<stream>.collect(Collectors.toCollection(<工厂>));`
```java
// 收集到 LinkedList
LinkedList<String> ll = stream.collect(Collectors.toCollection(LinkedList::new));
```

---

## Collectors.toMap

**基本写法：转 Map**
`<stream>.collect(Collectors.toMap(<键映射>, <值映射>));`
```java
// 把对象流转换为以 id 为键的 Map
Map<Long, User> map = users.stream()
    .collect(Collectors.toMap(User::getId, u -> u));
```

---

**基本写法：处理键冲突**
`<stream>.collect(Collectors.toMap(<键>, <值>, <合并函数>));`
```java
// 遇到重复键时保留新值
Map<String, Integer> m = list.stream()
    .collect(Collectors.toMap(s -> s, String::length, (a, b) -> b));
```

---

## Collectors.joining 拼接

**基本写法：字符串拼接**
`<stream>.collect(Collectors.joining());`
```java
// 直接拼接所有字符串
String s = stream.collect(Collectors.joining());
```

---

**基本写法：带分隔符**
`<stream>.collect(Collectors.joining(<分隔符>));`
```java
// 用逗号分隔拼接
String s = stream.collect(Collectors.joining(", "));
```

---

**基本写法：带前后缀**
`<stream>.collect(Collectors.joining(<分隔符>, <前缀>, <后缀>));`
```java
// 用方括号包裹
String s = stream.collect(Collectors.joining(", ", "[", "]"));
```

---

## Collectors.groupingBy 分组

**基本写法：按属性分组**
`<stream>.collect(Collectors.groupingBy(<分类函数>));`
```java
// 按首字母分组
Map<Character, List<String>> g = list.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0)));
```

---

**基本写法：多级分组**
`<stream>.collect(Collectors.groupingBy(<分类1>, Collectors.groupingBy(<分类2>)));`
```java
// 先按部门再按职级分组
Map<String, Map<String, List<Emp>>> g = emps.stream()
    .collect(Collectors.groupingBy(Emp::getDept,
             Collectors.groupingBy(Emp::getLevel)));
```

---

**基本写法：分组后统计**
`<stream>.collect(Collectors.groupingBy(<分类>, Collectors.counting()));`
```java
// 统计每个分组元素个数
Map<String, Long> count = list.stream()
    .collect(Collectors.groupingBy(s -> s, Collectors.counting()));
```

---

## Collectors.partitioningBy 分区

**基本写法：按条件分区**
`<stream>.collect(Collectors.partitioningBy(<Predicate>));`
```java
// 把流分为 true/false 两组
Map<Boolean, List<Integer>> p = nums.stream()
    .collect(Collectors.partitioningBy(n -> n > 0));
```

---

**基本写法：分区后归约**
`<stream>.collect(Collectors.partitioningBy(<Predicate>, <下游>));`
```java
// 分区后统计每组数量
Map<Boolean, Long> p = nums.stream()
    .collect(Collectors.partitioningBy(n -> n > 0, Collectors.counting()));
```

---

## Collectors.counting/summing

**基本写法：计数**
`<stream>.collect(Collectors.counting());`
```java
// 统计元素个数
long n = stream.collect(Collectors.counting());
```

---

**基本写法：求和**
`<stream>.collect(Collectors.summingInt(<映射>));`
```java
// 对属性求和
int total = users.stream().collect(Collectors.summingInt(User::getAge));
```

---

**基本写法：求平均值**
`<stream>.collect(Collectors.averagingInt(<映射>));`
```java
// 求属性平均值
double avg = users.stream().collect(Collectors.averagingInt(User::getAge));
```

---

## Collectors.summarizing 统计

**基本写法：完整统计**
`<stream>.collect(Collectors.summarizingInt(<映射>));`
```java
// 一次性获取 count/sum/min/avg/max
IntSummaryStatistics stat = users.stream()
    .collect(Collectors.summarizingInt(User::getAge));
```

---

## Collectors.reducing 归约

**基本写法：自定义归约**
`<stream>.collect(Collectors.reducing(<BinaryOperator>));`
```java
// 求最长字符串
Optional<String> max = list.stream()
    .collect(Collectors.reducing((a, b) -> a.length() >= b.length() ? a : b));
```

---

## Collectors.collectingAndThen

**基本写法：收集后转换**
`<stream>.collect(Collectors.collectingAndThen(<下游>, <finisher>));`
```java
// 收集后转不可变集合
List<String> imm = list.stream()
    .collect(Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList));
```

---

## Collectors.teeing 多路收集

**基本写法：双路收集合并**
`<stream>.collect(Collectors.teeing(<下游1>, <下游2>, <合并>));`
```java
// 同时求和与计数
record Stat(int sum, long count) {}
Stat s = nums.stream().collect(Collectors.teeing(
    Collectors.summingInt(n -> n),
    Collectors.counting(),
    Stat::new));
```

---
