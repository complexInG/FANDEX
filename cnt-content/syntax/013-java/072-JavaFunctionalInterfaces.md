# Java 函数式接口 Function/Predicate/Consumer/Supplier 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Function 函数

**基本写法：定义 Function**
`Function<<入参类型>, <返回类型>> <变量> = <Lambda>;`
```java
// 接收一个参数返回一个结果
Function<String, Integer> len = s -> s.length();
```

---

**基本写法：应用函数**
`<function>.apply(<参数>);`
```java
// 执行函数并返回结果
int n = len.apply("hello");
```

---

**基本写法：复合函数**
`<f1>.andThen(<f2>);`
```java
// 先执行 f1 再执行 f2
Function<String, String> upper = s -> s.toUpperCase();
Function<String, String> bang = upper.andThen(s -> s + "!");
```

---

**基本写法：反向复合**
`<f2>.compose(<f1>);`
```java
// 先执行 f1 再执行 f2
Function<Integer, Integer> add1 = x -> x + 1;
Function<Integer, Integer> mul2 = x -> x * 2;
Function<Integer, Integer> h = mul2.compose(add1);
```

---

## Predicate 断言

**基本写法：定义 Predicate**
`Predicate<<类型>> <变量> = <Lambda>;`
```java
// 返回 boolean 的判断函数
Predicate<String> nonEmpty = s -> s != null && !s.isEmpty();
```

---

**基本写法：测试断言**
`<predicate>.test(<参数>);`
```java
// 对输入进行判断
boolean ok = nonEmpty.test("abc");
```

---

**基本写法：与运算**
`<p1>.and(<p2>);`
```java
// 两个断言都为真
Predicate<Integer> positive = x -> x > 0;
Predicate<Integer> even = x -> x % 2 == 0;
Predicate<Integer> posEven = positive.and(even);
```

---

**基本写法：取反**
`<predicate>.negate();`
```java
// 取反断言
Predicate<String> isEmpty = nonEmpty.negate();
```

---

## Consumer 消费者

**基本写法：定义 Consumer**
`Consumer<<类型>> <变量> = <Lambda>;`
```java
// 接收一个参数无返回值
Consumer<String> printer = s -> System.out.println(s);
```

---

**基本写法：链式消费**
`<c1>.andThen(<c2>);`
```java
// 先执行 c1 再执行 c2
Consumer<String> c1 = s -> System.out.print("[" + s);
Consumer<String> c2 = s -> System.out.println("]");
Consumer<String> chained = c1.andThen(c2);
```

---

## Supplier 供应者

**基本写法：定义 Supplier**
`Supplier<<类型>> <变量> = <Lambda>;`
```java
// 无参数返回一个结果
Supplier<String> now = () -> java.time.Instant.now().toString();
```

---

**基本写法：获取值**
`<supplier>.get();`
```java
// 执行并返回结果
String v = now.get();
```

---

## BiFunction 双参函数

**基本写法：定义 BiFunction**
`BiFunction<<T>, <U>, <R>> <变量> = <Lambda>;`
```java
// 接收两个参数返回一个结果
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
```

---

## 原始类型特化

**基本写法：IntFunction**
`IntFunction<<R>> <变量> = <Lambda>;`
```java
// 接收 int 返回 R
IntFunction<String> idx = i -> "#" + i;
```

---

**基本写法：IntPredicate**
`IntPredicate <变量> = <Lambda>;`
```java
// 接收 int 返回 boolean
IntPredicate positive = i -> i > 0;
```

---
