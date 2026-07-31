# Java Stream reduce 与并行流语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## reduce 归约

**基本写法：无初始值归约**
`<stream>.reduce(<BinaryOperator>);`
```java
// 求最大值，返回 Optional
Optional<Integer> max = nums.stream().reduce(Integer::max);
```

---

**基本写法：带初始值归约**
`<stream>.reduce(<初始值>, <BinaryOperator>);`
```java
// 求和，初始值为 0
int sum = nums.stream().reduce(0, Integer::sum);
```

---

**基本写法：三参归约**
`<stream>.reduce(<初始值>, <累加器>, <组合器>);`
```java
// 并行归约，组合器用于合并子结果
int sum = users.parallelStream().reduce(
    0,
    (acc, u) -> acc + u.getAge(),
    Integer::sum);
```

---

**基本写法：字符串拼接**
`<stream>.reduce(<初始值>, <拼接函数>);`
```java
// 把字符串流拼接成单个字符串
String r = list.stream().reduce("", (a, s) -> a + s);
```

---

## 并行流

**基本写法：创建并行流**
`<collection>.parallelStream();`
```java
// 从集合创建并行流
Stream<String> ps = list.parallelStream();
```

---

**基本写法：流转并行**
`<stream>.parallel();`
```java
// 把顺序流转为并行流
Stream<String> ps = list.stream().parallel();
```

---

**基本写法：转回顺序流**
`<stream>.sequential();`
```java
// 把并行流转回顺序流
Stream<String> ss = ps.sequential();
```

---

**基本写法：判断是否并行**
`<stream>.isParallel();`
```java
// 查询流是否并行
boolean p = stream.isParallel();
```

---

**基本写法：无序流**
`<stream>.unordered();`
```java
// 标记为无序以便并行优化
Stream<Integer> u = nums.stream().unordered();
```

---

## 并行流注意事项

**基本写法：避免共享可变状态**
```java
// 错误：共享 ArrayList 会有并发问题
List<String> bad = Collections.synchronizedList(new ArrayList<>());
nums.parallelStream().forEach(bad::add); // 不推荐

// 正确：使用 collect 收集
List<String> good = nums.parallelStream()
    .map(Object::toString)
    .collect(Collectors.toList());
```

---

## Stream.generate 生成

**基本写法：无限流**
`Stream.generate(<Supplier>);`
```java
// 生成随机数无限流
Stream<Double> randoms = Stream.generate(Math::random);
```

---

## Stream.iterate 迭代

**基本写法：迭代生成**
`Stream.iterate(<种子>, <UnaryOperator>);`
```java
// 生成 0,1,2,... 无限流
Stream<Integer> nat = Stream.iterate(0, n -> n + 1);
```

---

**基本写法：带终止条件**
`Stream.iterate(<种子>, <Predicate>, <UnaryOperator>);`
```java
// 生成 0 到 9 的流
Stream<Integer> ten = Stream.iterate(0, n -> n < 10, n -> n + 1);
```

---

## Stream 排序与去重

**基本写法：排序**
`<stream>.sorted();`
```java
// 自然顺序排序
Stream<String> s = list.stream().sorted();
```

---

**基本写法：自定义排序**
`<stream>.sorted(<Comparator>);`
```java
// 按长度排序
Stream<String> s = list.stream().sorted(Comparator.comparingInt(String::length));
```

---

**基本写法：去重**
`<stream>.distinct();`
```java
// 去除重复元素
Stream<Integer> d = nums.stream().distinct();
```

---

## IntStream 数值流

**基本写法：范围流**
`IntStream.range(<起>, <止>);`
```java
// 生成 [0, 10) 的整数流
IntStream r = IntStream.range(0, 10);
```

---

**基本写法：闭合范围**
`IntStream.rangeClosed(<起>, <止>);`
```java
// 生成 [0, 10] 的整数流
IntStream r = IntStream.rangeClosed(0, 10);
```

---
