# Java Stream 进阶 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## collect 与 Collectors

**基本写法：收集为 List**
`<stream>.collect(Collectors.toList());`
```java
// 收集为 List（Java 16+ 推荐 toList()）
List<String> list = stream.collect(Collectors.toList());
```

---

**基本写法：直接 toList**
`<stream>.toList();`
```java
// Java 16+，返回不可变 List
List<String> list = stream.toList();
```

---

**基本写法：收集为 Set/Map**
`<stream>.collect(Collectors.toSet());`
```java
// 收集为 Set
Set<String> set = stream.collect(Collectors.toSet());
// 收集为 Map
Map<String, Integer> map = stream.collect(
    Collectors.toMap(s -> s, String::length));
```

---

**基本写法：指定 Map 类型**
`Collectors.toMap(<key>, <value>, <合并>, <Map工厂>);`
```java
// 指定 TreeMap 并处理键冲突
Map<String, Integer> m = stream.collect(Collectors.toMap(
    String::toLowerCase,
    String::length,
    (a, b) -> a,
    TreeMap::new));
```

---

**基本写法：拼接字符串**
`Collectors.joining(<分隔符>);`
```java
// 用分隔符拼接
String r = stream.collect(Collectors.joining(", "));
```

---

## 分组分区

**基本写法：单级分组**
`Collectors.groupingBy(<分类函数>);`
```java
// 按长度分组
Map<Integer, List<String>> byLen =
    stream.collect(Collectors.groupingBy(String::length));
```

---

**基本写法：分组后映射值**
`Collectors.groupingBy(<分类>, <下游收集器>);`
```java
// 按长度分组，每组只取字符串集合
Map<Integer, Set<String>> g = stream.collect(
    Collectors.groupingBy(String::length, Collectors.toSet()));
```

---

**基本写法：分组后计数**
`Collectors.groupingBy(<分类>, Collectors.counting());`
```java
// 按长度分组并计数
Map<Integer, Long> cnt = stream.collect(
    Collectors.groupingBy(String::length, Collectors.counting()));
```

---

**基本写法：分组后求和**
`Collectors.groupingBy(<分类>, Collectors.summingInt(<函数>));`
```java
// 按部门分组求薪资和
Map<String, Integer> sum = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.summingInt(Employee::salary)));
```

---

**基本写法：分组后归约**
`Collectors.groupingBy(<分类>, Collectors.reducing(<归约>));`
```java
// 每组求最大值
Map<String, Optional<Employee>> max = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.maxBy(Comparator.comparingInt(Employee::salary))));
```

---

**基本写法：多级分组**
`Collectors.groupingBy(<分类1>, Collectors.groupingBy(<分类2>));`
```java
// 先按部门再按性别分组
Map<String, Map<String, List<Employee>>> g = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.groupingBy(Employee::gender)));
```

---

**基本写法：分区**
`Collectors.partitioningBy(<谓词>);`
```java
// 按条件分为 true/false 两组
Map<Boolean, List<Integer>> p =
    stream.collect(Collectors.partitioningBy(n -> n > 0));
```

---

## reduce 归约

**基本写法：无初始值归约**
`<stream>.reduce(<BinaryOperator>);`
```java
// 返回 Optional
Optional<Integer> sum = stream.reduce(Integer::sum);
```

---

**基本写法：带初始值归约**
`<stream>.reduce(<初始值>, <BinaryOperator>);`
```java
// 带初始值，直接返回结果
int sum = stream.reduce(0, Integer::sum);
```

---

**基本写法：组合归约**
`<stream>.reduce(<初始值>, <映射>, <合并>);`
```java
// map + reduce，并行友好
int totalLen = stream.reduce(
    0,
    (acc, s) -> acc + s.length(),
    Integer::sum);
```

---

## 数字流统计

**基本写法：IntStream 统计**
`<IntStream>.summaryStatistics();`
```java
// 一次性获取计数、总和、最小、最大、平均
IntSummaryStatistics st = stream.mapToInt(String::length)
    .summaryStatistics();
st.getAverage();
st.getMax();
```

---

**基本写法：求平均值**
`Collectors.averagingInt(<函数>);`
```java
// 按部门求平均薪资
Map<String, Double> avg = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.averagingInt(Employee::salary)));
```

---

## 收集器进阶

**基本写法：mapping 映射后收集**
`Collectors.mapping(<映射>, <下游>);`
```java
// 每组只取姓名列表
Map<String, List<String>> names = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.mapping(Employee::name, Collectors.toList())));
```

---

**基本写法：filtering 过滤后收集**
`Collectors.filtering(<谓词>, <下游>);`
```java
// Java 9+，分组后对组内元素过滤
Map<String, List<Employee>> high = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.filtering(e -> e.salary() > 10000, Collectors.toList())));
```

---

**基本写法：flatMapping 扁平后收集**
`Collectors.flatMapping(<扁平函数>, <下游>);`
```java
// Java 9+，每组收集标签扁平化
Map<String, Set<String>> tags = employees.stream().collect(
    Collectors.groupingBy(Employee::dept,
        Collectors.flatMapping(e -> e.tags().stream(), Collectors.toSet())));
```

---

**基本写法：teeing 合并两个收集器**
`Collectors.teeing(<收集器1>, <收集器2>, <合并>);`
```java
// Java 12+，同时求平均值与计数
String r = stream.collect(Collectors.teeing(
    Collectors.averagingInt(String::length),
    Collectors.counting(),
    (avg, n) -> "avg=" + avg + ",n=" + n));
```

---

## 无序与去重

**基本写法：按属性去重**
`<stream>.filter(<状态Map去重>);`
```java
// 按姓名去重，保留首个
Collection<Employee> dedup = employees.stream().collect(
    Collectors.toMap(Employee::name, e -> e, (a, b) -> a,
        LinkedHashMap::new)).values();
```

---

**基本写法：并行流收集**
`<stream>.parallel().collect(<收集器>);`
```java
// 并行流分组
Map<Integer, List<String>> g = bigList.parallelStream()
    .collect(Collectors.groupingBy(String::length));
```
