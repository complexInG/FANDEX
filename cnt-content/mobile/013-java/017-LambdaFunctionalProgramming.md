# Java Lambda 与函数式编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Lambda 基础语法

**基本写法：无参数**
`() -> <表达式>`
```java
// 无参数 Lambda
Runnable r = () -> System.out.println("Hello");
```

---

**基本写法：单参数**
`<参数> -> <表达式>`
```java
// 单参数 Lambda
Consumer<String> c = s -> System.out.println(s);
```

---

**基本写法：多参数**
`(<参数1>, <参数2>) -> <表达式>`
```java
// 多参数 Lambda
Comparator<Integer> cmp = (a, b) -> a - b;
```

---

**基本写法：带类型参数**
`(<类型1> <参数1>, <类型2> <参数2>) -> <表达式>`
```java
// 显式声明参数类型
Comparator<Integer> cmp = (Integer a, Integer b) -> a - b;
```

---

**基本写法：代码块**
`(<参数>) -> { <语句1>; <语句2>; return <返回值>; }`
```java
// 多语句代码块
Comparator<Integer> cmp = (a, b) -> {
    System.out.println("comparing");
    return a.compareTo(b);
};
```

---

## 方法引用

**基本写法：静态方法引用**
`<类名>::<静态方法>`
```java
// 引用静态方法
Function<String, Integer> parser = Integer::parseInt;
```

---

**基本写法：实例方法引用（对象）**
`<实例>::<方法>`
```java
// 引用特定对象的实例方法
String str = "Hello";
Supplier<Integer> len = str::length;
```

---

**基本写法：实例方法引用（类）**
`<类名>::<实例方法>`
```java
// 引用任意对象的实例方法
Function<String, String> upper = String::toUpperCase;
```

---

**基本写法：构造方法引用**
`<类名>::new`
```java
// 引用构造方法
Supplier<ArrayList<String>> factory = ArrayList::new;
```

---

**基本写法：数组构造引用**
`<类型>[]::new`
```java
// 创建数组
Function<Integer, String[]> arrayFactory = String[]::new;
```

---

## 函数式接口

**基本写法：Predicate 断言**
`Predicate<<类型>> <变量> = <lambda>;`
```java
// 判断字符串是否为空
Predicate<String> isEmpty = String::isEmpty;
boolean result = isEmpty.test("");
```

---

**基本写法：Consumer 消费者**
`Consumer<<类型>> <变量> = <lambda>;`
```java
// 消费元素
Consumer<String> printer = System.out::println;
printer.accept("Hello");
```

---

**基本写法：Function 函数**
`Function<<输入类型>, <输出类型>> <变量> = <lambda>;`
```java
// 字符串转整数
Function<String, Integer> parser = Integer::parseInt;
Integer num = parser.apply("42");
```

---

**基本写法：Supplier 供应商**
`Supplier<<类型>> <变量> = <lambda>;`
```java
// 生成随机数
Supplier<Double> random = Math::random;
Double value = random.get();
```

---

**基本写法：BiFunction 二元函数**
`BiFunction<<类型1>, <类型2>, <结果类型>> <变量> = <lambda>;`
```java
// 两数相加
BiFunction<Integer, Integer, Integer> adder = (a, b) -> a + b;
Integer sum = adder.apply(1, 2);
```

---

**基本写法：BinaryOperator 二元运算符**
`BinaryOperator<<类型>> <变量> = <lambda>;`
```java
// 求最大值
BinaryOperator<Integer> max = Integer::max;
Integer result = max.apply(3, 5);
```

---

## 默认方法组合

**基本写法：Predicate.and**
`<predicate1>.and(<predicate2>);`
```java
// 组合两个条件
Predicate<String> nonEmpty = s -> !s.isEmpty();
Predicate<String> longEnough = s -> s.length() > 3;
Predicate<String> combined = nonEmpty.and(longEnough);
```

---

**基本写法：Predicate.or**
`<predicate1>.or(<predicate2>);`
```java
// 或条件
Predicate<String> startsA = s -> s.startsWith("A");
Predicate<String> startsB = s -> s.startsWith("B");
Predicate<String> combined = startsA.or(startsB);
```

---

**基本写法：Predicate.negate**
`<predicate>.negate();`
```java
// 取反
Predicate<String> isEmpty = String::isEmpty;
Predicate<String> isNotEmpty = isEmpty.negate();
```

---

**基本写法：Function.andThen**
`<function1>.andThen(<function2>);`
```java
// 先解析再乘以 2
Function<String, Integer> parser = Integer::parseInt;
Function<Integer, Integer> doubler = n -> n * 2;
Function<String, Integer> combined = parser.andThen(doubler);
```

---

**基本写法：Function.compose**
`<function2>.compose(<function1>);`
```java
// 先执行 function1 再执行 function2
Function<String, Integer> combined = doubler.compose(parser);
```
