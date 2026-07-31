# Java Stream API 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Stream

**基本写法：从集合创建**
`<collection>.stream();`
```java
// 从 List 创建 Stream
Stream<String> stream = list.stream();
```

---

**基本写法：从数组创建**
`Arrays.stream(<数组>);`
```java
// 从数组创建 Stream
IntStream stream = Arrays.stream(new int[]{1, 2, 3});
```

---

**基本写法：使用 Stream.of**
`Stream.of(<元素1>, <元素2>, ...);`
```java
// 创建包含指定元素的 Stream
Stream<String> stream = Stream.of("A", "B", "C");
```

---

**基本写法：使用 Stream.generate**
`Stream.generate(<Supplier>);`
```java
// 生成无限流（需配合 limit 使用）
Stream<Double> randoms = Stream.generate(Math::random).limit(10);
```

---

## 中间操作

**基本写法：过滤**
`<stream>.filter(<Predicate>);`
```java
// 过滤出长度大于 3 的字符串
stream.filter(s -> s.length() > 3);
```

---

**基本写法：映射**
`<stream>.map(<Function>);`
```java
// 将字符串映射为大写
stream.map(String::toUpperCase);
```

---

**基本写法：扁平映射**
`<stream>.flatMap(<Function>);`
```java
// 将嵌套列表扁平化
list.stream().flatMap(sub -> sub.stream());
```

---

**基本写法：去重**
`<stream>.distinct();`
```java
// 去除重复元素
stream.distinct();
```

---

**基本写法：排序**
`<stream>.sorted();`
```java
// 自然顺序排序
stream.sorted();
```

---

**基本写法：自定义排序**
`<stream>.sorted(<Comparator>);`
```java
// 按字符串长度排序
stream.sorted(Comparator.comparingInt(String::length));
```

---

**基本写法：截取前 N 个**
`<stream>.limit(<数量>);`
```java
// 只取前 5 个元素
stream.limit(5);
```

---

**基本写法：跳过前 N 个**
`<stream>.skip(<数量>);`
```java
// 跳过前 2 个元素
stream.skip(2);
```

---

**基本写法：peek 查看元素**
`<stream>.peek(<Consumer>);`
```java
// 流经时执行操作（主要用于调试）
stream.peek(System.out::println);
```

---

## 终止操作

**基本写法：遍历**
`<stream>.forEach(<Consumer>);`
```java
// 遍历每个元素
stream.forEach(System.out::println);
```

---

**基本写法：收集为 List**
`<stream>.collect(Collectors.toList());`
```java
// 收集为 List
List<String> result = stream.collect(Collectors.toList());
```

---

**基本写法：收集为 Map**
`<stream>.collect(Collectors.toMap(<keyMapper>, <valueMapper>));`
```java
// 收集为 Map，以 name 为 key，age 为 value
Map<String, Integer> map = list.stream()
    .collect(Collectors.toMap(User::getName, User::getAge));
```

---

**基本写法：分组**
`<stream>.collect(Collectors.groupingBy(<classifier>));`
```java
// 按年龄分组
Map<Integer, List<User>> grouped = list.stream()
    .collect(Collectors.groupingBy(User::getAge));
```

---

**基本写法：连接字符串**
`<stream>.collect(Collectors.joining(<分隔符>));`
```java
// 用逗号连接所有字符串
String result = stream.collect(Collectors.joining(", "));
```

---

**基本写法：计算数量**
`<stream>.count();`
```java
// 计算元素数量
long count = stream.count();
```

---

**基本写法：查找第一个**
`<stream>.findFirst();`
```java
// 查找第一个元素
Optional<String> first = stream.filter(s -> s.startsWith("A")).findFirst();
```

---

**基本写法：判断任意匹配**
`<stream>.anyMatch(<Predicate>);`
```java
// 判断是否有元素匹配
boolean hasA = stream.anyMatch(s -> s.startsWith("A"));
```

---

**基本写法：判断全部匹配**
`<stream>.allMatch(<Predicate>);`
```java
// 判断是否全部匹配
boolean allLong = stream.allMatch(s -> s.length() > 3);
```

---

**基本写法：归约**
`<stream>.reduce(<初始值>, <BinaryOperator>);`
```java
// 计算元素总和
int sum = stream.reduce(0, Integer::sum);
```

---

**基本写法：求最大值**
`<stream>.max(<Comparator>);`
```java
// 查找最大值
Optional<Integer> max = stream.max(Integer::compareTo);
```

---

## 数值流

**基本写法：转 IntStream**
`<stream>.mapToInt(<ToIntFunction>);`
```java
// 转换为 IntStream
IntStream intStream = list.stream().mapToInt(User::getAge);
```

---

**基本写法：数值统计**
`<intStream>.summaryStatistics();`
```java
// 获取统计信息（总和、平均、最大、最小、数量）
IntSummaryStatistics stats = intStream.summaryStatistics();
```
