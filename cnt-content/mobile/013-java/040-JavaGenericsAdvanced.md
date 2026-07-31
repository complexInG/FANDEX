# Java 泛型进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型方法

**基本写法：定义泛型方法**
`public <类型变量> <返回类型> <方法名>(<参数>) {}`
```java
// 方法级泛型
public static <T> T first(List<T> list) {
    return list.get(0);
}
```

---

**基本写法：多类型变量**
`public <T, U> <返回> <方法>(<参数>) {}`
```java
// 多类型参数泛型方法
public static <T, U> String pair(T t, U u) {
    return t + ":" + u;
}
```

---

## 泛型边界

**基本写法：上界约束**
`<T extends <边界>>`
```java
// 限制 T 必须是 Number 子类
public static <T extends Number> double sum(T t) {
    return t.doubleValue();
}
```

---

**基本写法：多边界**
`<T extends <边界1> & <边界2>>`
```java
// 多个边界，类在前接口在后
public static <T extends Number & Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) > 0 ? a : b;
}
```

---

## 通配符

**基本写法：上界通配符**
`<? extends <类型>>`
```java
// 生产者使用 extends（PECS 原则）
public static void process(List<? extends Number> list) {
    Number n = list.get(0);
}
```

---

**基本写法：下界通配符**
`<? super <类型>>`
```java
// 消费者使用 super（PECS 原则）
public static void addNumbers(List<? super Integer> list) {
    list.add(1);
}
```

---

**基本写法：无界通配符**
`<?>`
```java
// 仅读取不写入场景
public static void print(List<?> list) {
    list.forEach(System.out::println);
}
```

---

## 泛型类与接口

**基本写法：定义泛型类**
`class <类名><<类型变量>> {}`
```java
// 泛型类
public class Box<T> {
    private T value;
    public void set(T v) { this.value = v; }
    public T get() { return value; }
}
```

---

**基本写法：多类型变量泛型类**
`class <类名><<变量1>, <变量2>> {}`
```java
// 双类型变量泛型类
public class Pair<K, V> {
    private K key; private V value;
}
```

---

**基本写法：泛型接口**
`interface <接口名><<类型变量>> {}`
```java
// 泛型接口
public interface Repository<T, ID> {
    T findById(ID id);
}
```

---

## 泛型继承

**基本写法：继承泛型类**
`class <子类> extends <父类><<具体类型>> {}`
```java
// 子类指定具体类型
public class StringBox extends Box<String> {}
```

---

**基本写法：保留类型变量**
`class <子类><<T>> extends <父类><<T>> {}`
```java
// 子类保留类型变量
public class IntBox<T> extends Box<T> {}
```

---

## 类型擦除

**基本写法：运行时获取泛型**
`<class>.getTypeParameters();`
```java
// 运行时只能获取泛型声明
TypeVariable<?>[] vars = Box.class.getTypeParameters();
```

---

**基本写法：获取父类泛型实参**
`<class>.getGenericSuperclass();`
```java
// 通过超类 Token 获取实参类型
Type t = new TypeToken<List<String>>(){}.getClass().getGenericSuperclass();
```

---

## 泛型数组

**基本写法：创建泛型数组**
`(T[]) new Object[<长度>];`
```java
// 通过 Object 数组强转创建
T[] arr = (T[]) new Object[10];
```

---

**基本写法：Array.newInstance 创建**
`Array.newInstance(<类型>, <长度>);`
```java
// 反射创建泛型数组
T[] arr = (T[]) Array.newInstance(clazz, 10);
```

---

## 泛型与可变参数

**基本写法：泛型可变参数**
`public <T> <返回> <方法>(T... <参数>) {}`
```java
// 泛型可变参数（含堆污染警告）
@SafeVarargs
public static <T> List<T> of(T... elements) {
    return List.of(elements);
}
```

---

**基本写法：抑制堆污染警告**
`@SafeVarargs`
```java
// 标记安全可变参数方法
@SafeVarargs
public static <T> void print(T... args) {}
```

---

## 自限定类型

**基本写法：自限定泛型**
`class <类><T extends <类><T>> {}`
```java
// 自限定用于流畅 API
public class Builder<T extends Builder<T>> {
    public T build() { return (T) this; }
}
```

---

## 泛型边界与 lambda

**基本写法：泛型函数式接口**
`interface <接口><<T>> { <返回> <方法>(T t); }`
```java
// 泛型函数式接口
@FunctionalInterface
public interface Mapper<T, R> {
    R map(T t);
}
```

---

## Class<T> 反射泛型

**基本写法：传递 Class<T>**
`public <T> <返回> <方法>(Class<T> <clazz>) {}`
```java
// 通过 Class<T> 保留类型信息
public static <T> T newInstance(Class<T> clazz) throws Exception {
    return clazz.getDeclaredConstructor().newInstance();
}
```

---

## 类型Token 模式

**基本写法：保留泛型类型**
`new TypeToken<<泛型类型>>() {}`
```java
// 通过匿名内部类保留泛型
TypeToken<List<String>> token = new TypeToken<>() {};
Type t = token.getType();
```

---

## PECS 原则总结

**基本写法：生产者 extends 消费者 super**
`List<? extends T> // 读 | List<? super T> // 写`
```java
// 复制元素的经典 PECS 应用
public static <T> void copy(List<? super T> dst, List<? extends T> src) {
    for (T t : src) dst.add(t);
}
```
