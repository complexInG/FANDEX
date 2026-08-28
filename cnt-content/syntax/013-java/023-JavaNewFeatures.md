# Java 17-21 新特性速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## record 记录类（Java 14 预览 / 16 正式）

**基本写法：定义不可变数据类**
`record <名称>(<字段列表>)`
```java
// 自动生成构造、getter、equals、hashCode、toString
public record Point(int x, int y) { }
Point p = new Point(1, 2);
int x = p.x();
```

---

**基本写法：紧凑构造器**
`public <名称> { <校验> }`
```java
// 用于参数校验
public record Age(int value) {
    public Age {
        if (value < 0) throw new IllegalArgumentException();
    }
}
```

---

**基本写法：自定义构造**
`public <名称>(<参数>) { this(<参数>); }`
```java
// 委托给规范构造器
public record User(String name, int age) {
    public User(String name) {
        this(name, 0);
    }
}
```

---

**基本写法：实现接口**
`record <名称>(<字段>) implements <接口>`
```java
// record 可实现接口但不可继承类
public record Point(int x, int y) implements Comparable<Point> {
    @Override
    public int compareTo(Point o) {
        return Integer.compare(x, o.x);
    }
}
```

---

## sealed 密封类（Java 17 正式）

**基本写法：声明密封类**
`sealed class <名称> permits <子类1>, <子类2>`
```java
// 限制可继承的子类
public sealed class Shape permits Circle, Square, Triangle { }
```

---

**基本写法：密封接口**
`sealed interface <名称> permits <实现1>, <实现2>`
```java
// 限制接口的实现
public sealed interface Shape permits Circle, Square { }
```

---

**基本写法：子类声明**
`final class <名称> extends <密封类>`
```java
// 子类必须为 final、sealed 或 non-sealed
final class Circle extends Shape { }
non-sealed class Square extends Shape { }
```

---

## pattern matching 模式匹配

**基本写法：instanceof 模式匹配（Java 16）**
`if (<对象> instanceof <类型> <变量>)`
```java
// 自动绑定变量，无需强转
if (obj instanceof String s) {
    System.out.println(s.length());
}
```

---

**基本写法：switch 模式匹配（Java 21 正式）**
`switch (<对象>) { case <类型> <变量> -> ... }`
```java
// 类型模式匹配
static String format(Object obj) {
    return switch (obj) {
        case Integer i -> String.format("int %d", i);
        case Long l    -> String.format("long %d", l);
        case Double d  -> String.format("double %f", d);
        case String s  -> String.format("String %s", s);
        case null      -> "null";
        default        -> obj.toString();
    };
}
```

---

**基本写法：带守卫条件**
`case <类型> <变量> when <条件>`
```java
// 模式匹配加额外条件
switch (shape) {
    case Circle c when c.radius() > 100 -> "big circle";
    case Circle c                        -> "small circle";
    case Square s                        -> "square";
}
```

---

**基本写法：record 解构模式（Java 21 预览）**
`case <Record类型>(<字段1>, <字段2>)`
```java
// 直接解构 record 字段
static int sum(Point p) {
    return switch (p) {
        case Point(int x, int y) -> x + y;
    };
}
```

---

## 文本块（Java 15 正式）

**基本写法：多行字符串**
`"""<内容>"""`
```java
// 三引号定义多行字符串，保留格式
String json = """
    {
        "name": "Alice",
        "age": 30
    }
    """;
```

---

**基本写法：保留前导空格**
`"""<内容>\s"""`
```java
// \s 表示保留尾部空格
String text = """
    line1   \s
    line2   \s
    """;
```

---

## switch 表达式（Java 14 正式）

**基本写法：switch 作为表达式**
`var <变量> = switch (<值>) { case <分支> -> <结果>; }`
```java
// 直接返回值，无 fall-through
int days = switch (month) {
    case 1, 3, 5, 7, 8, 10, 12 -> 31;
    case 4, 6, 9, 11 -> 30;
    case 2 -> isLeap ? 29 : 28;
    default -> throw new IllegalArgumentException();
};
```

---

**基本写法：yield 返回值**
`case <分支> -> { yield <值>; }`
```java
// 代码块中用 yield 返回
int days = switch (month) {
    case 2 -> {
        if (isLeap) yield 29;
        else yield 28;
    }
    default -> 30;
};
```

---

## var 局部变量类型推断（Java 10）

**基本写法：var 声明**
`var <变量> = <值>`
```java
// 编译期推断类型，仅限局部变量
var list = new ArrayList<String>();
var stream = list.stream();
```

---

## Enhanced instanceof（Java 16）

**基本写法：模式变量作用域**
`if (<对象> instanceof <类型> <变量> && <变量>.<方法>())`
```java
// 变量在后续条件中可用
if (obj instanceof String s && s.length() > 3) {
    System.out.println(s.toUpperCase());
}
```

---

## Helpful NullPointerException（Java 14）

**基本写法：详细空指针定位**
`-XX:+ShowCodeDetailsInExceptionMessages`
```java
// JVM 自动提示哪个变量为 null
// 输出：Cannot invoke "String.length()" because "name" is null
int len = person.name.length();
```

---

## Stream 增强

**基本写法：toList 直接收集（Java 16）**
`<stream>.toList()`
```java
// 简化 collect(Collectors.toList())
List<String> result = stream.map(String::toUpperCase).toList();
```

---

**基本写法：mapMulti 一对多（Java 16）**
`<stream>.mapMulti(<BiConsumer>)`
```java
// 一个元素展开为多个元素
stream.mapMulti((Integer n, Consumer<Integer> downstream) -> {
    for (int i = 0; i < n; i++) downstream.accept(i);
});
```

---

## String 增强

**基本写法：重复字符串（Java 11）**
`<string>.repeat(<次数>)`
```java
// 字符串重复 N 次
String sep = "-".repeat(10);
```

---

**基本写法：判断空白（Java 11）**
`<string>.isBlank()`
```java
// 仅含空白字符则为 true
boolean blank = "   ".isBlank();
```

---

**基本写法：按行分割（Java 11）**
`<string>.lines()`
```java
// 返回按行分割的 Stream
Stream<String> lines = "a\nb\nc".lines();
```

---

**基本写法：strip 去空白（Java 11）**
`<string>.strip()`
```java
// 去除首尾 Unicode 空白（优于 trim）
String s = " hello ".strip();
```

---

**基本写法：模板预览（Java 21 预览）**
`STR."<模板>"`
```java
// 字符串模板（预览特性，需 --enable-preview）
String name = "Alice";
String msg = STR."Hello, \{name}!";
```

---

## 接口增强

**基本写法：私有方法（Java 9）**
`private <返回值> <方法>()`
```java
// 接口中的私有方法，复用 default 方法逻辑
interface MyInterface {
    default int compute() { return base() * 2; }
    private int base() { return 10; }
}
```

---

## 集合工厂方法（Java 9）

**基本写法：不可变 List**
`List.of(<元素>...)`
```java
// 创建不可变 List
List<String> list = List.of("a", "b", "c");
```

---

**基本写法：不可变 Map**
`Map.of(<k1>, <v1>, <k2>, <v2>)`
```java
// 创建不可变 Map
Map<String, Integer> map = Map.of("a", 1, "b", 2);
```

---

**基本写法：超过 10 对的 Map**
`Map.ofEntries(Map.entry(<k>, <v>)...)`
```java
// 大量键值对的不可变 Map
Map<String, Integer> map = Map.ofEntries(
    Map.entry("a", 1),
    Map.entry("b", 2)
);
```

---

## Stream toList 注意事项（Java 16）

**基本写法：toList 返回不可变 List**
`<stream>.toList()`
```java
// 结果不可变，与 Collectors.toList() 行为不同
List<String> list = stream.toList();
list.add("x"); // 抛出 UnsupportedOperationException
```

---

## 紧凑数字格式（Java 12）

**基本写法：紧凑数字**
`NumberFormat.getCompactNumberInstance()`
```java
// 1000 -> 1K
NumberFormat fmt = NumberFormat.getCompactNumberInstance(Locale.US, NumberFormat.Style.SHORT);
String s = fmt.format(1000);
```
