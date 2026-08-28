# Java 泛型通配符与边界语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 上界通配符

**基本写法：上界通配符**
`<? extends <类型>>`
```java
// 接受 Number 及其子类型的 List
void sum(List<? extends Number> list) {
    double s = 0;
    for (Number n : list) s += n.doubleValue();
}
```

---

**基本写法：读取上界元素**
`<? extends <类型>> <变量> = <list>.get(0);`
```java
// 可以安全读取为上界类型
Number n = list.get(0);
```

---

## 下界通配符

**基本写法：下界通配符**
`<? super <类型>>`
```java
// 接受 Integer 及其父类型的 List
void addInt(List<? super Integer> list) {
    list.add(42);
}
```

---

**基本写法：写入下界元素**
`<list>.add(<类型值>);`
```java
// 可以安全写入下界类型
list.add(Integer.valueOf(10));
```

---

## PECS 原则

**基本写法：生产者用 extends**
`List<? extends <类型>>`
```java
// 从集合读取数据用 extends
double sum(List<? extends Number> src) {
    return src.stream().mapToDouble(Number::doubleValue).sum();
}
```

---

**基本写法：消费者用 super**
`List<? super <类型>>`
```java
// 向集合写入数据用 super
void fill(List<? super Integer> dst, int n) {
    for (int i = 0; i < n; i++) dst.add(i);
}
```

---

## 无界通配符

**基本写法：无界通配符**
`<?>`
```java
// 接受任何类型但不写入
void printSize(List<?> list) {
    System.out.println(list.size());
}
```

---

## 泛型方法

**基本写法：泛型方法**
`public <T> <返回> <方法>(<参数>) {}`
```java
// 方法级泛型
public static <T> T first(List<T> list) {
    return list.get(0);
}
```

---

**基本写法：带边界的方法泛型**
`public <T extends <边界>> <返回> <方法>(<参数>) {}`
```java
// 限制类型必须实现 Comparable
public static <T extends Comparable<T>> T max(List<T> list) {
    return list.stream().max(Comparable::compareTo).orElse(null);
}
```

---

**基本写法：多边界**
`<T extends <边界1> & <边界2>>`
```java
// 类型必须同时实现多个接口
public static <T extends Number & Comparable<T>> T largest(List<T> list) {
    T max = list.get(0);
    for (T t : list) if (t.compareTo(max) > 0) max = t;
    return max;
}
```

---

## 泛型类

**基本写法：泛型类**
```java
public class <类名><T> { ... }
```
```java
// 简单泛型容器
public class Box<T> {
    private T value;
    public void set(T v) { this.value = v; }
    public T get() { return value; }
}
```

---

**基本写法：带边界泛型类**
```java
public class <类名><T extends <边界>> { ... }
```
```java
// 限定类型参数
public class NumberBox<T extends Number> {
    private T value;
    public double doubleValue() { return value.doubleValue(); }
}
```

---

**基本写法：多类型参数**
```java
public class <类名><K, V> { ... }
```
```java
// 多类型参数泛型类
public class Pair<K, V> {
    private final K key;
    private final V value;
    public Pair(K k, V v) { key = k; value = v; }
}
```

---

## 类型推断

**基本写法：菱形语法**
`new <类名><>()`
```java
// Java 7+ 菱形语法省略类型
Box<String> box = new Box<>();
```

---

**基本写法：方法引用类型推断**
`<类>::<方法>`
```java
// 类型由上下文推断
Function<String, Integer> f = String::length;
```

---
