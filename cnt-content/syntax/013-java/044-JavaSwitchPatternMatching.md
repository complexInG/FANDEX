# Java Switch 模式匹配 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类型模式

**基本写法：instanceof 类型模式**
`if (<变量> instanceof <类型> <变量名>) { ... }`
```java
// Java 16+，类型转换自动绑定变量
Object obj = "hello";
if (obj instanceof String s) {
    System.out.println(s.length());
}
```

---

**基本写法：switch 类型模式**
`case <类型> <变量名> -> <结果>;`
```java
// Java 21 正式，按类型分支
static String format(Object obj) {
    return switch (obj) {
        case Integer i -> "int: " + i;
        case String s  -> "str: " + s;
        case null      -> "null";
        default        -> "other";
    };
}
```

---

## 守卫模式

**基本写法：when 条件守卫**
`case <类型> <变量名> when <条件> -> <结果>;`
```java
// Java 21 正式，在 case 后追加条件
static String classify(Integer i) {
    return switch (i) {
        case Integer v when v > 0  -> "positive";
        case Integer v when v == 0 -> "zero";
        case Integer v             -> "negative";
    };
}
```

---

## null 处理

**基本写法：显式 null 分支**
`case null -> <结果>;`
```java
// Java 21，switch 内直接处理 null
String label = switch (obj) {
    case null      -> "N/A";
    case String s  -> s;
    default        -> obj.toString();
};
```

---

**基本写法：null 合并分支**
`case null, default -> <结果>;`
```java
// null 与 default 合并处理
String label = switch (obj) {
    case String s -> s;
    case null, default -> "fallback";
};
```

---

## 记录模式

**基本写法：解构记录**
`case <记录名>(<组件1>, <组件2>) -> <结果>;`
```java
// Java 21 正式，解构 record 组件
record Point(int x, int y) {}
static int sum(Point p) {
    return switch (p) {
        case Point(int x, int y) -> x + y;
    };
}
```

---

**基本写法：嵌套记录模式**
`case <外层>(<内层>, <值>) -> <结果>;`
```java
// 嵌套解构
record Point(int x, int y) {}
record Line(Point start, Point end) {}
static String desc(Line l) {
    return switch (l) {
        case Line(Point(int x1, int y1), Point(int x2, int y2))
            -> "(" + x1 + "," + y1 + ")->(" + x2 + "," + y2 + ")";
    };
}
```

---

**基本写法：类型 + 守卫结合**
`case <类型> <名> when <条件> -> <结果>;`
```java
// 组合类型模式与守卫
record Point(int x, int y) {}
static String where(Point p) {
    return switch (p) {
        case Point(int x, int y) when x == y -> "diagonal";
        case Point(int x, int y)             -> "other";
    };
}
```

---

## 穷举性与密封类

**基本写法：密封类穷举**
`sealed interface <名称> permits <子类1>, <子类2>`
```java
// 密封层级 + switch 穷举，无需 default
sealed interface Shape permits Circle, Square {}
record Circle(double r) implements Shape {}
record Square(double s) implements Shape {}

static double area(Shape s) {
    return switch (s) {
        case Circle c -> Math.PI * c.r() * c.r();
        case Square q -> q.s() * q.s();
    };
}
```

---

**基本写法：未命名模式变量**
`case <类型> _ -> <结果>;`
```java
// Java 22+，不需要组件值时用 _ 占位
static boolean isCircle(Shape s) {
    return switch (s) {
        case Circle _ -> true;
        case Square _ -> false;
    };
}
```

---

## 表达式与语句

**基本写法：switch 表达式**
`switch (<值>) { case ... -> <结果>; }`
```java
// 返回值，用 -> 箭头
int len = switch (s) {
    case null -> 0;
    case String v -> v.length();
};
```

---

**基本写法：switch 语句带 yield**
`switch (<值>) { case <模式>: yield <值>; }`
```java
// 块语句中用 yield 返回
int len = switch (s) {
    case String v: {
        System.out.println("got string");
        yield v.length();
    }
    case null: yield 0;
};
```

---

## 进阶用法

**基本写法：父类型分支需在前**
`case <子类型> -> ...; case <父类型> -> ...;`
```java
// 子类型分支必须在父类型之前
static String of(Number n) {
    return switch (n) {
        case Integer i -> "int " + i;
        case Double d  -> "dbl " + d;
        case Number x  -> "num " + x;
    };
}
```

---

**基本写法：数组与集合判断**
`case <类型>[] <名> -> ...;`
```java
// 数组类型模式
static String desc(Object o) {
    return switch (o) {
        case int[] arr   -> "int[" + arr.length + "]";
        case String[] arr-> "str[" + arr.length + "]";
        default          -> "other";
    };
}
```
