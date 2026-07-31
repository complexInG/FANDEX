# Java 密封类 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 声明密封类

**基本写法：密封类**
`sealed class <类名> permits <子类1>, <子类2>;`
```java
// Java 17 正式，限制可继承的子类
public sealed class Shape
    permits Circle, Square, Triangle {}
```

---

**基本写法：密封接口**
`sealed interface <接口名> permits <实现1>, <实现2>;`
```java
// 密封接口，限定实现
public sealed interface Event
    permits Login, Logout, Purchase {}
```

---

**基本写法：同文件省略 permits**
`sealed class <类名> {}`
```java
// 子类在同一文件时，编译器自动推断 permits
public sealed class Shape {}
final class Circle extends Shape {}
final class Square extends Shape {}
```

---

## 子类声明

**基本写法：final 子类**
`final class <子类> extends <密封类> {}`
```java
// final 表示不可再被继承
public final class Circle extends Shape {}
```

---

**基本写法：密封子类**
`sealed class <子类> extends <密封类> permits <孙类>;`
```java
// 子类本身也是密封的
public sealed class Polygon extends Shape
    permits Triangle, Rectangle {}
```

---

**基本写法：非密封子类**
`non-sealed class <子类> extends <密封类> {}`
```java
// non-sealed 打开继承限制
public non-sealed class FreeShape extends Shape {}
```

---

## 与 record 结合

**基本写法：record 实现密封接口**
`record <名称>(<字段>) implements <密封接口>;`
```java
// record 隐式 final，天然适合做密封层级的叶子
public sealed interface Shape permits Circle, Square {}
public record Circle(double r) implements Shape {}
public record Square(double s) implements Shape {}
```

---

**基本写法：代数数据类型**
`sealed interface <名称> permits <记录1>, <记录2>;`
```java
// ADT：用密封接口 + record 表达封闭数据
sealed interface Tree permits Leaf, Node {}
record Leaf(int v) implements Tree {}
record Node(Tree l, Tree r) implements Tree {}
```

---

## 穷举 switch

**基本写法：穷举密封类**
`switch (<密封类变量>) { case <子类1> -> ...; case <子类2> -> ...; }`
```java
// 无需 default，编译器校验穷举
static int area(Shape s) {
    return switch (s) {
        case Circle c -> (int)(Math.PI * c.r() * c.r());
        case Square q -> (int)(q.s() * q.s());
    };
}
```

---

**基本写法：instanceof 穷举**
`if (<变量> instanceof <子类1> <名>) { ... } else if (...)`
```java
// 按层级判断
static String name(Shape s) {
    if (s instanceof Circle c) return "Circle";
    if (s instanceof Square q) return "Square";
    throw new IllegalArgumentException();
}
```

---

## 模块与可见性

**基本写法：跨模块 permits**
`sealed class <类名> permits <全限定子类>;`
```java
// permits 中可用全限定名
public sealed class com.example.Shape
    permits com.example.Circle, com.example.Square {}
```

---

**基本写法：子类与父类同模块**
`module <模块名> { exports <包>; }`
```java
// 密封类与子类必须同一模块
module shapes {
    exports com.example;
}
```

---

## 反射 API

**基本写法：获取 permits 列表**
`<Class>.getPermittedSubclasses();`
```java
// 反射获取允许的子类
Class<?>[] subs = Shape.class.getPermittedSubclasses();
for (Class<?> c : subs) {
    System.out.println(c.getSimpleName());
}
```

---

**基本写法：判断是否密封**
`<Class>.isSealed();`
```java
// 反射判断是否为密封类
if (Shape.class.isSealed()) {
    System.out.println("sealed");
}
```
