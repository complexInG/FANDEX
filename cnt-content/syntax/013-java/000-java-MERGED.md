---
order: 10
title: java 模块文档合集
module: 'java'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：013-java/001-VariableConstant.md ============ -->

# Java 变量与常量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量声明

**基本写法：声明变量**
`<类型> <变量名>;`
```java
// 声明一个整型变量
int age;
```

---

**基本写法：变量赋值**
`<变量名> = <值>;`
```java
// 给已声明的变量赋值
age = 18;
```

---

**基本写法：声明并初始化**
`<类型> <变量名> = <值>;`
```java
// 声明并初始化整型变量
int age = 18;
```

---

**单行写法：多变量声明**
`<类型> <变量名1>, <变量名2> = <值>, <变量名3>;`
```java
// 一次声明多个相同类型的变量
int x, y = 5, z;
```

---

## 局部变量

**基本写法：局部变量声明**
`<类型> <变量名> = <值>;`
```java
// 在方法内部声明局部变量
public void method() {
    int localVariable = 10;
}
```

---

**基本写法：代码块内局部变量**
`<类型> <变量名> = <值>;`
```java
// 在 if 块内声明局部变量
if (condition) {
    int ifVariable = 20;
}
```

---

## 成员变量

**基本写法：成员变量声明**
`<修饰符> <类型> <变量名>;`
```java
// 在类中定义成员变量
public class Person {
    private String name;
}
```

---

**换行写法：多成员变量声明**
`<修饰符> <类型> <变量名1>; <修饰符> <类型> <变量名2>;`
```java
// 在类中定义多个成员变量
public class Person {
    private String name;
    private int age;
    private boolean isAdult;
}
```

---

## 静态变量

**基本写法：静态变量声明**
`public static <类型> <变量名> = <值>;`
```java
// 定义静态变量
public class Counter {
    public static int count = 0;
}
```

---

**基本写法：访问静态变量**
`<类名>.<静态变量>`
```java
// 通过类名访问静态变量
int currentCount = Counter.count;
```

---

## final 常量

**基本写法：类级别 final 常量**
`public static final <类型> <常量名> = <值>;`
```java
// 定义不可修改的静态常量
public static final double PI = 3.1415926535;
```

---

**基本写法：实例级别 final 常量**
`public final <类型> <常量名>;`
```java
// 定义在构造方法中初始化的常量
public class Student {
    public final int ID;
}
```

---

**基本写法：局部 final 常量**
`final <类型> <常量名> = <值>;`
```java
// 在方法内定义不可变变量
public void method() {
    final int LOCAL_CONSTANT = 100;
}
```

---

## 枚举常量

**单行写法：枚举定义**
`public enum <枚举名> { <常量1>, <常量2> }`
```java
// 单行定义枚举
public enum Day { MONDAY, TUESDAY, WEDNESDAY }
```

---

**换行写法：枚举定义**
`public enum <枚举名> { <常量1>, <常量2>, ... }`
```java
// 换行定义枚举
public enum Day {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
}
```

---

**基本写法：使用枚举常量**
`<枚举名>.<常量名>`
```java
// 引用枚举常量
Day today = Day.MONDAY;
```

---

## var 类型推断

**基本写法：var 声明基本类型**
`var <变量名> = <值>;`
```java
// 使用 var 推断整型
var count = 10;
```

---

**基本写法：var 声明字符串**
`var <变量名> = "<字符串>";`
```java
// 使用 var 推断字符串类型
var name = "Java";
```

---

**基本写法：var 声明集合**
`var <变量名> = new <集合类><>();`
```java
// 使用 var 推断集合类型
var list = new ArrayList<String>();
```

---

**基本写法：var 声明数组**
`var <变量名> = new <类型>[]{ <元素> };`
```java
// 使用 var 推断数组类型
var numbers = new int[]{1, 2, 3};
```



<!-- ============ 文档分隔线：013-java/002-ProgramStructureBasicSyntax.md ============ -->

# Java 程序结构与基本语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 源文件结构

**基本写法：包声明**
`package <包名>;`
```java
// 声明源文件所属的包
package com.example;
```

---

**基本写法：导入单个类**
`import <全限定类名>;`
```java
// 导入需要使用的类
import java.util.Scanner;
```

---

**基本写法：导入整个包**
`import <包名>.*;`
```java
// 导入整个包下的所有类
import java.util.*;
```

---

**基本写法：类定义**
`<修饰符> class <类名> { }`
```java
// 定义一个公开类
public class HelloWorld {
}
```

---

**单行写法：简单类定义**
`<修饰符> class <类名> { }`
```java
// 单行定义一个空类
public class Empty { }
```

---

**换行写法：完整类定义**
`<修饰符> class <类名> extends <父类> implements <接口> { <成员变量> <构造方法> <成员方法> }`
```java
// 定义带继承与接口实现的完整类
public class Student extends Person implements Serializable {
    private String studentId;
    private String major;
}
```

---

## 主方法

**基本写法：主方法定义**
`public static void main(String[] args) { }`
```java
// 定义程序入口方法
public static void main(String[] args) {
}
```

---

**基本写法：主方法输出**
`public static void main(String[] args) { System.out.println(<内容>); }`
```java
// 在主方法中输出字符串
public static void main(String[] args) {
    System.out.println("Hello, World!");
}
```

---

**基本写法：读取命令行参数**
`<参数>[<索引>]`
```java
// 读取第一个命令行参数
public static void main(String[] args) {
    String firstArg = args[0];
}
```

---

## 注释规范

**基本写法：单行注释**
`// <注释内容>`
```java
// 这是一个单行注释
int age = 18;
```

---

**基本写法：多行注释**
`/* <注释内容> */`
```java
/* 这是一个多行注释 */
int sum = 0;
```

---

**换行写法：多行注释**
`/* <注释内容> */`
```java
/*
 * 这是一个多行注释
 * 可以跨越多行
 */
int sum = 0;
```

---

**基本写法：文档注释**
`/** <注释内容> */`
```java
/** 计算两个数的和 */
public int add(int a, int b) {
    return a + b;
}
```

---

**换行写法：文档注释带标签**
`/** <描述> @param <参数名> <说明> @return <说明> */`
```java
/**
 * 计算两个数的和
 * @param a 第一个加数
 * @param b 第二个加数
 * @return 两个数的和
 */
public int add(int a, int b) {
    return a + b;
}
```

---

## 标识符命名规范

**基本写法：类名命名**
`<UpperCamelCase>`
```java
// 类名使用大驼峰命名法
HelloWorld
```

---

**基本写法：方法名命名**
`<lowerCamelCase>`
```java
// 方法名使用小驼峰命名法
getUserName
```

---

**基本写法：变量名命名**
`<lowerCamelCase>`
```java
// 变量名使用小驼峰命名法
ageCount
```

---

**基本写法：包名命名**
`<全小写.分隔>`
```java
// 包名全小写使用点分隔
com.example.util
```

---

**基本写法：常量名命名**
`<UPPER_SNAKE_CASE>`
```java
// 常量名全大写使用下划线分隔
MAX_VALUE
```

---

## 键盘录入

**基本写法：创建 Scanner 对象**
`Scanner <变量名> = new Scanner(System.in);`
```java
// 创建用于读取控制台输入的 Scanner 对象
Scanner sc = new Scanner(System.in);
```

---

**基本写法：读取整数**
`<Scanner对象>.nextInt();`
```java
// 读取用户输入的整数
int num = sc.nextInt();
```

---

**基本写法：读取浮点数**
`<Scanner对象>.nextDouble();`
```java
// 读取用户输入的浮点数
double d = sc.nextDouble();
```

---

**基本写法：读取布尔值**
`<Scanner对象>.nextBoolean();`
```java
// 读取用户输入的布尔值
boolean b = sc.nextBoolean();
```

---

**基本写法：读取一个单词**
`<Scanner对象>.next();`
```java
// 读取一个单词遇到空格停止
String str = sc.next();
```

---

**基本写法：读取整行**
`<Scanner对象>.nextLine();`
```java
// 读取整行输入
String line = sc.nextLine();
```

---

**基本写法：关闭 Scanner**
`<Scanner对象>.close();`
```java
// 关闭 Scanner 释放资源
sc.close();
```

---

## 代码风格

**基本写法：K&R 风格左大括号**
`if (<条件>) { }`
```java
// 左大括号放在行尾
if (condition) {
}
```

---

**基本写法：try-with-resources**
`try (<资源声明>) { }`
```java
// 自动关闭资源的 try 语句
try (Scanner sc = new Scanner(System.in)) {
}
```

---

## Java 25+ 新特性

**基本写法：Java 21+ record 记录类**
`public record <名称>(<字段>) { }`
```java
// 定义不可变的数据载体记录类
public record Point(int x, int y) { }
```

---

**基本写法：Java 21+ sealed 密封类**
`public sealed class <名称> permits <子类> { }`
```java
// 限制可继承的子类范围
public sealed class Shape permits Circle, Square, Triangle { }
```

---

**基本写法：Java 21+ 模式匹配 switch**
`switch (<obj>) { case <类型> <变量> -> <语句>; }`
```java
// 使用类型模式匹配的 switch 表达式
String result = switch (obj) {
    case Integer i -> "整数: " + i;
    case String s -> "字符串: " + s;
    default -> "未知类型";
};
```

---

**基本写法：Java 21+ 文本块**
`"""<多行文本>"""`
```java
// 使用三引号定义多行字符串
String json = """
        {
            "name": "Tom",
            "age": 18
        }
        """;
```

---

**基本写法：Java 25+ 严格浮点（默认恢复 strictfp 行为）**
`<修饰符> class <类名> { }`
```java
// Java 25 起默认采用严格浮点语义，无需显式声明 strictfp
public class Calculator {
    public double compute() {
        return 0.1 + 0.2;  // 在所有平台上结果一致
    }
}
```

---

**基本写法：Java 25+ scoped values**
`ScopedValue.where(<name>, <value>).run(() -> { })`
```java
// 使用 ScopedValue 在线程作用域内共享不可变值
private static final ScopedValue<String> USER_ID = ScopedValue.newInstance();
ScopedValue.where(USER_ID, "user123").run(() -> {
    System.out.println(USER_ID.get());
});
```

---

**基本写法：Java 25+ structured concurrency**
`try (var scope = new StructuredTaskScope.ShutdownOnFailure()) { }`
```java
// 使用结构化并发管理多个子任务的生命周期
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    var task1 = scope.fork(() -> fetchUser());
    var task2 = scope.fork(() -> fetchOrders());
    scope.join().throwIfFailed();
    var user = task1.get();
    var orders = task2.get();
}
```

---

**基本写法：Java 25+ virtual threads**
`Thread.ofVirtual().start(() -> { })`
```java
// 启动虚拟线程执行轻量级并发任务
Thread vThread = Thread.ofVirtual().start(() -> {
    System.out.println("运行在虚拟线程: " + Thread.currentThread());
});
```

---

**基本写法：Java 25+ module info 模块声明**
`module <模块名> { exports <包>; requires <模块>; }`
```java
// 在 module-info.java 中声明模块依赖关系
module com.example.app {
    exports com.example.app.api;
    requires java.sql;
    requires transitive java.base;
}
```



<!-- ============ 文档分隔线：013-java/003-AbstractClassInterface.md ============ -->

# Java 抽象类与接口

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 抽象类

**基本写法：抽象类定义**
`abstract class <类名> { }`
```java
// 定义抽象类
public abstract class Shape {
}
```

---

**基本写法：抽象方法**
`abstract <返回类型> <方法名>(<参数>);`
```java
// 定义抽象方法无方法体
public abstract double calculateArea();
```

---

**基本写法：抽象类继承**
`<修饰符> class <子类> extends <抽象类> { }`
```java
// 子类继承抽象类并实现抽象方法
public class Circle extends Shape {
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}
```

---

**基本写法：抽象类构造方法**
`protected <类名>(<参数>) { }`
```java
// 抽象类中定义受保护的构造方法
protected Shape(String name) {
    this.name = name;
}
```

---

**基本写法：抽象类包含具体方法**
`<修饰符> <返回类型> <方法名>(<参数>) { }`
```java
// 抽象类中定义具体方法
public String getName() {
    return name;
}
```

---

## 接口定义

**基本写法：接口定义**
`interface <接口名> { }`
```java
// 定义接口
public interface Drawable {
}
```

---

**基本写法：接口常量**
`<类型> <常量名> = <值>;`
```java
// 接口中定义常量默认 public static final
int MAX_SIZE = 100;
```

---

**基本写法：抽象方法**
`<返回类型> <方法名>(<参数>);`
```java
// 接口中定义抽象方法
void draw();
```

---

**基本写法：默认方法**
`default <返回类型> <方法名>(<参数>) { }`
```java
// 接口中定义默认方法带实现
default void printInfo() {
    System.out.println("Drawable");
}
```

---

**基本写法：静态方法**
`static <返回类型> <方法名>(<参数>) { }`
```java
// 接口中定义静态方法
static Drawable createDefault() {
    return new Circle();
}
```

---

**基本写法：私有方法**
`private <返回类型> <方法名>(<参数>) { }`
```java
// 接口中定义私有方法 Java 9+
private void validateInput(int value) {
}
```

---

## 接口实现

**基本写法：实现单个接口**
`<修饰符> class <类名> implements <接口> { }`
```java
// 类实现单个接口
public class Circle implements Drawable {
    @Override
    public void draw() {
    }
}
```

---

**单行写法：实现多个接口**
`<修饰符> class <类名> implements <接口1>, <接口2> { }`
```java
// 类实现多个接口
public class Circle implements Drawable, Comparable {
}
```

---

**换行写法：实现多个接口**
`<修饰符> class <类名> implements <接口1>, <接口2>, <接口3> { }`
```java
// 换行书写实现多个接口
public class Circle implements Drawable,
        Comparable,
        Serializable {
}
```

---

## 接口继承

**基本写法：接口继承单个接口**
`interface <子接口> extends <父接口> { }`
```java
// 接口继承单个父接口
public interface AdvancedDrawable extends Drawable {
}
```

---

**单行写法：接口继承多个接口**
`interface <子接口> extends <父接口1>, <父接口2> { }`
```java
// 接口继承多个父接口
public interface AdvancedList extends List, RandomAccess {
}
```

---

**换行写法：接口继承多个接口**
`interface <子接口> extends <父接口1>, <父接口2>, <父接口3> { }`
```java
// 换行书写接口继承多个父接口
public interface AdvancedList extends List,
        RandomAccess,
        Cloneable {
}
```

---

## 函数式接口

**基本写法：函数式接口定义**
`@FunctionalInterface interface <接口名> { <单抽象方法> }`
```java
// 定义函数式接口
@FunctionalInterface
public interface Calculator {
    int calculate(int a, int b);
}
```

---

**基本写法：Lambda 实现**
`(<参数>) -> <表达式>`
```java
// 使用 Lambda 实现函数式接口
Calculator add = (a, b) -> a + b;
```

---

**基本写法：方法引用实现**
`<类名>::<方法名>`
```java
// 使用方法引用实现函数式接口
Calculator add = Integer::sum;
```

---

## 抽象类与接口结合

**基本写法：抽象类实现接口**
`abstract class <类名> implements <接口> { }`
```java
// 抽象类实现接口可部分实现
public abstract class AbstractShape implements Drawable {
    @Override
    public void draw() {
    }
}
```

---

**基本写法：抽象类实现部分接口**
`abstract class <类名> implements <接口> { <具体方法> <抽象方法> }`
```java
// 抽象类实现部分接口方法
public abstract class AbstractShape implements Drawable {
    @Override
    public void draw() {
    }

    public abstract double calculateArea();
}
```

---

## 默认方法冲突解决

**基本写法：重写冲突的默认方法**
`<修饰符> <返回类型> <方法名>(<参数>) { <接口>.super.<方法>(); }`
```java
// 解决多个接口默认方法冲突
public class MyClass implements InterfaceA, InterfaceB {
    @Override
    public void method() {
        InterfaceA.super.method();
    }
}
```



<!-- ============ 文档分隔线：013-java/004-GenericDetailed.md ============ -->

# Java 泛型详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型类

**基本写法：泛型类定义**
`class <类名><T> { }`
```java
// 定义单类型参数的泛型类
public class Box<T> {
    private T item;
}
```

---

**换行写法：多类型参数泛型类**
`class <类名><T1, T2, T3> { }`
```java
// 定义多类型参数的泛型类
public class Pair<K, V> {
    private K key;
    private V value;
}
```

---

**基本写法：使用泛型类**
`<类名><<类型>> <变量> = new <类名><>();`
```java
// 使用泛型类指定具体类型
Box<String> box = new Box<>();
```

---

**基本写法：泛型类方法**
`public <返回类型> <方法名>(T <参数>) { }`
```java
// 泛型类中使用类型参数的方法
public void setItem(T item) {
    this.item = item;
}
```

---

**基本写法：泛型类返回类型**
`public T <方法名>() { }`
```java
// 方法返回类型为类型参数
public T getItem() {
    return item;
}
```

---

## 泛型接口

**基本写法：泛型接口定义**
`interface <接口名><T> { }`
```java
// 定义泛型接口
public interface Repository<T> {
}
```

---

**基本写法：实现泛型接口指定类型**
`class <类名> implements <接口><<具体类型>> { }`
```java
// 实现泛型接口并指定具体类型
public class UserRepository implements Repository<User> {
}
```

---

**基本写法：实现泛型接口保留泛型**
`class <类名><T> implements <接口><T> { }`
```java
// 实现泛型接口保留泛型参数
public class GenericRepository<T> implements Repository<T> {
}
```

---

## 泛型方法

**基本写法：泛型方法定义**
`public <T> <返回类型> <方法名>(T <参数>) { }`
```java
// 定义泛型方法
public <T> void printItem(T item) {
}
```

---

**基本写法：泛型方法有返回值**
`public <T> T <方法名>(T <参数>) { }`
```java
// 泛型方法返回类型参数
public <T> T process(T input) {
    return input;
}
```

---

**换行写法：多类型参数泛型方法**
`public <T, U> <返回类型> <方法名>(T <参数1>, U <参数2>) { }`
```java
// 泛型方法接受多个类型参数
public <T, U> String combine(T first, U second) {
    return first.toString() + second.toString();
}
```

---

**基本写法：静态泛型方法**
`public static <T> <返回类型> <方法名>(T <参数>) { }`
```java
// 定义静态泛型方法
public static <T> T getFirst(List<T> list) {
    return list.get(0);
}
```

---

## 类型通配符

**基本写法：无界通配符**
`<?>`
```java
// 接受任意类型的泛型
List<?> list = new ArrayList<String>();
```

---

**基本写法：上界通配符**
`<? extends <类型>>`
```java
// 接受指定类型及其子类
List<? extends Number> list = new ArrayList<Integer>();
```

---

**基本写法：下界通配符**
`<? super <类型>>`
```java
// 接受指定类型及其父类
List<? super Integer> list = new ArrayList<Number>();
```

---

## 类型约束

**基本写法：泛型上界约束**
`<T extends <类型>>`
```java
// 限制类型参数必须是指定类型或子类
public class NumberBox<T extends Number> {
}
```

---

**换行写法：多边界约束**
`<T extends <类型1> & <接口2>>`
```java
// 类型参数必须同时满足多个边界
public class Container<T extends Number & Comparable<T>> {
}
```

---

**基本写法：泛型方法上界约束**
`public <T extends <类型>> <方法名>(T <参数>)`
```java
// 泛型方法限制类型上界
public <T extends Number> double sum(T num) {
    return num.doubleValue();
}
```

---

## 类型擦除

**基本写法：运行时类型检查**
`<对象> instanceof <原始类型>`
```java
// 泛型在运行时被擦除只能检查原始类型
List<String> list = new ArrayList<>();
boolean isList = list instanceof List;
```

---

**基本写法：无法实例化类型参数**
`new T()`
```java
// 泛型类型参数无法直接实例化编译错误
// T item = new T();
```

---

**基本写法：无法创建泛型数组**
`new T[<长度>]`
```java
// 无法创建泛型类型数组编译错误
// T[] array = new T[10];
```

---

## 泛型集合

**基本写法：泛型 List**
`List<<类型>> <变量> = new ArrayList<>();`
```java
// 创建泛型 List
List<String> names = new ArrayList<>();
```

---

**基本写法：泛型 Map**
`Map<<键类型>, <值类型>> <变量> = new HashMap<>();`
```java
// 创建泛型 Map
Map<String, Integer> ages = new HashMap<>();
```

---

**基本写法：泛型 Set**
`Set<<类型>> <变量> = new HashSet<>();`
```java
// 创建泛型 Set
Set<Integer> numbers = new HashSet<>();
```

---

## PECS 原则

**基本写法：生产者使用 extends**
`List<? extends <类型>> <变量>`
```java
// 从集合读取数据使用上界通配符
List<? extends Number> producer = new ArrayList<Integer>();
Number n = producer.get(0);
```

---

**基本写法：消费者使用 super**
`List<? super <类型>> <变量>`
```java
// 向集合写入数据使用下界通配符
List<? super Integer> consumer = new ArrayList<Number>();
consumer.add(1);
```

---

## 泛型工具方法

**基本写法：泛型数组创建**
`@SuppressWarnings("unchecked") T[] <变量> = (T[]) new Object[<长度>];`
```java
// 通过 Object 数组创建泛型数组
@SuppressWarnings("unchecked")
T[] array = (T[]) new Object[10];
```

---

**基本写法：泛型类型转换**
`(<类型>) <对象>`
```java
// 泛型类型转换需要强制
Object obj = "Hello";
String str = (String) obj;
```

---

**基本写法：Class 类型参数**
`Class<<类型>> <变量> = <类型>.class;`
```java
// 获取泛型 Class 对象
Class<String> clazz = String.class;
```

---

**基本写法：泛型方法实例化**
`<类型>.newInstance()`
```java
// 通过 Class 创建实例
T instance = clazz.newInstance();
```



<!-- ============ 文档分隔线：013-java/005-MethodDetailed.md ============ -->

# Java 方法详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 方法定义

**基本写法：有返回值方法**
`<修饰符> <返回值类型> <方法名>(<参数列表>) { return <返回值>; }`
```java
// 定义返回 int 的方法
public int add(int a, int b) {
    return a + b;
}
```

---

**基本写法：无返回值方法**
`<修饰符> void <方法名>(<参数列表>) { }`
```java
// 定义无返回值的方法
public void printMessage(String message) {
}
```

---

## 方法调用

**基本写法：非静态方法调用**
`<对象>.<方法名>(<参数>);`
```java
// 通过对象实例调用方法
MyClass obj = new MyClass();
int result = obj.add(1, 2);
```

---

**基本写法：静态方法调用**
`<类名>.<方法名>(<参数>);`
```java
// 通过类名直接调用静态方法
int result = Math.abs(-10);
```

---

## 参数传递

**基本写法：基本类型参数**
`<方法名>(<基本类型> <参数名>)`
```java
// 传递基本类型的副本
public void modify(int x) {
    x = 10;
}
```

---

**基本写法：引用类型参数**
`<方法名>(<引用类型>[] <参数名>)`
```java
// 传递引用地址的副本
public void modifyArray(int[] arr) {
    arr[0] = 100;
}
```

---

## 方法重载

**基本写法：参数数量不同重载**
`<修饰符> <返回类型> <方法名>(<参数列表1>) { }`
```java
// 同名方法参数数量不同
public int add(int a, int b) {
    return a + b;
}
```

---

**基本写法：参数类型不同重载**
`<修饰符> <返回类型> <方法名>(<参数类型2>) { }`
```java
// 同名方法参数类型不同
public double add(double a, double b) {
    return a + b;
}
```

---

## 递归

**基本写法：递归结构**
`<返回类型> <方法名>(<参数>) { if (<基准条件>) return <基准值>; return <方法名>(<修改参数>); }`
```java
// 递归方法基本结构
public int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

---

**基本写法：斐波那契递归**
`<返回类型> fibonacci(<参数>)`
```java
// 斐波那契数列递归实现
public int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

---

**基本写法：二分查找递归**
`<返回类型> binarySearch(<参数>)`
```java
// 二分查找递归实现
public int binarySearch(int[] arr, int target, int low, int high) {
    if (low > high) return -1;
    int mid = (low + high) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] > target) {
        return binarySearch(arr, target, low, mid - 1);
    }
    return binarySearch(arr, target, mid + 1, high);
}
```

---

## 可变参数

**基本写法：可变参数定义**
`<修饰符> <返回类型> <方法名>(<参数类型>... <参数名>) { }`
```java
// 接受任意数量的参数
public int sum(int... numbers) {
    int total = 0;
    for (int num : numbers) {
        total += num;
    }
    return total;
}
```

---

**基本写法：可变参数调用**
`<方法名>(<元素1>, <元素2>, ...)`
```java
// 传入多个参数调用可变参数方法
int result = sum(1, 2, 3, 4, 5);
```

---

## 静态泛型方法

**基本写法：静态泛型方法**
`public static <T> void <方法名>(T <参数>) { }`
```java
// 定义静态泛型方法
public static <T> void staticGenericMethod(T value) {
}
```

---

**基本写法：泛型方法类型推断**
`public <T> T <方法名>(List<T> <参数>)`
```java
// 编译器自动推断类型
public <T> T getFirstElement(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
}
```



<!-- ============ 文档分隔线：013-java/006-CollectionFrameworkDetailed.md ============ -->

# Java 集合框架详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ArrayList

**基本写法：创建 ArrayList**
`List<<类型>> <变量> = new ArrayList<>();`
```java
// 创建字符串 ArrayList
List<String> list = new ArrayList<>();
```

---

**基本写法：添加元素**
`<list>.add(<元素>);`
```java
// 向列表末尾添加元素
list.add("Apple");
```

---

**基本写法：指定位置添加**
`<list>.add(<索引>, <元素>);`
```java
// 在指定位置插入元素
list.add(0, "Banana");
```

---

**基本写法：获取元素**
`<list>.get(<索引>);`
```java
// 获取指定位置的元素
String item = list.get(0);
```

---

**基本写法：修改元素**
`<list>.set(<索引>, <元素>);`
```java
// 替换指定位置的元素
list.set(0, "Cherry");
```

---

**基本写法：删除元素**
`<list>.remove(<索引>);`
```java
// 删除指定位置的元素
list.remove(0);
```

---

**基本写法：获取大小**
`<list>.size();`
```java
// 获取列表元素个数
int size = list.size();
```

---

**基本写法：判断包含**
`<list>.contains(<元素>);`
```java
// 判断列表是否包含元素
boolean has = list.contains("Apple");
```

---

**基本写法：清空列表**
`<list>.clear();`
```java
// 清空列表所有元素
list.clear();
```

---

**基本写法：遍历 ArrayList**
`for (<类型> <变量> : <list>) { }`
```java
// 增强 for 循环遍历
for (String item : list) {
}
```

---

## LinkedList

**基本写法：创建 LinkedList**
`LinkedList<<类型>> <变量> = new LinkedList<>();`
```java
// 创建 LinkedList
LinkedList<String> linked = new LinkedList<>();
```

---

**基本写法：头部添加**
`<list>.addFirst(<元素>);`
```java
// 在列表头部添加元素
linked.addFirst("First");
```

---

**基本写法：尾部添加**
`<list>.addLast(<元素>);`
```java
// 在列表尾部添加元素
linked.addLast("Last");
```

---

**基本写法：获取头部**
`<list>.getFirst();`
```java
// 获取列表头部元素
String first = linked.getFirst();
```

---

**基本写法：获取尾部**
`<list>.getLast();`
```java
// 获取列表尾部元素
String last = linked.getLast();
```

---

**基本写法：删除头部**
`<list>.removeFirst();`
```java
// 删除并返回头部元素
String removed = linked.removeFirst();
```

---

## HashMap

**基本写法：创建 HashMap**
`Map<<键类型>, <值类型>> <变量> = new HashMap<>();`
```java
// 创建 HashMap
Map<String, Integer> map = new HashMap<>();
```

---

**基本写法：添加键值对**
`<map>.put(<键>, <值>);`
```java
// 向 Map 添加键值对
map.put("Alice", 25);
```

---

**基本写法：获取值**
`<map>.get(<键>);`
```java
// 根据键获取值
Integer age = map.get("Alice");
```

---

**基本写法：删除键值对**
`<map>.remove(<键>);`
```java
// 根据键删除键值对
map.remove("Alice");
```

---

**基本写法：判断包含键**
`<map>.containsKey(<键>);`
```java
// 判断是否包含指定键
boolean has = map.containsKey("Alice");
```

---

**基本写法：判断包含值**
`<map>.containsValue(<值>);`
```java
// 判断是否包含指定值
boolean has = map.containsValue(25);
```

---

**基本写法：获取所有键**
`<map>.keySet();`
```java
// 获取所有键的集合
Set<String> keys = map.keySet();
```

---

**基本写法：获取所有值**
`<map>.values();`
```java
// 获取所有值的集合
Collection<Integer> values = map.values();
```

---

**基本写法：获取所有键值对**
`<map>.entrySet();`
```java
// 获取所有键值对集合
Set<Map.Entry<String, Integer>> entries = map.entrySet();
```

---

**基本写法：遍历 Map**
`for (Map.Entry<<键类型>, <值类型>> <变量> : <map>.entrySet()) { }`
```java
// 遍历 Map 的键值对
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    String key = entry.getKey();
    Integer value = entry.getValue();
}
```

---

## HashSet

**基本写法：创建 HashSet**
`Set<<类型>> <变量> = new HashSet<>();`
```java
// 创建 HashSet
Set<String> set = new HashSet<>();
```

---

**基本写法：添加元素**
`<set>.add(<元素>);`
```java
// 向 Set 添加元素
set.add("Apple");
```

---

**基本写法：删除元素**
`<set>.remove(<元素>);`
```java
// 从 Set 删除元素
set.remove("Apple");
```

---

**基本写法：判断包含**
`<set>.contains(<元素>);`
```java
// 判断 Set 是否包含元素
boolean has = set.contains("Apple");
```

---

**基本写法：遍历 Set**
`for (<类型> <变量> : <set>) { }`
```java
// 遍历 Set
for (String item : set) {
}
```

---

## TreeMap

**基本写法：创建 TreeMap**
`Map<<键类型>, <值类型>> <变量> = new TreeMap<>();`
```java
// 创建按键排序的 TreeMap
Map<String, Integer> treeMap = new TreeMap<>();
```

---

**基本写法：获取第一个键**
`((TreeMap<<K>, <V>>) <map>).firstKey();`
```java
// 获取最小的键
String first = ((TreeMap<String, Integer>) treeMap).firstKey();
```

---

**基本写法：获取最后一个键**
`((TreeMap<<K>, <V>>) <map>).lastKey();`
```java
// 获取最大的键
String last = ((TreeMap<String, Integer>) treeMap).lastKey();
```

---

## 集合工具

**基本写法：排序 List**
`Collections.sort(<list>);`
```java
// 对 List 进行升序排序
Collections.sort(list);
```

---

**基本写法：降序排序**
`Collections.sort(<list>, Collections.reverseOrder());`
```java
// 对 List 进行降序排序
Collections.sort(list, Collections.reverseOrder());
```

---

**基本写法：反转 List**
`Collections.reverse(<list>);`
```java
// 反转 List 中元素的顺序
Collections.reverse(list);
```

---

**基本写法：打乱顺序**
`Collections.shuffle(<list>);`
```java
// 随机打乱 List 中元素的顺序
Collections.shuffle(list);
```

---

**基本写法：查找最大值**
`Collections.max(<list>);`
```java
// 查找 List 中的最大值
String max = Collections.max(list);
```

---

**基本写法：查找最小值**
`Collections.min(<list>);`
```java
// 查找 List 中的最小值
String min = Collections.min(list);
```

---

**基本写法：填充 List**
`Collections.fill(<list>, <值>);`
```java
// 用指定值填充整个 List
Collections.fill(list, "Default");
```

---

**基本写法：不可变 List**
`List.of(<元素1>, <元素2>)`
```java
// Java 9+ 创建不可变 List
List<String> immutable = List.of("A", "B", "C");
```

---

**基本写法：不可变 Set**
`Set.of(<元素1>, <元素2>)`
```java
// Java 9+ 创建不可变 Set
Set<String> immutable = Set.of("A", "B", "C");
```

---

**基本写法：不可变 Map**
`Map.of(<键1>, <值1>, <键2>, <值2>)`
```java
// Java 9+ 创建不可变 Map
Map<String, Integer> immutable = Map.of("A", 1, "B", 2);
```

---

## 迭代器

**基本写法：获取迭代器**
`<集合>.iterator()`
```java
// 获取集合的迭代器
Iterator<String> it = list.iterator();
```

---

**基本写法：迭代器遍历**
`while (<迭代器>.hasNext()) { <迭代器>.next(); }`
```java
// 使用迭代器遍历
while (it.hasNext()) {
    String item = it.next();
}
```

---

**基本写法：迭代器删除**
`<迭代器>.remove();`
```java
// 使用迭代器安全删除元素
while (it.hasNext()) {
    String item = it.next();
    it.remove();
}
```

---

## 集合转换

**基本写法：List 转数组**
`<list>.toArray(new <类型>[0]);`
```java
// 将 List 转换为数组
String[] arr = list.toArray(new String[0]);
```

---

**基本写法：数组转 List**
`Arrays.asList(<数组>);`
```java
// 将数组转换为 List
String[] arr = {"A", "B"};
List<String> list = Arrays.asList(arr);
```

---

**基本写法：List 转 Set**
`new HashSet<>(<list>);`
```java
// 将 List 转换为 Set 去重
Set<String> set = new HashSet<>(list);
```

---

## 集合流操作

**基本写法：创建流**
`<集合>.stream()`
```java
// 从集合创建流
list.stream();
```

---

**基本写法：过滤**
`<stream>.filter(<条件>)`
```java
// 过滤满足条件的元素
list.stream().filter(s -> s.length() > 3);
```

---

**基本写法：映射**
`<stream>.map(<映射函数>)`
```java
// 将元素映射为新元素
list.stream().map(String::toUpperCase);
```

---

**基本写法：收集为 List**
`<stream>.collect(Collectors.toList())`
```java
// 将流收集为 List
List<String> result = list.stream().collect(Collectors.toList());
```

---

**基本写法：计数**
`<stream>.count()`
```java
// 统计流中元素个数
long count = list.stream().count();
```



<!-- ============ 文档分隔线：013-java/007-ControlFlow.md ============ -->

# Java 控制流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## if-else 语句

**基本写法：if 语句**
`if (<条件>) { }`
```java
// 条件为真时执行
if (score >= 90) {
}
```

---

**基本写法：if-else 语句**
`if (<条件>) { } else { }`
```java
// 条件为真执行 if 块否则执行 else 块
if (score >= 60) {
} else {
}
```

---

**换行写法：if-else if-else 链**
`if (<条件>) { } else if (<条件>) { } else { }`
```java
// 多条件分支判断
if (score >= 90) {
} else if (score >= 80) {
} else if (score >= 60) {
} else {
}
```

---

**基本写法：嵌套 if**
`if (<条件>) { if (<条件>) { } else { } }`
```java
// if 语句内部嵌套 if
if (score >= 90) {
    if (score >= 95) {
    } else {
    }
}
```

---

**基本写法：卫语句提前返回**
`if (<条件>) { return; }`
```java
// 条件不满足时提前返回
if (order == null) {
    return;
}
```

---

## switch 语句

**基本写法：传统 switch**
`switch (<表达式>) { case <值>: break; default: }`
```java
// 传统 switch 多分支
switch (day) {
    case 1:
        break;
    case 2:
        break;
    default:
}
```

---

**基本写法：switch case 穿透**
`case <值1>: case <值2>: <语句>; break;`
```java
// 多个 case 共享同一处理
switch (day) {
    case 1:
    case 2:
    case 3:
        System.out.println("Weekday");
        break;
    default:
}
```

---

**基本写法：switch 表达式箭头语法**
`switch (<表达式>) { case <值> -> <结果>; default -> <结果>; }`
```java
// Java 12+ switch 表达式
String dayName = switch (day) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    default -> "Invalid";
};
```

---

**基本写法：switch 表达式多值匹配**
`case <值1>, <值2> -> <结果>;`
```java
// 多个值匹配同一结果
String type = switch (day) {
    case 1, 2, 3, 4, 5 -> "Weekday";
    case 6, 7 -> "Weekend";
    default -> "Invalid";
};
```

---

**基本写法：switch 表达式 yield**
`switch (<表达式>) { case <值> -> { yield <结果>; } }`
```java
// 复杂逻辑使用 yield 返回
int result = switch (operation) {
    case "add" -> {
        yield a + b;
    }
    default -> {
        yield 0;
    }
};
```

---

## for 循环

**基本写法：标准 for 循环**
`for (<初始化>; <条件>; <更新>) { }`
```java
// 已知次数的循环
for (int i = 0; i < 10; i++) {
}
```

---

**基本写法：增强型 for 循环**
`for (<类型> <变量> : <可迭代对象>) { }`
```java
// 遍历数组
int[] numbers = {1, 2, 3};
for (int num : numbers) {
}
```

---

**基本写法：带标签的 for 循环**
`<标签>: for (...) { }`
```java
// 为外层循环添加标签
outer: for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
    }
}
```

---

## while 循环

**基本写法：while 循环**
`while (<条件>) { }`
```java
// 先判断后执行
int i = 0;
while (i < 10) {
    i++;
}
```

---

## do-while 循环

**基本写法：do-while 循环**
`do { } while (<条件>);`
```java
// 先执行后判断至少执行一次
int i = 0;
do {
    i++;
} while (i < 10);
```

---

## 循环控制

**基本写法：break 语句**
`break;`
```java
// 跳出当前循环
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;
    }
}
```

---

**基本写法：带标签的 break**
`break <标签>;`
```java
// 跳出多层循环
outerLoop: for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
        if (i * j > 6) {
            break outerLoop;
        }
    }
}
```

---

**基本写法：continue 语句**
`continue;`
```java
// 跳过当前迭代
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;
    }
}
```

---

**基本写法：带标签的 continue**
`continue <标签>;`
```java
// 跳过外层循环的当前迭代
outer: for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) {
            continue outer;
        }
    }
}
```

---

## return 语句

**基本写法：返回值**
`return <值>;`
```java
// 返回计算结果
public int add(int a, int b) {
    return a + b;
}
```

---

**基本写法：无返回值提前结束**
`return;`
```java
// 提前结束方法
public void validate(int value) {
    if (value < 0) {
        return;
    }
}
```



<!-- ============ 文档分隔线：013-java/008-JavaAnnotationsTutorial.md ============ -->

# Java 枚举与注解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 枚举定义

**单行写法：简单枚举**
`public enum <枚举名> { <常量1>, <常量2> }`
```java
// 单行定义简单枚举
public enum Day { MONDAY, TUESDAY, WEDNESDAY }
```

---

**换行写法：多常量枚举**
`public enum <枚举名> { <常量1>, <常量2>, ... }`
```java
// 换行定义多常量枚举
public enum Day {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
}
```

---

**基本写法：枚举使用**
`<枚举名> <变量> = <枚举名>.<常量>;`
```java
// 使用枚举常量
Day today = Day.MONDAY;
```

---

## 枚举带属性

**换行写法：带属性的枚举**
`public enum <枚举名> { <常量>(<值>); private <类型> <字段>; <构造方法> <getter> }`
```java
// 定义带属性的枚举
public enum Color {
    RED("#FF0000"),
    GREEN("#00FF00"),
    BLUE("#0000FF");

    private String hex;

    Color(String hex) {
        this.hex = hex;
    }

    public String getHex() {
        return hex;
    }
}
```

---

**基本写法：访问枚举属性**
`<枚举变量>.<getter方法>()`
```java
// 获取枚举常量的属性值
String hex = Color.RED.getHex();
```

---

## 枚举方法

**基本写法：枚举抽象方法**
`public enum <枚举名> { <常量> { @Override public <方法> { } }; abstract <方法签名>; }`
```java
// 每个枚举常量实现自己的逻辑
public enum Operation {
    ADD {
        @Override
        public int apply(int a, int b) {
            return a + b;
        }
    },
    SUBTRACT {
        @Override
        public int apply(int a, int b) {
            return a - b;
        }
    };

    public abstract int apply(int a, int b);
}
```

---

**基本写法：枚举实现接口**
`public enum <枚举名> implements <接口> { }`
```java
// 枚举实现接口
public enum Status implements Comparable<Status> {
}
```

---

## 枚举常用方法

**基本写法：获取所有常量**
`<枚举名>.values()`
```java
// 获取枚举所有常量数组
Day[] days = Day.values();
```

---

**基本写法：字符串转枚举**
`<枚举名>.valueOf(<字符串>)`
```java
// 将字符串转换为枚举常量
Day day = Day.valueOf("MONDAY");
```

---

**基本写法：获取枚举序号**
`<枚举变量>.ordinal()`
```java
// 获取枚举常量的序号从 0 开始
int index = Day.MONDAY.ordinal();
```

---

**基本写法：枚举比较**
`<枚举变量1>.compareTo(<枚举变量2>)`
```java
// 比较两个枚举常量的顺序
int result = Day.MONDAY.compareTo(Day.FRIDAY);
```

---

**基本写法：枚举 switch**
`switch (<枚举变量>) { case <常量>: }`
```java
// 在 switch 中使用枚举
switch (day) {
    case MONDAY:
        break;
    case FRIDAY:
        break;
    default:
}
```

---

## 枚举集合

**基本写法：EnumSet 创建**
`EnumSet.of(<枚举常量1>, <枚举常量2>)`
```java
// 创建包含指定枚举常量的集合
EnumSet<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
```

---

**基本写法：EnumSet 全部**
`EnumSet.allOf(<枚举类>.class)`
```java
// 创建包含所有枚举常量的集合
EnumSet<Day> allDays = EnumSet.allOf(Day.class);
```

---

**基本写法：EnumMap 创建**
`new EnumMap<>(<枚举类>.class)`
```java
// 创建以枚举为键的 Map
EnumMap<Day, String> schedule = new EnumMap<>(Day.class);
```

---

## 内置注解

**基本写法：@Override**
`@Override`
```java
// 标记方法重写父类方法
@Override
public String toString() {
    return "Custom";
}
```

---

**基本写法：@Deprecated**
`@Deprecated`
```java
// 标记方法已过时
@Deprecated
public void oldMethod() {
}
```

---

**基本写法：@SuppressWarnings**
`@SuppressWarnings("<警告类型>")`
```java
// 抑制指定类型的警告
@SuppressWarnings("unchecked")
List list = new ArrayList();
```

---

**基本写法：@FunctionalInterface**
`@FunctionalInterface`
```java
// 标记函数式接口
@FunctionalInterface
public interface MyFunction {
    void apply();
}
```

---

## 元注解

**基本写法：@Target**
`@Target(<元素类型>)`
```java
// 指定注解可用于类上
@Target(ElementType.TYPE)
```

---

**基本写法：@Retention**
`@Retention(<保留策略>)`
```java
// 指定注解运行时保留
@Retention(RetentionPolicy.RUNTIME)
```

---

**基本写法：@Documented**
`@Documented`
```java
// 标记注解包含在 Javadoc 中
@Documented
```

---

**基本写法：@Inherited**
`@Inherited`
```java
// 标记注解可被子类继承
@Inherited
```

---

## 自定义注解

**基本写法：自定义注解定义**
`@interface <注解名> { }`
```java
// 定义自定义注解
public @interface MyAnnotation {
}
```

---

**基本写法：注解成员**
`<类型> <成员名>() [default <默认值>];`
```java
// 定义带成员的注解
public @interface MyAnnotation {
    String value();
    int priority() default 0;
}
```

---

**基本写法：使用自定义注解**
`@<注解名>(<成员> = <值>)`
```java
// 使用自定义注解并指定成员值
@MyAnnotation(value = "test", priority = 1)
public void method() {
}
```

---

**基本写法：注解默认值**
`@<注解名>`
```java
// 使用注解的默认值
@MyAnnotation
public void method() {
}
```

---

**基本写法：注解单一成员 value 简写**
`@<注解名>("<值>")`
```java
// 单一成员 value 时可省略成员名
@MyAnnotation("test")
public void method() {
}
```

---

## 注解组合

**换行写法：多注解组合**
`@<注解1> @<注解2>`
```java
// 同时使用多个注解
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {
}
```

---

**基本写法：重复注解**
`@<注解名>(<值1>) @<注解名>(<值2>)`
```java
// Java 8+ 支持重复注解
@Schedule(day = "Monday")
@Schedule(day = "Wednesday")
public void task() {
}
```

---

## 注解处理

**基本写法：获取类注解**
`<类>.getAnnotation(<注解类>.class)`
```java
// 通过反射获取类上的注解
MyAnnotation ann = MyClass.class.getAnnotation(MyAnnotation.class);
```

---

**基本写法：判断注解存在**
`<类>.isAnnotationPresent(<注解类>.class)`
```java
// 检查类上是否存在指定注解
boolean hasAnnotation = MyClass.class.isAnnotationPresent(MyAnnotation.class);
```

---

**基本写法：获取方法注解**
`<方法>.getAnnotation(<注解类>.class)`
```java
// 通过反射获取方法上的注解
Method method = MyClass.class.getMethod("process");
MyAnnotation ann = method.getAnnotation(MyAnnotation.class);
```

---

**基本写法：获取注解成员值**
`<注解>.<成员名>()`
```java
// 获取注解成员的值
String value = ann.value();
```



<!-- ============ 文档分隔线：013-java/009-OOP.md ============ -->

# Java 面向对象编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类定义

**基本写法：类定义**
`<修饰符> class <类名> { }`
```java
// 定义一个公开类
public class Person {
}
```

---

**换行写法：多字段类定义**
`<修饰符> class <类名> { <字段1> <字段2> <方法> }`
```java
// 定义包含多个字段的类
public class Person {
    private String name;
    private int age;
    private String address;
}
```

---

## 成员变量

**基本写法：实例变量声明**
`<修饰符> <类型> <变量名>;`
```java
// 声明实例变量
private String name;
```

---

**基本写法：实例变量初始化**
`<修饰符> <类型> <变量名> = <值>;`
```java
// 声明并初始化实例变量
private int age = 18;
```

---

**基本写法：静态变量声明**
`<修饰符> static <类型> <变量名>;`
```java
// 声明静态变量
private static int count;
```

---

## 构造方法

**基本写法：无参构造方法**
`<修饰符> <类名>() { }`
```java
// 定义无参构造方法
public Person() {
}
```

---

**基本写法：有参构造方法**
`<修饰符> <类名>(<参数列表>) { }`
```java
// 定义有参构造方法
public Person(String name, int age) {
    this.name = name;
    this.age = age;
}
```

---

**基本写法：构造方法重载**
`<修饰符> <类名>(<参数列表>) { this(<参数>); }`
```java
// 构造方法调用另一个构造方法
public Person() {
    this("Unknown", 0);
}
```

---

## 方法

**基本写法：实例方法**
`<修饰符> <返回类型> <方法名>(<参数>) { }`
```java
// 定义实例方法
public String getName() {
    return name;
}
```

---

**基本写法：静态方法**
`<修饰符> static <返回类型> <方法名>(<参数>) { }`
```java
// 定义静态方法
public static int getCount() {
    return count;
}
```

---

## 对象创建与使用

**基本写法：创建对象**
`<类名> <变量名> = new <类名>(<参数>);`
```java
// 创建 Person 对象
Person p = new Person("Alice", 25);
```

---

**基本写法：调用实例方法**
`<对象>.<方法名>(<参数>);`
```java
// 调用对象的方法
String name = p.getName();
```

---

**基本写法：访问实例变量**
`<对象>.<变量名>`
```java
// 访问对象的公开变量
String name = p.name;
```

---

## 封装

**基本写法：私有字段**
`private <类型> <变量名>;`
```java
// 使用 private 修饰字段
private String password;
```

---

**基本写法：getter 方法**
`public <类型> get<字段名>() { return <字段>; }`
```java
// 提供字段的读取方法
public String getPassword() {
    return password;
}
```

---

**基本写法：setter 方法**
`public void set<字段名>(<类型> <参数>) { <字段> = <参数>; }`
```java
// 提供字段的设置方法
public void setPassword(String password) {
    this.password = password;
}
```

---

## 继承

**基本写法：类继承**
`<修饰符> class <子类> extends <父类> { }`
```java
// Student 类继承 Person 类
public class Student extends Person {
}
```

---

**基本写法：调用父类构造方法**
`super(<参数>);`
```java
// 在子类构造方法中调用父类构造方法
public Student(String name, int age, String studentId) {
    super(name, age);
    this.studentId = studentId;
}
```

---

**基本写法：调用父类方法**
`super.<方法名>(<参数>);`
```java
// 调用父类的方法
super.display();
```

---

**基本写法：方法重写**
`@Override <修饰符> <返回类型> <方法名>(<参数>) { }`
```java
// 重写父类方法
@Override
public String toString() {
    return "Student: " + getName();
}
```

---

## 多态

**基本写法：父类引用指向子类对象**
`<父类> <变量> = new <子类>();`
```java
// 父类引用指向子类对象
Person p = new Student();
```

---

**基本写法：instanceof 检查**
`<对象> instanceof <类>`
```java
// 检查对象是否为特定类型
if (p instanceof Student) {
    Student s = (Student) p;
}
```

---

**基本写法：Java 16+ instanceof 模式匹配**
`if (<对象> instanceof <类型> <变量名>) { }`
```java
// 模式匹配直接绑定变量
if (p instanceof Student s) {
    s.getStudentId();
}
```

---

## final 关键字

**基本写法：final 类**
`final class <类名> { }`
```java
// final 类不能被继承
public final class String {
}
```

---

**基本写法：final 方法**
`<修饰符> final <返回类型> <方法名>() { }`
```java
// final 方法不能被重写
public final void secureMethod() {
}
```

---

**基本写法：final 变量**
`final <类型> <变量名> = <值>;`
```java
// final 变量只能赋值一次
final int MAX_VALUE = 100;
```

---

## static 关键字

**基本写法：静态代码块**
`static { }`
```java
// 类加载时执行的静态代码块
static {
    count = 0;
}
```

---

**基本写法：实例代码块**
`{ }`
```java
// 每次创建对象时执行的代码块
{
    count++;
}
```

---

## 内部类

**基本写法：成员内部类**
`<修饰符> class <外部类> { <修饰符> class <内部类> { } }`
```java
// 定义成员内部类
public class Outer {
    public class Inner {
    }
}
```

---

**基本写法：创建内部类实例**
`<外部类>.<内部类> <变量> = <外部类实例>.new <内部类>();`
```java
// 创建成员内部类对象
Outer.Inner inner = outer.new Inner();
```

---

**基本写法：静态内部类**
`<修饰符> static class <静态内部类> { }`
```java
// 定义静态内部类
public class Outer {
    public static class StaticInner {
    }
}
```

---

**基本写法：创建静态内部类实例**
`<外部类>.<静态内部类> <变量> = new <外部类>.<静态内部类>();`
```java
// 创建静态内部类对象
Outer.StaticInner inner = new Outer.StaticInner();
```

---

**基本写法：匿名内部类**
`new <类名|接口>() { <方法实现> }`
```java
// 匿名实现接口
Runnable r = new Runnable() {
    @Override
    public void run() {
    }
};
```

---

## 抽象类

**基本写法：抽象类定义**
`abstract class <类名> { }`
```java
// 定义抽象类
public abstract class Animal {
}
```

---

**基本写法：抽象方法**
`abstract <返回类型> <方法名>(<参数>);`
```java
// 定义抽象方法
public abstract void makeSound();
```

---

## 接口

**基本写法：接口定义**
`interface <接口名> { }`
```java
// 定义接口
public interface Comparable {
}
```

---

**基本写法：接口默认方法**
`default <返回类型> <方法名>(<参数>) { }`
```java
// 接口中的默认方法
default void printInfo() {
}
```

---

**基本写法：接口静态方法**
`static <返回类型> <方法名>(<参数>) { }`
```java
// 接口中的静态方法
static Comparable getDefault() {
    return null;
}
```

---

**基本写法：接口私有方法**
`private <返回类型> <方法名>(<参数>) { }`
```java
// 接口中的私有方法 Java 9+
private void helperMethod() {
}
```

---

**基本写法：实现接口**
`<修饰符> class <类名> implements <接口> { }`
```java
// 类实现接口
public class Student implements Comparable {
}
```

---

**基本写法：接口继承**
`interface <接口> extends <父接口1>, <父接口2> { }`
```java
// 接口继承多个接口
public interface AdvancedList extends List, RandomAccess {
}
```

---

## this 关键字

**基本写法：this 引用当前对象**
`this.<字段名>`
```java
// 区分成员变量和参数
this.name = name;
```

---

**基本写法：this 调用构造方法**
`this(<参数>);`
```java
// 在构造方法中调用另一个构造方法
public Person() {
    this("Unknown");
}
```

---

**基本写法：this 作为参数传递**
`method(this);`
```java
// 将当前对象作为参数传递
someMethod(this);
```

---

**基本写法：this 作为返回值**
`return this;`
```java
// 返回当前对象实现链式调用
public Builder setName(String name) {
    this.name = name;
    return this;
}
```



<!-- ============ 文档分隔线：013-java/010-DataTypeConversion.md ============ -->

# Java 数据类型与类型转换

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 整数类型

**基本写法：byte 类型**
`byte <变量名> = <值>;`
```java
// 声明 1 字节整数
byte b = 100;
```

---

**基本写法：short 类型**
`short <变量名> = <值>;`
```java
// 声明 2 字节整数
short s = 1000;
```

---

**基本写法：int 类型**
`int <变量名> = <值>;`
```java
// 声明 4 字节整数（默认）
int i = 100000;
```

---

**基本写法：long 类型**
`long <变量名> = <值>L;`
```java
// 声明 8 字节整数必须加 L 后缀
long l = 10000000000L;
```

---

## 浮点数类型

**基本写法：float 类型**
`float <变量名> = <值>F;`
```java
// 声明单精度浮点数必须加 F 后缀
float f = 3.14f;
```

---

**基本写法：double 类型**
`double <变量名> = <值>;`
```java
// 声明双精度浮点数（默认）
double d = 3.1415926535;
```

---

## 字符类型

**基本写法：字符字面量**
`char <变量名> = '<字符>';`
```java
// 使用字符字面量声明
char c1 = 'A';
```

---

**基本写法：ASCII 码赋值**
`char <变量名> = <ASCII码>;`
```java
// 使用 ASCII 码赋值
char c2 = 65;
```

---

**基本写法：Unicode 编码赋值**
`char <变量名> = '\u<编码>';`
```java
// 使用 Unicode 编码赋值
char c3 = '\u0041';
```

---

## 布尔类型

**基本写法：布尔类型**
`boolean <变量名> = <true|false>;`
```java
// 声明布尔类型变量
boolean flag = true;
```

---

## 引用数据类型

**基本写法：类类型声明**
`<类名> <变量名> = new <类名>();`
```java
// 声明集合对象
ArrayList<String> list = new ArrayList<>();
```

---

**基本写法：字符串声明**
`String <变量名> = "<字符串>";`
```java
// 声明字符串对象
String str = "Hello, Java!";
```

---

**基本写法：数组类型声明**
`<类型>[] <变量名> = { <元素> };`
```java
// 声明并初始化数组
int[] numbers = {1, 2, 3, 4, 5};
```

---

## 自动类型转换

**基本写法：小类型转大类型**
`<大类型> <变量名> = <小类型变量>;`
```java
// byte 自动转换为 short
byte b = 100;
short s = b;
```

---

**基本写法：int 转 long**
`long <变量名> = <int变量>;`
```java
// int 自动转换为 long
int i = 100;
long l = i;
```

---

**基本写法：char 转 int**
`int <变量名> = <char变量>;`
```java
// char 自动转换为 int
char c = 'A';
int i = c;
```

---

## 强制类型转换

**基本写法：强制类型转换**
`(<目标类型>) <表达式>`
```java
// double 强制转换为 int
double pi = 3.14159;
int num = (int) pi;
```

---

**基本写法：int 转 byte**
`byte <变量名> = (byte) <int变量>;`
```java
// int 强制转换为 byte
int i = 100;
byte b = (byte) i;
```

---

## 装箱与拆箱

**基本写法：手动装箱**
`<包装类> <变量名> = <包装类>.valueOf(<基本类型>);`
```java
// int 手动装箱为 Integer
int i = 100;
Integer iObj = Integer.valueOf(i);
```

---

**基本写法：自动装箱**
`<包装类> <变量名> = <基本类型>;`
```java
// int 自动装箱为 Integer
Integer iObj = 100;
```

---

**基本写法：手动拆箱**
`<基本类型> <变量名> = <包装类变量>.<xxxValue>();`
```java
// Integer 手动拆箱为 int
Integer iObj = 100;
int i = iObj.intValue();
```

---

**基本写法：自动拆箱**
`<基本类型> <变量名> = <包装类变量>;`
```java
// Integer 自动拆箱为 int
Integer iObj = 100;
int i = iObj;
```

---

## 字符串与基本类型转换

**基本写法：基本类型转字符串**
`String <变量名> = String.valueOf(<基本类型>);`
```java
// int 转换为字符串
int i = 100;
String s = String.valueOf(i);
```

---

**基本写法：字符串转 int**
`int <变量名> = Integer.parseInt(<字符串>);`
```java
// 字符串转换为 int
String s = "100";
int i = Integer.parseInt(s);
```

---

**基本写法：字符串转 double**
`double <变量名> = Double.parseDouble(<字符串>);`
```java
// 字符串转换为 double
String s = "3.14";
double d = Double.parseDouble(s);
```

---

**基本写法：字符串转 boolean**
`boolean <变量名> = Boolean.parseBoolean(<字符串>);`
```java
// 字符串转换为 boolean
String s = "true";
boolean b = Boolean.parseBoolean(s);
```

---

## 运算中的类型提升

**基本写法：byte 运算提升为 int**
`int <变量名> = <byte变量1> + <byte变量2>;`
```java
// 两个 byte 相加结果为 int
byte b1 = 10;
byte b2 = 20;
int i = b1 + b2;
```

---

**基本写法：int 与 double 运算**
`double <变量名> = <int变量> + <double变量>;`
```java
// int 与 double 运算结果为 double
int i = 100;
double d = 3.14;
double result = i + d;
```

---

## 字符串拼接

**基本写法：字符串与数字拼接**
`String <变量名> = <字符串> + <数字>;`
```java
// 字符串与数字拼接
String s = "Result: " + 42;
```

---

**基本写法：括号优先拼接**
`String <变量名> = <字符串> + (<表达式>);`
```java
// 使用括号先计算再拼接
String s = "Result: " + (10 + 20);
```

---

## BigDecimal 精确计算

**基本写法：创建 BigDecimal**
`BigDecimal <变量名> = new BigDecimal("<数值>");`
```java
// 使用字符串创建 BigDecimal
BigDecimal bd = new BigDecimal("0.1");
```

---

**基本写法：BigDecimal 加法**
`BigDecimal <结果> = <bd1>.add(<bd2>);`
```java
// 两个 BigDecimal 相加
BigDecimal bd1 = new BigDecimal("0.1");
BigDecimal bd2 = new BigDecimal("0.2");
BigDecimal sum = bd1.add(bd2);
```



<!-- ============ 文档分隔线：013-java/011-ArrayDetailed.md ============ -->

# Java 数组详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数组声明

**基本写法：声明数组**
`<类型>[] <变量名>;`
```java
// 声明整型数组
int[] numbers;
```

---

**基本写法：C 风格声明**
`<类型> <变量名>[];`
```java
// C 风格声明数组
int numbers[];
```

---

## 数组创建

**基本写法：指定长度创建**
`<变量名> = new <类型>[<长度>];`
```java
// 创建长度为 5 的数组
numbers = new int[5];
```

---

**基本写法：声明并创建**
`<类型>[] <变量名> = new <类型>[<长度>];`
```java
// 声明并创建数组
int[] numbers = new int[5];
```

---

**基本写法：静态初始化**
`<类型>[] <变量名> = { <元素1>, <元素2>, ... };`
```java
// 声明并初始化数组
int[] numbers = {1, 2, 3, 4, 5};
```

---

**基本写法：new 关键字初始化**
`<类型>[] <变量名> = new <类型>[]{ <元素1>, <元素2> };`
```java
// 使用 new 关键字初始化
int[] numbers = new int[]{1, 2, 3};
```

---

## 数组访问

**基本写法：访问元素**
`<数组>[<索引>]`
```java
// 获取索引为 0 的元素
int first = numbers[0];
```

---

**基本写法：修改元素**
`<数组>[<索引>] = <值>;`
```java
// 修改索引为 0 的元素
numbers[0] = 100;
```

---

**基本写法：获取长度**
`<数组>.length`
```java
// 获取数组长度
int len = numbers.length;
```

---

## 数组遍历

**基本写法：for 循环遍历**
`for (int i = 0; i < <数组>.length; i++) { }`
```java
// 使用索引遍历数组
for (int i = 0; i < numbers.length; i++) {
    int num = numbers[i];
}
```

---

**基本写法：增强 for 循环遍历**
`for (<类型> <变量> : <数组>) { }`
```java
// 使用增强 for 循环遍历
for (int num : numbers) {
}
```

---

## 多维数组

**基本写法：二维数组声明**
`<类型>[][] <变量名> = new <类型>[<行>][<列>];`
```java
// 创建 3 行 4 列的二维数组
int[][] matrix = new int[3][4];
```

---

**基本写法：二维数组初始化**
`<类型>[][] <变量名> = { {<元素>}, {<元素>} };`
```java
// 静态初始化二维数组
int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
```

---

**基本写法：访问二维数组元素**
`<数组>[<行>][<列>]`
```java
// 获取第二行第三列的元素
int element = matrix[1][2];
```

---

**基本写法：遍历二维数组**
`for (int i = 0; i < <数组>.length; i++) { for (int j = 0; j < <数组>[i].length; j++) { } }`
```java
// 嵌套循环遍历二维数组
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        int element = matrix[i][j];
    }
}
```

---

## 不规则数组

**基本写法：创建不规则数组**
`<类型>[][] <变量名> = new <类型>[<行>][];`
```java
// 创建不规则二维数组
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[3];
jagged[2] = new int[4];
```

---

## 数组排序

**基本写法：升序排序**
`Arrays.sort(<数组>);`
```java
// 对数组进行升序排序
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers);
```

---

**基本写法：部分排序**
`Arrays.sort(<数组>, <起始索引>, <结束索引>);`
```java
// 对数组指定范围排序
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers, 1, 4);
```

---

**基本写法：降序排序**
`Arrays.sort(<数组>, Collections.reverseOrder());`
```java
// 对 Integer 数组降序排序
Integer[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers, Collections.reverseOrder());
```

---

## 数组搜索

**基本写法：二分查找**
`Arrays.binarySearch(<数组>, <目标值>);`
```java
// 在已排序数组中二分查找
int[] numbers = {1, 2, 3, 4, 5};
int index = Arrays.binarySearch(numbers, 3);
```

---

## 数组复制

**基本写法：copyOf 复制**
`Arrays.copyOf(<原数组>, <新长度>);`
```java
// 复制数组并指定新长度
int[] original = {1, 2, 3};
int[] copy = Arrays.copyOf(original, 5);
```

---

**基本写法：copyOfRange 复制**
`Arrays.copyOfRange(<原数组>, <起始>, <结束>);`
```java
// 复制数组指定范围
int[] original = {1, 2, 3, 4, 5};
int[] copy = Arrays.copyOfRange(original, 1, 4);
```

---

**基本写法：System.arraycopy**
`System.arraycopy(<源数组>, <源位置>, <目标数组>, <目标位置>, <长度>);`
```java
// 系统级数组复制
int[] src = {1, 2, 3, 4, 5};
int[] dest = new int[3];
System.arraycopy(src, 1, dest, 0, 3);
```

---

## 数组转换

**基本写法：数组转字符串**
`Arrays.toString(<数组>);`
```java
// 将数组转换为字符串表示
int[] numbers = {1, 2, 3};
String str = Arrays.toString(numbers);
```

---

**基本写法：二维数组转字符串**
`Arrays.deepToString(<数组>);`
```java
// 将多维数组转换为字符串
int[][] matrix = {{1, 2}, {3, 4}};
String str = Arrays.deepToString(matrix);
```

---

**基本写法：数组转 List**
`Arrays.asList(<数组>);`
```java
// 将数组转换为固定大小的 List
String[] arr = {"a", "b", "c"};
List<String> list = Arrays.asList(arr);
```

---

**基本写法：数组转可变 List**
`new ArrayList<>(Arrays.asList(<数组>));`
```java
// 将数组转换为可修改的 ArrayList
String[] arr = {"a", "b", "c"};
List<String> list = new ArrayList<>(Arrays.asList(arr));
```

---

## 数组填充

**基本写法：填充所有元素**
`Arrays.fill(<数组>, <值>);`
```java
// 用指定值填充整个数组
int[] numbers = new int[5];
Arrays.fill(numbers, 0);
```

---

**基本写法：填充指定范围**
`Arrays.fill(<数组>, <起始>, <结束>, <值>);`
```java
// 用指定值填充数组指定范围
int[] numbers = new int[5];
Arrays.fill(numbers, 1, 3, 9);
```

---

## 数组比较

**基本写法：一维数组比较**
`Arrays.equals(<数组1>, <数组2>);`
```java
// 比较两个一维数组内容是否相同
int[] a = {1, 2, 3};
int[] b = {1, 2, 3};
boolean result = Arrays.equals(a, b);
```

---

**基本写法：多维数组比较**
`Arrays.deepEquals(<数组1>, <数组2>);`
```java
// 比较两个多维数组内容是否相同
int[][] a = {{1, 2}, {3, 4}};
int[][] b = {{1, 2}, {3, 4}};
boolean result = Arrays.deepEquals(a, b);
```



<!-- ============ 文档分隔线：013-java/012-ExceptionHandlingMechanism.md ============ -->

# Java 异常处理机制

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 异常体系

**基本写法：Throwable 体系**
`Throwable -> Error | Exception`
```java
// 异常体系根类
Throwable
```

---

**基本写法：Error 不可恢复**
`class <错误类> extends Error`
```java
// 严重错误程序无法处理
OutOfMemoryError
```

---

**基本写法：Exception 可恢复**
`class <异常类> extends Exception`
```java
// 可检查异常必须处理
IOException
```

---

**基本写法：RuntimeException 运行时异常**
`class <异常类> extends RuntimeException`
```java
// 运行时异常可不处理
NullPointerException
```

---

## try-catch

**基本写法：单 catch**
`try { } catch (<异常类型> <变量>) { }`
```java
// 捕获单个异常
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
}
```

---

**基本写法：多 catch**
`try { } catch (<异常1> <变量>) { } catch (<异常2> <变量>) { }`
```java
// 捕获多种异常分别处理
try {
} catch (ArithmeticException e) {
} catch (NullPointerException e) {
}
```

---

**基本写法：Java 7+ 多异常合并**
`try { } catch (<异常1> | <异常2> <变量>) { }`
```java
// 多种异常合并捕获
try {
} catch (IOException | SQLException e) {
}
```

---

**基本写法：try-catch-finally**
`try { } catch (<异常> <变量>) { } finally { }`
```java
// finally 块无论是否异常都执行
try {
} catch (Exception e) {
} finally {
}
```

---

**基本写法：try-finally**
`try { } finally { }`
```java
// 无 catch 仅 finally
try {
} finally {
}
```

---

## try-with-resources

**基本写法：自动资源管理**
`try (<资源声明>) { }`
```java
// 自动关闭实现 AutoCloseable 的资源
try (FileReader fr = new FileReader("file.txt")) {
}
```

---

**换行写法：多个资源**
`try (<资源1>; <资源2>) { }`
```java
// 管理多个资源按声明逆序关闭
try (
    FileReader fr = new FileReader("input.txt");
    FileWriter fw = new FileWriter("output.txt")
) {
}
```

---

**基本写法：try-with-resources 异常处理**
`try (<资源>) { } catch (<异常> <变量>) { }`
```java
// 自动关闭资源并捕获异常
try (FileReader fr = new FileReader("file.txt")) {
} catch (IOException e) {
}
```

---

## throw 抛出异常

**基本写法：抛出异常**
`throw new <异常类>("<消息>");`
```java
// 手动抛出异常
throw new IllegalArgumentException("Invalid parameter");
```

---

**基本写法：抛出已存在异常**
`throw <异常变量>;`
```java
// 重新抛出捕获的异常
throw e;
```

---

**基本写法：抛出带原因的异常**
`throw new <异常类>("<消息>", <原因>);`
```java
// 抛出异常并附带原因
throw new RuntimeException("Operation failed", cause);
```

---

## throws 声明异常

**基本写法：声明单个异常**
`<方法签名> throws <异常类型>`
```java
// 方法声明可能抛出的异常
public void readFile() throws IOException {
}
```

---

**单行写法：声明多个异常**
`<方法签名> throws <异常1>, <异常2>`
```java
// 方法声明抛出多种异常
public void process() throws IOException, SQLException {
}
```

---

**换行写法：声明多个异常**
`<方法签名> throws <异常1>, <异常2>, <异常3>`
```java
// 换行声明抛出多种异常
public void process()
        throws IOException,
        SQLException,
        ClassNotFoundException {
}
```

---

## 自定义异常

**基本写法：自定义检查异常**
`class <异常名> extends Exception { }`
```java
// 继承 Exception 定义检查异常
public class BusinessException extends Exception {
    public BusinessException(String message) {
        super(message);
    }
}
```

---

**基本写法：自定义运行时异常**
`class <异常名> extends RuntimeException { }`
```java
// 继承 RuntimeException 定义运行时异常
public class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}
```

---

**换行写法：带属性的自定义异常**
`class <异常名> extends Exception { private <字段>; <构造方法> <getter> }`
```java
// 自定义异常带额外属性
public class BusinessException extends Exception {
    private int errorCode;

    public BusinessException(int errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public int getErrorCode() {
        return errorCode;
    }
}
```

---

## 异常链

**基本写法：保留原始异常**
`throw new <异常类>("<消息>", <原始异常>);`
```java
// 抛出新异常并保留原始异常
try {
} catch (IOException e) {
    throw new BusinessException("File operation failed", e);
}
```

---

**基本写法：initCause 设置原因**
`<异常>.initCause(<原因>)`
```java
// 使用 initCause 设置异常原因
BusinessException be = new BusinessException("Error");
be.initCause(originalException);
throw be;
```

---

**基本写法：获取原始异常**
`<异常>.getCause()`
```java
// 获取异常的根本原因
Throwable cause = e.getCause();
```

---

## 异常信息获取

**基本写法：获取消息**
`<异常>.getMessage()`
```java
// 获取异常的详细消息
String message = e.getMessage();
```

---

**基本写法：获取堆栈**
`<异常>.getStackTrace()`
```java
// 获取异常的堆栈跟踪数组
StackTraceElement[] stack = e.getStackTrace();
```

---

**基本写法：打印堆栈**
`<异常>.printStackTrace()`
```java
// 打印异常堆栈到标准错误流
e.printStackTrace();
```

---

**基本写法：获取所有异常**
`<异常>.getSuppressed()`
```java
// 获取 try-with-resources 中被抑制的异常
Throwable[] suppressed = e.getSuppressed();
```

---

## 异常处理最佳实践

**基本写法：捕获具体异常**
`catch (<具体异常类型> <变量>)`
```java
// 捕获具体的异常类型而非通用 Exception
try {
} catch (FileNotFoundException e) {
}
```

---

**基本写法：异常不忽略**
`catch (<异常> <变量>) { <处理逻辑> }`
```java
// catch 块中必须有处理逻辑
try {
} catch (Exception e) {
    log.error("Error occurred", e);
}
```

---

**基本写法：finally 不 return**
`finally { <清理逻辑> }`
```java
// finally 块只做资源清理不返回值
try {
} finally {
    resource.close();
}
```

---

## 常见运行时异常

**基本写法：空指针异常**
`throw new NullPointerException("<消息>");`
```java
// 抛出空指针异常
throw new NullPointerException("Object is null");
```

---

**基本写法：数组越界异常**
`throw new ArrayIndexOutOfBoundsException(<索引>);`
```java
// 抛出数组越界异常
throw new ArrayIndexOutOfBoundsException(10);
```

---

**基本写法：类型转换异常**
`throw new ClassCastException("<消息>");`
```java
// 抛出类型转换异常
throw new ClassCastException("Cannot cast to String");
```

---

**基本写法：非法参数异常**
`throw new IllegalArgumentException("<消息>");`
```java
// 抛出非法参数异常
throw new IllegalArgumentException("Age must be positive");
```

---

**基本写法：非法状态异常**
`throw new IllegalStateException("<消息>");`
```java
// 抛出非法状态异常
throw new IllegalStateException("Connection is closed");
```

---

**基本写法：不支持操作异常**
`throw new UnsupportedOperationException();`
```java
// 抛出不支持操作异常
throw new UnsupportedOperationException();
```



<!-- ============ 文档分隔线：013-java/013-OperatorExpression.md ============ -->

# Java 运算符与表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 算术运算符

**基本写法：加法运算**
`<操作数1> + <操作数2>`
```java
// 两个整数相加
int sum = 10 + 3;
```

---

**基本写法：减法运算**
`<操作数1> - <操作数2>`
```java
// 两个整数相减
int diff = 10 - 3;
```

---

**基本写法：乘法运算**
`<操作数1> * <操作数2>`
```java
// 两个整数相乘
int product = 10 * 3;
```

---

**基本写法：除法运算**
`<操作数1> / <操作数2>`
```java
// 两个整数相除取整
int quotient = 10 / 3;
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`
```java
// 取余数
int remainder = 10 % 3;
```

---

## 自增自减

**基本写法：后置自增**
`<变量>++`
```java
// 先使用后加 1
int a = 5;
int b = a++;
```

---

**基本写法：前置自增**
`++<变量>`
```java
// 先加 1 后使用
int a = 5;
int b = ++a;
```

---

**基本写法：后置自减**
`<变量>--`
```java
// 先使用后减 1
int a = 5;
int b = a--;
```

---

**基本写法：前置自减**
`--<变量>`
```java
// 先减 1 后使用
int a = 5;
int b = --a;
```

---

## 字符串拼接

**基本写法：字符串拼接**
`<字符串> + <其他类型>`
```java
// 字符串与字符串拼接
String result = "Hello" + " " + "World";
```

---

**基本写法：字符串与数字拼接**
`<字符串> + <数字>`
```java
// 字符串与数字拼接
String result = "The answer is: " + 42;
```

---

## 关系运算符

**基本写法：等于比较**
`<操作数1> == <操作数2>`
```java
// 比较两个值是否相等
boolean result = (10 == 3);
```

---

**基本写法：不等于比较**
`<操作数1> != <操作数2>`
```java
// 比较两个值是否不相等
boolean result = (10 != 3);
```

---

**基本写法：大于比较**
`<操作数1> > <操作数2>`
```java
// 比较左边是否大于右边
boolean result = (10 > 3);
```

---

**基本写法：小于比较**
`<操作数1> < <操作数2>`
```java
// 比较左边是否小于右边
boolean result = (10 < 3);
```

---

**基本写法：大于等于比较**
`<操作数1> >= <操作数2>`
```java
// 比较左边是否大于等于右边
boolean result = (10 >= 3);
```

---

**基本写法：小于等于比较**
`<操作数1> <= <操作数2>`
```java
// 比较左边是否小于等于右边
boolean result = (10 <= 3);
```

---

**基本写法：引用类型内容比较**
`<对象1>.equals(<对象2>)`
```java
// 比较两个字符串内容是否相同
String s1 = "Hello";
String s2 = new String("Hello");
boolean result = s1.equals(s2);
```

---

## 逻辑运算符

**基本写法：短路与**
`<布尔表达式1> && <布尔表达式2>`
```java
// 第一个为 false 则不计算第二个
boolean result = (x > 10) && (x++ > 0);
```

---

**基本写法：短路或**
`<布尔表达式1> || <布尔表达式2>`
```java
// 第一个为 true 则不计算第二个
boolean result = (y < 10) || (y++ > 0);
```

---

**基本写法：逻辑非**
`!<布尔表达式>`
```java
// 对布尔值取反
boolean result = !flag;
```

---

**基本写法：逻辑异或**
`<布尔表达式1> ^ <布尔表达式2>`
```java
// 相同为 false 不同为 true
boolean result = true ^ false;
```

---

## 位运算符

**基本写法：按位与**
`<操作数1> & <操作数2>`
```java
// 二进制位与运算
int result = 6 & 3;
```

---

**基本写法：按位或**
`<操作数1> | <操作数2>`
```java
// 二进制位或运算
int result = 6 | 3;
```

---

**基本写法：按位异或**
`<操作数1> ^ <操作数2>`
```java
// 二进制位异或运算
int result = 6 ^ 3;
```

---

**基本写法：按位取反**
`~<操作数>`
```java
// 二进制位取反
int result = ~6;
```

---

**基本写法：左移**
`<操作数> << <位数>`
```java
// 二进制位左移相当于乘以 2
int result = 6 << 1;
```

---

**基本写法：右移**
`<操作数> >> <位数>`
```java
// 二进制位右移相当于除以 2
int result = 6 >> 1;
```

---

**基本写法：无符号右移**
`<操作数> >>> <位数>`
```java
// 高位补 0 的右移
int result = -6 >>> 1;
```

---

## 赋值运算符

**基本写法：简单赋值**
`<变量> = <值>`
```java
// 给变量赋值
int a = 10;
```

---

**基本写法：加法复合赋值**
`<变量> += <值>`
```java
// 等价于 a = a + 5
int a = 10;
a += 5;
```

---

**基本写法：减法复合赋值**
`<变量> -= <值>`
```java
// 等价于 a = a - 3
int a = 10;
a -= 3;
```

---

**基本写法：乘法复合赋值**
`<变量> *= <值>`
```java
// 等价于 a = a * 2
int a = 10;
a *= 2;
```

---

**基本写法：除法复合赋值**
`<变量> /= <值>`
```java
// 等价于 a = a / 4
int a = 10;
a /= 4;
```

---

**基本写法：取模复合赋值**
`<变量> %= <值>`
```java
// 等价于 a = a % 3
int a = 10;
a %= 3;
```

---

## 三元运算符

**基本写法：三元运算符**
`<条件表达式> ? <表达式1> : <表达式2>`
```java
// 根据条件选择值
int max = (a > b) ? a : b;
```

---

**基本写法：三元运算符赋值字符串**
`<条件> ? "<字符串1>" : "<字符串2>"`
```java
// 根据条件选择字符串
String result = (a > b) ? "a is larger" : "b is larger";
```

---

## 运算符优先级

**基本写法：使用括号明确顺序**
`(<表达式>)`
```java
// 使用括号改变运算顺序
int result = (a + b) * (c - d);
```

---

## 整数溢出处理

**基本写法：溢出检查加法**
`Math.addExact(<a>, <b>)`
```java
// 溢出时抛出 ArithmeticException
int result = Math.addExact(Integer.MAX_VALUE, 1);
```

---

**基本写法：使用更大类型**
`long <变量名> = <int变量> + <值>;`
```java
// 使用 long 类型避免溢出
long max = Integer.MAX_VALUE;
long result = max + 1;
```

---

## 字符串拼接性能

**基本写法：创建 StringBuilder**
`StringBuilder <变量名> = new StringBuilder();`
```java
// 创建 StringBuilder 对象
StringBuilder sb = new StringBuilder();
```

---

**基本写法：StringBuilder 追加**
`<StringBuilder>.append(<内容>)`
```java
// 追加内容到 StringBuilder
sb.append("Hello").append(" ").append("World");
```

---

**基本写法：转换为字符串**
`<StringBuilder>.toString()`
```java
// 将 StringBuilder 转换为字符串
String result = sb.toString();
```

---

## 位运算应用

**基本写法：位掩码定义**
`int <标志> = 1 << <位数>;`
```java
// 定义权限标志位
int FLAG_READ = 1 << 0;
```

---

**基本写法：位掩码组合**
`<标志1> | <标志2>`
```java
// 组合多个权限标志
int permissions = FLAG_READ | FLAG_WRITE;
```

---

**基本写法：检查位掩码**
`(<组合标志> & <单个标志>) != 0`
```java
// 检查是否包含某权限
boolean hasRead = (permissions & FLAG_READ) != 0;
```



<!-- ============ 文档分隔线：013-java/014-IOStreamFileOperation.md ============ -->

# Java IO 流与文件操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字节流

**基本写法：FileInputStream 创建**
`FileInputStream <变量> = new FileInputStream("<文件路径>");`
```java
// 创建字节输入流
FileInputStream fis = new FileInputStream("input.txt");
```

---

**基本写法：读取单字节**
`<fis>.read()`
```java
// 读取一个字节返回 -1 表示结束
int data = fis.read();
```

---

**基本写法：读取多字节**
`<fis>.read(byte[] <缓冲区>)`
```java
// 读取多个字节到缓冲区
byte[] buffer = new byte[1024];
int len = fis.read(buffer);
```

---

**基本写法：FileOutputStream 创建**
`FileOutputStream <变量> = new FileOutputStream("<文件路径>");`
```java
// 创建字节输出流
FileOutputStream fos = new FileOutputStream("output.txt");
```

---

**基本写法：写入字节**
`<fos>.write(<字节>)`
```java
// 写入单个字节
fos.write(65);
```

---

**基本写法：写入字节数组**
`<fos>.write(byte[] <数据>)`
```java
// 写入字节数组
fos.write(buffer);
```

---

**基本写法：关闭流**
`<流>.close();`
```java
// 关闭流释放资源
fis.close();
```

---

## 字符流

**基本写法：FileReader 创建**
`FileReader <变量> = new FileReader("<文件路径>");`
```java
// 创建字符输入流
FileReader fr = new FileReader("input.txt");
```

---

**基本写法：读取单字符**
`<fr>.read()`
```java
// 读取一个字符
int ch = fr.read();
```

---

**基本写法：读取多字符**
`<fr>.read(char[] <缓冲区>)`
```java
// 读取多个字符到缓冲区
char[] buffer = new char[1024];
int len = fr.read(buffer);
```

---

**基本写法：FileWriter 创建**
`FileWriter <变量> = new FileWriter("<文件路径>");`
```java
// 创建字符输出流
FileWriter fw = new FileWriter("output.txt");
```

---

**基本写法：写入字符串**
`<fw>.write("<字符串>")`
```java
// 写入字符串
fw.write("Hello, World!");
```

---

**基本写法：追加写入**
`FileWriter <变量> = new FileWriter("<文件路径>", true);`
```java
// 创建追加模式的 FileWriter
FileWriter fw = new FileWriter("log.txt", true);
```

---

## 缓冲流

**基本写法：BufferedReader 创建**
`BufferedReader <变量> = new BufferedReader(new FileReader("<文件>"));`
```java
// 创建带缓冲的字符输入流
BufferedReader br = new BufferedReader(new FileReader("input.txt"));
```

---

**基本写法：读取一行**
`<br>.readLine()`
```java
// 读取一行文本返回 null 表示结束
String line = br.readLine();
```

---

**基本写法：BufferedWriter 创建**
`BufferedWriter <变量> = new BufferedWriter(new FileWriter("<文件>"));`
```java
// 创建带缓冲的字符输出流
BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
```

---

**基本写法：写入并换行**
`<bw>.write("<字符串>"); <bw>.newLine();`
```java
// 写入字符串并换行
bw.write("Hello");
bw.newLine();
```

---

## try-with-resources

**基本写法：自动关闭资源**
`try (<资源声明>) { }`
```java
// 自动关闭实现 AutoCloseable 的资源
try (FileReader fr = new FileReader("file.txt")) {
}
```

---

**换行写法：多个资源自动关闭**
`try (<资源1>; <资源2>) { }`
```java
// 多个资源按声明逆序自动关闭
try (
    BufferedReader br = new BufferedReader(new FileReader("in.txt"));
    BufferedWriter bw = new BufferedWriter(new FileWriter("out.txt"))
) {
}
```

---

## File 类

**基本写法：创建 File 对象**
`File <变量> = new File("<路径>");`
```java
// 创建 File 对象
File file = new File("test.txt");
```

---

**基本写法：判断文件存在**
`<file>.exists()`
```java
// 判断文件或目录是否存在
boolean exists = file.exists();
```

---

**基本写法：判断是文件**
`<file>.isFile()`
```java
// 判断是否为文件
boolean isFile = file.isFile();
```

---

**基本写法：判断是目录**
`<file>.isDirectory()`
```java
// 判断是否为目录
boolean isDir = file.isDirectory();
```

---

**基本写法：创建文件**
`<file>.createNewFile()`
```java
// 创建新文件
boolean created = file.createNewFile();
```

---

**基本写法：创建目录**
`<file>.mkdir()`
```java
// 创建单层目录
boolean created = file.mkdir();
```

---

**基本写法：创建多层目录**
`<file>.mkdirs()`
```java
// 创建多层目录
boolean created = file.mkdirs();
```

---

**基本写法：删除文件**
`<file>.delete()`
```java
// 删除文件或目录
boolean deleted = file.delete();
```

---

**基本写法：获取文件名**
`<file>.getName()`
```java
// 获取文件名
String name = file.getName();
```

---

**基本写法：获取路径**
`<file>.getPath()`
```java
// 获取路径字符串
String path = file.getPath();
```

---

**基本写法：获取绝对路径**
`<file>.getAbsolutePath()`
```java
// 获取绝对路径
String absPath = file.getAbsolutePath();
```

---

**基本写法：获取文件大小**
`<file>.length()`
```java
// 获取文件字节数
long size = file.length();
```

---

**基本写法：列出目录文件**
`<file>.listFiles()`
```java
// 列出目录下的文件数组
File[] files = dir.listFiles();
```

---

## NIO Path

**基本写法：创建 Path**
`Path <变量> = Paths.get("<路径>");`
```java
// 创建 Path 对象
Path path = Paths.get("test.txt");
```

---

**基本写法：判断文件存在**
`Files.exists(<path>)`
```java
// 判断路径是否存在
boolean exists = Files.exists(path);
```

---

**基本写法：创建文件**
`Files.createFile(<path>)`
```java
// 创建新文件
Files.createFile(path);
```

---

**基本写法：创建目录**
`Files.createDirectory(<path>)`
```java
// 创建目录
Files.createDirectory(path);
```

---

**基本写法：删除文件**
`Files.delete(<path>)`
```java
// 删除文件不存在则抛异常
Files.delete(path);
```

---

**基本写法：复制文件**
`Files.copy(<源路径>, <目标路径>)`
```java
// 复制文件
Files.copy(source, target);
```

---

**基本写法：移动文件**
`Files.move(<源路径>, <目标路径>)`
```java
// 移动或重命名文件
Files.move(source, target);
```

---

## NIO 文件读写

**基本写法：读取所有字节**
`Files.readAllBytes(<path>)`
```java
// 读取文件所有字节
byte[] data = Files.readAllBytes(path);
```

---

**基本写法：读取所有行**
`Files.readAllLines(<path>)`
```java
// 读取文件所有行
List<String> lines = Files.readAllLines(path);
```

---

**基本写法：写入字节**
`Files.write(<path>, <字节数组>)`
```java
// 写入字节数组到文件
Files.write(path, data);
```

---

**基本写法：写入字符串**
`Files.writeString(<path>, "<字符串>")`
```java
// Java 11+ 写入字符串到文件
Files.writeString(path, "Hello");
```

---

**基本写法：读取字符串**
`Files.readString(<path>)`
```java
// Java 11+ 读取文件为字符串
String content = Files.readString(path);
```

---

## 对象序列化

**基本写法：实现 Serializable**
`class <类名> implements Serializable { }`
```java
// 类实现序列化接口
public class User implements Serializable {
}
```

---

**基本写法：序列化对象**
`new ObjectOutputStream(new FileOutputStream("<文件>")).writeObject(<对象>)`
```java
// 将对象写入文件
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("user.dat"))) {
    oos.writeObject(user);
}
```

---

**基本写法：反序列化对象**
`new ObjectInputStream(new FileInputStream("<文件>")).readObject()`
```java
// 从文件读取对象
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("user.dat"))) {
    User user = (User) ois.readObject();
}
```

---

**基本写法：transient 关键字**
`transient <类型> <字段名>;`
```java
// 标记字段不参与序列化
private transient String password;
```

---

**基本写法：serialVersionUID**
`private static final long serialVersionUID = <值>L;`
```java
// 定义序列化版本号
private static final long serialVersionUID = 1L;
```



<!-- ============ 文档分隔线：013-java/015-JavaRecordClass.md ============ -->

# Java 记录类

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 记录类定义

**单行写法：简单记录类**
`public record <记录名>(<类型1> <字段1>, <类型2> <字段2>) { }`
```java
// 单行定义简单记录类
public record Point(int x, int y) { }
```

---

**换行写法：多字段记录类**
`public record <记录名>(<类型1> <字段1>, <类型2> <字段2>, <类型3> <字段3>) { }`
```java
// 换行定义多字段记录类
public record User(
        String name,
        int age,
        String email
) { }
```

---

**基本写法：使用记录类**
`<记录名> <变量> = new <记录名>(<值1>, <值2>);`
```java
// 创建记录类实例
Point p = new Point(10, 20);
```

---

## 访问器方法

**基本写法：访问字段**
`<记录变量>.<字段名>()`
```java
// 获取记录类字段值
int x = p.x();
```

---

**基本写法：访问多个字段**
`<记录变量>.<字段1>(); <记录变量>.<字段2>();`
```java
// 获取多个字段值
int x = p.x();
int y = p.y();
```

---

## 自动生成方法

**基本写法：toString**
`<记录变量>.toString()`
```java
// 自动生成的 toString 方法
String str = p.toString();
```

---

**基本写法：equals**
`<记录变量1>.equals(<记录变量2>)`
```java
// 自动生成的 equals 方法比较字段值
boolean same = p1.equals(p2);
```

---

**基本写法：hashCode**
`<记录变量>.hashCode()`
```java
// 自动生成的 hashCode 方法
int hash = p.hashCode();
```

---

## 紧凑构造方法

**基本写法：紧凑构造方法验证**
`public <记录名> { if (<条件>) throw new <异常>; }`
```java
// 紧凑构造方法进行参数验证
public record Age(int value) {
    public Age {
        if (value < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
    }
}
```

---

**基本写法：紧凑构造方法规范化**
`public <记录名> { <字段> = <规范化值>; }`
```java
// 紧凑构造方法规范化字段值
public record Name(String value) {
    public Name {
        value = value.trim();
    }
}
```

---

## 自定义构造方法

**基本写法：规范构造方法**
`public <记录名>(<类型1> <参数1>, <类型2> <参数2>) { this.<字段1> = <参数1>; }`
```java
// 显式定义规范构造方法
public record Point(int x, int y) {
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

---

**基本写法：自定义构造方法**
`public <记录名>(<参数>) { this(<默认值>, <默认值>); }`
```java
// 自定义辅助构造方法
public record Point(int x, int y) {
    public Point() {
        this(0, 0);
    }
}
```

---

## 添加成员方法

**基本写法：添加实例方法**
`public <返回类型> <方法名>() { }`
```java
// 记录类中添加实例方法
public record Point(int x, int y) {
    public double distanceFromOrigin() {
        return Math.sqrt(x * x + y * y);
    }
}
```

---

**基本写法：添加静态方法**
`public static <返回类型> <方法名>() { }`
```java
// 记录类中添加静态方法
public record Point(int x, int y) {
    public static Point origin() {
        return new Point(0, 0);
    }
}
```

---

## 实现接口

**基本写法：记录类实现接口**
`public record <记录名>(<字段>) implements <接口> { }`
```java
// 记录类实现接口
public record Point(int x, int y) implements Comparable<Point> {
    @Override
    public int compareTo(Point other) {
        return Integer.compare(this.x, other.x);
    }
}
```

---

## 局部记录类

**基本写法：方法内定义记录类**
`record <记录名>(<类型> <字段>) { }`
```java
// 在方法内部定义局部记录类
public void process() {
    record Pair(int a, int b) { }
    Pair pair = new Pair(1, 2);
}
```

---

## 记录类与模式匹配

**基本写法：instanceof 模式匹配**
`if (<对象> instanceof <记录类>(<变量1>, <变量2>)) { }`
```java
// 记录类与 instanceof 模式匹配
if (obj instanceof Point(int x, int y)) {
}
```

---

**基本写法：switch 模式匹配**
`switch (<对象>) { case <记录类>(<变量1>, <变量2>) -> <结果>; }`
```java
// 记录类与 switch 模式匹配
String desc = switch (shape) {
    case Point(int x, int y) -> "Point at " + x + "," + y;
    default -> "Unknown";
};
```



<!-- ============ 文档分隔线：013-java/016-StreamAPI.md ============ -->

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



<!-- ============ 文档分隔线：013-java/017-LambdaFunctionalProgramming.md ============ -->

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



<!-- ============ 文档分隔线：013-java/018-CompletableFutureAsync.md ============ -->

# Java CompletableFuture 异步编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 CompletableFuture

**基本写法：supplyAsync 异步执行**
`CompletableFuture.supplyAsync(<Supplier>);`
```java
// 异步执行并返回结果
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "Result";
});
```

---

**基本写法：runAsync 无返回值**
`CompletableFuture.runAsync(<Runnable>);`
```java
// 异步执行无返回值任务
CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
    System.out.println("Running");
});
```

---

**基本写法：completedFuture 已完成**
`CompletableFuture.completedFuture(<值>);`
```java
// 创建已完成的 Future
CompletableFuture<String> future = CompletableFuture.completedFuture("Done");
```

---

## 获取结果

**基本写法：get 阻塞获取**
`<future>.get();`
```java
// 阻塞等待结果
String result = future.get();
```

---

**基本写法：get 超时获取**
`<future>.get(<超时>, <时间单位>);`
```java
// 最多等待 1 秒
String result = future.get(1, TimeUnit.SECONDS);
```

---

**基本写法：join 阻塞获取（不抛受检异常）**
`<future>.join();`
```java
// 阻塞获取结果
String result = future.join();
```

---

**基本写法：getNow 立即获取**
`<future>.getNow(<默认值>);`
```java
// 未完成则返回默认值
String result = future.getNow("Default");
```

---

## 结果处理

**基本写法：thenApply 转换结果**
`<future>.thenApply(<Function>);`
```java
// 转换结果类型
CompletableFuture<Integer> next = future.thenApply(String::length);
```

---

**基本写法：thenAccept 消费结果**
`<future>.thenAccept(<Consumer>);`
```java
// 消费结果（无返回值）
CompletableFuture<Void> next = future.thenAccept(System.out::println);
```

---

**基本写法：thenRun 不使用结果**
`<future>.thenRun(<Runnable>);`
```java
// 结果完成后执行其他操作
CompletableFuture<Void> next = future.thenRun(() -> {
    System.out.println("Done");
});
```

---

## 异步组合

**基本写法：thenCompose 串联**
`<future>.thenCompose(<Function>);`
```java
// 串联两个异步任务
CompletableFuture<String> next = future.thenCompose(s -> CompletableFuture.supplyAsync(() -> s + "!"));
```

---

**基本写法：thenCombine 合并两个**
`<future>.thenCombine(<other>, <BiFunction>);`
```java
// 合并两个独立 Future 的结果
CompletableFuture<String> combined = future1.thenCombine(future2, (s1, s2) -> s1 + s2);
```

---

**基本写法：allOf 等待全部完成**
`CompletableFuture.allOf(<future1>, <future2>, ...);`
```java
// 等待所有任务完成
CompletableFuture<Void> all = CompletableFuture.allOf(f1, f2, f3);
all.join();
```

---

**基本写法：anyOf 任一完成**
`CompletableFuture.anyOf(<future1>, <future2>, ...);`
```java
// 任一任务完成即返回
CompletableFuture<Object> any = CompletableFuture.anyOf(f1, f2);
Object result = any.get();
```

---

## 异常处理

**基本写法：exceptionally 异常恢复**
`<future>.exceptionally(<Function>);`
```java
// 发生异常时返回默认值
CompletableFuture<String> safe = future.exceptionally(ex -> "Fallback");
```

---

**基本写法：handle 处理结果与异常**
`<future>.handle(<BiFunction>);`
```java
// 同时处理正常结果与异常
CompletableFuture<String> handled = future.handle((result, ex) -> {
    if (ex != null) return "Error";
    return result;
});
```

---

**基本写法：whenComplete 完成时执行**
`<future>.whenComplete(<BiConsumer>);`
```java
// 完成时执行副作用（不改变结果）
CompletableFuture<String> next = future.whenComplete((result, ex) -> {
    if (ex != null) {
        log.error("Failed", ex);
    }
});
```

---

## 线程池控制

**基本写法：指定线程池**
`CompletableFuture.supplyAsync(<Supplier>, <Executor>);`
```java
// 使用自定义线程池
ExecutorService executor = Executors.newFixedThreadPool(10);
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> "Result", executor);
```

---

**基本写法：thenApplyAsync 异步转换**
`<future>.thenApplyAsync(<Function>, [<Executor>]);`
```java
// 在默认或指定线程池中异步执行
CompletableFuture<Integer> next = future.thenApplyAsync(String::length, executor);
```

---

## 多任务编排

**基本写法：thenAcceptBoth 消费两个结果**
`<future>.thenAcceptBoth(<other>, <BiConsumer>);`
```java
// 消费两个 Future 的结果
future1.thenAcceptBoth(future2, (s1, s2) -> {
    System.out.println(s1 + s2);
});
```

---

**基本写法：runAfterBoth 都完成后执行**
`<future>.runAfterBoth(<other>, <Runnable>);`
```java
// 两个 Future 都完成后执行
future1.runAfterBoth(future2, () -> {
    System.out.println("Both done");
});
```

---

**基本写法：runAfterEither 任一完成后执行**
`<future>.runAfterEither(<other>, <Runnable>);`
```java
// 任一 Future 完成后执行
future1.runAfterEither(future2, () -> {
    System.out.println("One done");
});
```

---

**基本写法：applyToEither 取先完成的结果**
`<future>.applyToEither(<other>, <Function>);`
```java
// 取先完成的 Future 结果转换
CompletableFuture<String> next = future1.applyToEither(future2, s -> s + "!");
```



<!-- ============ 文档分隔线：013-java/019-SpringBasicsIoCAOPBeanLifecycle.md ============ -->

# Spring 框架核心注解速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 组件注册

**基本写法：@Component 通用组件**
`@Component [("<bean名称>")]`
```java
// 注册为 Spring Bean
@Component
public class UserService { }
```

---

**基本写法：@Service 业务层**
`@Service [("<bean名称>")]`
```java
// 标记业务逻辑层组件
@Service
public class UserService { }
```

---

**基本写法：@Repository 持久层**
`@Repository [("<bean名称>")]`
```java
// 标记数据访问层组件
@Repository
public class UserRepository { }
```

---

**基本写法：@Controller 控制层**
`@Controller [("<bean名称>")]`
```java
// 标记 MVC 控制器
@Controller
public class HomeController { }
```

---

**基本写法：@RestController REST 控制器**
`@RestController`
```java
// 等同于 @Controller + @ResponseBody
@RestController
public class ApiController { }
```

---

**基本写法：@Configuration 配置类**
`@Configuration`
```java
// 声明配置类
@Configuration
public class AppConfig { }
```

---

**基本写法：@Bean 声明 Bean**
`@Bean [("<名称>")]`
```java
// 在配置类中声明 Bean
@Bean
public DataSource dataSource() {
    return new HikariDataSource();
}
```

---

## 依赖注入

**基本写法：@Autowired 按类型注入**
`@Autowired`
```java
// 按类型自动注入
@Autowired
private UserRepository userRepository;
```

---

**基本写法：@Autowired 构造方法注入**
`@Autowired` （构造方法上方）
```java
// 推荐的构造方法注入
@Autowired
public UserService(UserRepository userRepository) {
    this.userRepository = userRepository;
}
```

---

**基本写法：@Qualifier 按名称注入**
`@Qualifier("<bean名称>")`
```java
// 指定注入的 Bean 名称
@Autowired
@Qualifier("primaryDataSource")
private DataSource dataSource;
```

---

**基本写法：@Resource 按名称注入**
`@Resource(name = "<bean名称>")`
```java
// JSR-250 标准注解
@Resource(name = "userRepository")
private UserRepository userRepository;
```

---

**基本写法：@Value 注入配置值**
`@Value("${<属性键>}")`
```java
// 注入配置文件中的值
@Value("${app.name}")
private String appName;
```

---

## 作用域

**基本写法：@Scope 单例**
`@Scope("singleton")`
```java
// 单例作用域（默认）
@Scope("singleton")
@Component
public class SingletonService { }
```

---

**基本写法：@Scope 原型**
`@Scope("prototype")`
```java
// 每次注入都创建新实例
@Scope("prototype")
@Component
public class PrototypeService { }
```

---

## AOP 切面

**基本写法：@Aspect 声明切面**
`@Aspect`
```java
// 声明切面类
@Aspect
@Component
public class LogAspect { }
```

---

**基本写法：@Pointcut 切入点**
`@Pointcut("<切入点表达式>")`
```java
// 定义切入点
@Pointcut("execution(* com.example.service.*.*(..))")
public void serviceMethods() { }
```

---

**基本写法：@Before 前置通知**
`@Before("<切入点>")`
```java
// 方法执行前执行
@Before("serviceMethods()")
public void beforeLog(JoinPoint jp) {
    System.out.println("Before: " + jp.getSignature());
}
```

---

**基本写法：@After 后置通知**
`@After("<切入点>")`
```java
// 方法执行后执行（无论是否异常）
@After("serviceMethods()")
public void afterLog() { }
```

---

**基本写法：@AfterReturning 返回通知**
`@AfterReturning(pointcut = "<切入点>", returning = "<结果变量>")`
```java
// 方法成功返回后执行
@AfterReturning(pointcut = "serviceMethods()", returning = "result")
public void afterReturning(Object result) { }
```

---

**基本写法：@AfterThrowing 异常通知**
`@AfterThrowing(pointcut = "<切入点>", throwing = "<异常变量>")`
```java
// 方法抛出异常后执行
@AfterThrowing(pointcut = "serviceMethods()", throwing = "ex")
public void afterThrowing(Exception ex) { }
```

---

**基本写法：@Around 环绕通知**
`@Around("<切入点>")`
```java
// 环绕通知（最强大）
@Around("serviceMethods()")
public Object around(ProceedingJoinPoint pjp) throws Throwable {
    long start = System.currentTimeMillis();
    Object result = pjp.proceed();
    System.out.println("Cost: " + (System.currentTimeMillis() - start));
    return result;
}
```

---

## 生命周期

**基本写法：@PostConstruct 初始化**
`@PostConstruct`
```java
// Bean 初始化完成后执行
@PostConstruct
public void init() {
    System.out.println("Initialized");
}
```

---

**基本写法：@PreDestroy 销毁前**
`@PreDestroy`
```java
// Bean 销毁前执行
@PreDestroy
public void cleanup() {
    System.out.println("Cleanup");
}
```

---

## 条件装配

**基本写法：@Conditional 条件注册**
`@Conditional(<条件类>.class)`
```java
// 满足条件才注册 Bean
@Bean
@Conditional(OnLinuxCondition.class)
public DataSource linuxDataSource() { }
```

---

**基本写法：@Profile 环境配置**
`@Profile("<环境>")`
```java
// 仅在指定环境生效
@Bean
@Profile("dev")
public DataSource devDataSource() { }
```

---

**基本写法：@ConditionalOnProperty 属性条件**
`@ConditionalOnProperty(name = "<属性>", havingValue = "<值>")`
```java
// 配置属性满足条件时注册
@Bean
@ConditionalOnProperty(name = "cache.enabled", havingValue = "true")
public CacheService cacheService() { }
```



<!-- ============ 文档分隔线：013-java/020-SpringBootAdvanced.md ============ -->

# Java SpringBoot 进阶配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## application.yml 基础配置

**基本写法：服务端口与上下文配置**
`server.port: <端口>`
```java
// application.yml
server:
  port: 8081
  servlet:
    context-path: /api
```

---

**基本写法：应用名称配置**
`spring.application.name: <名称>`
```java
// 应用名称（SpringBoot 2.7+ 推荐写法）
spring:
  application:
    name: my-app
```

---

**基本写法：多环境配置**
`spring.profiles.active: <profile>`
```java
// 激活 dev 环境
spring:
  profiles:
    active: dev
```

---

**基本写法：自定义配置项**
`<前缀>.<字段>: <值>`
```java
// application.yml 自定义属性
app:
  cache:
    ttl: 3600
    maxSize: 1000
```

---

## 读取配置

**基本写法：使用 @Value 注入**
`@Value("${<属性名>}")`
```java
// 注入单个配置项
@Value("${app.cache.ttl}")
private long cacheTtl;
```

---

**基本写法：使用 @ConfigurationProperties 绑定**
`@ConfigurationProperties(prefix = "<前缀>")`
```java
// 批量绑定配置到对象
@Component
@ConfigurationProperties(prefix = "app.cache")
public class CacheProperties {
    private long ttl;
    private int maxSize;
}
```

---

**基本写法：注入 Environment**
`@Autowired Environment <env>`
```java
// 通过 Environment 动态读取配置
@Autowired
private Environment env;
String ttl = env.getProperty("app.cache.ttl");
```

---

## 核心注解

**基本写法：启动类注解**
`@SpringBootApplication`
```java
// 标记 SpringBoot 启动类
@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
```

---

**基本写法：自定义 Component 扫描**
`@ComponentScan(basePackages = {"<包1>", "<包2>"})`
```java
// 指定扫描的包路径
@SpringBootApplication
@ComponentScan(basePackages = {"com.example.service", "com.example.dao"})
public class App { }
```

---

**基本写法：排除自动配置**
`@SpringBootApplication(exclude = {<配置类>.class})`
```java
// 排除数据源自动配置
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class App { }
```

---

**基本写法：定义 Bean**
`@Bean`
```java
// 在配置类中声明 Bean
@Configuration
public class AppConfig {
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

---

**基本写法：条件化 Bean**
`@ConditionalOnProperty(name = "<属性>", havingValue = "<值>")`
```java
// 仅在配置项匹配时生效
@Bean
@ConditionalOnProperty(name = "app.cache.enabled", havingValue = "true")
public CacheManager cacheManager() {
    return new ConcurrentMapCacheManager();
}
```

---

**基本写法：缺失时创建**
`@ConditionalOnMissingBean(<类型>.class)`
```java
// 容器中无该类型 Bean 时才创建
@Bean
@ConditionalOnMissingBean(RestTemplate.class)
public RestTemplate defaultRestTemplate() {
    return new RestTemplate();
}
```

---

## 自动配置机制

**基本写法：自定义 AutoConfiguration**
`@AutoConfiguration`
```java
// SpringBoot 2.7+ 自动配置类写法
@AutoConfiguration
@ConditionalOnClass(RestTemplate.class)
public class MyAutoConfiguration {
    @Bean
    @ConditionalOnMissingBean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

---

**基本写法：注册自动配置**
`META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`
```java
// 文件内每行写一个全限定类名
com.example.MyAutoConfiguration
com.example.OtherAutoConfiguration
```

---

## Profile 环境

**基本写法：声明 Profile Bean**
`@Profile("<名称>")`
```java
// 仅在 dev 环境生效
@Bean
@Profile("dev")
public DataSource devDataSource() {
    return new HikariDataSource();
}
```

---

**基本写法：Profile 配置文件**
`application-<profile>.yml`
```java
// 文件名约定：application-dev.yml、application-prod.yml
// 激活 dev 后会合并 application.yml 与 application-dev.yml
```

---

## 条件装配

**基本写法：类路径存在时生效**
`@ConditionalOnClass(<类>.class)`
```java
// 类路径存在该类时配置才生效
@Configuration
@ConditionalOnClass(RestTemplate.class)
public class WebConfig { }
```

---

**基本写法：Bean 存在时生效**
`@ConditionalOnBean(<类型>.class)`
```java
// 容器中存在 DataSource 时生效
@Bean
@ConditionalOnBean(DataSource.class)
public JdbcTemplate jdbcTemplate(DataSource ds) {
    return new JdbcTemplate(ds);
}
```

---

## 常用 Starter 依赖

**基本写法：Web Starter**
`spring-boot-starter-web`
```java
// pom.xml 引入后自动配置 Tomcat + Spring MVC
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

---

**基本写法：数据访问 Starter**
`spring-boot-starter-data-jpa`
```java
// 引入后自动配置 Hibernate + JPA
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

---

## 启动与运行

**基本写法：以编程方式启动**
`SpringApplication.run(<配置类>.class, <args>)`
```java
// 通过 API 启动并定制
new SpringApplicationBuilder(App.class)
    .bannerMode(Banner.Mode.OFF)
    .logStartupInfo(false)
    .run(args);
```

---

**基本写法：命令行传参**
`--<属性名>=<值>`
```java
// 启动时覆盖配置
java -jar app.jar --server.port=9090 --spring.profiles.active=prod
```

---

**基本写法：CommandLineRunner 初始化**
`@Bean CommandLineRunner <方法>`
```java
// 启动完成后执行
@Bean
public CommandLineRunner init(DataService service) {
    return args -> service.loadData();
}
```

---

## 外部化配置加载顺序

**基本写法：命令行参数优先级最高**
`java -jar <jar> --<属性>=<值>`
```java
// 优先级（从高到低）：
// 命令行参数 > 环境变量 > application-{profile}.yml > application.yml
java -jar app.jar --server.port=9090
```



<!-- ============ 文档分隔线：013-java/021-JavaUnitTest.md ============ -->

# Java 单元测试 JUnit 5

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Maven 依赖

**基本写法：引入 JUnit 5**
`<artifactId>junit-jupiter</artifactId>`
```java
// pom.xml 引入 JUnit 5（Jupiter 聚合包）
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.12.1</version>
    <scope>test</scope>
</dependency>
```

---

## 测试方法

**基本写法：标记测试方法**
`@Test`
```java
// 标记一个测试方法（无返回值）
@Test
void shouldAddTwoNumbers() {
    assertEquals(4, 2 + 2);
}
```

---

**基本写法：显示名称**
`@DisplayName("<名称>")`
```java
// 自定义测试报告显示名
@Test
@DisplayName("当输入 1 和 2 时应返回 3")
void shouldReturnThree() {
    assertEquals(3, 1 + 2);
}
```

---

**基本写法：禁用测试**
`@Disabled("<原因>")`
```java
// 临时禁用测试
@Test
@Disabled("待实现的功能")
void notReadyYet() { }
```

---

## 生命周期

**基本写法：所有测试前执行一次**
`@BeforeAll`
```java
// 必须为 static，常用于全局初始化
@BeforeAll
static void initAll() {
    System.out.println("全部测试开始前执行");
}
```

---

**基本写法：所有测试后执行一次**
`@AfterAll`
```java
// 必须为 static，常用于全局清理
@AfterAll
static void cleanupAll() {
    System.out.println("全部测试结束后执行");
}
```

---

**基本写法：每个测试前执行**
`@BeforeEach`
```java
// 每个测试方法执行前都会调用
@BeforeEach
void init() {
    list = new ArrayList<>();
}
```

---

**基本写法：每个测试后执行**
`@AfterEach`
```java
// 每个测试方法执行后都会调用
@AfterEach
void tearDown() {
    list.clear();
}
```

---

## 断言 Assertions

**基本写法：相等断言**
`assertEquals(<期望>, <实际>)`
```java
// 验证两值相等
assertEquals(4, calculator.add(2, 2));
```

---

**基本写法：不相等断言**
`assertNotEquals(<期望>, <实际>)`
```java
// 验证两值不相等
assertNotEquals(5, calculator.add(2, 2));
```

---

**基本写法：为真断言**
`assertTrue(<条件>)`
```java
// 验证条件为 true
assertTrue(list.isEmpty());
```

---

**基本写法：为假断言**
`assertFalse(<条件>)`
```java
// 验证条件为 false
assertFalse(list.contains("x"));
```

---

**基本写法：空对象断言**
`assertNull(<对象>)`
```java
// 验证对象为 null
assertNull(service.find(-1));
```

---

**基本写法：非空断言**
`assertNotNull(<对象>)`
```java
// 验证对象不为 null
assertNotNull(service.find(1));
```

---

**基本写法：抛出异常断言**
`assertThrows(<异常类>.class, <Executable>)`
```java
// 验证代码块抛出指定异常
assertThrows(ArithmeticException.class, () -> {
    int x = 1 / 0;
});
```

---

**基本写法：带消息断言**
`assertEquals(<期望>, <实际>, <消息>)`
```java
// 断言失败时显示自定义消息（Supplier 延迟构造）
assertEquals(4, result, () -> "计算结果应为 4，实际为 " + result);
```

---

**基本写法：批量断言**
`assertAll(<Executable>...)`
```java
// 多个断言一起执行，互不影响
assertAll(
    () -> assertEquals("Alice", user.getName()),
    () -> assertEquals(30, user.getAge()),
    () -> assertNotNull(user.getEmail())
);
```

---

**基本写法：超时断言**
`assertTimeout(<Duration>, <Executable>)`
```java
// 验证代码块在指定时间内完成
assertTimeout(Duration.ofMillis(100), () -> {
    Thread.sleep(50);
});
```

---

## 参数化测试

**基本写法：标记参数化测试**
`@ParameterizedTest`
```java
// 需配合参数源注解使用
@ParameterizedTest
@ValueSource(strings = {"a", "b", "c"})
void shouldNotBeNull(String input) {
    assertNotNull(input);
}
```

---

**基本写法：值源参数**
`@ValueSource(strings = {...})`
```java
// 提供简单类型参数数组
@ParameterizedTest
@ValueSource(ints = {1, 2, 3, 4})
void shouldbePositive(int n) {
    assertTrue(n > 0);
}
```

---

**基本写法：CSV 源参数**
`@CsvSource({ "<值1>,<值2>" })`
```java
// 多参数 CSV 形式
@ParameterizedTest
@CsvSource({ "1, 2, 3", "4, 5, 9" })
void shouldAdd(int a, int b, int expected) {
    assertEquals(expected, a + b);
}
```

---

**基本写法：方法源参数**
`@MethodSource("<方法名>")`
```java
// 静态方法返回参数流
@ParameterizedTest
@MethodSource("provideArgs")
void shouldTest(String input, int expected) {
    assertEquals(expected, input.length());
}
static Stream<Arguments> provideArgs() {
    return Stream.of(Arguments.of("abc", 3), Arguments.of("hello", 5));
}
```

---

**基本写法：空与 null 源**
`@NullSource` / `@EmptySource`
```java
// 提供单 null 或空值
@ParameterizedTest
@NullSource
@EmptySource
void shouldHandleNullOrEmpty(String input) {
    assertTrue(input == null || input.isEmpty());
}
```

---

## 嵌套测试

**基本写法：嵌套测试类**
`@Nested`
```java
// 非静态内部类，按组组织测试
@Nested
class WhenListIsEmpty {
    @Test
    void shouldReturnTrue() {
        assertTrue(list.isEmpty());
    }
}
```

---

## 假设 Assumptions

**基本写法：满足假设才执行**
`assumeTrue(<条件>)`
```java
// 条件不成立则跳过测试
@Test
void shouldRunOnlyOnLinux() {
    assumeTrue(System.getProperty("os.name").contains("Linux"));
    // 仅在 Linux 下执行后续断言
}
```

---

**基本写法：满足假设才执行（带 lambda）**
`assumingThat(<条件>, <Executable>)`
```java
// 条件成立才执行代码块，否则跳过但不失败
@Test
void shouldTestConditionally() {
    assumingThat("dev".equals(env), () -> {
        assertEquals("debug", config.getMode());
    });
}
```

---

## 测试执行顺序

**基本写法：方法排序**
`@TestMethodOrder(MethodOrderer.OrderAnnotation.class)`
```java
// 按 @Order 注解顺序执行
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class OrderedTest {
    @Test @Order(1) void first() { }
    @Test @Order(2) void second() { }
}
```

---

**基本写法：随机顺序**
`@TestMethodOrder(MethodOrderer.Random.class)`
```java
// 随机执行顺序（避免依赖隐式顺序）
@TestMethodOrder(MethodOrderer.Random.class)
class RandomTest { }
```

---

## 标签与过滤

**基本写法：标记标签**
`@Tag("<标签名>")`
```java
// 给测试打标签便于过滤执行
@Test
@Tag("slow")
void shouldRunSlowTest() { }
```

---

## 临时目录

**基本写法：临时目录**
`@TempDir`
```java
// 自动创建并清理临时目录
@Test
void shouldWriteFile(@TempDir Path dir) throws IOException {
    Path file = dir.resolve("test.txt");
    Files.writeString(file, "hello");
    assertTrue(Files.exists(file));
}
```

---

## 重复测试

**基本写法：重复执行**
`@RepeatedTest(<次数>)`
```java
// 重复执行同一测试 N 次
@RepeatedTest(value = 5, name = "第 {currentRepetition} 次")
void shouldRepeat() {
    assertTrue(true);
}
```

---

## Mock 框架（Mockito）

**基本写法：创建 Mock**
`Mockito.mock(<类>.class)`
```java
// 创建模拟对象
List<String> mockList = Mockito.mock(List.class);
when(mockList.size()).thenReturn(10);
assertEquals(10, mockList.size());
```

---

**基本写法：验证调用**
`verify(<mock>).<方法>(<参数>)`
```java
// 验证方法是否被调用
verify(mockList).add("hello");
verify(mockList, times(2)).size();
```

---

**基本写法：注解方式 Mock**
`@Mock`
```java
// 配合 @ExtendWith(MockitoExtension.class) 使用
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock
    private UserRepository repo;
    @InjectMocks
    private UserService service;
}
```



<!-- ============ 文档分隔线：013-java/022-ConcurrencyDetailed.md ============ -->

# Java 并发工具速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Lock 锁机制

**基本写法：使用 ReentrantLock**
`ReentrantLock <lock> = new ReentrantLock()`
```java
// 显式加锁与释放锁（必须在 finally 中释放）
ReentrantLock lock = new ReentrantLock();
lock.lock();
try {
    // 临界区代码
} finally {
    lock.unlock();
}
```

---

**基本写法：可中断锁获取**
`<lock>.lockInterruptibly()`
```java
// 等待锁过程中可被中断
lock.lockInterruptibly();
try {
    // 临界区代码
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
} finally {
    lock.unlock();
}
```

---

**基本写法：尝试获取锁**
`<lock>.tryLock(<超时>, <单位>)`
```java
// 尝试在 3 秒内获取锁，失败则跳过
if (lock.tryLock(3, TimeUnit.SECONDS)) {
    try {
        // 获取锁成功
    } finally {
        lock.unlock();
    }
}
```

---

**基本写法：读写锁**
`ReentrantReadWriteLock`
```java
// 读多写少场景提升并发度
ReentrantReadWriteLock rwLock = new ReentrantReadWriteLock();
rwLock.readLock().lock();
try { /* 读操作 */ } finally { rwLock.readLock().unlock(); }
rwLock.writeLock().lock();
try { /* 写操作 */ } finally { rwLock.writeLock().unlock(); }
```

---

**基本写法：Condition 条件变量**
`<lock>.newCondition()`
```java
// 配合 Lock 实现等待/通知
Condition notEmpty = lock.newCondition();
lock.lock();
try {
    while (queue.isEmpty()) {
        notEmpty.await();
    }
    // 消费元素
} finally {
    lock.unlock();
}
```

---

## CountDownLatch 倒计时门闩

**基本写法：等待 N 个线程完成**
`CountDownLatch <latch> = new CountDownLatch(<count>)`
```java
// 主线程等待所有工作线程完成
CountDownLatch latch = new CountDownLatch(3);
for (int i = 0; i < 3; i++) {
    new Thread(() -> {
        try { doWork(); } finally { latch.countDown(); }
    }).start();
}
latch.await();
```

---

**基本写法：带超时等待**
`<latch>.await(<超时>, <单位>)`
```java
// 最多等待 5 秒
boolean done = latch.await(5, TimeUnit.SECONDS);
if (!done) { /* 超时处理 */ }
```

---

**基本写法：递减计数**
`<latch>.countDown()`
```java
// 计数减 1，归零时唤醒 await 的线程
latch.countDown();
```

---

## CyclicBarrier 循环屏障

**基本写法：N 个线程到达屏障后统一放行**
`CyclicBarrier <barrier> = new CyclicBarrier(<count>)`
```java
// 3 个线程都到达后才继续执行
CyclicBarrier barrier = new CyclicBarrier(3);
new Thread(() -> {
    barrier.await(); // 等待其他线程
}).start();
```

---

**基本写法：屏障动作**
`new CyclicBarrier(<count>, <Runnable>)`
```java
// 所有线程到达后执行一次动作
CyclicBarrier barrier = new CyclicBarrier(3, () -> {
    System.out.println("所有线程到达屏障");
});
barrier.await();
```

---

## Semaphore 信号量

**基本写法：限流并发访问**
`Semaphore <sem> = new Semaphore(<许可数>)`
```java
// 同时只允许 5 个线程访问资源
Semaphore sem = new Semaphore(5);
sem.acquire();
try {
    // 访问受限资源
} finally {
    sem.release();
}
```

---

**基本写法：批量获取许可**
`<sem>.acquire(<数量>)`
```java
// 一次获取 3 个许可
sem.acquire(3);
try { /* 资源使用 */ } finally { sem.release(3); }
```

---

## ConcurrentHashMap

**基本写法：创建并发 Map**
`new ConcurrentHashMap<K, V>()`
```java
// 线程安全的 HashMap
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
map.put("a", 1);
```

---

**基本写法：原子更新**
`<map>.compute(<key>, <BiFunction>)`
```java
// 原子地更新指定 key 的值
map.compute("a", (k, v) -> v == null ? 1 : v + 1);
```

---

**基本写法：不存在时放入**
`<map>.putIfAbsent(<key>, <value>)`
```java
// 仅当 key 不存在时才放入
map.putIfAbsent("b", 100);
```

---

**基本写法：合并值**
`<map>.merge(<key>, <默认值>, <BiFunction>)`
```java
// 统计词频的惯用写法
map.merge(word, 1, Integer::sum);
```

---

**基本写法：原子替换**
`<map>.replace(<key>, <旧值>, <新值>)`
```java
// CAS 替换，旧值匹配才更新
boolean ok = map.replace("a", 1, 2);
```

---

## 原子类

**基本写法：原子整数**
`AtomicInteger <ai> = new AtomicInteger(<初始值>)`
```java
// 无锁线程安全的整数
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();
int now = counter.get();
```

---

**基本写法：CAS 更新**
`<ai>.compareAndSet(<期望值>, <新值>)`
```java
// 期望值匹配才更新
boolean updated = counter.compareAndSet(0, 1);
```

---

**基本写法：累加器（高并发更优）**
`LongAdder <adder> = new LongAdder()`
```java
// 高并发计数性能优于 AtomicLong
LongAdder adder = new LongAdder();
adder.increment();
long sum = adder.sum();
```

---

**基本写法：原子引用**
`AtomicReference<T> <ref> = new AtomicReference<>(<初始值>)`
```java
// 引用类型的原子更新
AtomicReference<String> ref = new AtomicReference<>("init");
ref.compareAndSet("init", "updated");
```

---

**基本写法：字段原子更新器**
`AtomicIntegerFieldUpdater.newUpdater(<类>.class, "<字段名>")`
```java
// 对 volatile 字段进行原子更新
class Account {
    volatile int balance;
}
AtomicIntegerFieldUpdater<Account> u =
    AtomicIntegerFieldUpdater.newUpdater(Account.class, "balance");
u.incrementAndGet(account);
```

---

## 并发集合

**基本写法：阻塞队列**
`ArrayBlockingQueue<E> <q> = new ArrayBlockingQueue<>(<容量>)`
```java
// 生产者-消费者模式
ArrayBlockingQueue<String> q = new ArrayBlockingQueue<>(100);
q.put("task");          // 队列满则阻塞
String task = q.take(); // 队列空则阻塞
```

---

**基本写法：并发链表队列**
`ConcurrentLinkedQueue<E>`
```java
// 无界非阻塞队列（基于 CAS）
ConcurrentLinkedQueue<Integer> q = new ConcurrentLinkedQueue<>();
q.offer(1);
Integer head = q.poll();
```

---

**基本写法：并发跳表 Map**
`ConcurrentSkipListMap<K, V>`
```java
// 线程安全的有序 Map
ConcurrentSkipListMap<String, Integer> map = new ConcurrentSkipListMap<>();
map.put("b", 2);
map.put("a", 1);
```

---

## 线程池

**基本写法：固定大小线程池**
`Executors.newFixedThreadPool(<大小>)`
```java
// 固定线程数的线程池
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> System.out.println("task"));
pool.shutdown();
```

---

**基本写法：自定义线程池**
`new ThreadPoolExecutor(...)`
```java
// 推荐方式，参数可控
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(1000),
    Executors.defaultThreadFactory(),
    new ThreadPoolExecutor.CallerRunsPolicy()
);
```

---

**基本写法：定时任务线程池**
`Executors.newScheduledThreadPool(<大小>)`
```java
// 延迟或周期执行任务
ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
scheduler.scheduleAtFixedRate(() -> doWork(), 0, 1, TimeUnit.SECONDS);
```

---

**基本写法：优雅关闭**
`<pool>.shutdown()` + `<pool>.awaitTermination(...)`
```java
// 优雅关闭线程池
pool.shutdown();
if (!pool.awaitTermination(60, TimeUnit.SECONDS)) {
    pool.shutdownNow();
}
```

---

## 同步工具

**基本写法：交换器**
`Exchanger<T>`
```java
// 两个线程交换数据
Exchanger<String> exchanger = new Exchanger<>();
String received = exchanger.exchange("data");
```

---

**基本写法：同步队列**
`SynchronousQueue<E>`
```java
// 无容量，put 必须等待 take
SynchronousQueue<String> q = new SynchronousQueue<>();
new Thread(() -> q.put("hello")).start();
String data = q.take();
```

---

## CompletableFuture 并发

**基本写法：异步执行任务**
`CompletableFuture.supplyAsync(<Supplier>)`
```java
// 异步执行有返回值的任务
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return fetchData();
});
String result = future.get();
```

---

**基本写法：链式转换**
`<future>.thenApply(<Function>)`
```java
// 任务完成后转换结果
CompletableFuture<Integer> f = future.thenApply(String::length);
```

---

**基本写法：组合两个任务**
`<future1>.thenCombine(<future2>, <BiFunction>)`
```java
// 等两个任务都完成后合并结果
CompletableFuture<Integer> combined = f1.thenCombine(f2, (a, b) -> a + b);
```

---

**基本写法：等待全部完成**
`CompletableFuture.allOf(<future>...)`
```java
// 等待所有任务完成
CompletableFuture.allOf(f1, f2, f3).join();
```

---

## ThreadLocal

**基本写法：线程本地变量**
`ThreadLocal<T> <tl> = new ThreadLocal<>()`
```java
// 每个线程独立副本
ThreadLocal<SimpleDateFormat> tl =
    ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyy-MM-dd"));
String date = tl.get().format(new Date());
tl.remove(); // 用完清理避免内存泄漏
```



<!-- ============ 文档分隔线：013-java/023-JavaNewFeatures.md ============ -->

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



<!-- ============ 文档分隔线：013-java/024-JavaVirtualThread.md ============ -->

# Java 虚拟线程 API 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建虚拟线程

**基本写法：快速启动虚拟线程**
`Thread.startVirtualThread(<Runnable>)`
```java
// 创建并立即启动一个虚拟线程（Java 21+）
Thread vt = Thread.startVirtualThread(() -> {
    System.out.println("运行于: " + Thread.currentThread());
});
vt.join();
```

---

**基本写法：使用 Builder 创建**
`Thread.ofVirtual().start(<Runnable>)`
```java
// 通过 Builder 创建并启动
Thread vt = Thread.ofVirtual().start(() -> {
    doWork();
});
```

---

**基本写法：创建未启动的虚拟线程**
`Thread.ofVirtual().unstarted(<Runnable>)`
```java
// 先创建 Thread 引用，后续手动 start
Thread vt = Thread.ofVirtual().name("worker-1").unstarted(() -> doWork());
vt.start();
```

---

**基本写法：命名虚拟线程**
`Thread.ofVirtual().name(<名称>).start(...)`
```java
// 指定线程名称便于排查
Thread vt = Thread.ofVirtual()
    .name("db-worker")
    .start(() -> queryDatabase());
```

---

**基本写法：命名前缀 + 计数**
`Thread.ofVirtual().name(<前缀>, <起始>).start(...)`
```java
// 名称形如 worker-0、worker-1、worker-2...
Thread vt = Thread.ofVirtual()
    .name("worker-", 0)
    .start(() -> doWork());
```

---

**基本写法：设置未捕获异常处理器**
`Thread.ofVirtual().uncaughtExceptionHandler(<handler>).start(...)`
```java
// 虚拟线程异常未捕获时回调
Thread vt = Thread.ofVirtual()
    .uncaughtExceptionHandler((t, e) ->
        System.err.println(t.getName() + " 异常: " + e.getMessage()))
    .start(() -> { throw new RuntimeException("boom"); });
```

---

## 虚拟线程执行器

**基本写法：每任务一虚拟线程的执行器**
`Executors.newVirtualThreadPerTaskExecutor()`
```java
// 适用于提交大量任务，每个任务一个虚拟线程
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> doWork());
    executor.submit(() -> doWork());
}
```

---

**基本写法：批量提交任务**
`<executor>.submit(<task>)`
```java
// 提交大量任务，每个任务在独立虚拟线程上运行
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<String>> futures = new ArrayList<>();
    for (int i = 0; i < 10_000; i++) {
        final int id = i;
        futures.add(executor.submit(() -> "result-" + id));
    }
    for (Future<String> f : futures) {
        System.out.println(f.get());
    }
}
```

---

**基本写法：执行器作为 ThreadFactory**
`Thread.ofVirtual().factory()`
```java
// 获取虚拟线程工厂，供自定义执行器使用
ThreadFactory factory = Thread.ofVirtual().name("vt-", 0).factory();
ExecutorService executor = Executors.newThreadPerTaskExecutor(factory);
```

---

## 判断线程类型

**基本写法：判断是否为虚拟线程**
`<thread>.isVirtual()`
```java
// 返回 true 表示当前为虚拟线程
boolean isVirtual = Thread.currentThread().isVirtual();
```

---

**基本写法：判断任意线程**
`Thread.ofVirtual().start(...).isVirtual()`
```java
// 用于日志或调试时区分线程类型
Thread vt = Thread.startVirtualThread(() -> { });
System.out.println("isVirtual: " + vt.isVirtual());
```

---

## 平台线程对比

**基本写法：创建平台线程**
`Thread.ofPlatform().start(<Runnable>)`
```java
// 传统 OS 线程，1:1 映射到内核线程
Thread pt = Thread.ofPlatform().name("platform-1").start(() -> doWork());
```

---

**基本写法：Builder 平台线程属性配置**
`Thread.ofPlatform().name(...).priority(...).start(...)`
```java
// 平台线程支持更丰富的属性设置
Thread pt = Thread.ofPlatform()
    .name("io-thread")
    .priority(Thread.MAX_PRIORITY)
    .start(() -> doWork());
```

---

## 阻塞操作

**基本写法：虚拟线程中的阻塞调用**
`Thread.sleep(<duration>)`
```java
// 阻塞时虚拟线程会让出载体线程，不浪费 OS 线程
Thread.startVirtualThread(() -> {
    Thread.sleep(Duration.ofSeconds(1));
});
```

---

**基本写法：阻塞 IO 操作**
`<channel>.read(...)` / `<socket>.connect(...)`
```java
// 网络 IO 阻塞时自动让出载体线程
Thread.startVirtualThread(() -> {
    try (Socket socket = new Socket("example.com", 80)) {
        socket.getInputStream().readAllBytes();
    }
});
```

---

## 等待与协调

**基本写法：等待虚拟线程结束**
`<thread>.join()`
```java
// 等待虚拟线程执行完成
Thread vt = Thread.startVirtualThread(() -> doWork());
vt.join();
```

---

**基本写法：带超时的等待**
`<thread>.join(<超时>)`
```java
// 最多等待 5 秒
Thread vt = Thread.startVirtualThread(() -> doWork());
if (!vt.join(Duration.ofSeconds(5))) {
    System.out.println("任务超时");
}
```

---

**基本写法：使用 CountDownLatch 协调**
`new CountDownLatch(<n>)`
```java
// 多虚拟线程同步点
CountDownLatch latch = new CountDownLatch(3);
for (int i = 0; i < 3; i++) {
    Thread.startVirtualThread(() -> {
        try { doWork(); } finally { latch.countDown(); }
    });
}
latch.await();
```

---

## 虚拟线程与锁

**基本写法：使用 ReentrantLock 推荐替代 synchronized**
`ReentrantLock`
```java
// synchronized 会 pin 虚拟线程，ReentrantLock 更友好
ReentrantLock lock = new ReentrantLock();
Thread.startVirtualThread(() -> {
    lock.lock();
    try { doWork(); } finally { lock.unlock(); }
});
```

---

**基本写法：避免在 synchronized 中阻塞**
`synchronized (<锁>) { <阻塞调用> }`
```java
// 不推荐：阻塞会 pin 住载体线程
synchronized (lock) {
    Thread.sleep(1000); // 应改用 ReentrantLock
}
```

---

## 结构化并发（Java 21 预览）

**基本写法：结构化任务作用域**
`StructuredTaskScope.open()`
```java
// 父子任务生命周期绑定（预览特性）
try (var scope = StructuredTaskScope.open()) {
    Subtask<String> user = scope.fork(() -> fetchUser());
    Subtask<Order> order = scope.fork(() -> fetchOrder());
    scope.join();
    System.out.println(user.get() + " " + order.get());
}
```

---

**基本写法：关闭策略 ShutdownOnFailure**
`new StructuredTaskScope.ShutdownOnFailure()`
```java
// 任一失败则取消所有任务
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Subtask<String> a = scope.fork(() -> queryA());
    Subtask<String> b = scope.fork(() -> queryB());
    scope.join();
    scope.throwIfFailed();
    System.out.println(a.get() + " " + b.get());
}
```

---

## 作用域值（Java 21 预览）

**基本写法：定义 ScopedValue**
`private static final ScopedValue<String> USER = ScopedValue.newInstance()`
```java
// 替代 ThreadLocal 的不可变线程局部值
static final ScopedValue<String> USER = ScopedValue.newInstance();
ScopedValue.where(USER, "Alice").run(() -> {
    System.out.println(USER.get());
});
```

---

## 虚拟线程适用场景

**基本写法：IO 密集型任务**
`Thread.startVirtualThread(() -> { <IO 调用> })`
```java
// 适用于网络请求、数据库查询、文件读写等阻塞场景
Thread.startVirtualThread(() -> httpClient.send(request, BodyHandlers.ofString()));
```

---

**基本写法：CPU 密集型任务不推荐**
`Thread.ofPlatform().start(...)`
```java
// CPU 密集型任务应使用平台线程或 ForkJoinPool
Thread.ofPlatform().start(() -> heavyCompute());
```

---

## Spring Boot 启用虚拟线程

**基本写法：开启虚拟线程支持**
`spring.threads.virtual.enabled: true`
```java
// application.yml 启用虚拟线程处理请求
spring:
  threads:
    virtual:
      enabled: true
```

---

**基本写法：自定义 Tomcat 协议处理器**
`protocolHandler`
```java
// 底层机制：Tomcat 使用虚拟线程处理每个请求
// 配置 enabled=true 后，请求处理将运行在虚拟线程上
```

---

## 调试与观测

**基本写法：线程转储**
`jcmd <pid> Thread.dump_to_file -format=json <file>`
```java
// 输出包含虚拟线程的线程转储
// jcmd <pid> Thread.dump_to_file -format=json dump.json
```

---

**基本写法：检测 pinning**
`-Djdk.tracePinnedThreads=full`
```java
// JVM 启动参数检测被 pin 住的虚拟线程
// java -Djdk.tracePinnedThreads=full -jar app.jar
```

---

## 注意事项

**基本写法：不要池化虚拟线程**
`Thread.startVirtualThread(<task>)`
```java
// 虚拟线程用完即弃，无需复用，无池化必要
Thread.startVirtualThread(() -> doWork());
```

---

**基本写法：避免大量使用 ThreadLocal**
`ThreadLocal.withInitial(...)`
```java
// 百万虚拟线程会复制 ThreadLocal，内存开销大
// 推荐改用 ScopedValue（预览特性）
```



<!-- ============ 文档分隔线：013-java/025-JVMMemoryModel.md ============ -->

# Java JVM 内存模型速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 运行时数据区

**基本写法：堆内存 Heap**
`-Xmx<size>`
```java
// 所有对象实例与数组存放区域，GC 主战场
// -Xmx2g 设置最大堆为 2GB
ArrayList<String> list = new ArrayList<>();
```

---

**基本写法：方法区 Method Area**
`-XX:MaxMetaspaceSize=<size>`
```java
// 存储类元信息、常量池、静态变量（JDK 8+ 为 Metaspace）
// -XX:MaxMetaspaceSize=256m
```

---

**基本写法：虚拟机栈 VM Stack**
`-Xss<size>`
```java
// 每个线程私有，存储栈帧（局部变量、操作数栈）
// -Xss512k 设置每个线程栈大小
```

---

**基本写法：本地方法栈 Native Method Stack**
`-Xss<size>`
```java
// Native 方法调用使用，与 VM Stack 类似
```

---

**基本写法：程序计数器 PC Register**
`<线程私有>`
```java
// 当前线程执行字节码的行号指示器，线程私有无 OOM
```

---

## 堆内存分代

**基本写法：新生代 Young Generation**
`-Xmn<size>`
```java
// Eden + Survivor0 + Survivor1，对象出生地
// -Xmn512m 设置新生代大小
```

---

**基本写法：老年代 Old Generation**
`-XX:NewRatio=<ratio>`
```java
// 新生代:老年代 = 1:2（NewRatio=2 时）
// -XX:NewRatio=2
```

---

**基本写法：Eden 与 Survivor 比例**
`-XX:SurvivorRatio=<ratio>`
```java
// Eden:Survivor = 8:1:1（SurvivorRatio=8 时）
// -XX:SurvivorRatio=8
```

---

## GC 垃圾回收器

**基本写法：G1 回收器（JDK 9+ 默认）**
`-XX:+UseG1GC`
```java
// 面向大堆的 Region 化回收器
// java -XX:+UseG1GC -Xmx4g -jar app.jar
```

---

**基本写法：ZGC 低延迟回收器**
`-XX:+UseZGC`
```java
// 亚毫秒级停顿（JDK 15+ 生产可用）
// java -XX:+UseZGC -Xmx16g -jar app.jar
```

---

**基本写法：设置 GC 日志**
`-Xlog:gc*:<file>`
```java
// JDK 9+ 统一日志格式
// -Xlog:gc*:file=gc.log:time,uptime,level,tags
```

---

**基本写法：设置期望停顿时间**
`-XX:MaxGCPauseMillis=<ms>`
```java
// G1/ZGC 设置目标停顿时间
// -XX:MaxGCPauseMillis=200
```

---

## 对象生命周期

**基本写法：对象分配在 Eden**
`new <类型>()`
```java
// 新对象优先在 Eden 区分配
Object obj = new Object();
```

---

**基本写法：进入 Survivor**
`<对象> 经历 Minor GC`
```java
// Eden 满时触发 Minor GC，存活对象进入 Survivor
// 每经历一次 GC 年龄 +1
```

---

**基本写法：晋升老年代**
`-XX:MaxTenuringThreshold=<年龄>`
```java
// 对象年龄达到阈值进入老年代
// -XX:MaxTenuringThreshold=15
```

---

**基本写法：大对象直接进老年代**
`-XX:PretenureSizeThreshold=<size>`
```java
// 超过阈值的对象直接分配到老年代
// -XX:PretenureSizeThreshold=1048576（1MB）
```

---

## 内存溢出排查

**基本写法：堆 OOM 转储**
`-XX:+HeapDumpOnOutOfMemoryError`
```java
// OOM 时自动生成堆转储文件
// -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/dump.hprof
```

---

**基本写法：手动触发堆转储**
`jcmd <pid> GC.heap_dump <file>`
```java
// 运行时手动生成堆 dump
// jcmd 12345 GC.heap_dump /tmp/heap.hprof
```

---

**基本写法：jmap 查看堆概况**
`jmap -heap <pid>`
```java
// 查看堆配置与使用情况
// jmap -heap 12345
```

---

**基本写法：查看对象统计**
`jmap -histo <pid>`
```java
// 按对象大小排序统计
// jmap -histo 12345 | head -20
```

---

## 内存监控工具

**基本写法：jstat 查看 GC 统计**
`jstat -gcutil <pid> <间隔>`
```java
// 每 1 秒打印一次各区使用率
// jstat -gcutil 12345 1000
```

---

**基本写法：jcmd 列出进程命令**
`jcmd <pid> <command>`
```java
// 查看支持的命令
// jcmd 12345 help
```

---

**基本写法：JFR 录制**
`jcmd <pid> JFR.start duration=60s filename=<file>`
```java
// 录制 60 秒 Java Flight Recorder 数据
// jcmd 12345 JFR.start duration=60s filename=/tmp/rec.jfr
```

---

## 内存可见性

**基本写法：volatile 保证可见性**
`volatile <类型> <字段>`
```java
// 写入立即对其他线程可见，禁止指令重排
private volatile boolean running = true;
```

---

**基本写法：happens-before 规则**
`<线程A> happens-before <线程B>`
```java
// 锁释放 happens-before 后续锁获取
// volatile 写 happens-before 后续 volatile 读
// 线程启动 happens-before 其 run 方法
```

---

## 常用 JVM 参数

**基本写法：设置堆初始与最大值**
`-Xms<size> -Xmx<size>`
```java
// 推荐初始与最大值相同避免动态扩容
// -Xms2g -Xmx2g
```

---

**基本写法：设置元空间**
`-XX:MetaspaceSize=<size> -XX:MaxMetaspaceSize=<size>`
```java
// 元空间初始与最大值
// -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=256m
```

---

**基本写法：开启压缩指针**
`-XX:+UseCompressedOops`
```java
// 堆小于 32G 时开启可节省内存（默认开启）
// -XX:+UseCompressedOops
```

---

**基本写法：禁用偏向锁**
`-XX:-UseBiasedLocking`
```java
// JDK 15+ 弃用偏向锁，高并发场景可禁用
// -XX:-UseBiasedLocking
```

---

## 字符串常量池

**基本写法：字符串驻留**
`<string>.intern()`
```java
// 将字符串放入常量池并返回引用
String s = new String("hello").intern();
```

---

**基本写法：调整字符串表大小**
`-XX:StringTableSize=<buckets>`
```java
// 调整常量池哈希桶数量
// -XX:StringTableSize=65536
```

---

## 直接内存

**基本写法：分配直接内存**
`ByteBuffer.allocateDirect(<size>)`
```java
// 堆外内存，不受 GC 控制，NIO 使用
ByteBuffer buf = ByteBuffer.allocateDirect(1024 * 1024);
```

---

**基本写法：设置直接内存上限**
`-XX:MaxDirectMemorySize=<size>`
```java
// 限制堆外内存使用
// -XX:MaxDirectMemorySize=512m
```

---

## 类加载机制

**基本写法：双亲委派模型**
`<ClassLoader>.loadClass(<name>)`
```java
// 先委托父加载器加载，失败才自己加载
ClassLoader cl = ClassLoader.getSystemClassLoader();
Class<?> clazz = cl.loadClass("com.example.App");
```

---

**基本写法：自定义类加载器**
`extends ClassLoader`
```java
// 重写 findClass 实现自定义加载
class MyLoader extends ClassLoader {
    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        byte[] bytes = loadClassData(name);
        return defineClass(name, bytes, 0, bytes.length);
    }
}
```

---

## 内存模型三大特性

**基本写法：原子性**
`synchronized` / `AtomicInteger`
```java
// 通过锁或原子类保证操作原子性
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();
```

---

**基本写法：可见性**
`volatile` / `synchronized`
```java
// 通过 volatile 保证变量修改对所有线程可见
private volatile boolean flag = false;
```

---

**基本写法：有序性**
`volatile` / `happens-before`
```java
// volatile 写之前的操作不会被重排到写之后
private int x = 0;
private volatile boolean ready = false;
public void writer() { x = 42; ready = true; }
```



<!-- ============ 文档分隔线：013-java/026-NetworkProgramming.md ============ -->

# Java 网络编程 API 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Socket TCP 客户端

**基本写法：创建客户端连接**
`new Socket(<host>, <port>)`
```java
// 建立与服务端的 TCP 连接
try (Socket socket = new Socket("example.com", 8080)) {
    OutputStream out = socket.getOutputStream();
    out.write("hello".getBytes());
}
```

---

**基本写法：读取服务端响应**
`<socket>.getInputStream()`
```java
// 从输入流读取服务端返回数据
try (Socket socket = new Socket("example.com", 8080);
     BufferedReader reader = new BufferedReader(
         new InputStreamReader(socket.getInputStream()))) {
    String line = reader.readLine();
}
```

---

**基本写法：设置超时**
`<socket>.setSoTimeout(<ms>)`
```java
// 读操作最长等待时间
Socket socket = new Socket("example.com", 8080);
socket.setSoTimeout(5000);
```

---

**基本写法：连接超时**
`new Socket()` + `<socket>.connect(<endpoint>, <timeout>)`
```java
// 控制连接建立阶段超时
Socket socket = new Socket();
socket.connect(new InetSocketAddress("example.com", 8080), 3000);
```

---

## Socket TCP 服务端

**基本写法：创建服务端**
`new ServerSocket(<port>)`
```java
// 监听指定端口
try (ServerSocket server = new ServerSocket(8080)) {
    Socket client = server.accept();
    handleClient(client);
}
```

---

**基本写法：循环接收连接**
`while (true) { <server>.accept(); }`
```java
// 持续接收客户端连接
try (ServerSocket server = new ServerSocket(8080)) {
    while (true) {
        Socket client = server.accept();
        new Thread(() -> handleClient(client)).start();
    }
}
```

---

**基本写法：设置接收缓冲区**
`<server>.setReceiveBufferSize(<size>)`
```java
// 调整服务端接收缓冲区大小
ServerSocket server = new ServerSocket(8080);
server.setReceiveBufferSize(64 * 1024);
```

---

## UDP 数据报

**基本写法：发送 UDP 包**
`new DatagramSocket()` + `<socket>.send(<packet>)`
```java
// 发送数据报到目标地址
try (DatagramSocket socket = new DatagramSocket()) {
    byte[] data = "hello".getBytes();
    DatagramPacket packet = new DatagramPacket(
        data, data.length, InetAddress.getByName("127.0.0.1"), 9090);
    socket.send(packet);
}
```

---

**基本写法：接收 UDP 包**
`new DatagramSocket(<port>)` + `<socket>.receive(<packet>)`
```java
// 在指定端口监听 UDP 数据报
try (DatagramSocket socket = new DatagramSocket(9090)) {
    byte[] buffer = new byte[1024];
    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
    socket.receive(packet);
    String msg = new String(packet.getData(), 0, packet.getLength());
}
```

---

## URL 访问

**基本写法：打开 URL 连接**
`new URL(<url>).openConnection()`
```java
// 传统 URL 读取方式
URL url = new URL("https://example.com/api");
try (BufferedReader reader = new BufferedReader(
        new InputStreamReader(url.openStream()))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
}
```

---

**基本写法：HTTP GET 请求**
`<conn>.setRequestMethod("GET")`
```java
// 通过 HttpURLConnection 发送 GET
URL url = new URL("https://example.com/api");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
conn.setRequestProperty("Accept", "application/json");
int code = conn.getResponseCode();
```

---

**基本写法：HTTP POST 请求**
`<conn>.setRequestMethod("POST")` + `<conn>.getOutputStream()`
```java
// 发送 POST 请求并写入请求体
HttpURLConnection conn = (HttpURLConnection) new URL("https://example.com/api").openConnection();
conn.setRequestMethod("POST");
conn.setDoOutput(true);
conn.setRequestProperty("Content-Type", "application/json");
try (OutputStream os = conn.getOutputStream()) {
    os.write("{\"name\":\"Alice\"}".getBytes());
}
```

---

## HttpClient（Java 11+）

**基本写法：创建 HttpClient**
`HttpClient.newHttpClient()`
```java
// 创建默认 HTTP 客户端
HttpClient client = HttpClient.newHttpClient();
```

---

**基本写法：自定义 HttpClient**
`HttpClient.newBuilder()`
```java
// 配置连接超时、HTTP 版本等
HttpClient client = HttpClient.newBuilder()
    .version(HttpClient.Version.HTTP_2)
    .connectTimeout(Duration.ofSeconds(10))
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();
```

---

**基本写法：发送 GET 请求**
`<client>.send(<request>, <handler>)`
```java
// 同步发送 GET 并返回响应
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .timeout(Duration.ofSeconds(10))
    .header("Accept", "application/json")
    .GET()
    .build();
HttpResponse<String> response =
    client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

---

**基本写法：发送 POST 请求**
`HttpRequest.BodyPublishers.ofString(<body>)`
```java
// 发送 JSON 请求体
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("{\"name\":\"Alice\"}"))
    .build();
HttpResponse<String> response =
    client.send(request, HttpResponse.BodyHandlers.ofString());
```

---

**基本写法：异步发送请求**
`<client>.sendAsync(<request>, <handler>)`
```java
// 返回 CompletableFuture，非阻塞
client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
    .thenApply(HttpResponse::body)
    .thenAccept(System.out::println);
```

---

**基本写法：发送 PUT 请求**
`.PUT(HttpRequest.BodyPublishers.ofString(<body>))`
```java
// RESTful PUT 请求
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api/1"))
    .header("Content-Type", "application/json")
    .PUT(HttpRequest.BodyPublishers.ofString("{\"name\":\"Bob\"}"))
    .build();
```

---

**基本写法：发送 DELETE 请求**
`.DELETE()`
```java
// RESTful DELETE 请求
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api/1"))
    .DELETE()
    .build();
```

---

**基本写法：处理响应体为字节数组**
`HttpResponse.BodyHandlers.ofByteArray()`
```java
// 适用于下载二进制文件
HttpResponse<byte[]> response =
    client.send(request, HttpResponse.BodyHandlers.ofByteArray());
Files.write(Path.of("out.bin"), response.body());
```

---

**基本写法：流式处理响应体**
`HttpResponse.BodyHandlers.ofInputStream()`
```java
// 大响应体流式读取
HttpResponse<InputStream> response =
    client.send(request, HttpResponse.BodyHandlers.ofInputStream());
try (InputStream is = response.body()) {
    is.transferTo(System.out);
}
```

---

## 基本参数与查询

**基本写法：拼接查询参数**
`URI.create(<url> + "?" + <query>)`
```java
// 手动拼接 URL 查询参数
String url = "https://example.com/search?q=" + URLEncoder.encode("Java 编程", StandardCharsets.UTF_8);
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(url))
    .GET()
    .build();
```

---

**基本写法：设置 Basic 认证**
`<builder>.header("Authorization", "Basic " + <encoded>)`
```java
// 用户名密码 Basic 认证
String auth = "alice:secret";
String encoded = Base64.getEncoder().encodeToString(auth.getBytes());
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .header("Authorization", "Basic " + encoded)
    .GET()
    .build();
```

---

## InetSocketAddress 地址

**基本写法：创建地址对象**
`new InetSocketAddress(<host>, <port>)`
```java
// 封装主机名与端口
InetSocketAddress addr = new InetSocketAddress("example.com", 8080);
```

---

**基本写法：未解析地址**
`InetSocketAddress.createUnresolved(<host>, <port>)`
```java
// 不进行 DNS 解析，连接时才解析
InetSocketAddress addr = InetSocketAddress.createUnresolved("example.com", 8080);
```

---

## NetworkInterface 网络接口

**基本写法：列举所有网卡**
`NetworkInterface.getNetworkInterfaces()`
```java
// 遍历本机所有网络接口
Enumeration<NetworkInterface> nics = NetworkInterface.getNetworkInterfaces();
while (nics.hasMoreElements()) {
    NetworkInterface nic = nics.nextElement();
    System.out.println(nic.getName());
}
```

---

**基本写法：获取本机 IP**
`NetworkInterface.getByName(<name>)`
```java
// 通过网卡名获取其 IP 地址
NetworkInterface nic = NetworkInterface.getByName("eth0");
Enumeration<InetAddress> addrs = nic.getInetAddresses();
while (addrs.hasMoreElements()) {
    System.out.println(addrs.nextElement().getHostAddress());
}
```

---

## ServerSocket 多线程处理

**基本写法：线程池处理客户端**
`ExecutorService` + `server.accept()`
```java
// 使用线程池避免无限创建线程
ExecutorService pool = Executors.newFixedThreadPool(50);
try (ServerSocket server = new ServerSocket(8080)) {
    while (true) {
        Socket client = server.accept();
        pool.submit(() -> handleClient(client));
    }
}
```

---

**基本写法：NIO Selector 监听**
`Selector.open()`
```java
// 单线程管理多通道，适合高并发
Selector selector = Selector.open();
ServerSocketChannel server = ServerSocketChannel.open();
server.configureBlocking(false);
server.register(selector, SelectionKey.OP_ACCEPT);
```

---

## 文件传输

**基本写法：服务端发送文件**
`Files.copy(<path>, <outputStream>)`
```java
// 将文件写入 Socket 输出流
try (Socket socket = server.accept();
     OutputStream out = socket.getOutputStream()) {
    Files.copy(Path.of("data.txt"), out);
}
```

---

**基本写法：客户端接收文件**
`<inputStream>.transferTo(<outputStream>)`
```java
// 接收服务端传输的文件内容
try (InputStream in = socket.getInputStream();
     FileOutputStream fos = new FileOutputStream("received.txt")) {
    in.transferTo(fos);
}
```



<!-- ============ 文档分隔线：013-java/027-JavaBuildTool.md ============ -->

# Java 构建工具 Maven/Gradle 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Maven 常用命令

**基本写法：清理构建产物**
`mvn clean`
```java
// 删除 target 目录，确保全新构建
mvn clean
```

---

**基本写法：编译主代码**
`mvn compile`
```java
// 编译 src/main/java 到 target/classes
mvn compile
```

---

**基本写法：编译测试代码**
`mvn test-compile`
```java
// 编译 src/test/java 到 target/test-classes
mvn test-compile
```

---

**基本写法：运行测试**
`mvn test`
```java
// 执行所有单元测试，报告输出到 target/surefire-reports
mvn test
```

---

**基本写法：打包**
`mvn package`
```java
// 打包为 jar/war，输出到 target/
mvn package
```

---

**基本写法：安装到本地仓库**
`mvn install`
```java
// 安装到 ~/.m2/repository 供其他本地项目依赖
mvn install
```

---

**基本写法：部署到远程仓库**
`mvn deploy`
```java
// 上传构件到 Nexus/Artifactory 等远程仓库
mvn deploy
```

---

**基本写法：跳过测试打包**
`mvn package -DskipTests`
```java
// 编译测试代码但不执行测试
mvn clean package -DskipTests
```

---

**基本写法：完全跳过测试**
`mvn package -Dmaven.test.skip=true`
```java
// 既不编译也不执行测试
mvn clean package -Dmaven.test.skip=true
```

---

**基本写法：激活 Profile**
`mvn package -P<profileId>`
```java
// 激活指定 profile 进行打包
mvn clean package -Pprod
```

---

**基本写法：离线构建**
`mvn -o <goal>`
```java
// 不访问远程仓库，仅使用本地依赖
mvn -o clean package
```

---

**基本写法：多线程构建**
`mvn -T <threads> <goal>`
```java
// 使用 4 线程并行构建
mvn -T 4 clean install
```

---

**基本写法：查看依赖树**
`mvn dependency:tree`
```java
// 排查依赖冲突必备
mvn dependency:tree
```

---

**基本写法：过滤依赖**
`mvn dependency:tree -Dincludes=<groupId>:<artifactId>`
```java
// 只查看指定依赖的引入路径
mvn dependency:tree -Dincludes=org.springframework:spring-core
```

---

**基本写法：分析依赖**
`mvn dependency:analyze`
```java
// 检查未使用与未声明依赖
mvn dependency:analyze
```

---

**基本写法：查看有效 POM**
`mvn help:effective-pom`
```java
// 输出合并父 POM 后的最终 POM
mvn help:effective-pom
```

---

**基本写法：创建项目骨架**
`mvn archetype:generate`
```java
// 交互式生成 Maven 项目结构
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

---

**基本写法：Spring Boot 运行**
`mvn spring-boot:run`
```java
// 直接从源码启动 Spring Boot 应用
mvn spring-boot:run
```

---

**基本写法：多模块构建**
`mvn -pl <module> -am <goal>`
```java
// 只构建指定模块及其依赖模块
mvn -pl my-module -am clean install
```

---

## Maven 依赖 Scope

**基本写法：编译期依赖**
`<scope>compile</scope>`
```java
// 默认 scope，全阶段可用
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-core</artifactId>
    <scope>compile</scope>
</dependency>
```

---

**基本写法：测试期依赖**
`<scope>test</scope>`
```java
// 仅测试阶段可用
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <scope>test</scope>
</dependency>
```

---

**基本写法：已提供依赖**
`<scope>provided</scope>`
```java
// 编译测试可用，打包时不包含（由容器提供）
<dependency>
    <groupId>jakarta.servlet</groupId>
    <artifactId>jakarta.servlet-api</artifactId>
    <scope>provided</scope>
</dependency>
```

---

**基本写法：运行时依赖**
`<scope>runtime</scope>`
```java
// 编译不需要，运行时需要
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

---

## Gradle 常用命令

**基本写法：列出所有任务**
`./gradlew tasks`
```java
// 查看项目可用的所有 Gradle 任务
./gradlew tasks
```

---

**基本写法：清理构建**
`./gradlew clean`
```java
// 删除 build 目录
./gradlew clean
```

---

**基本写法：编译代码**
`./gradlew build`
```java
// 完整构建（编译、测试、打包）
./gradlew build
```

---

**基本写法：跳过测试构建**
`./gradlew build -x test`
```java
// 排除 test 任务
./gradlew build -x test
```

---

**基本写法：运行测试**
`./gradlew test`
```java
// 执行所有测试
./gradlew test
```

---

**基本写法：运行指定测试类**
`./gradlew test --tests <类名>`
```java
// 只运行某个测试类
./gradlew test --tests com.example.UserServiceTest
```

---

**基本写法：运行 Spring Boot**
`./gradlew bootRun`
```java
// 启动 Spring Boot 应用
./gradlew bootRun
```

---

**基本写法：打包**
`./gradlew bootJar`
```java
// 生成可执行 fat jar
./gradlew bootJar
```

---

**基本写法：查看依赖树**
`./gradlew dependencies`
```java
// 打印项目依赖树
./gradlew dependencies
```

---

**基本写法：查看指定配置的依赖**
`./gradlew dependencies --configuration <配置>`
```java
// 只查看 runtimeClasspath 的依赖
./gradlew dependencies --configuration runtimeClasspath
```

---

**基本写法：依赖分析**
`./gradlew dependencyInsight --dependency <名称>`
```java
// 查看某个依赖的详细解析过程
./gradlew dependencyInsight --dependency spring-core
```

---

**基本写法：刷新依赖**
`./gradlew --refresh-dependencies build`
```java
// 强制重新下载依赖
./gradlew --refresh-dependencies build
```

---

**基本写法：并行构建**
`./gradlew build --parallel`
```java
// 多模块并行构建
./gradlew build --parallel
```

---

**基本写法：构建缓存**
`./gradlew build --build-cache`
```java
// 启用 Gradle 构建缓存
./gradlew build --build-cache
```

---

**基本写法：查看任务详情**
`./gradlew help --task <任务名>`
```java
// 查看某任务的描述与依赖
./gradlew help --task build
```

---

**基本写法：初始化 Wrapper**
`gradle wrapper --gradle-version <版本>`
```java
// 生成 gradlew 脚本，统一团队 Gradle 版本
gradle wrapper --gradle-version 8.5
```

---

## build.gradle 关键配置

**基本写法：插件声明**
`plugins { id '<plugin>' version '<version>' }`
```java
// Groovy DSL 声明插件
plugins {
    id 'org.springframework.boot' version '3.2.0'
    id 'java'
}
```

---

**基本写法：依赖声明**
`implementation '<group>:<name>:<version>'`
```java
// Groovy DSL 添加依赖
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.2.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.12.1'
}
```

---

**基本写法：Kotlin DSL 依赖**
`implementation("<group>:<name>:<version>")`
```java
// build.gradle.kts 写法
dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web:3.2.0")
    testImplementation("org.junit.jupiter:junit-jupiter:5.12.1")
}
```

---

**基本写法：Java 版本配置**
`java { sourceCompatibility = JavaVersion.VERSION_17 }`
```java
// 指定编译目标版本
java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}
```

---

**基本写法：仓库配置**
`repositories { mavenCentral() }`
```java
// 配置依赖仓库
repositories {
    mavenCentral()
    maven { url 'https://maven.aliyun.com/repository/public' }
}
```

---

**基本写法：自定义任务**
`task <name> { doLast { ... } }`
```java
// Groovy DSL 定义任务
task printVersion {
    doLast {
        println "Project version: ${project.version}"
    }
}
```

---

## 仓库镜像配置

**基本写法：Maven 阿里云镜像**
`<mirror>` in settings.xml
```java
// ~/.m2/settings.xml 配置镜像加速
<mirror>
    <id>aliyun</id>
    <mirrorOf>central</mirrorOf>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>
```

---

**基本写法：Gradle 阿里云镜像**
`repositories { maven { url '...' } }`
```java
// settings.gradle 或 build.gradle 配置
repositories {
    maven { url 'https://maven.aliyun.com/repository/public' }
    mavenCentral()
}
```

---

## 版本管理

**基本写法：Maven 版本号约定**
`<major>.<minor>.<patch>-<qualifier>`
```java
// 语义化版本号约定
// 1.0.0-SNAPSHOT 快照版本
// 1.0.0-RELEASE 正式版本
```

---

**基本写法：Maven 版本更新检查**
`mvn versions:display-dependency-updates`
```java
// 列出可用的依赖新版本
mvn versions:display-dependency-updates
```

---

**基本写法：Gradle 版本目录**
`libs.versions.toml`
```java
// gradle/libs.versions.toml 集中管理版本
[versions]
junit = "5.12.1"
[libraries]
junit = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }
```

---

## 发布构件

**基本写法：Maven 发布到远程仓库**
`<distributionManagement>`
```java
// pom.xml 配置发布目标
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>https://repo.example.com/releases</url>
    </repository>
</distributionManagement>
```

---

**基本写法：Gradle 发布**
`maven-publish` 插件
```java
// build.gradle 配置发布
publishing {
    publications {
        maven(MavenPublication) {
            from components.java
            groupId = 'com.example'
            artifactId = 'my-lib'
            version = '1.0.0'
        }
    }
}
```



<!-- ============ 文档分隔线：013-java/028-JavaReflectionDynamicProxy.md ============ -->

# Java 反射与动态代理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 获取 Class 对象

**基本写法：三种获取 Class 的方式**
`<类名>.class | <对象>.getClass() | Class.forName("<全限定名>")`
```java
// 三种方式获取 Class 对象
Class<String> c1 = String.class;
Class<?> c2 = "hello".getClass();
Class<?> c3 = Class.forName("java.lang.String");
```

---

## 反射创建实例

**基本写法：通过 Class 创建对象**
`<class>.getDeclaredConstructor().newInstance();`
```java
// 反射方式创建实例
Object obj = String.class.getDeclaredConstructor().newInstance();
```

---

**基本写法：带参构造**
`<class>.getDeclaredConstructor(<参数类型>...).newInstance(<参数>...);`
```java
// 通过带参构造创建实例
Object obj = String.class.getDeclaredConstructor(byte[].class).newInstance(new byte[]{65});
```

---

## 反射获取字段

**基本写法：获取声明字段**
`<class>.getDeclaredField("<字段名>");`
```java
// 获取私有字段
Field f = Person.class.getDeclaredField("name");
f.setAccessible(true);
```

---

**基本写法：读取字段值**
`<field>.get(<对象>);`
```java
// 读取对象字段值
Object value = f.get(person);
```

---

**基本写法：设置字段值**
`<field>.set(<对象>, <值>);`
```java
// 设置对象字段值
f.set(person, "Alice");
```

---

## 反射获取方法

**基本写法：获取声明方法**
`<class>.getDeclaredMethod("<方法名>", <参数类型>...);`
```java
// 获取私有方法
Method m = Person.class.getDeclaredMethod("greet", String.class);
m.setAccessible(true);
```

---

**基本写法：反射调用方法**
`<method>.invoke(<对象>, <参数>...);`
```java
// 反射调用方法
Object result = m.invoke(person, "World");
```

---

## 反射操作泛型

**基本写法：获取泛型返回类型**
`<method>.getGenericReturnType();`
```java
// 获取方法的泛型返回类型
Type type = method.getGenericReturnType();
```

---

**基本写法：获取参数泛型**
`<method>.getGenericParameterTypes();`
```java
// 获取方法参数的泛型类型数组
Type[] types = method.getGenericParameterTypes();
```

---

## JDK 动态代理

**基本写法：创建 JDK 动态代理**
`Proxy.newProxyInstance(<类加载器>, <接口数组>, <调用处理器>);`
```java
// 为 List 接口创建代理
List<String> proxy = (List<String>) Proxy.newProxyInstance(
    List.class.getClassLoader(),
    new Class[]{List.class},
    (proxyObj, method, args) -> {
        System.out.println("调用: " + method.getName());
        return null;
    }
);
```

---

**基本写法：实现 InvocationHandler**
`class <类名> implements InvocationHandler { public Object invoke(Object p, Method m, Object[] a) {} }`
```java
// 自定义调用处理器
class LogHandler implements InvocationHandler {
    private final Object target;
    public LogHandler(Object target) { this.target = target; }
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("before: " + method.getName());
        Object r = method.invoke(target, args);
        System.out.println("after: " + method.getName());
        return r;
    }
}
```

---

## CGLIB 风格代理（子类代理）

**基本写法：创建子类代理（需第三方库 cglib）**
`Enhancer.create(<类>, <回调>);`
```java
// cglib 创建子类代理
Enhancer enhancer = new Enhancer();
enhancer.setSuperclass(Person.class);
enhancer.setCallback((MethodInterceptor) (obj, method, args, proxy) -> {
    System.out.println("before");
    Object r = proxy.invokeSuper(obj, args);
    System.out.println("after");
    return r;
});
Person proxy = (Person) enhancer.create();
```

---

## 反射获取注解

**基本写法：获取类上注解**
`<class>.getAnnotation(<注解类型>);`
```java
// 获取类上的注解
Deprecated d = MyClass.class.getAnnotation(Deprecated.class);
```

---

**基本写法：判断注解存在**
`<class>.isAnnotationPresent(<注解类型>);`
```java
// 判断注解是否存在
boolean has = MyClass.class.isAnnotationPresent(Deprecated.class);
```

---

## 反射获取数组信息

**基本写法：创建数组实例**
`Array.newInstance(<元素类型>, <长度>);`
```java
// 反射创建数组
Object arr = Array.newInstance(int.class, 5);
```

---

**基本写法：反射读写数组**
`Array.get(<数组>, <索引>); | Array.set(<数组>, <索引>, <值>);`
```java
// 反射方式读写数组元素
Array.set(arr, 0, 42);
int v = (int) Array.get(arr, 0);
```

---

## Module 反射（Java 9+）

**基本写法：获取模块**
`<class>.getModule();`
```java
// 获取类所属模块
Module module = String.class.getModule();
System.out.println(module.getName());
```

---

**基本写法：导出包到指定模块**
`<module>.addExports("<包名>", <目标模块>);`
```java
// 反射方式导出包
module.addExports("com.example.internal", OtherModule);
```

---

## Record 反射（Java 16+）

**基本写法：判断是否为 Record**
`<class>.isRecord();`
```java
// 判断 Class 是否为 Record
boolean isRec = Point.class.isRecord();
```

---

**基本写法：获取 Record 组件**
`<class>.getRecordComponents();`
```java
// 获取 Record 的组件
RecordComponent[] comps = Point.class.getRecordComponents();
```



<!-- ============ 文档分隔线：013-java/029-JavaNIOChannelBuffer.md ============ -->

# Java NIO 通道与缓冲区

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Buffer 创建

**基本写法：创建字节缓冲区**
`ByteBuffer.allocate(<容量>);`
```java
// 分配堆内字节缓冲区
ByteBuffer buf = ByteBuffer.allocate(1024);
```

---

**基本写法：创建直接缓冲区**
`ByteBuffer.allocateDirect(<容量>);`
```java
// 分配堆外直接缓冲区（减少拷贝）
ByteBuffer direct = ByteBuffer.allocateDirect(1024);
```

---

**基本写法：包装数组**
`ByteBuffer.wrap(<字节数组>);`
```java
// 包装现有数组为 Buffer
ByteBuffer buf = ByteBuffer.wrap(new byte[]{1, 2, 3});
```

---

## Buffer 读写操作

**基本写法：写入数据**
`<buffer>.put(<值>);`
```java
// 向缓冲区写入字节
buf.put((byte) 65);
```

---

**基本写法：读取数据**
`<buffer>.get();`
```java
// 从缓冲区读取字节
byte b = buf.get();
```

---

**基本写法：切换为读模式**
`<buffer>.flip();`
```java
// 写完后翻转为读模式
buf.flip();
```

---

**基本写法：重置位置**
`<buffer>.rewind();`
```java
// 重置 position 以便重新读
buf.rewind();
```

---

**基本写法：清空缓冲区**
`<buffer>.clear();`
```java
// 清空缓冲区准备再次写入
buf.clear();
```

---

**基本写法：压缩缓冲区**
`<buffer>.compact();`
```java
// 压缩未读数据到头部
buf.compact();
```

---

## Buffer 状态属性

**基本写法：获取容量**
`<buffer>.capacity();`
```java
// 获取缓冲区容量
int cap = buf.capacity();
```

---

**基本写法：获取位置**
`<buffer>.position();`
```java
// 获取当前位置
int pos = buf.position();
```

---

**基本写法：获取限制**
`<buffer>.limit();`
```java
// 获取限制位置
int limit = buf.limit();
```

---

**基本写法：获取剩余量**
`<buffer>.remaining();`
```java
// 获取剩余可读元素数量
int rem = buf.remaining();
```

---

## FileChannel 文件通道

**基本写法：从文件获取通道**
`FileChannel.open(<路径>, <打开选项>...);`
```java
// 打开文件通道
FileChannel ch = FileChannel.open(Path.of("a.txt"), StandardOpenOption.READ);
```

---

**基本写法：通道读入缓冲区**
`<channel>.read(<buffer>);`
```java
// 从通道读取到 Buffer
int n = ch.read(buf);
```

---

**基本写法：缓冲区写入通道**
`<channel>.write(<buffer>);`
```java
// 将 Buffer 数据写入通道
ch.write(buf);
```

---

**基本写法：传输文件**
`<channel>.transferTo(<位置>, <数量>, <目标通道>);`
```java
// 零拷贝传输文件内容
src.transferTo(0, src.size(), dst);
```

---

## Scatter / Gather

**基本写法：分散读**
`<channel>.read(<buffer数组>);`
```java
// 一次读入多个 Buffer
ByteBuffer[] bufs = {header, body};
channel.read(bufs);
```

---

**基本写法：聚集写**
`<channel>.write(<buffer数组>);`
```java
// 多个 Buffer 一次写出
ByteBuffer[] bufs = {header, body};
channel.write(bufs);
```

---

## Selector 选择器

**基本写法：创建选择器**
`Selector.open();`
```java
// 打开选择器
Selector selector = Selector.open();
```

---

**基本写法：注册通道到选择器**
`<channel>.register(<selector>, <就绪事件>);`
```java
// 注册通道为可读事件
channel.configureBlocking(false);
channel.register(selector, SelectionKey.OP_READ);
```

---

**基本写法：选择就绪通道**
`<selector>.select();`
```java
// 阻塞直到有就绪通道
int ready = selector.select();
```

---

**基本写法：获取就绪键**
`<selector>.selectedKeys();`
```java
// 获取就绪的 SelectionKey 集合
Set<SelectionKey> keys = selector.selectedKeys();
```

---

## Charset 字符编码

**基本写法：编码字符串到字节**
`<charset>.encode(<字符串>);`
```java
// 使用 UTF-8 编码
ByteBuffer b = StandardCharsets.UTF_8.encode("hello");
```

---

**基本写法：解码字节到字符串**
`<charset>.decode(<buffer>);`
```java
// 使用 UTF-8 解码
String s = StandardCharsets.UTF_8.decode(buf).toString();
```

---

## Path 路径操作

**基本写法：创建路径**
`Path.of("<路径>");`
```java
// 创建 Path 对象
Path p = Path.of("a", "b", "c.txt");
```

---

**基本写法：读取文件所有字节**
`Files.readAllBytes(<路径>);`
```java
// 一次性读取小文件全部字节
byte[] all = Files.readAllBytes(Path.of("a.txt"));
```

---

**基本写法：写入文件**
`Files.write(<路径>, <字节数组>);`
```java
// 写入字节数组到文件
Files.write(Path.of("out.txt"), bytes);
```

---

**基本写法：按行读取**
`Files.readAllLines(<路径>);`
```java
// 按行读取文件
List<String> lines = Files.readAllLines(Path.of("a.txt"));
```

---

## 异步文件通道

**基本写法：打开异步文件通道**
`AsynchronousFileChannel.open(<路径>, <选项>...);`
```java
// 打开异步文件通道
AsynchronousFileChannel ch = AsynchronousFileChannel.open(
    Path.of("a.txt"), StandardOpenOption.READ);
```

---

**基本写法：异步读取**
`<channel>.read(<buffer>, <位置>, <附件>, <完成处理器>);`
```java
// 异步读取并回调
ch.read(buf, 0, null, new CompletionHandler<Integer, Object>() {
    public void completed(Integer n, Object att) { }
    public void failed(Throwable e, Object att) { }
});
```



<!-- ============ 文档分隔线：013-java/030-JVMTuningCommands.md ============ -->

# Java JVM 调优命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## jps 进程查询

**基本写法：列出 Java 进程**
`jps [-l]`
```bash
# 列出所有 Java 进程及主类全名
jps -l
```

---

**基本写法：查看 JVM 启动参数**
`jps -v`
```bash
# 显示各 Java 进程的 JVM 参数
jps -v
```

---

**基本写法：仅显示 PID**
`jps -q`
```bash
# 只输出进程 ID
jps -q
```

---

## jstat 统计监控

**基本写法：监控 GC 状态**
`jstat -gc <pid> [间隔ms] [次数]`
```bash
# 每 250ms 输出一次 GC 情况，共 4 次
jstat -gc 12345 250 4
```

---

**基本写法：监控类加载**
`jstat -class <pid>`
```bash
# 查看类加载统计
jstat -class 12345
```

---

**基本写法：带时间戳输出**
`jstat -gc -t <pid>`
```bash
# 显示程序运行时间戳的 GC 信息
jstat -gc -t 12345
```

---

**基本写法：周期性输出表头**
`jstat -gc -h<行数> <pid> <间隔>`
```bash
# 每 5 行重新输出表头
jstat -gc -h5 12345 1000
```

---

## jmap 内存映像

**基本写法：堆转储**
`jmap -dump:format=b,file=<文件名> <pid>`
```bash
# 生成堆转储 hprof 文件
jmap -dump:format=b,file=heap.hprof 12345
```

---

**基本写法：对象直方图**
`jmap -histo <pid>`
```bash
# 输出堆中对象统计直方图
jmap -histo 12345
```

---

**基本写法：仅存活对象**
`jmap -histo:live <pid>`
```bash
# 触发 GC 后统计存活对象
jmap -histo:live 12345
```

---

**基本写法：堆配置信息**
`jmap -heap <pid>`
```bash
# 查看堆内存配置和使用情况
jmap -heap 12345
```

---

## jstack 线程栈

**基本写法：导出线程栈**
`jstack <pid>`
```bash
# 输出所有线程堆栈
jstack 12345
```

---

**基本写法：检测死锁**
`jstack -l <pid>`
```bash
# 输出线程栈及锁信息
jstack -l 12345
```

---

**基本写法：强制输出**
`jstack -F <pid>`
```bash
# 进程无响应时强制输出栈
jstack -F 12345
```

---

## jcmd 诊断命令

**基本写法：列出进程**
`jcmd -l`
```bash
# 列出所有 Java 进程
jcmd -l
```

---

**基本写法：查看可用命令**
`jcmd <pid> help`
```bash
# 列出该进程支持的诊断命令
jcmd 12345 help
```

---

**基本写法：生成堆转储**
`jcmd <pid> GC.heap_dump <文件名>`
```bash
# 通过 jcmd 生成堆转储
jcmd 12345 GC.heap_dump heap.hprof
```

---

**基本写法：查看 JVM 参数**
`jcmd <pid> VM.flags`
```bash
# 查看进程实际生效的 JVM 参数
jcmd 12345 VM.flags
```

---

**基本写法：查看系统属性**
`jcmd <pid> VM.system_properties`
```bash
# 输出 JVM 系统属性
jcmd 12345 VM.system_properties
```

---

**基本写法：触发 GC**
`jcmd <pid> GC.run`
```bash
# 显式触发一次垃圾回收
jcmd 12345 GC.run
```

---

**基本写法：查看类直方图**
`jcmd <pid> GC.class_histogram`
```bash
# 输出类实例直方图
jcmd 12345 GC.class_histogram
```

---

## jinfo 配置信息

**基本写法：查看 JVM 参数**
`jinfo -flags <pid>`
```bash
# 查看进程所有 JVM 标志
jinfo -flags 12345
```

---

**基本写法：查看系统属性**
`jinfo -sysprops <pid>`
```bash
# 查看进程系统属性
jinfo -sysprops 12345
```

---

**基本写法：动态设置参数**
`jinfo -flag <名称>=<值> <pid>`
```bash
# 运行时设置布尔型 JVM 标志
jinfo -flag +PrintGCDetails 12345
```

---

## 常用 JVM 启动参数

**基本写法：设置堆大小**
`-Xms<大小> -Xmx<大小>`
```bash
# 设置初始堆和最大堆均为 2g
java -Xms2g -Xmx2g -jar app.jar
```

---

**基本写法：设置年轻代大小**
`-Xmn<大小>`
```bash
# 设置年轻代大小为 512m
java -Xmn512m -jar app.jar
```

---

**基本写法：设置元空间大小**
`-XX:MetaspaceSize=<大小> -XX:MaxMetaspaceSize=<大小>`
```bash
# 设置元空间初始和最大值
java -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=512m -jar app.jar
```

---

**基本写法：选择 GC 收集器**
`-XX:+UseG1GC`
```bash
# 启用 G1 垃圾收集器
java -XX:+UseG1GC -jar app.jar
```

---

**基本写法：启用 ZGC**
`-XX:+UseZGC`
```bash
# 启用低延迟 ZGC 收集器
java -XX:+UseZGC -jar app.jar
```

---

**基本写法：GC 日志**
`-Xlog:gc*:<文件>:time`
```bash
# JDK 9+ 统一日志输出 GC 日志
java -Xlog:gc*:gc.log:time -jar app.jar
```

---

**基本写法：堆溢出转储**
`-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=<路径>`
```bash
# OOM 时自动生成堆转储
java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/var/log/dump -jar app.jar
```

---

## JFR 飞行记录器

**基本写法：启动并录制**
`jcmd <pid> JFR.start duration=<时长>s filename=<文件>`
```bash
# 启动 60 秒的 JFR 录制
jcmd 12345 JFR.start duration=60s filename=rec.jfr
```

---

**基本写法：查看录制状态**
`jcmd <pid> JFR.check`
```bash
# 检查 JFR 录制状态
jcmd 12345 JFR.check
```

---

**基本写法：停止录制**
`jcmd <pid> JFR.stop filename=<文件>`
```bash
# 停止并保存录制
jcmd 12345 JFR.stop filename=rec.jfr
```



<!-- ============ 文档分隔线：013-java/031-ThreadLocalMemoryLeak.md ============ -->

# Java ThreadLocal 与内存泄漏

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 ThreadLocal

**基本写法：创建 ThreadLocal**
`ThreadLocal.<类型>withInitial(() -> <初始值>);`
```java
// 创建带初始值的 ThreadLocal
ThreadLocal<Integer> counter = ThreadLocal.withInitial(() -> 0);
```

---

**基本写法：匿名内部类创建**
`new ThreadLocal<<类型>>() { protected <类型> initialValue() {} }`
```java
// 重写 initialValue 创建
ThreadLocal<List<String>> ctx = new ThreadLocal<>() {
    @Override
    protected List<String> initialValue() { return new ArrayList<>(); }
};
```

---

## 读写操作

**基本写法：设置值**
`<threadLocal>.set(<值>);`
```java
// 为当前线程设置值
counter.set(10);
```

---

**基本写法：获取值**
`<threadLocal>.get();`
```java
// 获取当前线程的值
int v = counter.get();
```

---

**基本写法：移除值**
`<threadLocal>.remove();`
```java
// 移除当前线程的值，防止内存泄漏
counter.remove();
```

---

## InheritableThreadLocal 子线程继承

**基本写法：创建可继承 ThreadLocal**
`new InheritableThreadLocal<<类型>>();`
```java
// 子线程可继承父线程的值
InheritableThreadLocal<String> itl = new InheritableThreadLocal<>();
itl.set("parent");
```

---

**基本写法：自定义子线程值**
`new InheritableThreadLocal<<类型>>() { protected <类型> childValue(<类型> p) {} }`
```java
// 子线程继承时对值做转换
InheritableThreadLocal<String> itl = new InheritableThreadLocal<>() {
    @Override
    protected String childValue(String parent) { return parent + "-child"; }
};
```

---

## TransmittableThreadLocal 跨线程池传递

**基本写法：使用 TransmittableThreadLocal（阿里 TTL 库）**
`new TransmittableThreadLocal<<类型>>();`
```java
// 线程池场景下传递上下文
TransmittableThreadLocal<String> ttl = new TransmittableThreadLocal<>();
ttl.set("ctx");
```

---

**基本写法：包装 Runnable**
`TtlRunnable.get(<runnable>);`
```java
// 提交任务时包装以传递上下文
executor.submit(TtlRunnable.get(() -> doWork(ttl.get())));
```

---

## ScopedValue（Java 21+ 预览）

**基本写法：创建 ScopedValue**
`private static final ScopedValue<<类型>> NAME = ScopedValue.newInstance();`
```java
// 创建不可变作用域值
static final ScopedValue<String> USER = ScopedValue.newInstance();
```

---

**基本写法：绑定并执行**
`ScopedValue.where(<sv>, <值>).run(() -> <方法>);`
```java
// 在作用域内绑定值并执行
ScopedValue.where(USER, "Alice").run(() -> {
    System.out.println(USER.get());
});
```

---

**基本写法：返回结果**
`ScopedValue.where(<sv>, <值>).call(() -> <表达式>);`
```java
// 作用域内执行并返回值
String r = ScopedValue.where(USER, "Alice").call(() -> "hello " + USER.get());
```

---

## 内存泄漏原理与排查

**基本写法：try-finally 清理**
`try { <tl>.set(<值>); ... } finally { <tl>.remove(); }`
```java
// 标准清理模式防止线程池泄漏
try {
    ctx.set(request);
    handle();
} finally {
    ctx.remove();
}
```

---

## 与线程池配合

**基本写法：装饰 Runnable 自动清理**
`Runnable wrapped = () -> { try { <tl>.set(v); run(); } finally { <tl>.remove(); } };`
```java
// 线程池任务包装自动清理 ThreadLocal
Runnable task = () -> {
    try { counter.set(1); doWork(); }
    finally { counter.remove(); }
};
```

---

## ThreadLocalRandom 随机数

**基本写法：获取当前线程随机数**
`ThreadLocalRandom.current().nextInt(<上界>);`
```java
// 线程本地随机数生成器
int n = ThreadLocalRandom.current().nextInt(100);
```

---

**基本写法：指定范围**
`ThreadLocalRandom.current().nextInt(<起>, <止>);`
```java
// 生成区间内随机数
int n = ThreadLocalRandom.current().nextInt(10, 20);
```

---

## ThreadLocal 与虚拟线程

**基本写法：虚拟线程下使用 ThreadLocal**
`Thread.ofVirtual().start(() -> { <tl>.set(v); ... });`
```java
// 虚拟线程下使用 ThreadLocal（不推荐大量使用）
Thread.ofVirtual().start(() -> {
    ctx.set("v");
    try { work(); } finally { ctx.remove(); }
});
```



<!-- ============ 文档分隔线：013-java/032-AnnotationProcessorAPT.md ============ -->

# Java 注解处理器 APT

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 定义注解

**基本写法：定义运行时注解**
`@Retention(RetentionPolicy.RUNTIME) @Target(<目标>) @interface <名称> {}`
```java
// 定义运行时保留的字段注解
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface MyField {
    String value();
}
```

---

**基本写法：定义源码级注解**
`@Retention(RetentionPolicy.SOURCE) @interface <名称> {}`
```java
// 仅源码保留的注解（用于 APT 处理）
@Retention(RetentionPolicy.SOURCE)
@Target(ElementType.TYPE)
public @interface Builder {
}
```

---

**基本写法：定义元注解的成员**
`@interface <名称> { <类型> <成员>() [default <默认值>]; }`
```java
// 注解带默认值
public @interface Cache {
    int ttl() default 60;
    String name() default "";
}
```

---

## 编写注解处理器

**基本写法：声明处理器**
`@SupportedAnnotationTypes("<注解全名>") @SupportedSourceVersion(<版本>) public class <类> extends AbstractProcessor {}`
```java
// 自定义注解处理器
@SupportedAnnotationTypes("com.example.Builder")
@SupportedSourceVersion(SourceVersion.RELEASE_21)
public class BuilderProcessor extends AbstractProcessor {
    @Override
    public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment env) {
        return true;
    }
}
```

---

**基本写法：获取被注解元素**
`env.getElementsAnnotatedWith(<注解类>);`
```java
// 收集所有被注解的元素
Set<? extends Element> set = env.getElementsAnnotatedWith(Builder.class);
```

---

**基本写法：获取 Filer 生成文件**
`processingEnv.getFiler().createSourceFile("<类名>");`
```java
// 生成 Java 源文件
JavaFileObject f = processingEnv.getFiler().createSourceFile("com.example.Generated");
```

---

**基本写法：获取 Messager 输出**
`processingEnv.getMessager().printMessage(<类型>, <消息>, <元素>);`
```java
// 编译期输出错误信息
processingEnv.getMessager().printMessage(Diagnostic.Kind.ERROR, "missing field", element);
```

---

## 注册处理器

**基本写法：SPI 注册文件**
`META-INF/services/javax.annotation.processing.Processor`
```
# 文件内容为处理器全限定名
com.example.BuilderProcessor
```

---

## Maven 编译配置

**基本写法：Maven 编译插件配置**
`<plugin> <artifactId>maven-compiler-plugin</artifactId> <configuration>`
```xml
<!-- 配置编译器使用的注解处理器 -->
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <annotationProcessors>
      <processor>com.example.BuilderProcessor</processor>
    </annotationProcessors>
  </configuration>
</plugin>
```

---

**基本写法：禁用注解处理**
`<proc>none</proc>`
```xml
<!-- 编译时关闭注解处理 -->
<configuration>
  <proc>none</proc>
</configuration>
```

---

## Gradle 编译配置

**基本写法：Gradle 配置注解处理器**
`annotationProcessor '<依赖坐标>'`
```groovy
// Gradle 注册注解处理器依赖
dependencies {
  annotationProcessor 'com.example:builder-processor:1.0'
}
```

---

**基本写法：Kotlin 使用 KSP**
`ksp('<依赖坐标>')`
```groovy
// Kotlin 符号处理 KSP
plugins { id("com.google.devtools.ksp") }
dependencies {
  ksp 'com.example:builder-processor:1.0'
}
```

---

## javac 命令

**基本写法：编译时指定处理器**
`javac -processor <处理器类> <源文件>`
```bash
# 编译时显式指定注解处理器
javac -processor com.example.BuilderProcessor src/Main.java
```

---

**基本写法：指定处理器路径**
`javac -processorpath <路径> -processor <类> <源文件>`
```bash
# 指定处理器所在 jar 路径
javac -processorpath processor.jar -processor com.example.BuilderProcessor src/Main.java
```

---

**基本写法：输出生成源码目录**
`javac -s <输出目录> <源文件>`
```bash
# 指定生成源文件输出目录
javac -s build/generated -processor com.example.BuilderProcessor src/Main.java
```

---

**基本写法：禁用注解处理**
`javac -proc:none <源文件>`
```bash
# 仅编译不执行注解处理
javac -proc:none src/Main.java
```

---

## 元素模型 Element

**基本写法：获取元素类型**
`<element>.getKind()`
```java
// 判断元素是类还是方法
if (element.getKind() == ElementKind.CLASS) { }
```

---

**基本写法：获取元素注解**
`<element>.getAnnotation(<注解类>);`
```java
// 读取元素上的注解
Builder b = element.getAnnotation(Builder.class);
```

---

**基本写法：获取类元素字段**
`<typeElement>.getEnclosedElements();`
```java
// 获取类中所有成员
List<? extends Element> members = typeElement.getEnclosedElements();
```

---

## 类型模型 Types / Elements

**基本写法：获取 Types 工具**
`processingEnv.getTypeUtils();`
```java
// 获取类型工具类
Types types = processingEnv.getTypeUtils();
```

---

**基本写法：获取 Elements 工具**
`processingEnv.getElementUtils();`
```java
// 获取元素工具类
Elements elements = processingEnv.getElementUtils();
```

---

**基本写法：按名获取 TypeElement**
`elements.getTypeElement("<全限定名>");`
```java
// 通过全限定名获取类型元素
TypeElement e = elements.getTypeElement("java.lang.String");
```

---

## 编译参数传递

**基本写法：读取编译选项**
`processingEnv.getOptions().get("<键>");`
```java
// 获取 -A 传递的参数
String v = processingEnv.getOptions().get("myOption");
```

---

**基本写法：javac 传递参数**
`javac -A<键>=<值> <源文件>`
```bash
# 通过 -A 选项向处理器传参
javac -AmyOption=value -processor com.example.BuilderProcessor src/Main.java
```



<!-- ============ 文档分隔线：013-java/033-JavaModuleSystemJPMS.md ============ -->

# Java 模块系统 JPMS

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## module-info.java 声明

**基本写法：声明模块**
`module <模块名> {}`
```java
// 定义模块 com.example.app
module com.example.app {
}
```

---

**基本写法：导出包**
`exports <包名>;`
```java
// 导出包供其他模块使用
module com.example.app {
    exports com.example.api;
}
```

---

**基本写法：导出到指定模块**
`exports <包名> to <模块名>;`
```java
// 仅向指定模块导出
module com.example.app {
    exports com.example.internal to com.example.other;
}
```

---

**基本写法：依赖模块**
`requires <模块名>;`
```java
// 声明依赖模块
module com.example.app {
    requires java.net.http;
}
```

---

**基本写法：传递依赖**
`requires transitive <模块名>;`
```java
// 依赖可传递给下游模块
module com.example.app {
    requires transitive java.sql;
}
```

---

**基本写法：静态依赖**
`requires static <模块名>;`
```java
// 仅编译期需要的依赖
module com.example.app {
    requires static java.annotation;
}
```

---

## 服务声明与使用

**基本写法：提供服务**
`provides <服务接口> with <实现类>;`
```java
// 声明模块提供的服务实现
module com.example.app {
    provides com.example.Service with com.example.ServiceImpl;
}
```

---

**基本写法：使用服务**
`uses <服务接口>;`
```java
// 声明模块使用 ServiceLoader 加载的服务
module com.example.app {
    uses com.example.Service;
}
```

---

**基本写法：打开包用于反射**
`opens <包名>;`
```java
// 允许其他模块反射访问
module com.example.app {
    opens com.example.entity;
}
```

---

**基本写法：打开包到指定模块**
`opens <包名> to <模块名>;`
```java
// 仅对指定模块开放反射
module com.example.app {
    opens com.example.entity to com.fasterxml.jackson.databind;
}
```

---

## java 命令运行模块

**基本写法：运行模块主类**
`java -m <模块>/<主类>`
```bash
# 运行模块化应用
java -m com.example.app/com.example.app.Main
```

---

**基本写法：指定模块路径**
`java --module-path <路径> -m <模块>/<主类>`
```bash
# 指定模块路径运行
java --module-path mods -m com.example.app/com.example.app.Main
```

---

**基本写法：升级模块路径**
`java --upgrade-module-path <路径> -m <模块>/<主类>`
```bash
# 替换可升级模块
java --upgrade-module-path upgrades -m com.example.app/com.example.app.Main
```

---

**基本写法：限制模块**
`java --limit-modules <模块1>,<模块2> -m <模块>/<主类>`
```bash
# 限制可观察的模块集合
java --limit-modules java.base,com.example.app -m com.example.app/com.example.app.Main
```

---

## javac 编译模块

**基本写法：编译模块源码**
`javac -d <输出> --module-source-path <路径> --module <模块>`
```bash
# 编译指定模块
javac -d out --module-source-path src --module com.example.app
```

---

**基本写法：编译所有模块**
`javac -d <输出> --module-source-path <路径> --module-source-path <路径> *`
```bash
# 编译源码路径下所有模块
javac -d out --module-source-path src --module *
```

---

## 打包模块 jar

**基本写法：打包模块 jar**
`jar --create --file=<jar> --module-version=<版本> -C <类目录> .`
```bash
# 创建带版本的模块 jar
jar --create --file=mods/com.example.app.jar --module-version=1.0 -C out/com.example.app .
```

---

**基本写法：jar 包含 module-info**
`jar --create --file=<jar> --main-class=<主类> -C <目录> .`
```bash
# 创建可执行模块 jar
jar --create --file=app.jar --main-class=com.example.app.Main -C out .
```

---

## jlink 创建运行时镜像

**基本写法：创建自定义 JRE**
`jlink --module-path <路径> --add-modules <模块> --output <目录>`
```bash
# 生成仅含所需模块的运行时镜像
jlink --module-path mods --add-modules com.example.app --output myimage
```

---

**基本写法：指定启动器**
`jlink --launcher <名称>=<模块>/<主类> --add-modules <模块> --output <目录>`
```bash
# 生成带启动脚本的可执行镜像
jlink --launcher app=com.example.app/com.example.app.Main --module-path mods --add-modules com.example.app --output myimage
```

---

**基本写法：压缩镜像**
`jlink --compress=<级别> --add-modules <模块> --output <目录>`
```bash
# 压缩级别 0-2 减小镜像体积
jlink --compress=2 --module-path mods --add-modules com.example.app --output myimage
```

---

## 模块相关 API

**基本写法：获取模块**
`<类>.class.getModule();`
```java
// 获取类所属模块
Module m = String.class.getModule();
```

---

**基本写法：获取模块名**
`<module>.getName();`
```java
// 获取模块名称
String name = m.getName();
```

---

**基本写法：加载类**
`<module>.getClassLoader().loadClass("<类名>");`
```java
// 通过模块的类加载器加载类
Class<?> c = m.getClassLoader().loadClass("com.example.App");
```

---

## jdeps 依赖分析

**基本写法：分析模块依赖**
`jdeps --module-path <路径> -m <模块>`
```bash
# 分析模块的依赖关系
jdeps --module-path mods -m com.example.app
```

---

**基本写法：生成 module-info**
`jdeps --generate-module-info <输出目录> <jar>`
```bash
# 为已有 jar 生成模块描述
jdeps --generate-module-info out lib.jar
```

---

**基本写法：列出依赖**
`jdeps -s <jar>`
```bash
# 简洁列出 jar 包依赖
jdeps -s app.jar
```



<!-- ============ 文档分隔线：013-java/034-JavaTextBlock.md ============ -->

# Java 文本块与字符串

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文本块基础

**基本写法：创建文本块**
`"""<换行><内容><换行>"""`
```java
// Java 15+ 多行字符串文本块
String json = """
    {
      "name": "Alice"
    }
    """;
```

---

**基本写法：文本块结尾控制**
`<内容>\n    """`
```java
// 末尾缩进决定去除前导空格
String s = """
    hello
    """;
```

---

**基本写法：保留末尾换行**
`"""<换行><内容>\n"""`
```java
// 行尾反斜杠表示不换行
String s = """
    hello \
    world
    """;
```

---

## 字符串模板（Java 21 预览）

**基本写法：字符串模板表达式**
`StringTemplate.STR."<文本>\{<表达式>}"`
```java
// Java 21 预览特性字符串模板
String name = "Alice";
String s = STR."Hello \{name}";
```

---

**基本写法：多变量插值**
`STR."<文本>\{<变量1>}\{<变量2>}"`
```java
// 模板中嵌入多个表达式
int x = 1, y = 2;
String s = STR."\{x} + \{y} = \{x + y}";
```

---

## 字符串常用操作

**基本写法：字符串格式化**
`String.format("<模板>", <参数>...)`
```java
// printf 风格格式化
String s = String.format("name=%s, age=%d", "Alice", 20);
```

---

**基本写法：formatted 方法**
`"<模板>".formatted(<参数>...)`
```java
// Java 15+ 实例方法格式化
String s = "name=%s".formatted("Alice");
```

---

**基本写法：拼接**
`String.join("<分隔符>", <元素>...)`
```java
// 用分隔符拼接字符串
String r = String.join(",", "a", "b", "c");
```

---

## 文本块与格式化结合

**基本写法：文本块格式化**
`"""<内容>""".formatted(<参数>...)`
```java
// 文本块配合 formatted 占位
String json = """
    {"name":"%s","age":%d}
    """.formatted("Alice", 20);
```

---

## 缩进控制

**基本写法：去除缩进**
`<字符串>.stripIndent();`
```java
// 去除最小公共缩进
String s = raw.stripIndent();
```

---

**基本写法：转义换行**
`<字符串>.translateEscapes();`
```java
// 将转义字符翻译为实际字符
String s = "a\\nb".translateEscapes();
```

---

## 字符串拼接

**基本写法：StringBuilder 拼接**
`StringBuilder sb = new StringBuilder(); sb.append(<值>);`
```java
// 可变字符串拼接
StringBuilder sb = new StringBuilder();
sb.append("a").append(1);
String r = sb.toString();
```

---

**基本写法：StringJoiner 拼接**
`new StringJoiner("<分隔符>", "[", "]").add(<值>);`
```java
// 带前后缀的拼接器
String r = new StringJoiner(",", "[", "]").add("a").add("b").toString();
```

---

## 字符串查找与判断

**基本写法：判断前后缀**
`<字符串>.startsWith("<前缀>");`
```java
// 判断是否以指定前缀开头
boolean b = "hello".startsWith("he");
```

---

**基本写法：包含子串**
`<字符串>.contains("<子串>");`
```java
// 判断是否包含子串
boolean b = "hello".contains("ell");
```

---

**基本写法：查找位置**
`<字符串>.indexOf("<子串>);`
```java
// 查找子串首次出现位置
int i = "hello".indexOf("l");
```

---

## 字符串转换

**基本写法：分割**
`<字符串>.split("<正则>);`
```java
// 按正则分割字符串
String[] parts = "a,b,c".split(",");
```

---

**基本写法：替换**
`<字符串>.replace("<旧>", "<新>");`
```java
// 替换所有匹配字面量
String s = "hello".replace("l", "L");
```

---

**基本写法：replaceAll 正则替换**
`<字符串>.replaceAll("<正则>", "<替换>");`
```java
// 使用正则替换
String s = "a1b2".replaceAll("\\d", "_");
```

---

**基本写法：去除空白**
`<字符串>.strip();`
```java
// 去除首尾 Unicode 空白
String s = "  hi  ".strip();
```

---

## 字符串与字节转换

**基本写法：编码为字节**
`<字符串>.getBytes(<字符集>);`
```java
// 使用 UTF-8 编码为字节
byte[] b = "hi".getBytes(StandardCharsets.UTF_8);
```

---

**基本写法：字节解码**
`new String(<字节数组>, <字符集>);`
```java
// 用指定字符集构造字符串
String s = new String(bytes, StandardCharsets.UTF_8);
```

---

## 重复与缩进

**基本写法：重复字符串**
`"<字符串>".repeat(<次数>);`
```java
// Java 11+ 字符串重复
String s = "ab".repeat(3);
```

---

**基本写法：添加缩进**
`<字符串>.indent(<空格数>);`
```java
// Java 12+ 给每行增加缩进
String s = "a\nb".indent(4);
```

---

## 字符串判空

**基本写法：判断空白**
`<字符串>.isBlank();`
```java
// Java 11+ 判断是否空白
boolean b = "   ".isBlank();
```

---

**基本写法：判断空**
`<字符串>.isEmpty();`
```java
// 判断长度是否为 0
boolean b = "".isEmpty();
```



<!-- ============ 文档分隔线：013-java/035-JavaSerialization.md ============ -->

# Java 序列化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Serializable 接口

**基本写法：实现可序列化**
`class <类名> implements Serializable {}`
```java
// 标记类为可序列化
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
}
```

---

**基本写法：定义 serialVersionUID**
`private static final long serialVersionUID = <值>L;`
```java
// 显式声明版本号保证兼容
private static final long serialVersionUID = 42L;
```

---

## 对象流序列化

**基本写法：写入对象**
`new ObjectOutputStream(<输出流>).writeObject(<对象>);`
```java
// 序列化对象到文件
try (ObjectOutputStream oos = new ObjectOutputStream(
        new FileOutputStream("user.dat"))) {
    oos.writeObject(user);
}
```

---

**基本写法：读取对象**
`new ObjectInputStream(<输入流>).readObject();`
```java
// 从文件反序列化对象
try (ObjectInputStream ois = new ObjectInputStream(
        new FileInputStream("user.dat"))) {
    User u = (User) ois.readObject();
}
```

---

## 关键字 transient

**基本写法：排除字段**
`transient <类型> <字段名>;`
```java
// 标记字段不参与序列化
private transient String password;
```

---

## 自定义序列化

**基本写法：重写 writeObject**
`private void writeObject(ObjectOutputStream out) throws IOException {}`
```java
// 自定义写入逻辑
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    out.writeUTF(encrypt(password));
}
```

---

**基本写法：重写 readObject**
`private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {}`
```java
// 自定义读取逻辑
private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    this.password = decrypt(in.readUTF());
}
```

---

**基本写法：writeReplace 替换对象**
`private Object writeReplace() { return <新对象>; }`
```java
// 序列化时替换为另一个对象
private Object writeReplace() {
    return new UserProxy(name);
}
```

---

**基本写法：readResolve 单例恢复**
`private Object readResolve() { return <实例>; }`
```java
// 反序列化时返回单例实例
private Object readResolve() {
    return INSTANCE;
}
```

---

## Externalizable 接口

**基本写法：实现 Externalizable**
`class <类名> implements Externalizable { public void writeExternal(ObjectOutput o) {} public void readExternal(ObjectInput i) {} }`
```java
// 完全自定义序列化
public class User implements Externalizable {
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeUTF(name);
    }
    public void readExternal(ObjectInput in) throws IOException {
        this.name = in.readUTF();
    }
}
```

---

## 序列化过滤（Java 9+）

**基本写法：设置输入过滤器**
`ObjectInputFilter.Config.createFilter("<规则>")`
```java
// 反序列化白名单过滤
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.example.*;java.lang.*;!*");
ois.setObjectInputFilter(filter);
```

---

**基本写法：全局过滤器**
`ObjectInputFilter.Config.setSerialFilter(<过滤器>);`
```java
// 设置全局反序列化过滤器
ObjectInputFilter.Config.setSerialFilter(info -> {
    if (info.serialClass() == User.class) return ObjectInputFilter.Status.ALLOWED;
    return ObjectInputFilter.Status.REJECTED;
});
```

---

## JSON 序列化（Jackson）

**基本写法：Jackson 写 JSON**
`new ObjectMapper().writeValueAsString(<对象>);`
```java
// 将对象序列化为 JSON 字符串
String json = new ObjectMapper().writeValueAsString(user);
```

---

**基本写法：Jackson 读 JSON**
`new ObjectMapper().readValue(<json>, <类>.class);`
```java
// 将 JSON 字符串反序列化为对象
User u = new ObjectMapper().readValue(json, User.class);
```

---

**基本写法：Jackson 写文件**
`new ObjectMapper().writeValue(<文件>, <对象>);`
```java
// 将对象序列化到 JSON 文件
new ObjectMapper().writeValue(new File("user.json"), user);
```

---

**基本写法：忽略字段**
`@JsonIgnore`
```java
// 标记字段不参与 JSON 序列化
@JsonIgnore
private String password;
```

---

**基本写法：指定字段名**
`@JsonProperty("<名称>")`
```java
// 自定义 JSON 字段名
@JsonProperty("user_name")
private String userName;
```

---

## JSON 序列化（Gson）

**基本写法：Gson 写 JSON**
`new Gson().toJson(<对象>);`
```java
// 使用 Gson 序列化为 JSON
String json = new Gson().toJson(user);
```

---

**基本写法：Gson 读 JSON**
`new Gson().fromJson(<json>, <类>.class);`
```java
// 使用 Gson 反序列化
User u = new Gson().fromJson(json, User.class);
```

---

## ProtoBuf 二进制序列化

**基本写法：ProtoBuf 写入**
`<消息类>.writeTo(<输出流>);`
```java
// ProtoBuf 消息写入字节流
UserProto.User u = UserProto.User.newBuilder().setName("Alice").build();
u.writeTo(new FileOutputStream("u.bin"));
```

---

**基本写法：ProtoBuf 读取**
`<消息类>.parseFrom(<输入流>);`
```java
// 从字节流解析 ProtoBuf 消息
UserProto.User u = UserProto.User.parseFrom(new FileInputStream("u.bin"));
```



<!-- ============ 文档分隔线：013-java/036-JDBCDatabaseConnection.md ============ -->

# Java JDBC 数据库连接

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 建立连接

**基本写法：DriverManager 获取连接**
`DriverManager.getConnection("<url>", "<用户>", "<密码>");`
```java
// 建立数据库连接
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/db", "root", "pwd");
```

---

**基本写法：使用 Properties**
`DriverManager.getConnection(<url>, <properties>);`
```java
// 通过 Properties 传参
Properties p = new Properties();
p.setProperty("user", "root");
p.setProperty("password", "pwd");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", p);
```

---

## Statement 执行 SQL

**基本写法：创建 Statement**
`<connection>.createStatement();`
```java
// 创建静态 SQL 执行器
Statement st = conn.createStatement();
```

---

**基本写法：执行查询**
`<statement>.executeQuery("<sql>");`
```java
// 执行查询并返回结果集
ResultSet rs = st.executeQuery("SELECT * FROM user");
```

---

**基本写法：执行更新**
`<statement>.executeUpdate("<sql>");`
```java
// 执行 INSERT/UPDATE/DELETE
int rows = st.executeUpdate("DELETE FROM user WHERE id=1");
```

---

## PreparedStatement 参数化

**基本写法：创建预编译语句**
`<connection>.prepareStatement("<sql>");`
```java
// 预编译防 SQL 注入
PreparedStatement ps = conn.prepareStatement(
    "SELECT * FROM user WHERE id = ?");
```

---

**基本写法：设置参数**
`<ps>.setInt(<位置>, <值>);`
```java
// 按位置设置整型参数
ps.setInt(1, 100);
```

---

**基本写法：设置字符串参数**
`<ps>.setString(<位置>, <值>);`
```java
// 按位置设置字符串参数
ps.setString(1, "Alice");
```

---

**基本写法：执行预编译查询**
`<ps>.executeQuery();`
```java
// 执行预编译查询
ResultSet rs = ps.executeQuery();
```

---

**基本写法：执行预编译更新**
`<ps>.executeUpdate();`
```java
// 执行预编译更新
int rows = ps.executeUpdate();
```

---

## ResultSet 遍历

**基本写法：遍历结果集**
`while (<rs>.next()) { <rs>.getX("<列>"); }`
```java
// 按列名读取结果
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

---

**基本写法：按索引取值**
`<rs>.getInt(<位置>);`
```java
// 按列位置取值
int id = rs.getInt(1);
```

---

**基本写法：可滚动结果集**
`<connection>.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);`
```java
// 创建可前后滚动的结果集
Statement st = conn.createStatement(
    ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
```

---

**基本写法：跳转到指定行**
`<rs>.absolute(<行号>);`
```java
// 移动到绝对行
rs.absolute(5);
```

---

## 事务管理

**基本写法：关闭自动提交**
`<connection>.setAutoCommit(false);`
```java
// 开启手动事务
conn.setAutoCommit(false);
```

---

**基本写法：提交事务**
`<connection>.commit();`
```java
// 提交当前事务
conn.commit();
```

---

**基本写法：回滚事务**
`<connection>.rollback();`
```java
// 回滚当前事务
conn.rollback();
```

---

**基本写法：设置保存点**
`<connection>.setSavepoint();`
```java
// 设置保存点
Savepoint sp = conn.setSavepoint();
```

---

**基本写法：回滚到保存点**
`<connection>.rollback(<savepoint>);`
```java
// 回滚到指定保存点
conn.rollback(sp);
```

---

## 批处理

**基本写法：添加批处理**
`<ps>.addBatch();`
```java
// 添加到批处理
ps.setInt(1, 1); ps.addBatch();
ps.setInt(1, 2); ps.addBatch();
```

---

**基本写法：执行批处理**
`<ps>.executeBatch();`
```java
// 执行批量操作
int[] counts = ps.executeBatch();
```

---

**基本写法：清空批处理**
`<ps>.clearBatch();`
```java
// 清空批处理队列
ps.clearBatch();
```

---

## 获取自增主键

**基本写法：返回生成键**
`<connection>.prepareStatement(<sql>, Statement.RETURN_GENERATED_KEYS);`
```java
// 执行后获取自增主键
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO user(name) VALUES(?)", Statement.RETURN_GENERATED_KEYS);
ps.setString(1, "Alice");
ps.executeUpdate();
ResultSet keys = ps.getGeneratedKeys();
if (keys.next()) { long id = keys.getLong(1); }
```

---

## 连接池

**基本写法：HikariCP 配置**
`new HikariConfig(); new HikariDataSource(<config>);`
```java
// 配置 HikariCP 连接池
HikariConfig cfg = new HikariConfig();
cfg.setJdbcUrl("jdbc:mysql://localhost/db");
cfg.setUsername("root");
cfg.setPassword("pwd");
cfg.setMaximumPoolSize(10);
HikariDataSource ds = new HikariDataSource(cfg);
Connection conn = ds.getConnection();
```

---

## try-with-resources 自动关闭

**基本写法：自动关闭资源**
`try (Connection c = ...; PreparedStatement p = ...) { }`
```java
// 自动关闭连接、语句、结果集
try (Connection c = ds.getConnection();
     PreparedStatement p = c.prepareStatement(sql)) {
    try (ResultSet rs = p.executeQuery()) {
        while (rs.next()) { }
    }
}
```

---

## 元数据查询

**基本写法：获取表元数据**
`<connection>.getMetaData().getTables(null, null, "<表名>", null);`
```java
// 查询数据库表信息
ResultSet rs = conn.getMetaData().getTables(null, null, "user", null);
```

---

**基本写法：获取结果集元数据**
`<rs>.getMetaData().getColumnCount();`
```java
// 获取列数及列名
ResultSetMetaData md = rs.getMetaData();
int n = md.getColumnCount();
String name = md.getColumnName(1);
```

---

## DataSource 与 JNDI

**基本写法：从 JNDI 获取 DataSource**
`InitialContext.doLookup("java:comp/env/jdbc/db");`
```java
// 通过 JNDI 查找数据源
DataSource ds = InitialContext.doLookup("java:comp/env/jdbc/db");
Connection conn = ds.getConnection();
```



<!-- ============ 文档分隔线：013-java/037-JavaDateTimeAPI.md ============ -->

# Java 日期时间 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## LocalDate 本地日期

**基本写法：创建本地日期**
`LocalDate.of(<年>, <月>, <日>);`
```java
// 创建指定日期
LocalDate d = LocalDate.of(2025, 7, 31);
```

---

**基本写法：当前日期**
`LocalDate.now();`
```java
// 获取当前日期
LocalDate today = LocalDate.now();
```

---

**基本写法：解析日期**
`LocalDate.parse("<字符串>");`
```java
// 按默认格式解析
LocalDate d = LocalDate.parse("2025-07-31");
```

---

**基本写法：日期加减**
`<date>.plusDays(<天数>);`
```java
// 加 1 天
LocalDate tmw = today.plusDays(1);
```

---

**基本写法：日期减**
`<date>.minusMonths(<月数>);`
```java
// 减 1 个月
LocalDate last = today.minusMonths(1);
```

---

## LocalTime 本地时间

**基本写法：创建本地时间**
`LocalTime.of(<时>, <分>, <秒>);`
```java
// 创建指定时间
LocalTime t = LocalTime.of(10, 30, 0);
```

---

**基本写法：当前时间**
`LocalTime.now();`
```java
// 获取当前时间
LocalTime now = LocalTime.now();
```

---

## LocalDateTime 日期时间

**基本写法：创建日期时间**
`LocalDateTime.of(<日期>, <时间>);`
```java
// 组合日期和时间
LocalDateTime dt = LocalDateTime.of(LocalDate.now(), LocalTime.now());
```

---

**基本写法：当前日期时间**
`LocalDateTime.now();`
```java
// 获取当前日期时间
LocalDateTime now = LocalDateTime.now();
```

---

**基本写法：解析日期时间**
`LocalDateTime.parse("<字符串>");`
```java
// 解析 ISO 格式
LocalDateTime dt = LocalDateTime.parse("2025-07-31T10:30:00");
```

---

## ZonedDateTime 时区日期时间

**基本写法：指定时区**
`ZonedDateTime.now(ZoneId.of("<时区>"));`
```java
// 获取指定时区的当前时间
ZonedDateTime z = ZonedDateTime.now(ZoneId.of("Asia/Shanghai"));
```

---

**基本写法：转换为另一时区**
`<zonedDateTime>.withZoneSameInstant(ZoneId.of("<时区>"));`
```java
// 同一时刻转换时区
ZonedDateTime utc = z.withZoneSameInstant(ZoneId.of("UTC"));
```

---

## Instant 时间戳

**基本写法：当前 Instant**
`Instant.now();`
```java
// 获取 UTC 时间戳
Instant now = Instant.now();
```

---

**基本写法：从纪元创建**
`Instant.ofEpochSecond(<秒>);`
```java
// 从 Unix 时间戳创建
Instant i = Instant.ofEpochSecond(1700000000);
```

---

**基本写法：获取秒数**
`<instant>.getEpochSecond();`
```java
// 获取 Unix 秒数
long sec = now.getEpochSecond();
```

---

**基本写法：获取毫秒**
`<instant>.toEpochMilli();`
```java
// 获取 Unix 毫秒
long ms = now.toEpochMilli();
```

---

## Duration 时长

**基本写法：创建时长**
`Duration.ofMinutes(<分钟>);`
```java
// 创建 30 分钟时长
Duration d = Duration.ofMinutes(30);
```

---

**基本写法：计算两个时间差**
`Duration.between(<开始>, <结束>);`
```java
// 计算时长
Duration d = Duration.between(t1, t2);
```

---

**基本写法：获取秒数**
`<duration>.toSeconds();`
```java
// 转换为秒
long s = d.toSeconds();
```

---

## Period 日期段

**基本写法：创建日期段**
`Period.of(<年>, <月>, <日>);`
```java
// 创建 1 年 2 月 3 天
Period p = Period.of(1, 2, 3);
```

---

**基本写法：计算日期差**
`Period.between(<开始>, <结束>);`
```java
// 计算两个日期间隔
Period p = Period.between(d1, d2);
```

---

## DateTimeFormatter 格式化

**基本写法：自定义格式**
`DateTimeFormatter.ofPattern("<模式>");`
```java
// 定义格式化模式
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
```

---

**基本写法：格式化输出**
`<datetime>.format(<formatter>);`
```java
// 格式化为字符串
String s = now.format(fmt);
```

---

**基本写法：解析字符串**
`LocalDateTime.parse("<字符串>", <formatter>);`
```java
// 按指定格式解析
LocalDateTime dt = LocalDateTime.parse("2025-07-31 10:30:00", fmt);
```

---

**基本写法：内置格式**
`DateTimeFormatter.ISO_LOCAL_DATE;`
```java
// 使用内置 ISO 格式
String s = today.format(DateTimeFormatter.ISO_LOCAL_DATE);
```

---

## 时区与转换

**基本写法：LocalDateTime 转 Instant**
`<datetime>.atZone(ZoneId.of("<时区>")).toInstant();`
```java
// 本地时间转时间戳
Instant i = dt.atZone(ZoneId.of("Asia/Shanghai")).toInstant();
```

---

**基本写法：Instant 转 LocalDateTime**
`<instant>.atZone(ZoneId.of("<时区>")).toLocalDateTime();`
```java
// 时间戳转本地时间
LocalDateTime dt = i.atZone(ZoneId.of("Asia/Shanghai")).toLocalDateTime();
```

---

## Date 旧 API 转换

**基本写法：Date 转 Instant**
`<date>.toInstant();`
```java
// 旧 Date 转新 API
Instant i = new Date().toInstant();
```

---

**基本写法：Instant 转 Date**
`Date.from(<instant>);`
```java
// 新 API 转旧 Date
Date d = Date.from(Instant.now());
```

---

## ChronoUnit 计算差值

**基本写法：计算天数差**
`ChronoUnit.DAYS.between(<开始>, <结束>);`
```java
// 计算两个日期相差天数
long days = ChronoUnit.DAYS.between(d1, d2);
```

---

**基本写法：计算小时差**
`ChronoUnit.HOURS.between(<开始>, <结束>);`
```java
// 计算两个时间相差小时
long hours = ChronoUnit.HOURS.between(t1, t2);
```

---

## TemporalAdjusters 调整器

**基本写法：获取下周一**
`<date>.with(TemporalAdjusters.next(DayOfWeek.MONDAY));`
```java
// 调整到下一个周一
LocalDate next = today.with(TemporalAdjusters.next(DayOfWeek.MONDAY));
```

---

**基本写法：当月最后一天**
`<date>.with(TemporalAdjusters.lastDayOfMonth());`
```java
// 获取本月最后一天
LocalDate last = today.with(TemporalAdjusters.lastDayOfMonth());
```



<!-- ============ 文档分隔线：013-java/038-JavaOptionalClass.md ============ -->

# Java Optional 类

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Optional

**基本写法：创建非空 Optional**
`Optional.of(<值>);`
```java
// 包装非空值，为 null 抛 NPE
Optional<String> o = Optional.of("hello");
```

---

**基本写法：创建可空 Optional**
`Optional.ofNullable(<值>);`
```java
// 包装可能为 null 的值
Optional<String> o = Optional.ofNullable(getName());
```

---

**基本写法：创建空 Optional**
`Optional.empty();`
```java
// 创建空 Optional
Optional<String> empty = Optional.empty();
```

---

## 判断与获取

**基本写法：判断是否存在**
`<optional>.isPresent();`
```java
// 判断是否有值
boolean has = o.isPresent();
```

---

**基本写法：判断为空**
`<optional>.isEmpty();`
```java
// Java 11+ 判断是否为空
boolean empty = o.isEmpty();
```

---

**基本写法：获取值**
`<optional>.get();`
```java
// 获取值（为空抛 NoSuchElementException）
String v = o.get();
```

---

**基本写法：存在则执行**
`<optional>.ifPresent(<消费者>);`
```java
// 值存在时执行消费
o.ifPresent(System.out::println);
```

---

## 默认值

**基本写法：默认值**
`<optional>.orElse(<默认值>);`
```java
// 为空返回默认值
String v = o.orElse("default");
```

---

**基本写法：默认值惰性求值**
`<optional>.orElseGet(() -> <计算>);`
```java
// 为空时惰性计算默认值
String v = o.orElseGet(() -> fetchDefault());
```

---

**基本写法：为空抛异常**
`<optional>.orElseThrow();`
```java
// 为空抛 NoSuchElementException
String v = o.orElseThrow();
```

---

**基本写法：抛自定义异常**
`<optional>.orElseThrow(() -> new <异常>());`
```java
// 为空抛自定义异常
String v = o.orElseThrow(() -> new RuntimeException("no value"));
```

---

## 链式操作

**基本写法：map 转换**
`<optional>.map(<函数>);`
```java
// 值存在则转换
Optional<Integer> len = o.map(String::length);
```

---

**基本写法：flatMap 嵌套扁平化**
`<optional>.flatMap(<函数>);`
```java
// 处理返回 Optional 的函数
Optional<String> r = o.flatMap(this::findEmail);
```

---

**基本写法：filter 过滤**
`<optional>.filter(<条件>);`
```java
// 不满足条件则返回空
Optional<String> r = o.filter(s -> s.length() > 3);
```

---

## 提供备选 Optional

**基本写法：备选 Optional**
`<optional>.or(() -> <其他 Optional>);`
```java
// 为空则返回另一个 Optional
Optional<String> r = o.or(() -> Optional.of("backup"));
```

---

## 流式消费

**基本写法：存在则执行 else 执行**
`<optional>.ifPresentOrElse(<消费者>, <运行>);`
```java
// 存在执行 A 否则执行 B
o.ifPresentOrElse(
    v -> System.out.println(v),
    () -> System.out.println("empty")
);
```

---

## Optional 与 Stream

**基本写法：转 Stream**
`<optional>.stream();`
```java
// 转 Stream 便于链式处理
Stream<String> s = o.stream();
```

---

**基本写法：过滤空 Optional**
`<list>.stream().flatMap(Optional::stream)`
```java
// 过滤掉集合中的空 Optional
List<String> r = list.stream()
    .map(this::find)
    .flatMap(Optional::stream)
    .toList();
```

---

## 原始类型 Optional

**基本写法：OptionalInt**
`OptionalInt.of(<值>);`
```java
// int 专用 Optional
OptionalInt oi = OptionalInt.of(42);
```

---

**基本写法：OptionalDouble**
`OptionalDouble.of(<值>);`
```java
// double 专用 Optional
OptionalDouble od = OptionalDouble.of(3.14);
```

---

**基本写法：OptionalLong**
`OptionalLong.of(<值>);`
```java
// long 专用 Optional
OptionalLong ol = OptionalLong.of(100L);
```

---

## 实用模式

**基本写法：方法返回 Optional**
`public Optional<<类型>> <方法>() { return Optional.ofNullable(<值>); }`
```java
// 方法返回 Optional 表达可能为空
public Optional<User> findById(long id) {
    return Optional.ofNullable(map.get(id));
}
```

---

**基本写法：链式调用避免 null**
`opt.map(<取值>).map(<再取>).orElse(<默认>);`
```java
// 链式调用避免 NPE
String city = optUser.map(User::getAddr).map(Addr::getCity).orElse("unknown");
```

---

## equals 比较

**基本写法：安全比较**
`<optional>.equals(<其他 Optional>);`
```java
// 比较两个 Optional 的值
boolean same = o1.equals(o2);
```



<!-- ============ 文档分隔线：013-java/039-ExecutorForkJoinPool.md ============ -->

# Java Executor 与 ForkJoin

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ExecutorService 创建

**基本写法：固定线程池**
`Executors.newFixedThreadPool(<线程数>);`
```java
// 创建固定大小线程池
ExecutorService pool = Executors.newFixedThreadPool(4);
```

---

**基本写法：缓存线程池**
`Executors.newCachedThreadPool();`
```java
// 按需创建线程的缓存池
ExecutorService pool = Executors.newCachedThreadPool();
```

---

**基本写法：单线程池**
`Executors.newSingleThreadExecutor();`
```java
// 单线程顺序执行
ExecutorService pool = Executors.newSingleThreadExecutor();
```

---

**基本写法：定时任务线程池**
`Executors.newScheduledThreadPool(<线程数>);`
```java
// 支持定时和周期任务的线程池
ScheduledExecutorService pool = Executors.newScheduledThreadPool(2);
```

---

**基本写法：虚拟线程池（Java 21+）**
`Executors.newVirtualThreadPerTaskExecutor();`
```java
// 每任务一虚拟线程的执行器
ExecutorService pool = Executors.newVirtualThreadPerTaskExecutor();
```

---

## 自定义 ThreadPoolExecutor

**基本写法：自定义线程池**
`new ThreadPoolExecutor(<核心>, <最大>, <空闲时长>, <单位>, <队列>);`
```java
// 自定义线程池参数
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS, new LinkedBlockingQueue<>(100));
```

---

**基本写法：自定义线程工厂**
`new ThreadPoolExecutor(<参数>, <队列>, <线程工厂>);`
```java
// 设置命名线程工厂便于排查
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(),
    new ThreadFactoryBuilder().setNameFormat("worker-%d").build());
```

---

**基本写法：自定义拒绝策略**
`new ThreadPoolExecutor(<参数>, <队列>, <工厂>, <拒绝策略>);`
```java
// 队列满时由调用线程执行
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(10),
    new ThreadPoolExecutor.CallerRunsPolicy());
```

---

## 提交任务

**基本写法：提交 Runnable**
`<pool>.submit(<Runnable>);`
```java
// 提交无返回值任务
Future<?> f = pool.submit(() -> doWork());
```

---

**基本写法：提交 Callable**
`<pool>.submit(<Callable>);`
```java
// 提交有返回值任务
Future<Integer> f = pool.submit(() -> compute());
```

---

**基本写法：批量提交**
`<pool>.invokeAll(<任务集合>);`
```java
// 批量提交并等待全部完成
List<Future<Integer>> futures = pool.invokeAll(tasks);
```

---

**基本写法：任一完成返回**
`<pool>.invokeAny(<任务集合>);`
```java
// 任一任务完成即返回结果
Integer r = pool.invokeAny(tasks);
```

---

## Future 操作

**基本写法：获取结果**
`<future>.get();`
```java
// 阻塞等待结果
Integer r = future.get();
```

---

**基本写法：超时获取**
`<future>.get(<超时>, <单位>);`
```java
// 最多等待 1 秒
Integer r = future.get(1, TimeUnit.SECONDS);
```

---

**基本写法：取消任务**
`<future>.cancel(<是否中断>);`
```java
// 中断运行中的任务
future.cancel(true);
```

---

**基本写法：判断完成**
`<future>.isDone();`
```java
// 判断任务是否完成
boolean done = future.isDone();
```

---

## 关闭线程池

**基本写法：优雅关闭**
`<pool>.shutdown();`
```java
// 不再接受新任务，等待已提交任务完成
pool.shutdown();
```

---

**基本写法：立即关闭**
`<pool>.shutdownNow();`
```java
// 尝试中断所有任务并返回未执行任务
List<Runnable> notRun = pool.shutdownNow();
```

---

**基本写法：等待终止**
`<pool>.awaitTermination(<超时>, <单位>);`
```java
// 等待关闭完成最多 60 秒
pool.awaitTermination(60, TimeUnit.SECONDS);
```

---

**基本写法：try-with-resources 关闭**
`try (ExecutorService pool = ...) { }`
```java
// Java 19+ 自动关闭执行器
try (ExecutorService pool = Executors.newVirtualThreadPerTaskExecutor()) {
    pool.submit(() -> doWork());
}
```

---

## ScheduledExecutorService 定时任务

**基本写法：延迟执行**
`<pool>.schedule(<任务>, <延迟>, <单位>);`
```java
// 延迟 5 秒后执行一次
pool.schedule(() -> doWork(), 5, TimeUnit.SECONDS);
```

---

**基本写法：固定速率周期**
`<pool>.scheduleAtFixedRate(<任务>, <初始延迟>, <周期>, <单位>);`
```java
// 每 10 秒执行一次
pool.scheduleAtFixedRate(() -> doWork(), 0, 10, TimeUnit.SECONDS);
```

---

**基本写法：固定延迟周期**
`<pool>.scheduleWithFixedDelay(<任务>, <初始延迟>, <间隔>, <单位>);`
```java
// 上次结束后 10 秒再执行
pool.scheduleWithFixedDelay(() -> doWork(), 0, 10, TimeUnit.SECONDS);
```

---

## ForkJoinPool

**基本写法：创建 ForkJoinPool**
`new ForkJoinPool(<并行度>);`
```java
// 创建并行度为 CPU 核数的 ForkJoinPool
ForkJoinPool pool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());
```

---

**基本写法：提交 RecursiveTask**
`<pool>.invoke(<任务>);`
```java
// 提交有返回值的分治任务
Integer r = pool.invoke(new SumTask(0, 1000));
```

---

**基本写法：提交 RecursiveAction**
`<pool>.execute(<任务>);`
```java
// 提交无返回值的分治任务
pool.execute(new PrintTask(0, 100));
```

---

## RecursiveTask 分治

**基本写法：继承 RecursiveTask**
`class <类> extends RecursiveTask<<返回类型>> { protected <类型> compute() {} }`
```java
// 分治任务带返回值
class SumTask extends RecursiveTask<Integer> {
    private final int start, end;
    protected Integer compute() {
        if (end - start < 100) return start + end;
        SumTask left = new SumTask(start, (start + end) / 2);
        SumTask right = new SumTask((start + end) / 2 + 1, end);
        left.fork();
        return right.compute() + left.join();
    }
}
```

---

**基本写法：fork 异步执行**
`<task>.fork();`
```java
// 异步提交子任务
left.fork();
```

---

**基本写法：join 等待结果**
`<task>.join();`
```java
// 阻塞等待子任务结果
int r = left.join();
```

---

## 并行流底层

**基本写法：并行流使用 ForkJoinPool**
`<集合>.parallelStream().<操作>`
```java
// 并行流默认使用公共 ForkJoinPool
list.parallelStream().mapToInt(Integer::intValue).sum();
```

---

## CompletionService

**基本写法：按完成顺序获取**
`new ExecutorCompletionService<<类型>>(<pool>);`
```java
// 按完成顺序获取结果
CompletionService<Integer> cs = new ExecutorCompletionService<>(pool);
cs.submit(() -> compute());
Future<Integer> f = cs.take();
Integer r = f.get();
```



<!-- ============ 文档分隔线：013-java/040-JavaGenericsAdvanced.md ============ -->

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



<!-- ============ 文档分隔线：013-java/041-MultithreadingBasics.md ============ -->

# Java 多线程基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建线程

**基本写法：继承 Thread**
`class <类> extends Thread { public void run() {} }`
```java
// 继承 Thread 创建线程
class MyThread extends Thread {
    public void run() { System.out.println("running"); }
}
new MyThread().start();
```

---

**基本写法：实现 Runnable**
`new Thread(<Runnable>).start();`
```java
// 实现 Runnable 接口
new Thread(() -> System.out.println("running")).start();
```

---

**基本写法：实现 Callable**
`class <类> implements Callable<<类型>> { public <类型> call() {} }`
```java
// 带返回值的任务
Callable<Integer> task = () -> 42;
Future<Integer> f = Executors.newSingleThreadExecutor().submit(task);
```

---

## 线程基本操作

**基本写法：启动线程**
`<thread>.start();`
```java
// 启动线程执行 run
thread.start();
```

---

**基本写法：等待线程结束**
`<thread>.join();`
```java
// 阻塞当前线程直到目标结束
thread.join();
```

---

**基本写法：超时等待**
`<thread>.join(<毫秒>);`
```java
// 最多等待 1000 毫秒
thread.join(1000);
```

---

**基本写法：休眠**
`Thread.sleep(<毫秒>);`
```java
// 当前线程休眠 500 毫秒
Thread.sleep(500);
```

---

**基本写法：让出 CPU**
`Thread.yield();`
```java
// 提示调度器让出 CPU
Thread.yield();
```

---

## 线程状态

**基本写法：获取状态**
`<thread>.getState();`
```java
// 获取线程状态枚举
Thread.State s = thread.getState();
```

---

**基本写法：判断存活**
`<thread>.isAlive();`
```java
// 判断线程是否存活
boolean alive = thread.isAlive();
```

---

**基本写法：判断中断**
`<thread>.isInterrupted();`
```java
// 判断线程是否被中断
boolean i = thread.isInterrupted();
```

---

## 中断机制

**基本写法：请求中断**
`<thread>.interrupt();`
```java
// 设置线程中断标志
thread.interrupt();
```

---

**基本写法：检测中断并清除标志**
`Thread.interrupted();`
```java
// 静态方法检测并清除当前线程中断
boolean i = Thread.interrupted();
```

---

**基本写法：响应中断**
`if (Thread.currentThread().isInterrupted()) break;`
```java
// 循环中检测中断
while (!Thread.currentThread().isInterrupted()) {
    doWork();
}
```

---

## synchronized 同步

**基本写法：同步方法**
`public synchronized <返回> <方法>() {}`
```java
// 整个方法同步
public synchronized void inc() { count++; }
```

---

**基本写法：同步代码块**
`synchronized (<对象>) { }`
```java
// 同步代码块减少锁范围
synchronized (this) { count++; }
```

---

**基本写法：同步静态方法**
`public static synchronized <返回> <方法>() {}`
```java
// 静态方法锁 Class 对象
public static synchronized void inc() { total++; }
```

---

**基本写法：同步任意锁对象**
`private final Object <锁> = new Object();`
```java
// 使用私有锁对象
private final Object lock = new Object();
synchronized (lock) { count++; }
```

---

## volatile 关键字

**基本写法：声明 volatile 字段**
`private volatile <类型> <字段>;`
```java
// 保证可见性但不保证原子性
private volatile boolean running = true;
```

---

## wait / notify

**基本写法：等待**
`<对象>.wait();`
```java
// 释放锁并等待通知
synchronized (lock) {
    while (!ready) lock.wait();
}
```

---

**基本写法：通知一个**
`<对象>.notify();`
```java
// 唤醒一个等待线程
synchronized (lock) {
    ready = true;
    lock.notify();
}
```

---

**基本写法：通知所有**
`<对象>.notifyAll();`
```java
// 唤醒所有等待线程
synchronized (lock) {
    lock.notifyAll();
}
```

---

**基本写法：超时等待**
`<对象>.wait(<毫秒>);`
```java
// 最多等待 1000 毫秒
lock.wait(1000);
```

---

## 线程优先级

**基本写法：设置优先级**
`<thread>.setPriority(<级别>);`
```java
// 设置线程优先级 1-10
thread.setPriority(Thread.MAX_PRIORITY);
```

---

**基本写法：守护线程**
`<thread>.setDaemon(true);`
```java
// 设置为守护线程（主线程退出即结束）
thread.setDaemon(true);
thread.start();
```

---

## 线程异常处理

**基本写法：设置未捕获异常处理器**
`<thread>.setUncaughtExceptionHandler(<处理器>);`
```java
// 设置线程异常处理器
thread.setUncaughtExceptionHandler((t, e) -> {
    System.out.println(t.getName() + " " + e);
});
```

---

**基本写法：全局默认处理器**
`Thread.setDefaultUncaughtExceptionHandler(<处理器>);`
```java
// 设置全局默认异常处理器
Thread.setDefaultUncaughtExceptionHandler((t, e) -> log.error(e));
```

---

## 线程工厂

**基本写法：自定义线程工厂**
`new ThreadFactory() { public Thread newThread(Runnable r) {} }`
```java
// 自定义线程创建
ThreadFactory factory = r -> {
    Thread t = new Thread(r);
    t.setName("worker-" + t.getId());
    t.setDaemon(true);
    return t;
};
```

---

## 线程局部变量（简化版）

**基本写法：使用 ThreadLocal**
`ThreadLocal.<类型>withInitial(() -> <值>);`
```java
// 线程私有计数器
ThreadLocal<Integer> tl = ThreadLocal.withInitial(() -> 0);
```

---

## Thread 类静态方法

**基本写法：获取当前线程**
`Thread.currentThread();`
```java
// 获取当前执行线程
Thread t = Thread.currentThread();
```

---

**基本写法：获取所有栈帧**
`Thread.getAllStackTraces();`
```java
// 获取所有活动线程的栈帧
Map<Thread, StackTraceElement[]> m = Thread.getAllStackTraces();
```

---

**基本写法：onSpinWait 提示**
`Thread.onSpinWait();`
```java
// Java 9+ 自旋等待提示优化
while (!ready) Thread.onSpinWait();
```



<!-- ============ 文档分隔线：013-java/042-JavaLoggingAPI.md ============ -->

# Java 日志 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## JUL java.util.logging

**基本写法：获取 Logger**
`Logger.getLogger("<名称>");`
```java
// 获取 JDK 内置 Logger
Logger log = Logger.getLogger("com.example.App");
```

---

**基本写法：日志级别**
`<logger>.info("<消息>");`
```java
// 输出 INFO 级别日志
log.info("started");
```

---

**基本写法：带异常**
`<logger>.log(<级别>, "<消息>", <异常>);`
```java
// 输出异常堆栈
log.log(Level.SEVERE, "error", e);
```

---

**基本写法：设置级别**
`<logger>.setLevel(<级别>);`
```java
// 设置日志级别
log.setLevel(Level.FINE);
```

---

**基本写法：配置 ConsoleHandler**
`ConsoleHandler h = new ConsoleHandler(); h.setLevel(<级别>);`
```java
// 配置控制台处理器级别
ConsoleHandler h = new ConsoleHandler();
h.setLevel(Level.ALL);
log.addHandler(h);
```

---

## SLF4J 门面

**基本写法：通过 LoggerFactory 获取**
`LoggerFactory.getLogger(<类>.class);`
```java
// 使用 SLF4J 获取 Logger
Logger log = LoggerFactory.getLogger(App.class);
```

---

**基本写法：占位符日志**
`<logger>.info("<模板>", <参数>...);`
```java
// 占位符方式输出
log.info("user={} age={}", name, age);
```

---

**基本写法：异常日志**
`<logger>.error("<消息>", <异常>);`
```java
// 最后一个参数为异常
log.error("failed", e);
```

---

**基本写法：MDC 上下文**
`MDC.put("<键>", <值>);`
```java
// 设置诊断上下文
MDC.put("traceId", "abc123");
```

---

**基本写法：移除 MDC**
`MDC.remove("<键>");`
```java
// 清理上下文避免泄漏
MDC.remove("traceId");
```

---

## Logback 配置

**基本写法：logback.xml 控制台输出**
`<appender class="ch.qos.logback.core.ConsoleAppender">`
```xml
<!-- 控制台输出配置 -->
<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
  <encoder>
    <pattern>%d{HH:mm:ss} %-5level %logger{20} - %msg%n</pattern>
  </encoder>
</appender>
```

---

**基本写法：滚动文件输出**
`<appender class="ch.qos.logback.core.rolling.RollingFileAppender">`
```xml
<!-- 按日期滚动文件 -->
<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
  <file>app.log</file>
  <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <fileNamePattern>app.%d{yyyy-MM-dd}.log</fileNamePattern>
    <maxHistory>30</maxHistory>
  </rollingPolicy>
  <encoder><pattern>%msg%n</pattern></encoder>
</appender>
```

---

**基本写法：设置 Logger 级别**
`<logger name="<包名>" level="<级别>"/>`
```xml
<!-- 为指定包设置级别 -->
<logger name="com.example" level="DEBUG"/>
<root level="INFO">
  <appender-ref ref="STDOUT"/>
</root>
```

---

## Log4j2 配置

**基本写法：log4j2.xml Configuration**
`<Configuration status="WARN">`
```xml
<!-- Log4j2 根配置 -->
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d %p %c - %m%n"/>
    </Console>
  </Appenders>
</Configuration>
```

---

**基本写法：Loggers 配置**
`<Loggers> <Logger name="<包>" level="<级别>"/> <Root level="<级别>">`
```xml
<!-- 日志器与根配置 -->
<Loggers>
  <Logger name="com.example" level="debug" additivity="false">
    <AppenderRef ref="Console"/>
  </Logger>
  <Root level="info">
    <AppenderRef ref="Console"/>
  </Root>
</Loggers>
```

---

## System.Logger（Java 9+）

**基本写法：获取 SystemLogger**
`System.getLogger("<名称>");`
```java
// JDK 9+ 统一日志门面
System.Logger log = System.getLogger("app");
```

---

**基本写法：记录日志**
`<logger>.log(<级别>, "<消息>");`
```java
// 通过 System.Logger 输出
log.log(System.Logger.Level.INFO, "started");
```

---

**基本写法：带 Supplier 延迟求值**
`<logger>.log(<级别>, <Supplier>);`
```java
// 仅当日志级别开启时求值
log.log(System.Logger.Level.DEBUG, () -> "expensive: " + compute());
```

---

## 异步日志

**基本写法：Log4j2 异步配置**
`<AsyncLogger name="<包>" level="<级别>"/>`
```xml
<!-- 全异步日志提升性能 -->
<Loggers>
  <AsyncLogger name="com.example" level="info"/>
  <AsyncRoot level="info">
    <AppenderRef ref="Console"/>
  </AsyncRoot>
</Loggers>
```

---

## Logback AsyncAppender

**基本写法：包装异步**
`<appender class="ch.qos.logback.classic.AsyncAppender">`
```xml
<!-- 异步 Appender 包装 -->
<appender name="ASYNC" class="ch.qos.logback.classic.AsyncAppender">
  <appender-ref ref="FILE"/>
  <queueSize>1024</queueSize>
  <neverBlock>true</neverBlock>
</appender>
```

---

## 结构化日志（JSON）

**基本写法：Logback JSON 编码器**
`<encoder class="net.logstash.logback.encoder.LogstashEncoder">`
```xml
<!-- 输出 JSON 格式日志 -->
<appender name="JSON" class="ch.qos.logback.core.ConsoleAppender">
  <encoder class="net.logstash.logback.encoder.LogstashEncoder"/>
</appender>
```

---

## 日志参数化最佳实践

**基本写法：避免字符串拼接**
`<logger>.debug("<模板>", <参数>);`
```java
// 使用占位符而非字符串拼接
log.debug("value={}", value);
```

---

**基本写法：惰性求值**
`if (<logger>.isDebugEnabled()) { <logger>.debug(<计算>); }`
```java
// 开销大时先判断级别
if (log.isDebugEnabled()) {
    log.debug("data={}", expensiveSerialize());
}
```



<!-- ============ 文档分隔线：013-java/043-JavaRegex.md ============ -->

# Java 正则表达式 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Pattern 编译

**基本写法：编译正则**
`Pattern.compile("<regex>"[, <flags>]): Pattern`
```java
// 编译正则表达式
Pattern p = Pattern.compile("\\d+");
Pattern pi = Pattern.compile("abc", Pattern.CASE_INSENSITIVE);
Pattern pm = Pattern.compile("a.b", Pattern.DOTALL);
```

---

**基本写法：标志位组合**
`Pattern.compile("<regex>", Pattern.<flag1> | Pattern.<flag2>);`
```java
// 多个标志位用按位或组合
Pattern p = Pattern.compile("hello", Pattern.CASE_INSENSITIVE | Pattern.MULTILINE);
```

---

## Matcher 匹配

**基本写法：创建匹配器**
`<pattern>.matcher(<input>): Matcher`
```java
// 创建 Matcher 对象
Matcher m = p.matcher("123 456");
```

---

**基本写法：完整匹配**
`<matcher>.matches(): boolean`
```java
// 整个字符串是否匹配
boolean ok = p.matcher("123").matches();
```

---

**基本写法：查找下一个**
`<matcher>.find(): boolean`
```java
// 查找下一个匹配
while (m.find()) {
    System.out.println(m.group());
}
```

---

**基本写法：匹配位置**
`<matcher>.start(): int` / `<matcher>.end(): int`
```java
// 获取匹配起止索引
if (m.find()) {
    int start = m.start();
    int end = m.end();
}
```

---

## 分组捕获

**基本写法：捕获组**
`(<pattern>)`
```java
// 圆括号定义捕获组
Pattern p = Pattern.compile("(\\d+)-(\\d+)");
Matcher m = p.matcher("12-34");
if (m.matches()) {
    m.group(0); // "12-34" 整个匹配
    m.group(1); // "12" 第一组
    m.group(2); // "34" 第二组
}
```

---

**基本写法：命名捕获组**
`(?<<name><pattern>)`
```java
// 命名捕获组（Java 7+）
Pattern p = Pattern.compile("(?<year>\\d{4})-(?<month>\\d{2})");
Matcher m = p.matcher("2024-03");
if (m.matches()) {
    m.group("year");   // "2024"
    m.group("month");  // "03"
}
```

---

**基本写法：组总数**
`<matcher>.groupCount(): int`
```java
// 获取捕获组数量（不含 group(0)）
int count = m.groupCount();
```

---

## 替换操作

**基本写法：替换全部**
`<matcher>.replaceAll("<replacement>"): String`
```java
// 替换所有匹配
String r = p.matcher("a1b2").replaceAll("X");
```

---

**基本写法：替换首个**
`<matcher>.replaceFirst("<replacement>"): String`
```java
// 仅替换第一个匹配
String r = p.matcher("a1b2").replaceFirst("X");
```

---

**基本写法：引用捕获组替换**
`<matcher>.replaceAll("$<groupName>");` 或 `$<n>`
```java
// 引用命名组
Pattern p = Pattern.compile("(?<word>\\w+)");
String r = p.matcher("hello").replaceAll("${word}!");
// 引用编号组
String r2 = Pattern.compile("(\\w)(\\w)").matcher("ab").replaceAll("$2$1");
```

---

## 常用预定义字符

**基本写法：字符类**
```java
// .   任意字符（默认不含换行）
// \d  数字 [0-9]
// \D  非数字
// \w  单词字符 [a-zA-Z0-9_]
// \W  非单词字符
// \s  空白字符
// \S  非空白字符
```

---

**基本写法：量词**
```java
// ?     0 或 1 次
// *     0 次或多次
// +     1 次或多次
// {n}   恰好 n 次
// {n,}  至少 n 次
// {n,m} n 到 m 次
```

---

**基本写法：边界匹配**
```java
// ^   行开头
// $   行结尾
// \b  单词边界
// \B  非单词边界
// \A  输入开头
// \z  输入结尾
```

---

## 断言

**基本写法：正向先行断言**
`(?=<pattern>)`
```java
// 匹配后面跟着数字的字母
Pattern p = Pattern.compile("[a-z]+(?=\\d)");
```

---

**基本写法：负向先行断言**
`(?!<pattern>)`
```java
// 匹配后面不跟数字的字母
Pattern p = Pattern.compile("[a-z]+(?!\\d)");
```

---

## String 正则方法

**基本写法：分割**
`<string>.split("<regex>"[, <limit>]): String[]`
```java
// 按正则分割字符串
String[] parts = "a,b,,c".split(",");
String[] parts2 = "a1b2c".split("\\d", 2);
```

---

**基本写法：替换全部**
`<string>.replaceAll("<regex>", "<replacement>): String`
```java
// 字符串直接替换
String r = "2024-03".replaceAll("\\d", "*");
```

---

**基本写法：匹配判断**
`<string>.matches("<regex>"): boolean`
```java
// 整串是否匹配
boolean ok = "123".matches("\\d+");
```

---

## 标志位常量

**基本写法：常用标志**
```java
// Pattern.CASE_INSENSITIVE  忽略大小写
// Pattern.MULTILINE         ^ $ 匹配每行
// Pattern.DOTALL            . 匹配换行
// Pattern.UNICODE_CASE      Unicode 大小写
// Pattern.COMMENTS          忽略空白与注释
// Pattern.LITERAL           字面量模式
```

---



<!-- ============ 文档分隔线：013-java/044-JavaSwitchPatternMatching.md ============ -->

﻿# Java Switch 模式匹配 语法速查手册

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



<!-- ============ 文档分隔线：013-java/045-JavaSealedClass.md ============ -->

﻿# Java 密封类 语法速查手册

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



<!-- ============ 文档分隔线：013-java/046-JavaPathFiles.md ============ -->

# Java Path 与 Files 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Path 创建

**基本写法：从字符串创建**
`Path.of(<路径字符串>);`
```java
// Java 11+，等价于 Paths.get
Path p = Path.of("C:\\data\\file.txt");
```

---

**基本写法：从多段创建**
`Path.of(<根>, <段1>, <段2>);`
```java
// 拼接路径段
Path p = Path.of("C:", "data", "sub", "file.txt");
```

---

**基本写法：Paths.get**
`Paths.get(<路径字符串>);`
```java
// NIO.2 传统方式
Path p = Paths.get("/var/log/app.log");
```

---

**基本写法：从 URI 创建**
`Paths.get(<URI>);`
```java
// 通过 URI 创建
Path p = Paths.get(URI.create("file:///C:/data/file.txt"));
```

---

## Path 操作

**基本写法：拼接路径**
`<Path>.resolve(<子路径>);`
```java
// 拼接子路径
Path dir = Path.of("C:\\data");
Path file = dir.resolve("file.txt");
```

---

**基本写法：相对化**
`<Path>.relativize(<目标>);`
```java
// 求相对路径
Path a = Path.of("C:\\data\\sub");
Path b = Path.of("C:\\data\\other\\f.txt");
Path r = a.relativize(b);
```

---

**基本写法：规范化**
`<Path>.normalize();`
```java
// 消除 . 和 ..
Path p = Path.of("C:\\data\\..\\file.txt").normalize();
```

---

**基本写法：转绝对路径**
`<Path>.toAbsolutePath();`
```java
// 转换为绝对路径
Path p = Path.of("file.txt").toAbsolutePath();
```

---

**基本写法：访问路径组件**
`<Path>.getFileName();`
```java
// 获取文件名、父路径、根
Path p = Path.of("C:\\data\\file.txt");
p.getFileName();   // file.txt
p.getParent();     // C:\data
p.getRoot();       // C:\
```

---

## Files 文件操作

**基本写法：判断存在**
`Files.exists(<Path>);`
```java
// 判断文件是否存在
boolean ok = Files.exists(Path.of("a.txt"));
```

---

**基本写法：创建文件**
`Files.createFile(<Path>);`
```java
// 创建空文件
Files.createFile(Path.of("new.txt"));
```

---

**基本写法：创建目录**
`Files.createDirectory(<Path>);`
```java
// 创建单层目录
Files.createDirectory(Path.of("C:\\newdir"));
```

---

**基本写法：递归创建目录**
`Files.createDirectories(<Path>);`
```java
// 创建多层目录
Files.createDirectories(Path.of("C:\\a\\b\\c"));
```

---

**基本写法：删除文件**
`Files.delete(<Path>);`
```java
// 删除，不存在则抛异常
Files.delete(Path.of("old.txt"));
```

---

**基本写法：删除不存在不报错**
`Files.deleteIfExists(<Path>);`
```java
// 不存在时返回 false
boolean deleted = Files.deleteIfExists(Path.of("old.txt"));
```

---

**基本写法：复制文件**
`Files.copy(<源>, <目标>);`
```java
// 复制文件
Files.copy(Path.of("a.txt"), Path.of("b.txt"));
```

---

**基本写法：覆盖复制**
`Files.copy(<源>, <目标>, StandardCopyOption.REPLACE_EXISTING);`
```java
// 覆盖已存在目标
Files.copy(Path.of("a.txt"), Path.of("b.txt"),
    StandardCopyOption.REPLACE_EXISTING);
```

---

**基本写法：移动/重命名**
`Files.move(<源>, <目标>);`
```java
// 移动或重命名
Files.move(Path.of("a.txt"), Path.of("dir/a.txt"));
```

---

## 文件读写

**基本写法：读全部字节**
`Files.readAllBytes(<Path>);`
```java
// 读取整个文件为字节数组
byte[] data = Files.readAllBytes(Path.of("a.dat"));
```

---

**基本写法：读全部行**
`Files.readAllLines(<Path>);`
```java
// 读取所有行
List<String> lines = Files.readAllLines(Path.of("a.txt"));
```

---

**基本写法：读字符串**
`Files.readString(<Path>);`
```java
// Java 11+，读取为字符串
String text = Files.readString(Path.of("a.txt"));
```

---

**基本写法：写字符串**
`Files.writeString(<Path>, <内容>);`
```java
// Java 11+，写入字符串
Files.writeString(Path.of("a.txt"), "hello");
```

---

**基本写法：写行集合**
`Files.write(<Path>, <Iterable>);`
```java
// 写入多行
Files.write(Path.of("a.txt"), List.of("a", "b", "c"));
```

---

**基本写法：追加写入**
`Files.writeString(<Path>, <内容>, StandardOpenOption.APPEND);`
```java
// 追加到文件末尾
Files.writeString(Path.of("a.txt"), "more",
    StandardOpenOption.APPEND);
```

---

## 流式读写

**基本写法：行流**
`Files.lines(<Path>);`
```java
// 按行流式读取，需 try-with-resources
try (Stream<String> s = Files.lines(Path.of("big.log"))) {
    s.filter(l -> l.contains("ERROR")).forEach(System.out::println);
}
```

---

**基本写法：列出目录**
`Files.list(<Path>);`
```java
// 列出直接子项
try (Stream<Path> s = Files.list(Path.of("C:\\data"))) {
    s.forEach(System.out::println);
}
```

---

**基本写法：遍历目录树**
`Files.walk(<Path>, <深度>);`
```java
// 深度遍历
try (Stream<Path> s = Files.walk(Path.of("C:\\data"), 3)) {
    s.filter(Files::isRegularFile).forEach(System.out::println);
}
```

---

**基本写法：按 glob 查找**
`Files.find(<Path>, <深度>, <匹配器>);`
```java
// 按条件查找
try (Stream<Path> s = Files.find(Path.of("C:\\data"), 5,
        (p, a) -> p.toString().endsWith(".log"))) {
    s.forEach(System.out::println);
}
```

---

## 文件属性

**基本写法：基本属性**
`Files.size(<Path>);`
```java
// 文件大小（字节）
long size = Files.size(Path.of("a.txt"));
```

---

**基本写法：判断类型**
`Files.isDirectory(<Path>);`
```java
// 判断目录/文件/符号链接
boolean dir = Files.isDirectory(Path.of("C:\\data"));
boolean reg = Files.isRegularFile(Path.of("a.txt"));
boolean lnk = Files.isSymbolicLink(Path.of("link"));
```

---

**基本写法：读取属性对象**
`Files.readAttributes(<Path>, <属性类>);`
```java
// 一次性读取基本属性
BasicFileAttributes attrs = Files.readAttributes(
    Path.of("a.txt"), BasicFileAttributes.class);
attrs.size();
attrs.lastModifiedTime();
```

---

**基本写法：创建符号链接**
`Files.createSymbolicLink(<链接>, <目标>);`
```java
// 创建符号链接
Files.createSymbolicLink(Path.of("link.txt"), Path.of("a.txt"));
```

---

## PathMatcher 路径匹配

**基本写法：创建匹配器**
`FileSystems.getDefault().getPathMatcher("<语法>:<模式>");`
```java
// 创建 glob 路径匹配器
PathMatcher m = FileSystems.getDefault().getPathMatcher("glob:**/*.java");
// 也可使用 regex 语法
PathMatcher r = FileSystems.getDefault().getPathMatcher("regex:.*\\.java$");
```

---

**基本写法：匹配路径**
`<matcher>.matches(<Path>);`
```java
// 判断路径是否匹配
boolean ok = m.matches(Path.of("src/Main.java"));
```

---

**基本写法：glob 语法要点**
```java
// **   匹配任意层级目录
// *    匹配任意字符（不含目录分隔符）
// ?    匹配单个字符
// {}   逗号分隔的多个选项
PathMatcher m = FileSystems.getDefault().getPathMatcher("glob:*.{java,txt}");
```

---

## FileVisitor 递归

**基本写法：递归遍历回调**
`Files.walkFileTree(<Path>, <Visitor>);`
```java
// 自定义递归访问
Files.walkFileTree(Path.of("C:\\data"), new SimpleFileVisitor<>() {
    @Override public FileVisitResult visitFile(Path f, BasicFileAttributes a) {
        System.out.println(f);
        return FileVisitResult.CONTINUE;
    }
});
```



<!-- ============ 文档分隔线：013-java/047-JavaLockCondition.md ============ -->

﻿# Java Lock 与 Condition 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ReentrantLock 基础

**基本写法：创建可重入锁**
`ReentrantLock <变量> = new ReentrantLock();`
```java
// 创建非公平可重入锁
ReentrantLock lock = new ReentrantLock();
```

---

**基本写法：公平锁**
`new ReentrantLock(true);`
```java
// true 表示公平锁（按等待顺序获取）
ReentrantLock lock = new ReentrantLock(true);
```

---

**基本写法：try-finally 加锁**
`<lock>.lock(); <lock>.unlock();`
```java
// 标准加解锁模板
lock.lock();
try {
    // 临界区代码
} finally {
    lock.unlock();
}
```

---

## 非阻塞获取

**基本写法：tryLock 立即返回**
`<lock>.tryLock();`
```java
// 获取成功返回 true，失败立即返回 false
if (lock.tryLock()) {
    try {
        // 拿到锁
    } finally {
        lock.unlock();
    }
}
```

---

**基本写法：tryLock 超时**
`<lock>.tryLock(<超时>, <单位>);`
```java
// 最多等待指定时间
if (lock.tryLock(3, TimeUnit.SECONDS)) {
    try {
        // 拿到锁
    } finally {
        lock.unlock();
    }
}
```

---

**基本写法：可中断加锁**
`<lock>.lockInterruptibly();`
```java
// 等待锁时可以被 interrupt 打断
try {
    lock.lockInterruptibly();
    try {
        // 临界区
    } finally {
        lock.unlock();
    }
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
}
```

---

## Condition 等待通知

**基本写法：创建 Condition**
`<lock>.newCondition();`
```java
// 一个锁可绑定多个条件变量
ReentrantLock lock = new ReentrantLock();
Condition notEmpty = lock.newCondition();
Condition notFull  = lock.newCondition();
```

---

**基本写法：等待**
`<condition>.await();`
```java
// 释放锁并等待，唤醒后重新竞争锁
lock.lock();
try {
    while (queue.isEmpty()) {
        notEmpty.await();
    }
    // 取数据
} finally {
    lock.unlock();
}
```

---

**基本写法：唤醒一个**
`<condition>.signal();`
```java
// 唤醒一个等待在该条件上的线程
lock.lock();
try {
    queue.add(item);
    notEmpty.signal();
} finally {
    lock.unlock();
}
```

---

**基本写法：唤醒全部**
`<condition>.signalAll();`
```java
// 唤醒所有等待线程
notFull.signalAll();
```

---

**基本写法：超时等待**
`<condition>.await(<超时>, <单位>);`
```java
// 最多等待指定时间
boolean woken = notEmpty.await(1, TimeUnit.SECONDS);
```

---

**基本写法：不抛中断等待**
`<condition>.awaitUninterruptibly();`
```java
// 等待期间不响应中断
notEmpty.awaitUninterruptibly();
```

---

## ReadWriteLock

**基本写法：创建读写锁**
`ReentrantReadWriteLock <变量> = new ReentrantReadWriteLock();`
```java
// 读读共享，读写/写写互斥
ReentrantReadWriteLock rw = new ReentrantReadWriteLock();
```

---

**基本写法：读锁**
`<rw>.readLock().lock();`
```java
// 多个读线程可同时进入
rw.readLock().lock();
try {
    // 读取共享数据
} finally {
    rw.readLock().unlock();
}
```

---

**基本写法：写锁**
`<rw>.writeLock().lock();`
```java
// 写锁独占
rw.writeLock().lock();
try {
    // 修改共享数据
} finally {
    rw.writeLock().unlock();
}
```

---

## StampedLock

**基本写法：创建戳锁**
`StampedLock <变量> = new StampedLock();`
```java
// 高性能读写锁，附带戳（stamp）
StampedLock sl = new StampedLock();
```

---

**基本写法：乐观读**
`<sl>.tryOptimisticRead();`
```java
// 乐观读：不阻塞写线程
long stamp = sl.tryOptimisticRead();
double x = currentX;
if (!sl.validate(stamp)) {
    stamp = sl.readLock();
    try {
        x = currentX;
    } finally {
        sl.unlockRead(stamp);
    }
}
```

---

**基本写法：悲观读**
`<sl>.readLock();`
```java
// 悲观读锁
long stamp = sl.readLock();
try {
    return currentX;
} finally {
    sl.unlockRead(stamp);
}
```

---

**基本写法：写锁**
`<sl>.writeLock();`
```java
// 写锁
long stamp = sl.writeLock();
try {
    currentX = newX;
} finally {
    sl.unlockWrite(stamp);
}
```

---

## 锁状态查询

**基本写法：查询持有与等待**
`<lock>.getHoldCount();`
```java
// 当前线程持有次数
int hold = lock.getHoldCount();
// 等待队列长度
int queued = lock.getQueueLength();
```

---

**基本写法：判断当前线程是否持有**
`<lock>.isHeldByCurrentThread();`
```java
// 仅在持有时才能 unlock
if (lock.isHeldByCurrentThread()) {
    lock.unlock();
}
```



<!-- ============ 文档分隔线：013-java/048-JavaStreamAdvanced.md ============ -->

﻿# Java Stream 进阶 语法速查手册

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



<!-- ============ 文档分隔线：013-java/049-JavaJshellJpackage.md ============ -->

﻿# Java jshell 与 jpackage 命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## jshell 启动

**基本写法：进入交互**
`jshell`
```bash
# 启动 REPL 交互环境
jshell
```

---

**基本写法：指定版本进入**
`jshell --execution <模式>`
```bash
# 本地执行模式
jshell --execution local
```

---

**基本写法：执行片段**
`jshell -e "<代码>"`
```bash
# 直接执行单段代码
jshell -e "System.out.println(\"hi\");"
```

---

## jshell 会话控制

**基本写法：加载文件**
`/open <文件路径>`
```java
// 在 jshell 内加载脚本文件
/open snippet.java
```

---

**基本写法：保存片段**
`/save <文件路径>`
```java
// 保存当前会话片段到文件
/save session.java
```

---

**基本写法：列出片段**
`/list`
```java
// 列出已输入的代码片段（带编号）
/list
// 仅列出有效片段
/list -all
```

---

**基本写法：查看变量**
`/vars`
```java
// 列出已定义的变量及值
/vars
```

---

**基本写法：查看方法**
`/methods`
```java
// 列出已定义的方法
/methods
```

---

**基本写法：查看类型**
`/types`
```java
// 列出已定义的类与接口
/types
```

---

**基本写法：查看导入**
`/imports`
```java
// 列出已导入的包
/imports
```

---

**基本写法：编辑片段**
`/edit <片段编号>`
```java
// 用外部编辑器编辑片段
/edit 1
```

---

**基本写法：重置会话**
`/reset`
```java
// 清空所有片段，重新开始
/reset
```

---

**基本写法：退出**
`/exit`
```java
// 退出 jshell
/exit
```

---

## jshell 设置

**基本写法：设置反馈模式**
`/set feedback <模式>`
```java
// concise / normal / silent / verbose
/set feedback verbose
```

---

**基本写法：添加导入**
`import <包名>;`
```java
// 直接输入 import 语句即可
import java.util.stream.*;
```

---

**基本写法：执行外部命令**
`/!<shell 命令>`
```java
// 在 jshell 中执行系统命令
/! javac -version
```

---

**基本写法：设置类路径**
`jshell --class-path <路径>`
```bash
# 启动时指定类路径
jshell --class-path "lib/*;bin"
```

---

## jpackage 基础

**基本写法：构建 Windows 安装包**
`jpackage --name <名称> --input <输入> --main-jar <主jar>`
```bash
# 打包成 Windows 安装程序（msi/exe）
jpackage --name MyApp --input target --main-jar app.jar
```

---

**基本写法：指定主类**
`jpackage --name <名称> --module <模块>/<主类>`
```bash
# 模块化应用打包
jpackage --name MyApp --module com.example.app/com.example.app.Main
```

---

**基本写法：指定运行时镜像**
`jpackage --runtime-image <镜像目录>`
```bash
# 使用自定义 JRE
jpackage --name MyApp --input target --main-jar app.jar --runtime-image myjre
```

---

## jpackage 平台选项

**基本写法：Windows 安装器类型**
`jpackage --win-msi`
```bash
# 生成 MSI 安装包
jpackage --name MyApp --input target --main-jar app.jar --win-msi
```

---

**基本写法：Windows 快捷方式**
`jpackage --win-shortcut --win-menu`
```bash
# 创建桌面快捷方式与开始菜单项
jpackage --name MyApp --input target --main-jar app.jar --win-shortcut --win-menu
```

---

**基本写法：macOS dmg**
`jpackage --type dmg --name <名称>`
```bash
# 生成 macOS dmg 镜像
jpackage --type dmg --name MyApp --module com.example.app/com.example.app.Main
```

---

**基本写法：macOS 应用图标**
`jpackage --icon <icns 文件>`
```bash
# 指定应用图标
jpackage --name MyApp --input target --main-jar app.jar --icon icon.icns
```

---

**基本写法：Linux deb/rpm**
`jpackage --type <deb|rpm>`
```bash
# 生成 Linux 安装包
jpackage --type deb --name myapp --input target --main-jar app.jar
```

---

## jpackage 应用配置

**基本写法：设置版本与供应商**
`jpackage --app-version <版本> --vendor <供应商>`
```bash
# 应用版本与供应商
jpackage --name MyApp --input target --main-jar app.jar \
    --app-version 1.0.0 --vendor "Acme Inc"
```

---

**基本写法：传入 JVM 参数**
`jpackage --java-options "<参数>"`
```bash
# 启动时传入 JVM 参数
jpackage --name MyApp --input target --main-jar app.jar \
    --java-options "-Xmx512m -Dfile.encoding=UTF-8"
```

---

**基本写法：应用参数**
`jpackage --arguments "<参数>"`
```bash
# 启动应用时传入的命令行参数
jpackage --name MyApp --input target --main-jar app.jar \
    --arguments "--mode=prod"
```

---

**基本写法：关联文件类型**
`jpackage --file-associations <属性文件>`
```bash
# 关联文件扩展名
jpackage --name MyApp --input target --main-jar app.jar \
    --file-associations app.properties
```

---

**基本写法：添加资源**
`jpackage --resource-dir <目录>`
```bash
# 指定图标与许可文件目录
jpackage --name MyApp --input target --main-jar app.jar \
    --resource-dir res
```

---

**基本写法：临时目录与详细输出**
`jpackage --temp <目录> --verbose`
```bash
# 指定临时目录并输出详细信息
jpackage --name MyApp --input target --main-jar app.jar \
    --temp build/tmp --verbose
```



<!-- ============ 文档分隔线：013-java/050-JavaCountDownLatchCyclicBarrier.md ============ -->

# Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## CountDownLatch 一次性倒数

**基本写法：创建倒数器**
`new CountDownLatch(<计数>);`
```java
// 创建计数为 3 的倒数器
CountDownLatch latch = new CountDownLatch(3);
```

---

**基本写法：计数减一**
`<latch>.countDown();`
```java
// 计数减 1
latch.countDown();
```

---

**基本写法：等待计数归零**
`<latch>.await();`
```java
// 阻塞直到计数归零
latch.await();
```

---

**基本写法：超时等待**
`<latch>.await(<超时>, <单位>);`
```java
// 最多等待 5 秒
boolean ok = latch.await(5, TimeUnit.SECONDS);
```

---

**基本写法：获取剩余计数**
`<latch>.getCount();`
```java
// 查询当前剩余计数
long rest = latch.getCount();
```

---

## CyclicBarrier 可循环屏障

**基本写法：创建屏障**
`new CyclicBarrier(< parties >);`
```java
// 创建 3 个线程同步的屏障
CyclicBarrier barrier = new CyclicBarrier(3);
```

---

**基本写法：带动作的屏障**
`new CyclicBarrier(< parties >, <Runnable>);`
```java
// 所有线程到达后执行的动作
CyclicBarrier b = new CyclicBarrier(3, () -> System.out.println("all arrived"));
```

---

**基本写法：等待**
`<barrier>.await();`
```java
// 等待其他线程到达
barrier.await();
```

---

**基本写法：超时等待**
`<barrier>.await(<超时>, <单位>);`
```java
// 最多等待 10 秒
int idx = barrier.await(10, TimeUnit.SECONDS);
```

---

**基本写法：重置屏障**
`<barrier>.reset();`
```java
// 重置屏障以便复用
barrier.reset();
```

---

## Phaser 阶段同步器

**基本写法：创建 Phaser**
`new Phaser(< parties >);`
```java
// 创建包含 3 个参与者的 Phaser
Phaser phaser = new Phaser(3);
```

---

**基本写法：注册参与者**
`<phaser>.register();`
```java
// 动态注册一个参与者
phaser.register();
```

---

**基本写法：到达并等待**
`<phaser>.arriveAndAwaitAdvance();`
```java
// 到达当前阶段并等待其他人
int phase = phaser.arriveAndAwaitAdvance();
```

---

**基本写法：到达并注销**
`<phaser>.arriveAndDeregister();`
```java
// 到达并从后续阶段注销自己
phaser.arriveAndDeregister();
```

---

**基本写法：获取当前阶段**
`<phaser>.getPhase();`
```java
// 查询当前阶段编号
int phase = phaser.getPhase();
```

---

## Exchanger 交换器

**基本写法：创建交换器**
`new Exchanger<<类型>>();`
```java
// 创建字符串交换器
Exchanger<String> ex = new Exchanger<>();
```

---

**基本写法：交换数据**
`<exchanger>.exchange(<数据>);`
```java
// 与另一线程交换数据并返回对方的数据
String other = ex.exchange("mine");
```

---

**基本写法：超时交换**
`<exchanger>.exchange(<数据>, <超时>, <单位>);`
```java
// 最多等待 5 秒
String other = ex.exchange("mine", 5, TimeUnit.SECONDS);
```

---



<!-- ============ 文档分隔线：013-java/051-JavaSemaphorePhaser.md ============ -->

# Java Semaphore 信号量语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Semaphore 信号量

**基本写法：创建信号量**
`new Semaphore(<许可数>);`
```java
// 创建 3 个许可的信号量
Semaphore sem = new Semaphore(3);
```

---

**基本写法：公平信号量**
`new Semaphore(<许可数>, true);`
```java
// 使用公平模式获取许可
Semaphore sem = new Semaphore(3, true);
```

---

**基本写法：获取许可**
`<sem>.acquire();`
```java
// 阻塞获取一个许可
sem.acquire();
```

---

**基本写法：获取多个许可**
`<sem>.acquire(<数量>);`
```java
// 一次获取多个许可
sem.acquire(2);
```

---

**基本写法：释放许可**
`<sem>.release();`
```java
// 释放一个许可
sem.release();
```

---

**基本写法：尝试获取**
`<sem>.tryAcquire();`
```java
// 尝试获取，不阻塞
boolean got = sem.tryAcquire();
```

---

**基本写法：超时获取**
`<sem>.tryAcquire(<超时>, <单位>);`
```java
// 最多等待 5 秒获取许可
boolean ok = sem.tryAcquire(5, TimeUnit.SECONDS);
```

---

**基本写法：剩余许可**
`<sem>.availablePermits();`
```java
// 查询当前可用许可数
int rest = sem.availablePermits();
```

---

## Semaphore 限流示例

**基本写法：用作限流器**
```java
// 限制同时访问的线程数
class RateLimiter {
    private final Semaphore sem;
    public RateLimiter(int max) { sem = new Semaphore(max); }
    public void run(Runnable task) throws InterruptedException {
        sem.acquire();
        try { task.run(); } finally { sem.release(); }
    }
}
```

---



<!-- ============ 文档分隔线：013-java/052-JavaBlockingQueue.md ============ -->

# Java 阻塞队列 BlockingQueue 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ArrayBlockingQueue 有界数组队列

**基本写法：创建有界队列**
`new ArrayBlockingQueue<<类型>>(<容量>);`
```java
// 创建容量 100 的有界阻塞队列
ArrayBlockingQueue<String> q = new ArrayBlockingQueue<>(100);
```

---

**基本写法：公平队列**
`new ArrayBlockingQueue<<类型>>(<容量>, true);`
```java
// 使用公平锁的队列
ArrayBlockingQueue<String> q = new ArrayBlockingQueue<>(100, true);
```

---

## LinkedBlockingQueue 链式队列

**基本写法：创建链式队列**
`new LinkedBlockingQueue<<类型>>();`
```java
// 创建默认容量 Integer.MAX_VALUE 的链式队列
LinkedBlockingQueue<String> q = new LinkedBlockingQueue<>();
```

---

**基本写法：指定容量**
`new LinkedBlockingQueue<<类型>>(<容量>);`
```java
// 创建容量 1000 的链式队列
LinkedBlockingQueue<String> q = new LinkedBlockingQueue<>(1000);
```

---

## SynchronousQueue 同步队列

**基本写法：创建同步队列**
`new SynchronousQueue<<类型>>();`
```java
// 每个 put 必须等待一个 take
SynchronousQueue<String> q = new SynchronousQueue<>();
```

---

## PriorityBlockingQueue 优先级队列

**基本写法：创建优先级队列**
`new PriorityBlockingQueue<<类型>>();`
```java
// 自然顺序的优先级队列
PriorityBlockingQueue<Integer> q = new PriorityBlockingQueue<>();
```

---

**基本写法：带比较器**
`new PriorityBlockingQueue<<类型>>(<初始容量>, <比较器>);`
```java
// 自定义比较器
PriorityBlockingQueue<String> q = new PriorityBlockingQueue<>(11, Comparator.reverseOrder());
```

---

## DelayQueue 延迟队列

**基本写法：创建延迟队列**
`new DelayQueue<<类型>>();`
```java
// 元素必须实现 Delayed 接口
DelayQueue<DelayedTask> q = new DelayQueue<>();
```

---

## 通用操作

**基本写法：阻塞入队**
`<queue>.put(<元素>);`
```java
// 队列满时阻塞
q.put("item");
```

---

**基本写法：阻塞出队**
`<queue>.take();`
```java
// 队列空时阻塞
String item = q.take();
```

---

**基本写法：offer 超时入队**
`<queue>.offer(<元素>, <超时>, <单位>);`
```java
// 最多等待 5 秒
boolean ok = q.offer("item", 5, TimeUnit.SECONDS);
```

---

**基本写法：poll 超时出队**
`<queue>.poll(<超时>, <单位>);`
```java
// 最多等待 5 秒取元素
String item = q.poll(5, TimeUnit.SECONDS);
```

---

**基本写法：剩余容量**
`<queue>.remainingCapacity();`
```java
// 查询剩余容量
int cap = q.remainingCapacity();
```

---

## 生产者消费者示例

**基本写法：阻塞队列用作通道**
```java
BlockingQueue<String> queue = new LinkedBlockingQueue<>(10);
// 生产者
new Thread(() -> { for (int i = 0; i < 5; i++) queue.put("p" + i); }).start();
// 消费者
new Thread(() -> { for (int i = 0; i < 5; i++) System.out.println(queue.take()); }).start();
```

---



<!-- ============ 文档分隔线：013-java/053-JavaAtomicVariables.md ============ -->

# Java 原子变量 AtomicInteger/AtomicReference/LongAdder 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## AtomicInteger 原子整数

**基本写法：创建原子整数**
`new AtomicInteger(<初始值>);`
```java
// 创建初始值为 0 的原子整数
AtomicInteger ai = new AtomicInteger(0);
```

---

**基本写法：获取值**
`<ai>.get();`
```java
// 原子读取当前值
int v = ai.get();
```

---

**基本写法：设置值**
`<ai>.set(<值>);`
```java
// 原子设置新值
ai.set(10);
```

---

**基本写法：原子自增**
`<ai>.incrementAndGet();`
```java
// 先自增再获取
int v = ai.incrementAndGet();
```

---

**基本写法：原子自减**
`<ai>.decrementAndGet();`
```java
// 先自减再获取
int v = ai.decrementAndGet();
```

---

**基本写法：CAS 比较交换**
`<ai>.compareAndSet(<期望>, <新值>);`
```java
// 当值等于期望时更新
boolean ok = ai.compareAndSet(10, 20);
```

---

**基本写法：原子更新**
`<ai>.updateAndGet(<IntUnaryOperator>);`
```java
// 用函数更新值
int v = ai.updateAndGet(x -> x * 2);
```

---

**基本写法：原子累加**
`<ai>.getAndAccumulate(<增量>, <IntBinaryOperator>);`
```java
// 用函数累积并返回旧值
int old = ai.getAndAccumulate(5, Integer::sum);
```

---

## AtomicReference 原子引用

**基本写法：创建原子引用**
`new AtomicReference<<类型>>(<初始值>);`
```java
// 创建原子引用
AtomicReference<String> ref = new AtomicReference<>("init");
```

---

**基本写法：CAS 更新**
`<ref>.compareAndSet(<期望>, <新值>);`
```java
// 比较并设置
boolean ok = ref.compareAndSet("init", "new");
```

---

**基本写法：函数更新**
`<ref>.updateAndGet(<UnaryOperator>);`
```java
// 用函数更新引用
String v = ref.updateAndGet(s -> s.toUpperCase());
```

---

## AtomicStampedReference 防止 ABA

**基本写法：带版本号 CAS**
`new AtomicStampedReference<<类型>>(<初始值>, <初始版本>);`
```java
// 创建带版本戳的原子引用
AtomicStampedReference<String> ref = new AtomicStampedReference<>("a", 0);
int[] stamp = new int[1];
String cur = ref.get(stamp);
ref.compareAndSet(cur, "b", stamp[0], stamp[0] + 1);
```

---

## LongAdder 高并发累加器

**基本写法：创建累加器**
`new LongAdder();`
```java
// 高并发场景下比 AtomicLong 更高效
LongAdder adder = new LongAdder();
```

---

**基本写法：递增**
`<adder>.increment();`
```java
// 自增 1
adder.increment();
```

---

**基本写法：累加**
`<adder>.add(<值>);`
```java
// 累加指定值
adder.add(10);
```

---

**基本写法：求和**
`<adder>.sum();`
```java
// 返回当前总和
long total = adder.sum();
```

---

**基本写法：重置**
`<adder>.reset();`
```java
// 重置为 0
adder.reset();
```

---

## LongAccumulator 通用累加器

**基本写法：创建累加器**
`new LongAccumulator(<LongBinaryOperator>, <初始值>);`
```java
// 创建求最大值的累加器
LongAccumulator max = new LongAccumulator(Long::max, Long.MIN_VALUE);
```

---

**基本写法：累加**
`<acc>.accumulate(<值>);`
```java
// 用函数累加
max.accumulate(42);
```

---



<!-- ============ 文档分隔线：013-java/054-JavaStreamCollector.md ============ -->

# Java Stream Collector 与分组语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Collectors.toList/toSet

**基本写法：收集为 List**
`<stream>.collect(Collectors.toList());`
```java
// 把流收集到 List
List<String> list = stream.collect(Collectors.toList());
```

---

**基本写法：收集为 Set**
`<stream>.collect(Collectors.toSet());`
```java
// 把流收集到 Set 自动去重
Set<String> set = stream.collect(Collectors.toSet());
```

---

**基本写法：收集为指定集合**
`<stream>.collect(Collectors.toCollection(<工厂>));`
```java
// 收集到 LinkedList
LinkedList<String> ll = stream.collect(Collectors.toCollection(LinkedList::new));
```

---

## Collectors.toMap

**基本写法：转 Map**
`<stream>.collect(Collectors.toMap(<键映射>, <值映射>));`
```java
// 把对象流转换为以 id 为键的 Map
Map<Long, User> map = users.stream()
    .collect(Collectors.toMap(User::getId, u -> u));
```

---

**基本写法：处理键冲突**
`<stream>.collect(Collectors.toMap(<键>, <值>, <合并函数>));`
```java
// 遇到重复键时保留新值
Map<String, Integer> m = list.stream()
    .collect(Collectors.toMap(s -> s, String::length, (a, b) -> b));
```

---

## Collectors.joining 拼接

**基本写法：字符串拼接**
`<stream>.collect(Collectors.joining());`
```java
// 直接拼接所有字符串
String s = stream.collect(Collectors.joining());
```

---

**基本写法：带分隔符**
`<stream>.collect(Collectors.joining(<分隔符>));`
```java
// 用逗号分隔拼接
String s = stream.collect(Collectors.joining(", "));
```

---

**基本写法：带前后缀**
`<stream>.collect(Collectors.joining(<分隔符>, <前缀>, <后缀>));`
```java
// 用方括号包裹
String s = stream.collect(Collectors.joining(", ", "[", "]"));
```

---

## Collectors.groupingBy 分组

**基本写法：按属性分组**
`<stream>.collect(Collectors.groupingBy(<分类函数>));`
```java
// 按首字母分组
Map<Character, List<String>> g = list.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0)));
```

---

**基本写法：多级分组**
`<stream>.collect(Collectors.groupingBy(<分类1>, Collectors.groupingBy(<分类2>)));`
```java
// 先按部门再按职级分组
Map<String, Map<String, List<Emp>>> g = emps.stream()
    .collect(Collectors.groupingBy(Emp::getDept,
             Collectors.groupingBy(Emp::getLevel)));
```

---

**基本写法：分组后统计**
`<stream>.collect(Collectors.groupingBy(<分类>, Collectors.counting()));`
```java
// 统计每个分组元素个数
Map<String, Long> count = list.stream()
    .collect(Collectors.groupingBy(s -> s, Collectors.counting()));
```

---

## Collectors.partitioningBy 分区

**基本写法：按条件分区**
`<stream>.collect(Collectors.partitioningBy(<Predicate>));`
```java
// 把流分为 true/false 两组
Map<Boolean, List<Integer>> p = nums.stream()
    .collect(Collectors.partitioningBy(n -> n > 0));
```

---

**基本写法：分区后归约**
`<stream>.collect(Collectors.partitioningBy(<Predicate>, <下游>));`
```java
// 分区后统计每组数量
Map<Boolean, Long> p = nums.stream()
    .collect(Collectors.partitioningBy(n -> n > 0, Collectors.counting()));
```

---

## Collectors.counting/summing

**基本写法：计数**
`<stream>.collect(Collectors.counting());`
```java
// 统计元素个数
long n = stream.collect(Collectors.counting());
```

---

**基本写法：求和**
`<stream>.collect(Collectors.summingInt(<映射>));`
```java
// 对属性求和
int total = users.stream().collect(Collectors.summingInt(User::getAge));
```

---

**基本写法：求平均值**
`<stream>.collect(Collectors.averagingInt(<映射>));`
```java
// 求属性平均值
double avg = users.stream().collect(Collectors.averagingInt(User::getAge));
```

---

## Collectors.summarizing 统计

**基本写法：完整统计**
`<stream>.collect(Collectors.summarizingInt(<映射>));`
```java
// 一次性获取 count/sum/min/avg/max
IntSummaryStatistics stat = users.stream()
    .collect(Collectors.summarizingInt(User::getAge));
```

---

## Collectors.reducing 归约

**基本写法：自定义归约**
`<stream>.collect(Collectors.reducing(<BinaryOperator>));`
```java
// 求最长字符串
Optional<String> max = list.stream()
    .collect(Collectors.reducing((a, b) -> a.length() >= b.length() ? a : b));
```

---

## Collectors.collectingAndThen

**基本写法：收集后转换**
`<stream>.collect(Collectors.collectingAndThen(<下游>, <finisher>));`
```java
// 收集后转不可变集合
List<String> imm = list.stream()
    .collect(Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList));
```

---

## Collectors.teeing 多路收集

**基本写法：双路收集合并**
`<stream>.collect(Collectors.teeing(<下游1>, <下游2>, <合并>));`
```java
// 同时求和与计数
record Stat(int sum, long count) {}
Stat s = nums.stream().collect(Collectors.teeing(
    Collectors.summingInt(n -> n),
    Collectors.counting(),
    Stat::new));
```

---



<!-- ============ 文档分隔线：013-java/055-JavaStreamReduceParallel.md ============ -->

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



<!-- ============ 文档分隔线：013-java/056-JavaTryWithResources.md ============ -->

# Java try-with-resources 与异常链语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## try-with-resources

**基本写法：自动关闭资源**
```java
try (<资源声明>) { <语句> }
```
```java
// 自动关闭实现了 AutoCloseable 的资源
try (FileInputStream in = new FileInputStream("a.txt")) {
    int b = in.read();
}
```

---

**基本写法：多个资源**
```java
try (<资源1>; <资源2>) { <语句> }
```
```java
// 多个资源用分号分隔，关闭顺序与声明相反
try (FileInputStream in = new FileInputStream("in.txt");
     FileOutputStream out = new FileOutputStream("out.txt")) {
    out.write(in.readAllBytes());
}
```

---

**基本写法：引用外部变量**
```java
<AutoCloseable 变量> = ...;
try (<变量>) { <语句> }
```
```java
// Java 9+ 支持使用 effectively final 的外部资源
BufferedReader r = Files.newBufferedReader(Path.of("a.txt"));
try (r) {
    System.out.println(r.readLine());
}
```

---

## 异常捕获

**基本写法：多异常捕获**
```java
try { <语句> } catch (<类型1> | <类型2> <变量>) { <处理> }
```
```java
// 一个 catch 块处理多种异常
try {
    Files.readAllBytes(Path.of("a.txt"));
} catch (IOException | SecurityException e) {
    log.error(e);
}
```

---

**基本写法：异常重新抛出**
```java
catch (<类型> <变量>) { throw <变量>; }
```
```java
// 处理后再抛出
try { risky(); }
catch (IOException e) { log.error(e); throw e; }
```

---

## 异常链

**基本写法：包装异常**
`throw new <异常>(<消息>, <原因>);`
```java
// 把底层异常包装成业务异常
try {
    Files.readString(Path.of("a.txt"));
} catch (IOException e) {
    throw new BusinessException("读取配置失败", e);
}
```

---

**基本写法：获取根因**
`<throwable>.getCause();`
```java
// 获取异常的根本原因
Throwable root = e.getCause();
```

---

**基本写法：添加受抑制异常**
`<throwable>.addSuppressed(<异常>);`
```java
// 主异常抛出后关闭资源时的异常被抑制
try (Resource r = new Resource()) {
    throw new IOException("main");
} catch (IOException e) {
    for (Throwable s : e.getSuppressed()) {
        System.out.println(s);
    }
}
```

---

## finally 块

**基本写法：finally 执行清理**
```java
try { <语句> } catch (<类型> <变量>) { <处理> } finally { <清理> }
```
```java
// finally 块无论是否抛异常都会执行
try {
    return risky();
} finally {
    cleanup();
}
```

---

## StackWalker 栈遍历

**基本写法：遍历调用栈**
`StackWalker.getInstance().forEach(<消费者>);`
```java
// 打印调用栈
StackWalker.getInstance().forEach(f -> System.out.println(f.getClassName() + "#" + f.getMethodName()));
```

---

**基本写法：获取调用者**
`StackWalker.getInstance().walk(<函数>);`
```java
// 获取直接调用者的栈帧
StackTraceElement caller = StackWalker.getInstance()
    .walk(s -> s.skip(1).findFirst())
    .map(StackWalker.StackFrame::toStackTraceElement)
    .orElse(null);
```

---



<!-- ============ 文档分隔线：013-java/057-JavaCustomException.md ============ -->

# Java 自定义异常语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 自定义受检异常

**基本写法：继承 Exception**
```java
public class <名称> extends Exception {
  public <名称>(String msg) { super(msg); }
  public <名称>(String msg, Throwable cause) { super(msg, cause); }
}
```
```java
// 受检异常必须声明或捕获
public class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String msg) { super(msg); }
    public InsufficientFundsException(String msg, Throwable cause) { super(msg, cause); }
}
```

---

## 自定义非受检异常

**基本写法：继承 RuntimeException**
```java
public class <名称> extends RuntimeException {
  public <名称>(String msg) { super(msg); }
}
```
```java
// 运行时异常无需声明
public class BusinessException extends RuntimeException {
    public BusinessException(String msg) { super(msg); }
    public BusinessException(String msg, Throwable cause) { super(msg, cause); }
}
```

---

## 带字段的自定义异常

**基本写法：携带业务字段**
```java
public class <名称> extends RuntimeException {
  private final <类型> <字段>;
  public <名称>(<类型> <字段>, String msg) { super(msg); this.<字段> = <字段>; }
  public <类型> get<Field>() { return <字段>; }
}
```
```java
// 异常携带错误码与上下文
public class OrderException extends RuntimeException {
    private final int code;
    public OrderException(int code, String msg) {
        super(msg);
        this.code = code;
    }
    public int getCode() { return code; }
}
```

---

## 抛出自定义异常

**基本写法：抛出异常**
`throw new <异常>(<消息>);`
```java
// 抛出自定义异常
if (balance < 0) {
    throw new BusinessException("余额不能为负");
}
```

---

**基本写法：带原因抛出**
`throw new <异常>(<消息>, <原因>);`
```java
// 包装原始异常抛出
try { ... }
catch (IOException e) { throw new BusinessException("IO 失败", e); }
```

---

## 声明受检异常

**基本写法：方法声明 throws**
`public <返回> <方法>() throws <异常1>, <异常2> {}`
```java
// 方法声明可能抛出的受检异常
public void withdraw(double amt) throws InsufficientFundsException {
    if (amt > balance) throw new InsufficientFundsException("余额不足");
}
```

---

## 异常断言

**基本写法：断言**
`assert <条件> : <消息>;`
```java
// 启用 -ea 后生效
assert amount > 0 : "金额必须大于 0";
```

---

## 异常工具方法

**基本写法：Objects.requireNonNull**
`Objects.requireNonNull(<对象>, <消息>);`
```java
// 参数非空校验
public void set(String name) {
    this.name = Objects.requireNonNull(name, "name 不能为空");
}
```

---

**基本写法：检查索引**
`Objects.checkIndex(<索引>, <长度>);`
```java
// 检查索引是否在 [0, length) 范围
int i = Objects.checkIndex(5, 10);
```

---

## 异常匹配

**基本写法：模式匹配捕获**
```java
try { ... }
catch (Throwable t) {
  if (t instanceof IOException io) { handleIO(io); }
  else if (t instanceof SQLException sql) { handleSql(sql); }
}
```
```java
// Java 16+ instanceof 模式匹配
catch (Throwable t) {
    if (t instanceof IOException io) {
        System.out.println("IO: " + io.getMessage());
    }
}
```

---



<!-- ============ 文档分隔线：013-java/059-JavaHttpClientWebSocket.md ============ -->

# Java HttpClient 与 WebSocket 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## HttpClient 创建

**基本写法：创建客户端**
`HttpClient.newHttpClient();`
```java
// 创建默认 HTTP 客户端
HttpClient client = HttpClient.newHttpClient();
```

---

**基本写法：自定义客户端**
```java
HttpClient.newBuilder()
  .version(<版本>)
  .connectTimeout(<超时>)
  .build();
```
```java
// 配置 HTTP/2 与超时
HttpClient client = HttpClient.newBuilder()
    .version(HttpClient.Version.HTTP_2)
    .connectTimeout(Duration.ofSeconds(10))
    .build();
```

---

## HttpRequest 请求

**基本写法：构建 GET 请求**
```java
HttpRequest.newBuilder()
  .uri(URI.create(<URL>))
  .GET()
  .build();
```
```java
// 构建 GET 请求
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .GET()
    .build();
```

---

**基本写法：POST 请求体**
```java
HttpRequest.newBuilder()
  .uri(URI.create(<URL>))
  .POST(HttpRequest.BodyPublishers.ofString(<正文>))
  .build();
```
```java
// 发送 JSON POST 请求
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("{\"name\":\"Tom\"}"))
    .build();
```

---

**基本写法：设置头**
`<builder>.header(<名称>, <值>);`
```java
// 添加请求头
builder.header("Authorization", "Bearer token");
```

---

**基本写法：设置超时**
`<builder>.timeout(<超时>);`
```java
// 请求级超时
builder.timeout(Duration.ofSeconds(5));
```

---

## 发送请求

**基本写法：同步发送**
`<client>.send(<请求>, <响应处理器>);`
```java
// 同步获取响应
HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
int code = resp.statusCode();
String body = resp.body();
```

---

**基本写法：异步发送**
`<client>.sendAsync(<请求>, <处理器>);`
```java
// 异步获取响应
client.sendAsync(req, HttpResponse.BodyHandlers.ofString())
    .thenAccept(r -> System.out.println(r.body()));
```

---

**基本写法：响应处理器**
`HttpResponse.BodyHandlers.<类型>();`
```java
// 各种响应体处理器
HttpResponse.BodyHandlers.ofString();   // 字符串
HttpResponse.BodyHandlers.ofByteArray(); // 字节数组
HttpResponse.BodyHandlers.ofFile(Path.of("out.bin")); // 写入文件
HttpResponse.BodyHandlers.discarding();   // 丢弃
```

---

## WebSocket

**基本写法：创建 WebSocket**
```java
<client>.newWebSocketBuilder()
  .buildAsync(URI.create(<URL>), <监听器>)
  .join();
```
```java
// 连接 WebSocket
WebSocket ws = HttpClient.newHttpClient()
    .newWebSocketBuilder()
    .buildAsync(URI.create("wss://example.com/ws"), new WebSocket.Listener() {
        @Override public CompletionStage<?> onText(WebSocket ws, CharSequence data, boolean last) {
            System.out.println("recv: " + data);
            return null;
        }
    })
    .join();
```

---

**基本写法：发送消息**
`<ws>.sendText(<文本>, <是否最后>);`
```java
// 发送文本帧
ws.sendText("hello", true);
```

---

**基本写法：发送二进制**
`<ws>.sendBinary(<字节>, <是否最后>);`
```java
// 发送二进制帧
ws.sendBinary(ByteBuffer.wrap(new byte[]{1,2,3}), true);
```

---

**基本写法：关闭**
`<ws>.sendClose(<状态码>, <原因>);`
```java
// 发送关闭帧
ws.sendClose(WebSocket.NORMAL_CLOSURE, "bye");
```

---

## 传统 Socket

**基本写法：创建客户端**
`new Socket(<host>, <port>);`
```java
// 连接 TCP 服务端
try (Socket s = new Socket("example.com", 8080)) {
    OutputStream out = s.getOutputStream();
    out.write("hi\n".getBytes());
}
```

---

**基本写法：创建服务端**
`new ServerSocket(<端口>);`
```java
// 监听端口
try (ServerSocket ss = new ServerSocket(8080)) {
    Socket client = ss.accept();
    InputStream in = client.getInputStream();
}
```

---



<!-- ============ 文档分隔线：013-java/060-JavaTimeFormatting.md ============ -->

# Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## DateTimeFormatter 预定义

**基本写法：ISO 格式化**
`DateTimeFormatter.ISO_LOCAL_DATE;`
```java
// 使用预定义 ISO 格式
DateTimeFormatter f = DateTimeFormatter.ISO_LOCAL_DATE;
String s = f.format(LocalDate.now());
```

---

**基本写法：本地化格式**
`DateTimeFormatter.ofLocalizedDate(<FormatStyle>);`
```java
// 本地化日期格式
DateTimeFormatter f = DateTimeFormatter.ofLocalizedDate(FormatStyle.FULL);
String s = f.format(LocalDate.now());
```

---

## 自定义格式

**基本写法：自定义模式**
`DateTimeFormatter.ofPattern(<模式>);`
```java
// 自定义日期时间格式
DateTimeFormatter f = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String s = LocalDateTime.now().format(f);
```

---

**基本写法：带 Locale**
`DateTimeFormatter.ofPattern(<模式>, <Locale>);`
```java
// 指定地区与语言
DateTimeFormatter f = DateTimeFormatter.ofPattern("MMMM dd, yyyy", Locale.US);
String s = LocalDate.now().format(f);
```

---

## 格式化与解析

**基本写法：格式化**
`< temporal >.format(<formatter>);`
```java
// 把日期时间转为字符串
String s = LocalDateTime.now().format(f);
```

---

**基本写法：解析**
`<类型>.parse(<字符串>, <formatter>);`
```java
// 从字符串解析日期
LocalDate d = LocalDate.parse("2025-07-31", DateTimeFormatter.ISO_LOCAL_DATE);
```

---

**基本写法：解析为 LocalDateTime**
`LocalDateTime.parse(<字符串>, <formatter>);`
```java
// 解析为日期时间
LocalDateTime dt = LocalDateTime.parse("2025-07-31 10:15:30",
    DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
```

---

## ZoneId 时区

**基本写法：获取时区**
`ZoneId.of(<时区ID>);`
```java
// 创建时区对象
ZoneId sh = ZoneId.of("Asia/Shanghai");
```

---

**基本写法：系统默认时区**
`ZoneId.systemDefault();`
```java
// 获取系统默认时区
ZoneId z = ZoneId.systemDefault();
```

---

**基本写法：可用时区**
`ZoneId.getAvailableZoneIds();`
```java
// 列出所有可用时区 ID
Set<String> ids = ZoneId.getAvailableZoneIds();
```

---

## ZonedDateTime 带时区时间

**基本写法：创建带时区时间**
`ZonedDateTime.now(<ZoneId>);`
```java
// 获取指定时区的当前时间
ZonedDateTime sh = ZonedDateTime.now(ZoneId.of("Asia/Shanghai"));
```

---

**基本写法：时区转换**
`<zdt>.withZoneSameInstant(<ZoneId>);`
```java
// 把上海时间转换为纽约时间
ZonedDateTime ny = sh.withZoneSameInstant(ZoneId.of("America/New_York"));
```

---

## Instant 时间戳

**基本写法：当前时间戳**
`Instant.now();`
```java
// 获取 UTC 时间戳
Instant now = Instant.now();
```

---

**基本写法：从 epoch 创建**
`Instant.ofEpochSecond(<秒>);`
```java
// 从 Unix 时间戳创建
Instant t = Instant.ofEpochSecond(1700000000);
```

---

**基本写法：转 ZonedDateTime**
`<instant>.atZone(<ZoneId>);`
```java
// 时间戳转指定时区时间
ZonedDateTime sh = Instant.now().atZone(ZoneId.of("Asia/Shanghai"));
```

---

## Duration 与 Period

**基本写法：时间差**
`Duration.between(<起>, <止>);`
```java
// 计算两个时间点之间的时长
Duration d = Duration.between(t1, t2);
long seconds = d.getSeconds();
```

---

**基本写法：日期差**
`Period.between(<起>, <止>);`
```java
// 计算两个日期之间的差
Period p = Period.between(d1, d2);
int years = p.getYears();
```

---

**基本写法：创建 Duration**
`Duration.ofMinutes(<分钟>);`
```java
// 创建时长对象
Duration five = Duration.ofMinutes(5);
```

---

**基本写法：创建 Period**
`Period.ofDays(<天数>);`
```java
// 创建日期段对象
Period week = Period.ofDays(7);
```

---

## TemporalAdjusters 调整器

**基本写法：下周一**
`<date>.with(TemporalAdjusters.next(<DayOfWeek>));`
```java
// 获取下个周一
LocalDate next = LocalDate.now().with(TemporalAdjusters.next(DayOfWeek.MONDAY));
```

---

**基本写法：当月最后一天**
`<date>.with(TemporalAdjusters.lastDayOfMonth());`
```java
// 获取当月最后一天
LocalDate last = LocalDate.now().with(TemporalAdjusters.lastDayOfMonth());
```

---



<!-- ============ 文档分隔线：013-java/061-JavaGenericWildcards.md ============ -->

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



<!-- ============ 文档分隔线：013-java/062-JavaTypeErasure.md ============ -->

# Java 类型擦除与桥接方法语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类型擦除规则

**基本写法：擦除为上界**
```java
// 源码：List<T>  字节码：List<Object>
// 源码：List<T extends Number>  字节码：List<Number>
```
```java
// 编译后泛型类型参数被擦除
public class Box<T> {
    private T value;
    // 字节码中 value 类型为 Object
}
```

---

**基本写法：擦除影响**
```java
// 运行时无法获取泛型类型参数
if (list instanceof List<String>) { } // 编译错误
```
```java
// 不能 new 泛型类型
T t = new T(); // 编译错误
```

---

## 反射获取泛型

**基本写法：获取字段泛型**
`<field>.getGenericType();`
```java
// 通过反射获取字段的参数化类型
Field f = Box.class.getDeclaredField("value");
Type t = f.getGenericType();
if (t instanceof ParameterizedType pt) {
    Type[] args = pt.getActualTypeArguments();
}
```

---

**基本写法：获取方法返回泛型**
`<method>.getGenericReturnType();`
```java
// 获取方法的泛型返回类型
Method m = clazz.getMethod("getList");
Type rt = m.getGenericReturnType();
```

---

**基本写法：TypeToken 模式**
```java
// 通过子类保留泛型信息
Type type = new TypeToken<List<String>>() {}.getType();
```
```java
// Gson 等库常用此模式
Type type = new TypeToken<Map<String, List<Integer>>>() {}.getType();
```

---

## 桥接方法

**基本写法：桥接方法生成**
```java
// 子类覆盖泛型方法时编译器生成桥接方法
class StringBox extends Box<String> {
    @Override public void set(String v) { super.set(v); }
    // 编译器生成：public void set(Object v) { set((String) v); }
}
```
```java
// 桥接方法保证多态正确
Box<String> b = new StringBox();
b.set("hi"); // 实际调用桥接方法
```

---

**基本写法：识别桥接方法**
`<method>.isBridge();`
```java
// 反射判断是否桥接方法
for (Method m : StringBox.class.getMethods()) {
    if (m.isBridge()) System.out.println(m);
}
```

---

## 泛型数组

**基本写法：泛型数组限制**
```java
// 不能直接创建泛型数组
List<String>[] arr = new List<String>[10]; // 编译错误
```
```java
// 通过原始类型或 Array.newInstance 创建
List<?>[] arr = new List<?>[10];
```

---

**基本写法：Array.newInstance**
`Array.newInstance(<类型>, <长度>);`
```java
// 反射创建泛型数组
T[] arr = (T[]) Array.newInstance(componentType, 10);
```

---

## 可重写类型参数

**基本写法：保留泛型信息的类**
```java
// 通过 Class 对象保留类型
public class TypedBox<T> {
    private final Class<T> type;
    public TypedBox(Class<T> type) { this.type = type; }
    public T cast(Object o) { return type.cast(o); }
}
```
```java
// 运行时仍可使用类型
TypedBox<String> b = new TypedBox<>(String.class);
String s = b.cast("hello");
```

---



<!-- ============ 文档分隔线：013-java/063-JavaAnnotationMeta.md ============ -->

# Java 元注解 @Retention/@Target/@Inherited 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## @Retention 保留策略

**基本写法：源码级保留**
`@Retention(RetentionPolicy.SOURCE)`
```java
// 仅存在于源码，编译后丢弃（如 @Override）
@Retention(RetentionPolicy.SOURCE)
public @interface Temporary { }
```

---

**基本写法：类文件级保留**
`@Retention(RetentionPolicy.CLASS)`
```java
// 存在于 class 文件但运行时不可见（默认）
@Retention(RetentionPolicy.CLASS)
public @interface Internal { }
```

---

**基本写法：运行时保留**
`@Retention(RetentionPolicy.RUNTIME)`
```java
// 运行时可通过反射读取
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnno { String value(); }
```

---

## @Target 目标限制

**基本写法：限定目标**
`@Target(ElementType.<TYPE>)`
```java
// 仅允许标注类型
@Target(ElementType.TYPE)
public @interface Service { }
```

---

**基本写法：多目标**
`@Target({<TYPE1>, <TYPE2>})`
```java
// 允许标注方法与字段
@Target({ElementType.METHOD, ElementType.FIELD})
public @interface Inject { }
```

---

**基本写法：完整 ElementType 列表**
```java
// Java 8+ 可标注类型参数、记录组件等
ElementType.TYPE_USE         // 类型使用
ElementType.TYPE_PARAMETER   // 类型参数
ElementType.RECORD_COMPONENT // 记录组件
ElementType.MODULE           // 模块
```
```java
// 标注泛型类型参数
public class Box<@MyAnno T> { }
```

---

## @Inherited 继承

**基本写法：子类继承注解**
`@Inherited`
```java
// 子类自动继承该注解
@Inherited
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface InheritableAnno { }
```

---

## @Repeatable 重复

**基本写法：可重复注解**
```java
@Repeatable(<容器注解>.class)
public @interface <注解> { String value(); }
```
```java
// 定义可重复注解
@Retention(RetentionPolicy.RUNTIME)
@Repeatable(Schedules.class)
public @interface Schedule {
    String day();
    int hour();
}

@Retention(RetentionPolicy.RUNTIME)
public @interface Schedules {
    Schedule[] value();
}
```

---

**基本写法：使用重复注解**
```java
@<注解>(<属性>)
@<注解>(<属性>)
public void task() { }
```
```java
// 同一元素多次标注
@Schedule(day = "MON", hour = 9)
@Schedule(day = "WED", hour = 14)
public void backup() { }
```

---

## @Documented 文档化

**基本写法：包含到 Javadoc**
`@Documented`
```java
// 注解会出现在 Javadoc 中
@Documented
@Retention(RetentionPolicy.RUNTIME)
public @interface ApiNote { String value(); }
```

---

## 注解属性

**基本写法：定义属性**
```java
public @interface <名称> {
  <类型> <属性>() [default <默认值>];
}
```
```java
// 注解属性语法
public @interface MyAnno {
    String value();
    int count() default 1;
    String[] tags() default {};
}
```

---

**基本写法：使用 value 简写**
`@<注解>(<值>)`
```java
// 单值注解可省略属性名
@MyAnno("hello")
public class A {}
```

---

**基本写法：多属性**
`@<注解>(<属性1> = <值1>, <属性2> = <值2>)`
```java
// 多属性显式指定
@MyAnno(value = "hi", count = 5, tags = {"a", "b"})
public class B {}
```

---

## 反射读取注解

**基本写法：判断注解存在**
`<annotated>.isAnnotationPresent(<注解类>);`
```java
// 检查类是否标注
boolean has = MyClass.class.isAnnotationPresent(MyAnno.class);
```

---

**基本写法：获取注解**
`<annotated>.getAnnotation(<注解类>);`
```java
// 读取注解并访问属性
MyAnno a = MyClass.class.getAnnotation(MyAnno.class);
if (a != null) System.out.println(a.value());
```

---

**基本写法：获取所有注解**
`<annotated>.getAnnotations();`
```java
// 获取所有运行时注解
Annotation[] arr = MyClass.class.getAnnotations();
```

---



<!-- ============ 文档分隔线：013-java/064-JavaEnumAdvanced.md ============ -->

# Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 枚举定义

**基本写法：简单枚举**
```java
public enum <名称> { <常量1>, <常量2> }
```
```java
// 定义枚举类型
public enum Color { RED, GREEN, BLUE }
```

---

**基本写法：带字段枚举**
```java
public enum <名称> {
  <常量>(<参数>);
  private final <类型> <字段>;
  <名称>(<类型> <参数>) { this.<字段> = <参数>; }
}
```
```java
// 枚举带属性与方法
public enum Planet {
    EARTH(6371), MARS(3390);
    private final int radius;
    Planet(int r) { this.radius = r; }
    public int getRadius() { return radius; }
}
```

---

**基本写法：带抽象方法**
```java
public enum <名称> {
  <常量> { @Override public <返回> <方法>() { } };
  public abstract <返回> <方法>();
}
```
```java
// 每个常量实现自己的行为
public enum Op {
    PLUS { public int apply(int a, int b) { return a + b; } },
    MINUS { public int apply(int a, int b) { return a - b; } };
    public abstract int apply(int a, int b);
}
```

---

## 枚举方法

**基本写法：获取所有常量**
`<枚举>.values();`
```java
// 返回所有枚举常量数组
Color[] all = Color.values();
```

---

**基本写法：按名获取**
`<枚举>.valueOf(<名称>);`
```java
// 按字符串名获取常量
Color c = Color.valueOf("RED");
```

---

**基本写法：序号**
`<常量>.ordinal();`
```java
// 返回常量声明序号（从 0 开始）
int idx = Color.RED.ordinal();
```

---

**基本写法：比较**
`<常量>.compareTo(<其他>);`
```java
// 按 ordinal 比较
int r = Color.RED.compareTo(Color.BLUE);
```

---

**基本写法：名称**
`<常量>.name();`
```java
// 返回常量名字符串
String n = Color.RED.name();
```

---

## EnumSet 枚举集合

**基本写法：所有常量集合**
`EnumSet.allOf(<枚举类>.class);`
```java
// 创建包含全部常量的集合
EnumSet<Color> all = EnumSet.allOf(Color.class);
```

---

**基本写法：指定常量集合**
`EnumSet.of(<常量>...);`
```java
// 创建包含部分常量的集合
EnumSet<Color> warm = EnumSet.of(Color.RED);
```

---

**基本写法：补集**
`EnumSet.complementOf(<EnumSet>);`
```java
// 返回传入集合的补集
EnumSet<Color> rest = EnumSet.complementOf(warm);
```

---

**基本写法：范围**
`EnumSet.range(<起>, <止>);`
```java
// 创建常量区间集合
EnumSet<Color> r = EnumSet.range(Color.RED, Color.BLUE);
```

---

## EnumMap 枚举映射

**基本写法：创建 EnumMap**
`new EnumMap<<枚举>, <值>>(<枚举类>.class);`
```java
// 键为枚举的高效 Map
EnumMap<Color, String> names = new EnumMap<>(Color.class);
names.put(Color.RED, "红色");
```

---

## 枚举实现接口

**基本写法：枚举实现接口**
```java
public interface <接口> { <方法签名>; }
public enum <名称> implements <接口> { ... }
```
```java
// 枚举实现接口统一行为
public interface Operation { int apply(int a, int b); }
public enum BasicOp implements Operation {
    PLUS { public int apply(int a, int b) { return a + b; } }
}
```

---

## 枚举单例

**基本写法：枚举单例模式**
```java
public enum <名称> {
  INSTANCE;
  public void <方法>() { }
}
```
```java
// 线程安全的单例实现
public enum AppConfig {
    INSTANCE;
    private final Map<String, String> cfg = new HashMap<>();
    public String get(String k) { return cfg.get(k); }
}
// 使用：AppConfig.INSTANCE.get("key")
```

---



<!-- ============ 文档分隔线：013-java/065-JavaIteratorIterable.md ============ -->

# Java Iterator/Iterable/Spliterator 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Iterator 接口

**基本写法：获取迭代器**
`<collection>.iterator();`
```java
// 从集合获取迭代器
Iterator<String> it = list.iterator();
```

---

**基本写法：遍历**
```java
while (<it>.hasNext()) { <类型> <变量> = <it>.next(); }
```
```java
// 经典迭代器遍历
while (it.hasNext()) {
    String s = it.next();
    System.out.println(s);
}
```

---

**基本写法：移除元素**
`<it>.remove();`
```java
// 移除最近 next() 返回的元素
it.remove();
```

---

**基本写法：forEachRemaining**
`<it>.forEachRemaining(<消费者>);`
```java
// 用 lambda 处理剩余元素
it.forEachRemaining(System.out::println);
```

---

## Iterable 接口

**基本写法：实现 Iterable**
```java
public class <类> implements Iterable<<类型>> {
  public Iterator<<类型>> iterator() { ... }
}
```
```java
// 自定义可迭代集合
public class MyList implements Iterable<String> {
    public Iterator<String> iterator() { return list.iterator(); }
}
```

---

**基本写法：增强 for 循环**
```java
for (<类型> <变量> : <iterable>) { }
```
```java
// 任何 Iterable 都可用增强 for
for (String s : myList) {
    System.out.println(s);
}
```

---

**基本写法：默认 forEach**
`<iterable>.forEach(<消费者>);`
```java
// Iterable 接口的默认方法
list.forEach(System.out::println);
```

---

**基本写法：spliterator**
`<iterable>.spliterator();`
```java
// 获取可分割迭代器
Spliterator<String> sp = list.spliterator();
```

---

## Spliterator 可分割迭代器

**基本写法：tryAdvance 单个处理**
`<sp>.tryAdvance(<消费者>);`
```java
// 处理一个元素返回是否还有
boolean has = sp.tryAdvance(System.out::println);
```

---

**基本写法：forEachRemaining**
`<sp>.forEachRemaining(<消费者>);`
```java
// 处理所有剩余元素
sp.forEachRemaining(System.out::println);
```

---

**基本写法：尝试分割**
`<sp>.trySplit();`
```java
// 把迭代器一分为二用于并行
Spliterator<String> other = sp.trySplit();
```

---

**基本写法：估算大小**
`<sp>.estimateSize();`
```java
// 估算剩余元素数量
long n = sp.estimateSize();
```

---

**基本写法：特征**
`<sp>.characteristics();`
```java
// 返回特征位
int chars = sp.characteristics();
boolean sorted = sp.hasCharacteristics(Spliterator.SORTED);
```

---

## StreamSupport 转 Stream

**基本写法：Spliterator 转 Stream**
`StreamSupport.stream(<spliterator>, <并行>);`
```java
// 把 Spliterator 转为 Stream
Stream<String> s = StreamSupport.stream(sp, false);
```

---

**基本写法：从迭代器创建流**
`StreamSupport.stream(Spliterators.spliteratorUnknownSize(<it>, 0), false);`
```java
// Iterator 转 Stream
Stream<String> s = StreamSupport.stream(
    Spliterators.spliteratorUnknownSize(it, 0), false);
```

---

## 自定义 Iterator

**基本写法：实现 Iterator**
```java
public class <类> implements Iterator<<类型>> {
  public boolean hasNext() { ... }
  public <类型> next() { ... }
}
```
```java
// 自定义迭代器
public class RangeIt implements Iterator<Integer> {
    private int cur, end;
    public RangeIt(int s, int e) { cur = s; end = e; }
    public boolean hasNext() { return cur < end; }
    public Integer next() { return cur++; }
}
```

---

## ListIterator 双向迭代

**基本写法：获取 ListIterator**
`<list>.listIterator();`
```java
// 获取双向迭代器
ListIterator<String> li = list.listIterator();
```

---

**基本写法：向前遍历**
`<li>.hasPrevious(); <li>.previous();`
```java
// 反向遍历
while (li.hasPrevious()) {
    String s = li.previous();
}
```

---

**基本写法：set 修改**
`<li>.set(<值>);`
```java
// 修改最近 next/previous 返回的元素
li.set("new");
```

---

**基本写法：add 插入**
`<li>.add(<值>);`
```java
// 在当前位置插入元素
li.add("inserted");
```

---

**基本写法：nextIndex/previousIndex**
`<li>.nextIndex();`
```java
// 返回下一个元素索引
int i = li.nextIndex();
```

---



<!-- ============ 文档分隔线：013-java/066-JavaComparatorComparable.md ============ -->

# Java Comparator/Comparable 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Comparable 自然排序

**基本写法：实现 Comparable**
```java
public class <类> implements Comparable<<类>> {
  public int compareTo(<类> other) { ... }
}
```
```java
// 定义自然排序
public class Person implements Comparable<Person> {
    private int age;
    public int compareTo(Person other) {
        return Integer.compare(this.age, other.age);
    }
}
```

---

## Comparator 比较器

**基本写法：创建比较器**
`Comparator.<comparing方法>(<keyExtractor>);`
```java
// 按属性创建比较器
Comparator<Person> byAge = Comparator.comparingInt(Person::getAge);
```

---

**基本写法：链式比较**
`<comparator>.thenComparing(<keyExtractor>);`
```java
// 主排序字段相等时用次排序字段
Comparator<Person> c = Comparator
    .comparing(Person::getDept)
    .thenComparingInt(Person::getAge);
```

---

**基本写法：反向**
`<comparator>.reversed();`
```java
// 反转排序
Comparator<Person> desc = byAge.reversed();
```

---

**基本写法：nulls 优先**
`Comparator.nullsFirst(<比较器>);`
```java
// null 排在最前
Comparator<String> c = Comparator.nullsFirst(Comparator.naturalOrder());
```

---

**基本写法：nulls 最后**
`Comparator.nullsLast(<比较器>);`
```java
// null 排在最后
Comparator<String> c = Comparator.nullsLast(Comparator.naturalOrder());
```

---

**基本写法：自然顺序**
`Comparator.naturalOrder();`
```java
// 使用元素自然顺序
Comparator<String> c = Comparator.naturalOrder();
```

---

**基本写法：反向自然顺序**
`Comparator.reverseOrder();`
```java
// 反向自然顺序
Comparator<String> c = Comparator.reverseOrder();
```

---

## 排序使用

**基本写法：集合排序**
`<list>.sort(<比较器>);`
```java
// 用比较器排序
list.sort(Comparator.comparing(Person::getName));
```

---

**基本写法：Stream 排序**
`<stream>.sorted(<比较器>);`
```java
// 流排序
list.stream().sorted(Comparator.comparingInt(Person::getAge).reversed());
```

---

**基本写法：求最大最小**
`<stream>.max(<比较器>);`
```java
// 用比较器求最大值
Optional<Person> oldest = list.stream().max(Comparator.comparingInt(Person::getAge));
```

---

## 基本类型比较

**基本写法：Integer 比较**
`Integer.compare(<a>, <b>);`
```java
// 比较两个 int 返回 -1/0/1
int r = Integer.compare(1, 2);
```

---

**基本写法：比较静态方法**
`<包装类>.compare(<a>, <b>);`
```java
// Long/Double 等都有 compare
int r = Double.compare(1.0, 2.0);
```

---

**基本写法：Objects.compare**
`Objects.compare(<a>, <b>, <比较器>);`
```java
// 工具方法
int r = Objects.compare("a", "b", Comparator.naturalOrder());
```

---

## 自定义比较器

**基本写法：lambda 比较**
`Comparator<<类型>> <变量> = (a, b) -> <表达式>;`
```java
// 用 lambda 自定义比较逻辑
Comparator<String> byLen = (a, b) -> Integer.compare(a.length(), b.length());
```

---

**基本写法：comparingDouble**
`Comparator.comparingDouble(<keyExtractor>);`
```java
// 按 double 属性比较
Comparator<Product> byPrice = Comparator.comparingDouble(Product::getPrice);
```

---

**基本写法：comparingLong**
`Comparator.comparingLong(<keyExtractor>);`
```java
// 按 long 属性比较
Comparator<Event> byTime = Comparator.comparingLong(Event::getTimestamp);
```

---



<!-- ============ 文档分隔线：013-java/067-JavaStringFormat.md ============ -->

# Java String.format/printf/MessageFormat 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## String.format

**基本写法：格式化字符串**
`String.format(<格式>, <参数>...);`
```java
// 格式化字符串
String s = String.format("name=%s, age=%d", "Tom", 18);
```

---

**基本写法：带 Locale**
`String.format(<Locale>, <格式>, <参数>...);`
```java
// 指定地区
String s = String.format(Locale.US, "%,.2f", 1234567.89);
```

---

## 常用格式说明符

**基本写法：字符串**
`%s`
```java
// 字符串占位符
String s = String.format("hello %s", "world");
```

---

**基本写法：整数**
`%d`
```java
// 十进制整数
String s = String.format("count=%d", 42);
```

---

**基本写法：浮点**
`%.2f`
```java
// 保留两位小数
String s = String.format("%.2f", 3.14159);
```

---

**基本写法：十六进制**
`%x`
```java
// 十六进制小写
String s = String.format("%x", 255); // ff
```

---

**基本写法：八进制**
`%o`
```java
// 八进制
String s = String.format("%o", 8); // 10
```

---

**基本写法：字符**
`%c`
```java
// 字符
String s = String.format("%c", 65); // A
```

---

**基本写法：布尔**
`%b`
```java
// 布尔
String s = String.format("%b", true);
```

---

## 宽度与对齐

**基本写法：指定宽度**
`%<宽度>d`
```java
// 最小宽度 5
String s = String.format("%5d", 42); // "   42"
```

---

**基本写法：左对齐**
`%-<宽度>d`
```java
// 左对齐宽度 5
String s = String.format("%-5d|", 42); // "42   |"
```

---

**基本写法：零填充**
`%0<宽度>d`
```java
// 用 0 填充
String s = String.format("%05d", 42); // "00042"
```

---

**基本写法：千分位**
`%,d`
```java
// 千分位分隔符
String s = String.format("%,d", 1234567); // 1,234,567
```

---

**基本写法：正负号**
`%+d`
```java
// 显示正负号
String s = String.format("%+d", 42); // +42
```

---

## 参数索引

**基本写法：指定参数位置**
`%<索引>$<格式>`
```java
// 使用第 1 个参数
String s = String.format("%1$s = %1$s", "hello");
```

---

**基本写法：重复使用参数**
`%<索引>$<格式>`
```java
// 复用同一参数
String s = String.format("%1$s has %2$d items, %1$s is ok", "Tom", 5);
```

---

## System.out.printf

**基本写法：直接输出**
`System.out.printf(<格式>, <参数>...);`
```java
// 格式化打印到标准输出
System.out.printf("name=%s, age=%d%n", "Tom", 18);
```

---

## 换行符

**基本写法：平台无关换行**
`%n`
```java
// 平台无关的换行符
String s = String.format("line1%nline2");
```

---

**基本写法：System.lineSeparator**
`System.lineSeparator();`
```java
// 获取系统换行符
String nl = System.lineSeparator();
```

---

## MessageFormat

**基本写法：消息格式化**
`MessageFormat.format(<模板>, <参数>...);`
```java
// 使用 MessageFormat
String s = MessageFormat.format("At {0,time} on {0,date}, {1} sent", new Date(), "Tom");
```

---

**基本写法：占位符索引**
`{<索引>}`
```java
// 占位符格式 {索引,类型,样式}
String s = MessageFormat.format("{0} + {1} = {2}", 1, 2, 3);
```

---

**基本写法：数字格式**
`{<索引>,number,<样式>}`
```java
// 数字格式化
String s = MessageFormat.format("{0,number,#.##}", 3.14159);
```

---

**基本写法：选择格式**
`{<索引>,choice,<选项>}`
```java
// 选择性文本
String s = MessageFormat.format("{0,choice,0#no items|1#one item|1<many items}", 5);
```

---

## Formatter 类

**基本写法：使用 Formatter**
`new Formatter().format(<格式>, <参数>).toString();`
```java
// Formatter 流式格式化
String s = new Formatter().format("x=%d, y=%d", 1, 2).toString();
```

---

**基本写法：输出到 StringBuilder**
`new Formatter(<StringBuilder>).format(<格式>, <参数>);`
```java
// 把格式化结果追加到 StringBuilder
StringBuilder sb = new StringBuilder();
new Formatter(sb).format("value=%d%n", 42);
```

---



<!-- ============ 文档分隔线：013-java/068-JavaArraysUtility.md ============ -->

# Java Arrays 工具类语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数组排序

**基本写法：排序**
`Arrays.sort(<数组>);`
```java
// 对数组进行自然排序
int[] a = {3, 1, 2};
Arrays.sort(a);
```

---

**基本写法：范围排序**
`Arrays.sort(<数组>, <起>, <止>);`
```java
// 只排序 [1, 3) 范围
Arrays.sort(a, 1, 3);
```

---

**基本写法：并行排序**
`Arrays.parallelSort(<数组>);`
```java
// 并行排序大数组
Arrays.parallelSort(a);
```

---

**基本写法：自定义比较器排序**
`Arrays.sort(<数组>, <比较器>);`
```java
// 对象数组自定义排序
String[] s = {"b", "a"};
Arrays.sort(s, Comparator.reverseOrder());
```

---

## 数组搜索

**基本写法：二分查找**
`Arrays.binarySearch(<数组>, <key>);`
```java
// 在已排序数组中查找
int idx = Arrays.binarySearch(a, 2);
```

---

**基本写法：范围查找**
`Arrays.binarySearch(<数组>, <起>, <止>, <key>);`
```java
// 在 [1, 3) 范围查找
int idx = Arrays.binarySearch(a, 1, 3, 2);
```

---

## 数组拷贝

**基本写法：拷贝**
`Arrays.copyOf(<数组>, <新长度>);`
```java
// 拷贝并指定新长度
int[] b = Arrays.copyOf(a, 5);
```

---

**基本写法：范围拷贝**
`Arrays.copyOfRange(<数组>, <起>, <止>);`
```java
// 拷贝 [1, 3) 范围
int[] c = Arrays.copyOfRange(a, 1, 3);
```

---

## 数组填充

**基本写法：填充**
`Arrays.fill(<数组>, <值>);`
```java
// 用值填充整个数组
Arrays.fill(a, 0);
```

---

**基本写法：范围填充**
`Arrays.fill(<数组>, <起>, <止>, <值>);`
```java
// 填充 [1, 3) 范围
Arrays.fill(a, 1, 3, 99);
```

---

## 数组比较与哈希

**基本写法：数组相等**
`Arrays.equals(<数组1>, <数组2>);`
```java
// 比较两个数组内容
boolean ok = Arrays.equals(a, b);
```

---

**基本写法：深度比较**
`Arrays.deepEquals(<数组1>, <数组2>);`
```java
// 多维数组深度比较
boolean ok = Arrays.deepEquals(m1, m2);
```

---

**基本写法：哈希码**
`Arrays.hashCode(<数组>);`
```java
// 计算数组哈希码
int h = Arrays.hashCode(a);
```

---

**基本写法：深度哈希**
`Arrays.deepHashCode(<数组>);`
```java
// 多维数组哈希码
int h = Arrays.deepHashCode(m);
```

---

## 数组转字符串

**基本写法：转字符串**
`Arrays.toString(<数组>);`
```java
// 一维数组转字符串
String s = Arrays.toString(a); // [1, 2, 3]
```

---

**基本写法：深度转字符串**
`Arrays.deepToString(<数组>);`
```java
// 多维数组转字符串
String s = Arrays.deepToString(matrix);
```

---

## 数组转流

**基本写法：转 Stream**
`Arrays.stream(<数组>);`
```java
// 数组转 Stream
IntStream s = Arrays.stream(new int[]{1, 2, 3});
```

---

**基本写法：范围流**
`Arrays.stream(<数组>, <起>, <止>);`
```java
// 取数组部分转 Stream
IntStream s = Arrays.stream(a, 1, 3);
```

---

## 数组转列表

**基本写法：转固定大小列表**
`Arrays.asList(<元素>...);`
```java
// 数组转 List（固定大小，不可增删）
List<String> list = Arrays.asList("a", "b");
```

---

**基本写法：转可变列表**
`new ArrayList<>(Arrays.asList(<元素>...));`
```java
// 包装为可变 List
List<String> list = new ArrayList<>(Arrays.asList("a", "b"));
```

---

## 数组创建

**基本写法：setAll 创建**
`Arrays.setAll(<数组>, <生成器>);`
```java
// 用函数初始化数组
int[] a = new int[5];
Arrays.setAll(a, i -> i * 2);
```

---

**基本写法：parallelSetAll**
`Arrays.parallelSetAll(<数组>, <生成器>);`
```java
// 并行初始化数组
Arrays.parallelSetAll(a, i -> i * i);
```

---

**基本写法：parallelPrefix**
`Arrays.parallelPrefix(<数组>, <BinaryOperator>);`
```java
// 并行前缀计算（累加）
Arrays.parallelPrefix(a, Integer::sum);
```

---

## 数组工具

**基本写法：获取数组长度**
`<数组>.length`
```java
// 数组长度属性
int n = a.length;
```

---

**基本写法：Array.newInstance**
`Array.newInstance(<类型>, <长度>);`
```java
// 反射创建数组
Object arr = Array.newInstance(int.class, 5);
```

---

**基本写法：获取元素**
`Array.get(<数组>, <索引>);`
```java
// 反射获取数组元素
Object e = Array.get(arr, 0);
```

---



<!-- ============ 文档分隔线：013-java/069-JavaCollectionsUtility.md ============ -->

# Java Collections 工具类语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 排序与打乱

**基本写法：排序**
`Collections.sort(<list>);`
```java
// 对 List 自然排序
Collections.sort(list);
```

---

**基本写法：自定义排序**
`Collections.sort(<list>, <比较器>);`
```java
// 用比较器排序
Collections.sort(list, Comparator.reverseOrder());
```

---

**基本写法：打乱顺序**
`Collections.shuffle(<list>);`
```java
// 随机打乱列表
Collections.shuffle(list);
```

---

**基本写法：指定随机源**
`Collections.shuffle(<list>, <Random>);`
```java
// 用指定随机数打乱
Collections.shuffle(list, new Random(42));
```

---

**基本写法：反转**
`Collections.reverse(<list>);`
```java
// 反转列表顺序
Collections.reverse(list);
```

---

**基本写法：旋转**
`Collections.rotate(<list>, <距离>);`
```java
// 循环移动元素
Collections.rotate(list, 2);
```

---

## 查找与替换

**基本写法：二分查找**
`Collections.binarySearch(<list>, <key>);`
```java
// 在已排序列表中查找
int idx = Collections.binarySearch(sortedList, "b");
```

---

**基本写法：最大值**
`Collections.max(<collection>);`
```java
// 自然顺序最大值
String max = Collections.max(list);
```

---

**基本写法：最小值**
`Collections.min(<collection>);`
```java
// 自然顺序最小值
String min = Collections.min(list);
```

---

**基本写法：替换全部**
`Collections.replaceAll(<list>, <旧值>, <新值>);`
```java
// 把所有旧值替换为新值
Collections.replaceAll(list, "old", "new");
```

---

**基本写法：查找子列表**
`Collections.indexOfSubList(<list>, <子列表>);`
```java
// 查找子列表首次出现位置
int idx = Collections.indexOfSubList(list, sub);
```

---

**基本写法：频率**
`Collections.frequency(<collection>, <元素>);`
```java
// 统计元素出现次数
int n = Collections.frequency(list, "a");
```

---

**基本写法：不相交**
`Collections.disjoint(<c1>, <c2>);`
```java
// 判断两个集合是否无交集
boolean no = Collections.disjoint(c1, c2);
```

---

## 不可变包装

**基本写法：不可变 List**
`Collections.unmodifiableList(<list>);`
```java
// 包装为不可变 List
List<String> imm = Collections.unmodifiableList(list);
```

---

**基本写法：不可变 Set**
`Collections.unmodifiableSet(<set>);`
```java
// 包装为不可变 Set
Set<String> imm = Collections.unmodifiableSet(set);
```

---

**基本写法：不可变 Map**
`Collections.unmodifiableMap(<map>);`
```java
// 包装为不可变 Map
Map<String, Integer> imm = Collections.unmodifiableMap(map);
```

---

## 同步包装

**基本写法：同步 List**
`Collections.synchronizedList(<list>);`
```java
// 包装为线程安全 List
List<String> sync = Collections.synchronizedList(list);
```

---

**基本写法：同步 Set**
`Collections.synchronizedSet(<set>);`
```java
// 包装为线程安全 Set
Set<String> sync = Collections.synchronizedSet(set);
```

---

**基本写法：同步 Map**
`Collections.synchronizedMap(<map>);`
```java
// 包装为线程安全 Map
Map<String, Integer> sync = Collections.synchronizedMap(map);
```

---

## 类型检查视图

**基本写法：类型检查 List**
`Collections.checkedList(<list>, <元素类>);`
```java
// 运行时类型检查防止污染
List<String> safe = Collections.checkedList(new ArrayList<>(), String.class);
```

---

## 空与单例集合

**基本写法：空列表**
`Collections.emptyList();`
```java
// 返回不可变空 List
List<String> empty = Collections.emptyList();
```

---

**基本写法：单例列表**
`Collections.singletonList(<元素>);`
```java
// 只含一个元素的不可变 List
List<String> one = Collections.singletonList("a");
```

---

**基本写法：单例 Set**
`Collections.singleton(<元素>);`
```java
// 只含一个元素的不可变 Set
Set<String> one = Collections.singleton("a");
```

---

**基本写法：单例 Map**
`Collections.singletonMap(<键>, <值>);`
```java
// 只含一个键值对的不可变 Map
Map<String, Integer> one = Collections.singletonMap("k", 1);
```

---

## 添加元素

**基本写法：添加全部**
`Collections.addAll(<collection>, <元素>...);`
```java
// 批量添加元素
Collections.addAll(list, "a", "b", "c");
```

---

## 不可变集合工厂

**基本写法：List.of**
`List.of(<元素>...);`
```java
// Java 9+ 创建不可变 List
List<String> imm = List.of("a", "b");
```

---

**基本写法：Set.of**
`Set.of(<元素>...);`
```java
// Java 9+ 创建不可变 Set
Set<String> imm = Set.of("a", "b");
```

---

**基本写法：Map.of**
`Map.of(<键1>, <值1>, <键2>, <值2>);`
```java
// Java 9+ 创建不可变 Map
Map<String, Integer> imm = Map.of("a", 1, "b", 2);
```

---

**基本写法：Map.entry**
`Map.entry(<键>, <值>);`
```java
// 创建不可变 entry
Map.Entry<String, Integer> e = Map.entry("k", 1);
Map<String, Integer> m = Map.ofEntries(e);
```

---



<!-- ============ 文档分隔线：013-java/070-JavaObjectsUtility.md ============ -->

# Java Objects 工具类语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 非空检查

**基本写法：要求非空**
`Objects.requireNonNull(<对象>);`
```java
// 为 null 抛 NullPointerException
Objects.requireNonNull(name);
```

---

**基本写法：带消息的非空检查**
`Objects.requireNonNull(<对象>, <消息>);`
```java
// 抛出带消息的 NPE
Objects.requireNonNull(name, "name 不能为空");
```

---

**基本写法：带 Supplier 消息**
`Objects.requireNonNull(<对象>, <Supplier>);`
```java
// 延迟构造消息
Objects.requireNonNull(name, () -> "字段 " + fieldName + " 不能为空");
```

---

**基本写法：requireNonNullElse**
`Objects.requireNonNullElse(<对象>, <默认值>);`
```java
// Java 9+ 为 null 返回默认值
String v = Objects.requireNonNullElse(name, "default");
```

---

**基本写法：requireNonNullElseGet**
`Objects.requireNonNullElseGet(<对象>, <Supplier>);`
```java
// 为 null 时用 Supplier 生成默认值
String v = Objects.requireNonNullElseGet(name, () -> fetchDefault());
```

---

## 相等与哈希

**基本写法：判等**
`Objects.equals(<a>, <b>);`
```java
// 安全的 equals，避免 NPE
boolean ok = Objects.equals(a, b);
```

---

**基本写法：深度判等**
`Objects.deepEquals(<a>, <b>);`
```java
// 数组深度比较
boolean ok = Objects.deepEquals(arr1, arr2);
```

---

**基本写法：哈希码**
`Objects.hash(<字段>...);`
```java
// 多字段组合哈希码
@Override public int hashCode() {
    return Objects.hash(name, age);
}
```

---

**基本写法：单值哈希**
`Objects.hashCode(<对象>);`
```java
// 单个对象的哈希码
int h = Objects.hashCode(name);
```

---

## 字符串表示

**基本写法：toString**
`Objects.toString(<对象>);`
```java
// 调用 toString，null 返回 "null"
String s = Objects.toString(obj);
```

---

**基本写法：带默认值 toString**
`Objects.toString(<对象>, <默认值>);`
```java
// 为 null 返回默认值
String s = Objects.toString(obj, "N/A");
```

---

**基本写法：toIdentityString**
`Objects.toIdentityString(<对象>);`
```java
// 返回类名@哈希码形式
String s = Objects.toIdentityString(obj);
```

---

## 比较操作

**基本写法：比较**
`Objects.compare(<a>, <b>, <比较器>);`
```java
// 用比较器比较两个对象
int r = Objects.compare("a", "b", Comparator.naturalOrder());
```

---

## 索引检查

**基本写法：检查索引**
`Objects.checkIndex(<索引>, <长度>);`
```java
// 检查索引在 [0, length) 范围
int i = Objects.checkIndex(5, 10);
```

---

**基本写法：检查范围**
`Objects.checkFromToIndex(<起>, <止>, <长度>);`
```java
// 检查 [from, to) 在 [0, length) 范围
Objects.checkFromToIndex(2, 5, 10);
```

---

**基本写法：检查起始长度**
`Objects.checkFromIndexSize(<起>, <大小>, <长度>);`
```java
// 检查 [from, from+size) 在 [0, length) 范围
Objects.checkFromIndexSize(2, 3, 10);
```

---

## 数组相关

**基本写法：数组相等**
`Objects.equals(<数组1>, <数组2>);`
```java
// 用 Objects.equals 比较数组引用
boolean same = Objects.equals(arr1, arr2);
```

---

## 验证工具

**基本写法：校验后返回值**
`<表达式> == null ? <默认> : <对象>`
```java
// 配合 requireNonNullElse 使用
String v = Objects.requireNonNullElseElseGet(name, () -> "");
```

---

## 防御性拷贝

**基本写法：复制不可变**
```java
// 通过不可变工厂方法
List<String> imm = List.copyOf(mutableList);
```
```java
// Java 10+ 拷贝为不可变集合
List<String> safe = List.copyOf(original);
Set<String> safeSet = Set.copyOf(original);
Map<String, Integer> safeMap = Map.copyOf(original);
```

---

## 通用工具

**基本写法：获取类名**
`<对象>.getClass().getName();`
```java
// 获取运行时类名
String name = obj.getClass().getName();
```

---

**基本写法：instanceof 模式匹配**
`<对象> instanceof <类型> <变量>`
```java
// Java 16+ 模式匹配
if (obj instanceof String s) {
    System.out.println(s.length());
}
```

---

## 防御性编程

**基本写法：参数校验组合**
```java
public void set(String name, int age) {
    this.name = Objects.requireNonNull(name);
    if (Objects.checkIndex(age, 151) != age) throw new IllegalArgumentException();
}
```
```java
// 综合使用 Objects 进行参数校验
public User(String name, int age) {
    this.name = Objects.requireNonNull(name, "name");
    this.age = age >= 0 && age <= 150 ? age : -1;
}
```

---



<!-- ============ 文档分隔线：013-java/071-JavaCollectionAdvanced.md ============ -->

﻿﻿# Java 集合进阶 EnumMap/IdentityHashMap/CopyOnWrite/ConcurrentHashMap 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## EnumMap 枚举映射

**基本写法：创建 EnumMap**
`new EnumMap<<枚举类型>, <值类型>>(<枚举类>.class);`
```java
// 以枚举作为键的高性能 Map
EnumMap<Color, String> map = new EnumMap<>(Color.class);
```

---

**基本写法：增改元素**
`<map>.put(<枚举键>, <值>);`
```java
// 添加或更新键值
map.put(Color.RED, "红色");
```

---

## EnumSet 枚举集合

**基本写法：包含所有枚举**
`EnumSet.allOf(<枚举类>.class);`
```java
// 创建包含全部枚举常量的集合
EnumSet<Color> all = EnumSet.allOf(Color.class);
```

---

**基本写法：指定元素集合**
`EnumSet.of(<枚举值>...);`
```java
// 创建包含指定枚举值的集合
EnumSet<Color> subset = EnumSet.of(Color.RED, Color.GREEN);
```

---

**基本写法：范围集合**
`EnumSet.range(<起>, <止>);`
```java
// 创建枚举区间集合
EnumSet<Color> range = EnumSet.range(Color.RED, Color.BLUE);
```

---

## IdentityHashMap 身份映射

**基本写法：基于引用相等创建**
`new IdentityHashMap<>();`
```java
// 使用 == 而非 equals 比较键
IdentityHashMap<String, Integer> ihm = new IdentityHashMap<>();
```

---

**基本写法：放入元素**
`<map>.put(<键>, <值>);`
```java
// 同字面量但不同对象会被视为不同键
ihm.put(new String("k"), 1);
ihm.put(new String("k"), 2); // 两个键共存
```

---

## CopyOnWriteArrayList

**基本写法：创建写时复制列表**
`new CopyOnWriteArrayList<>();`
```java
// 适合读多写少的并发场景
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
```

---

**基本写法：添加元素**
`<list>.add(<元素>);`
```java
// 每次写入都会复制底层数组
list.add("a");
```

---

**基本写法：弱一致迭代**
`<list>.iterator();`
```java
// 迭代器不会抛 ConcurrentModificationException
for (String s : list) {
    System.out.println(s);
}
```

---

## CopyOnWriteArraySet

**基本写法：创建写时复制集合**
`new CopyOnWriteArraySet<>();`
```java
// 基于 CopyOnWriteArrayList 实现的并发 Set
CopyOnWriteArraySet<String> set = new CopyOnWriteArraySet<>();
```

---

## ConcurrentHashMap

**基本写法：创建并发哈希映射**
`new ConcurrentHashMap<>();`
```java
// 线程安全的高并发哈希表
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
```

---

**基本写法：原子 absent 放入**
`<map>.putIfAbsent(<键>, <值>);`
```java
// 仅当键不存在时放入
map.putIfAbsent("k", 1);
```

---

**基本写法：原子计算**
`<map>.compute(<键>, <BiFunction>);`
```java
// 原子地重算指定键的值
map.compute("k", (k, v) -> v == null ? 1 : v + 1);
```

---

**基本写法：合并值**
`<map>.merge(<键>, <值>, <BiFunction>);`
```java
// 合并新旧值
map.merge("k", 1, Integer::sum);
```

---

**基本写法：批量遍历**
`<map>.forEach(<BiConsumer>);`
```java
// 并发安全遍历
map.forEach((k, v) -> System.out.println(k + ":" + v));
```

---

**基本写法：搜索所有条目**
`<map>.search(<并行阈值>, <BiFunction>);`
```java
// 并行搜索并返回首个非空结果
String r = map.search(2, (k, v) -> v > 1 ? k : null);
```

---

**基本写法：并行归约**
`<map>.reduce(<并行阈值>, <Mapper>, <Reducer>);`
```java
// 并行归约所有值
int sum = map.reduce(2, (k, v) -> v, Integer::sum);
```

---

## ConcurrentLinkedQueue

**基本写法：创建无界非阻塞队列**
`new ConcurrentLinkedQueue<>();`
```java
// 基于 CAS 的非阻塞并发队列
ConcurrentLinkedQueue<String> q = new ConcurrentLinkedQueue<>();
```

---

**基本写法：入队**
`<queue>.offer(<元素>);`
```java
// 非阻塞地添加到队尾
q.offer("a");
```

---

**基本写法：出队**
`<queue>.poll();`
```java
// 取出并移除队首元素，空队列返回 null
String head = q.poll();
```

---



<!-- ============ 文档分隔线：013-java/072-JavaFunctionalInterfaces.md ============ -->

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



<!-- ============ 文档分隔线：013-java/073-JavaSecurityCryptography.md ============ -->

# Java 安全与加密 MessageDigest/Cipher/KeyStore/SecureRandom 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## MessageDigest 摘要

**基本写法：获取摘要实例**
`MessageDigest.getInstance(<算法名>);`
```java
// 创建 SHA-256 摘要计算器
MessageDigest md = MessageDigest.getInstance("SHA-256");
```

---

**基本写法：计算字节数组摘要**
`<md>.digest(<字节数组>);`
```java
// 一次性计算哈希
byte[] hash = md.digest("hello".getBytes(StandardCharsets.UTF_8));
```

---

**基本写法：分块更新**
`<md>.update(<字节数组>);`
```java
// 分块输入数据
md.update("part1".getBytes());
md.update("part2".getBytes());
byte[] h = md.digest();
```

---

## SecureRandom 随机数

**基本写法：创建安全随机数**
`new SecureRandom();`
```java
// 密码学安全的随机数生成器
SecureRandom sr = new SecureRandom();
```

---

**基本写法：生成随机字节**
`<sr>.nextBytes(<字节数组>);`
```java
// 填充随机字节
byte[] salt = new byte[16];
sr.nextBytes(salt);
```

---

**基本写法：生成随机整数**
`<sr>.nextInt(<上界>);`
```java
// 生成 0(含) 到 bound(不含) 的随机数
int code = sr.nextInt(1000000);
```

---

## KeyGenerator 密钥生成

**基本写法：生成对称密钥**
`KeyGenerator.getInstance(<算法>);`
```java
// 创建 AES 密钥生成器
KeyGenerator kg = KeyGenerator.getInstance("AES");
kg.init(256);
SecretKey key = kg.generateKey();
```

---

## Cipher 加解密

**基本写法：获取 Cipher 实例**
`Cipher.getInstance(<算法/模式/填充>);`
```java
// 创建 AES/GCM 加密器
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
```

---

**基本写法：初始化加密**
`<cipher>.init(Cipher.ENCRYPT_MODE, <密钥>);`
```java
// 用密钥初始化为加密模式
cipher.init(Cipher.ENCRYPT_MODE, key);
```

---

**基本写法：执行加密**
`<cipher>.doFinal(<明文>);`
```java
// 加密并返回密文
byte[] ct = cipher.doFinal("secret".getBytes());
```

---

**基本写法：解密**
`<cipher>.init(Cipher.DECRYPT_MODE, <密钥>);`
```java
// 用密钥初始化为解密模式
cipher.init(Cipher.DECRYPT_MODE, key, params);
byte[] pt = cipher.doFinal(ct);
```

---

## KeyStore 密钥库

**基本写法：加载默认密钥库**
`KeyStore.getInstance(<类型>);`
```java
// 创建 JKS 类型密钥库
KeyStore ks = KeyStore.getInstance("PKCS12");
ks.load(null, null); // 新建空密钥库
```

---

**基本写法：存储密钥**
`<ks>.setKeyEntry(<别名>, <密钥>, <密码>, <证书链>);`
```java
// 把密钥存入密钥库
ks.setKeyEntry("myKey", key, "pass".toCharArray(), null);
```

---

## Mac 消息认证码

**基本写法：计算 HMAC**
`Mac.getInstance(<算法>);`
```java
// 创建 HMAC-SHA256
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(key);
byte[] tag = mac.doFinal("data".getBytes());
```

---

## Signature 签名

**基本写法：数字签名**
`Signature.getInstance(<算法>);`
```java
// 创建 SHA256withRSA 签名对象
Signature sig = Signature.getInstance("SHA256withRSA");
sig.initSign(privateKey);
sig.update("data".getBytes());
byte[] sign = sig.sign();
```

---



<!-- ============ 文档分隔线：013-java/074-JavaCommandLineTools.md ============ -->

# Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## javac 编译

**基本写法：编译源文件**
`javac <源文件>.java`
```bash
# 编译单个源文件
javac Main.java
```

---

**基本写法：指定输出目录**
`javac -d <输出目录> <源文件>`
```bash
# 编译并输出到 bin 目录
javac -d bin src/Main.java
```

---

**基本写法：指定 classpath**
`javac -cp <路径> <源文件>`
```bash
# 编译时引用外部依赖
javac -cp "lib/*" -d bin src/Main.java
```

---

**基本写法：指定源版本与目标版本**
`javac --source <版本> --target <版本> <源文件>`
```bash
# 用 Java 21 语法编译为 21 字节码
javac --release 21 -d bin src/Main.java
```

---

**基本写法：启用预览特性**
`javac --enable-preview --release <版本> <源文件>`
```bash
# 启用 Java 23 预览特性
javac --enable-preview --release 23 src/Main.java
```

---

## java 运行

**基本写法：运行主类**
`java -cp <路径> <主类>`
```bash
# 运行编译后的类
java -cp bin com.example.Main
```

---

**基本写法：运行 jar**
`java -jar <文件>.jar`
```bash
# 运行可执行 jar
java -jar app.jar
```

---

**基本写法：传递程序参数**
`java -cp <路径> <主类> <参数>...`
```bash
# 传递命令行参数
java -cp bin Main arg1 arg2
```

---

**基本写法：设置 JVM 属性**
`java -D<名>=<值> -cp <路径> <主类>`
```bash
# 设置系统属性
java -Dconfig=prod -cp bin Main
```

---

**基本写法：设置堆内存**
`java -Xmx<大小> -Xms<大小> -cp <路径> <主类>`
```bash
# 设置最大堆 2G 初始堆 512M
java -Xmx2g -Xms512m -cp bin Main
```

---

## jar 打包

**基本写法：创建 jar**
`jar cf <文件>.jar -C <目录> .`
```bash
# 把 bin 目录打包成 app.jar
jar cf app.jar -C bin .
```

---

**基本写法：创建可执行 jar**
`jar cfe <文件>.jar <主类> -C <目录> .`
```bash
# 指定主类打成可执行 jar
jar cfe app.jar com.example.Main -C bin .
```

---

**基本写法：查看 jar 内容**
`jar tf <文件>.jar`
```bash
# 列出 jar 中的条目
jar tf app.jar
```

---

**基本写法：解压 jar**
`jar xf <文件>.jar`
```bash
# 解压到当前目录
jar xf app.jar
```

---

## jshell 交互式 REPL

**基本写法：启动 jshell**
`jshell`
```bash
# 启动 Java 交互式环境
jshell
```

---

**基本写法：执行片段**
`jshell -e "<表达式>"`
```bash
# 直接执行表达式
jshell -e "System.out.println(1+2)"
```

---

**基本写法：加载文件**
`/open <文件>`
```bash
# 在 jshell 中加载源文件
/open Main.java
```

---

## jpackage 打包

**基本写法：打包应用**
`jpackage --input <目录> --name <名称> --main-jar <文件> --main-class <类>`
```bash
# 打包成原生安装包
jpackage --input bin --name MyApp --main-jar app.jar --main-class com.example.Main
```

---

**基本写法：指定类型**
`jpackage --type <类型> --input <目录> --name <名称>`
```bash
# 指定输出类型 msi/exe/dmg/rpm/deb
jpackage --type msi --input bin --name MyApp --main-jar app.jar
```

---



<!-- ============ 文档分隔线：013-java/075-MavenPomConfiguration.md ============ -->

# Maven pom.xml 配置语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 项目坐标

**基本写法：定义项目坐标**
```xml
<groupId><组ID></groupId>
<artifactId><构件ID></artifactId>
<version><版本></version>
```
```xml
<!-- 项目唯一标识 -->
<groupId>com.example</groupId>
<artifactId>my-app</artifactId>
<version>1.0.0</version>
```

---

**基本写法：定义打包类型**
`<packaging><类型></packaging>`
```xml
<!-- jar/war/pom/ear -->
<packaging>jar</packaging>
```

---

## 属性定义

**基本写法：定义属性**
```xml
<properties>
  <属性名>属性值</属性名>
</properties>
```
```xml
<!-- 集中管理版本号 -->
<properties>
  <maven.compiler.release>21</maven.compiler.release>
  <junit.version>5.10.0</junit.version>
</properties>
```

---

## 依赖配置

**基本写法：添加依赖**
```xml
<dependency>
  <groupId><组ID></groupId>
  <artifactId><构件ID></artifactId>
  <version><版本></version>
</dependency>
```
```xml
<!-- 引入 JUnit 5 -->
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>${junit.version}</version>
  <scope>test</scope>
</dependency>
```

---

**基本写法：依赖范围**
`<scope><范围></scope>`
```xml
<!-- compile/provided/runtime/test/system -->
<scope>test</scope>
```

---

**基本写法：排除传递依赖**
```xml
<exclusions>
  <exclusion>
    <groupId><组ID></groupId>
    <artifactId><构件ID></artifactId>
  </exclusion>
</exclusions>
```
```xml
<!-- 排除不想要的传递依赖 -->
<exclusions>
  <exclusion>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
  </exclusion>
</exclusions>
```

---

## 构建配置

**基本写法：指定输出目录**
```xml
<build>
  <finalName><名称></finalName>
  <sourceDirectory><目录></sourceDirectory>
</build>
```
```xml
<!-- 自定义构建产物名 -->
<build>
  <finalName>my-app</finalName>
</build>
```

---

**基本写法：配置插件**
```xml
<plugin>
  <groupId><组ID></groupId>
  <artifactId><构件ID></artifactId>
  <version><版本></version>
  <configuration>...</configuration>
</plugin>
```
```xml
<!-- 配置编译插件 -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.13.0</version>
  <configuration>
    <release>21</release>
  </configuration>
</plugin>
```

---

**基本写法：插件执行目标**
```xml
<executions>
  <execution>
    <phase><阶段></phase>
    <goals><goal><目标></goal></goals>
  </execution>
</executions>
```
```xml
<!-- 绑定插件到生命周期阶段 -->
<executions>
  <execution>
    <phase>package</phase>
    <goals>
      <goal>shade</goal>
    </goals>
  </execution>
</executions>
```

---

## 仓库配置

**基本写法：配置仓库**
```xml
<repositories>
  <repository>
    <id><ID></id>
    <url><地址></url>
  </repository>
</repositories>
```
```xml
<!-- 添加阿里云镜像仓库 -->
<repositories>
  <repository>
    <id>aliyun</id>
    <url>https://maven.aliyun.com/repository/public</url>
  </repository>
</repositories>
```

---

## 多模块聚合

**基本写法：聚合子模块**
```xml
<modules>
  <module><模块名></module>
</modules>
```
```xml
<!-- 聚合多个子模块 -->
<modules>
  <module>core</module>
  <module>web</module>
  <module>service</module>
</modules>
```

---

## dependencyManagement

**基本写法：统一版本管理**
```xml
<dependencyManagement>
  <dependencies>
    <dependency>...</dependency>
  </dependencies>
</dependencyManagement>
```
```xml
<!-- 父 pom 中统一定义版本 -->
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>3.3.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

---



<!-- ============ 文档分隔线：013-java/076-GradleBuildConfiguration.md ============ -->

# Gradle build.gradle 配置语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 插件应用

**基本写法：应用插件**
```groovy
plugins {
  id '<插件ID>' version '<版本>'
}
```
```groovy
// 应用 Java 与应用插件
plugins {
    id 'java'
    id 'application'
}
```

---

**基本写法：应用 Kotlin 插件**
```groovy
plugins {
  id 'org.jetbrains.kotlin.jvm' version '<版本>'
}
```
```groovy
// Kotlin JVM 插件
plugins {
    id 'org.jetbrains.kotlin.jvm' version '2.0.0'
}
```

---

## 仓库配置

**基本写法：配置仓库**
```groovy
repositories {
  mavenCentral()
  maven { url '<地址>' }
}
```
```groovy
// 配置依赖来源仓库
repositories {
    mavenCentral()
    maven { url 'https://maven.aliyun.com/repository/public' }
}
```

---

## 依赖配置

**基本写法：添加依赖**
```groovy
dependencies {
  implementation '<组>:<构件>:<版本>'
}
```
```groovy
// 添加各类依赖
dependencies {
    implementation 'com.google.guava:guava:33.0.0-jre'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
    compileOnly 'org.projectlombok:lombok:1.18.32'
    runtimeOnly 'org.postgresql:postgresql:42.7.3'
}
```

---

**基本写法：平台依赖 BOM**
```groovy
implementation platform('<组>:<构件>:<版本>')
```
```groovy
// 使用 Spring Boot BOM 管理版本
dependencies {
    implementation platform('org.springframework.boot:spring-boot-dependencies:3.3.0')
    implementation 'org.springframework.boot:spring-boot-starter-web'
}
```

---

## Java 配置

**基本写法：配置 Java 版本**
```groovy
java {
  sourceCompatibility = JavaVersion.VERSION_21
  targetCompatibility = JavaVersion.VERSION_21
}
```
```groovy
// 设定 Java 21
java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}
```

---

**基本写法：工具链配置**
```groovy
java {
  toolchain {
    languageVersion = JavaLanguageVersion.of(21)
  }
}
```
```groovy
// 使用指定版本 JDK 编译
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}
```

---

## 任务配置

**基本写法：自定义任务**
```groovy
tasks.register('<名称>') {
  doLast { <动作> }
}
```
```groovy
// 定义自定义任务
tasks.register('hello') {
    doLast {
        println 'Hello Gradle'
    }
}
```

---

**基本写法：任务依赖**
`<任务>.dependsOn <其他任务>`
```groovy
// 让 build 依赖 hello
tasks.named('build') {
    dependsOn 'hello'
}
```

---

## 应用配置

**基本写法：指定主类**
```groovy
application {
  mainClass = '<全限定类名>'
}
```
```groovy
// 配置可运行应用主类
application {
    mainClass = 'com.example.Main'
}
```

---

## 测试配置

**基本写法：使用 JUnit 5**
```groovy
test {
  useJUnitPlatform()
}
```
```groovy
// 启用 JUnit 5 平台
test {
    useJUnitPlatform()
    testLogging {
        events 'passed', 'skipped', 'failed'
    }
}
```

---

## 版本与项目信息

**基本写法：项目元信息**
```groovy
group = '<组ID>'
version = '<版本>'
```
```groovy
// 设置项目坐标
group = 'com.example'
version = '1.0.0'
```

---
