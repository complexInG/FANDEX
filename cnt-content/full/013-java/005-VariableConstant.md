---
order: 50
tags:
  - java
difficulty: beginner
title: 变量与常量
module: java
category: 'Java Basics'
description: 变量声明、作用域、常量定义与命名规范。
author: Anonymous
related:
  - java/程序结构与基本语法
  - java/数据类型与类型转换
  - java/枚举与注解
  - java/泛型进阶
prerequisites:
  - java/概述与开发环境
updated: '2026-08-01'
---

# Java 变量与常量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 变量的概念与分类

### 1.1 变量的概念

变量是内存中存储数据的容器，其值可以在程序运行期间改变。变量具有以下特性：

- **类型**：每个变量都有一个类型，决定了变量可以存储的数据种类和范围。
- **名称**：变量的标识符，用于在程序中引用变量。
- **值**：变量存储的具体数据。
- **作用域**：变量可被访问的代码范围。
- **生命周期**：变量从创建到销毁的时间段。

### 1.2 变量的分类

根据变量的定义位置和作用域，Java 中的变量可以分为以下几类：

| 类型         | 定义位置                 | 作用域               | 生命周期                               | 默认值               |
| ------------ | ------------------------ | -------------------- | -------------------------------------- | -------------------- |
| **局部变量** | 方法、构造器或代码块内部 | 从定义处到所在块结束 | 从定义处到所在块结束                   | 无默认值，必须初始化 |
| **成员变量** | 类中，方法之外           | 整个类               | 随对象的创建而存在，随对象的销毁而消失 | 有默认值             |
| **静态变量** | 类中，使用 static 修饰   | 整个类               | 随类的加载而存在，随类的卸载而消失     | 有默认值             |

## 2. 变量的定义与初始化

### 2.1 变量的声明

**语法**：`类型 变量名;`
**示例**：

```java
 int age; // 声明一个整型变量
 double salary; // 声明一个双精度浮点型变量
 String name; // 声明一个字符串变量
 boolean isActive; // 声明一个布尔型变量
```

### 2.2 变量的赋值

**语法**：`变量名 = 值;`
**示例**：

```java
 age = 18; // 给整型变量赋值
 salary = 5000.50; // 给双精度浮点型变量赋值
 name = "John"; // 给字符串变量赋值
 isActive = true; // 给布尔型变量赋值
```

### 2.3 变量的声明与初始化

**语法**：`类型 变量名 = 值;`
**示例**：

```java
 int age = 18; // 声明并初始化整型变量
 double salary = 5000.50; // 声明并初始化双精度浮点型变量
 String name = "John"; // 声明并初始化字符串变量
 boolean isActive = true; // 声明并初始化布尔型变量
```

### 2.4 多个变量的声明与初始化

**语法**：`类型 变量名1, 变量名2 = 值, 变量名3;`
**示例**：

```java
 // 声明多个相同类型的变量
 int x, y = 5, z; // x 和 z 未初始化，y 初始化为 5
 // 建议：为了代码可读性，最好每行只声明一个变量
 int a;
 int b = 10;
 int c;
```

## 3. 变量的作用域与生命周期

### 3.1 局部变量

**定义**：在方法、构造器或代码块内部定义的变量。
**特点**：

- **作用域**：从定义处开始，到所在代码块结束。
- **生命周期**：从定义处开始创建，到所在代码块结束时销毁。
- **默认值**：没有默认值，必须显式初始化后才能使用。
- **存储位置**：存储在栈内存中。
  **示例**：

```java
 public void method() {
  int localVariable = 10; // 局部变量
  if (localVariable > 5) {
  int ifVariable = 20; // 局部变量，作用域在 if 块内
  System.out.println(ifVariable); // 可以访问
  }
  // System.out.println(ifVariable); // 错误：ifVariable 超出作用域
  System.out.println(localVariable); // 可以访问
 }
```

### 3.2 成员变量

**定义**：在类中定义，方法之外的变量，也称为实例变量。
**特点**：

- **作用域**：整个类。
- **生命周期**：随对象的创建而存在，随对象的销毁而消失。
- **默认值**：有默认值，根据类型不同而不同。
- **存储位置**：存储在堆内存中。
  **默认值表**：
  | 类型                           | 默认值   |
  | ------------------------------ | -------- |
  | `byte`, `short`, `int`, `long` | 0        |
  | `float`, `double`              | 0.0      |
  | `char`                         | '\u0000' |
  | `boolean`                      | false    |
  | 引用类型                       | null     |
  | **示例**：                     |

```java
 public class Person {
  // 成员变量
  String name; // 默认值为 null
  int age; // 默认值为 0
  boolean isAdult; // 默认值为 false
  public void display() {
  System.out.println("Name: " + name);
  System.out.println("Age: " + age);
  System.out.println("Is Adult: " + isAdult);
  }
 }
 // 使用
 Person person = new Person();
 person.display(); // 输出默认值
 person.name = "John";
 person.age = 30;
 person.isAdult = true;
 person.display(); // 输出赋值后的值
```

### 3.3 静态变量

**定义**：在类中定义，使用 `static` 关键字修饰的变量，也称为类变量。
**特点**：

- **作用域**：整个类。
- **生命周期**：随类的加载而存在，随类的卸载而消失。
- **默认值**：有默认值，与成员变量相同。
- **存储位置**：存储在方法区的静态存储区。
- **共享性**：所有对象共享同一个静态变量。
  **示例**：

```java
 public class Counter {
  // 静态变量
  public static int count = 0;
  // 构造方法
  public Counter() {
  count++; // 每次创建对象时，count 加 1
  }
  public static void main(String[] args) {
  Counter c1 = new Counter();
  System.out.println("Count: " + Counter.count); // 输出 1
  Counter c2 = new Counter();
  System.out.println("Count: " + Counter.count); // 输出 2
  Counter c3 = new Counter();
  System.out.println("Count: " + Counter.count); // 输出 3
  }
 }
```

## 4. 常量

### 4.1 常量的概念

常量是指在程序运行期间其值不可更改的量。常量可以提高代码的可读性和可维护性。

### 4.2 字面常量

字面常量是直接在代码中出现的常量值，包括以下类型：

| 类型           | 示例                      | 说明                             |
| -------------- | ------------------------- | -------------------------------- |
| **整数常量**   | `100`, `123L`, `0xFF`     | 十进制、长整型、十六进制         |
| **浮点常量**   | `3.14`, `3.14F`, `2.5e3`  | 双精度、单精度、科学计数法       |
| **字符常量**   | `'A'`, `'\n'`, `'\u0041'` | 普通字符、转义字符、Unicode 字符 |
| **字符串常量** | `"Hello"`, `"Java 17"`    | 字符串                           |
| **布尔常量**   | ``, `false`               | 布尔值                           |
| **空常量**     | `null`                    | 空引用                           |

### 4.3 final 常量

使用 `final` 关键字修饰的变量，一旦赋值，其值不可更改。
**特点**：

- **不可修改**：一旦赋值，就不能再修改。
- **命名规范**：全大写，单词之间用下划线分隔。
- **初始化**：必须在声明时或构造方法中初始化。
  **示例**：

```java
 // 类级别的 final 常量
 public static final double PI = 3.1415926535;
 public static final int MAX_SIZE = 100;
 // 实例级别的 final 常量
 public final int ID;
 // 构造方法中初始化
 public class Student {
  public final int ID;
  public final String NAME;
  public Student(int id, String name) {
  this.ID = id;
  this.NAME = name;
  }
 }
 // 局部 final 常量
 public void method() {
  final int LOCAL_CONSTANT = 100;
  // LOCAL_CONSTANT = 200; // 错误：final 变量不能修改
 }
```

### 4.4 枚举常量

枚举是一种特殊的类，用于定义一组常量。
**示例**：

```java
 public enum Day {
  MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
 }
 // 使用
 Day today = Day.MONDAY;
 System.out.println("Today is " + today);
```

## 5. var 类型推断

### 5.1 var 的概念

Java 10 引入了 `var` 关键字，用于局部变量的类型推断。编译器会根据变量的初始值自动推断变量的类型。

### 5.2 var 的使用

**语法**：`var 变量名 = 值;`
**特点**：

- **仅限局部变量**：只能在方法、构造器或代码块内部使用。
- **必须初始化**：声明时必须初始化，否则编译器无法推断类型。
- **不可修改类型**：一旦推断出类型，就不能再更改。
- **可读性**：应在类型明确的情况下使用，避免降低代码可读性。
  **示例**：

```java
 // 基本类型
 var count = 10; // 推断为 int
 var price = 3.14; // 推断为 double
 var flag = true; // 推断为 boolean
 var ch = 'A'; // 推断为 char
 // 引用类型
 var name = "Java"; // 推断为 String
 var list = new ArrayList<String>(); // 推断为 ArrayList<String>
 var map = new HashMap<String, Integer>(); // 推断为 HashMap<String, Integer>
 // 数组
 var numbers = new int[]{1, 2, 3, 4, 5}; // 推断为 int[]
 // 方法返回值
 var result = calculate(); // 推断为方法返回值的类型
```

### 5.3 var 的注意事项

1. **不能用于成员变量**：`var` 只能用于局部变量，不能用于成员变量。
2. **不能用于方法参数**：`var` 不能用于方法参数。
3. **不能用于返回类型**：`var` 不能用于方法的返回类型。
4. **不能用于数组声明**：`var[] arr = {1, 2, 3};` 是错误的，应该使用 `var arr = new int[]{1, 2, 3};`。
5. **类型推断的局限性**：对于复杂的表达式，类型推断可能不够明确，影响代码可读性。
   **示例**：

```java
 // 错误用法
 // public var name = "John"; // 不能用于成员变量
 // 错误用法
 // public void method(var param) { ... } // 不能用于方法参数
 // 错误用法
 // public var method() { return 10; } // 不能用于返回类型
 // 错误用法
 // var[] arr = {1, 2, 3}; // 不能这样声明数组
 // 正确用法
 var arr = new int[]{1, 2, 3}; // 正确的数组声明方式
```

## 6. 变量与常量的最佳实践

### 6.1 变量的命名规范

- **局部变量**：使用小驼峰命名法，如 `userName`、`ageCount`。
- **成员变量**：使用小驼峰命名法，如 `name`、`salary`。
- **静态变量**：使用大驼峰命名法或全大写加下划线，如 `MAX_VALUE`、`DEFAULT_TIMEOUT`。
- **命名原则**：
- 变量名应具有描述性，能够清晰表达变量的用途。
- 避免使用单个字母作为变量名（除了循环变量）。
- 避免使用缩写，除非是广为人知的缩写。
- 保持命名风格的一致性。

### 6.2 常量的命名规范

- **final 常量**：使用全大写，单词之间用下划线分隔，如 `PI`、`MAX_SIZE`。
- **枚举常量**：使用全大写，单词之间用下划线分隔，如 `MONDAY`、`SUNDAY`。
- **命名原则**：
- 常量名应具有描述性，能够清晰表达常量的用途。
- 避免使用魔法数字，应将常量定义为具名常量。
- 保持命名风格的一致性。

### 6.3 变量的使用建议

1. **最小作用域原则**：变量的作用域应尽可能小，只在需要的地方定义。
2. **初始化**：局部变量必须初始化后才能使用。
3. **避免使用 null**：尽量避免将变量初始化为 `null`，可以使用空对象或默认值。
4. **合理使用 var**：在类型明确的情况下使用 `var`，提高代码简洁性。
5. **避免变量遮蔽**：避免在内部作用域中定义与外部作用域同名的变量。

### 6.4 常量的使用建议

1. **使用 final**：对于不需要修改的值，应使用 `final` 修饰。
2. **集中管理**：将相关的常量集中定义在一个类中，便于管理和维护。
3. **使用枚举**：对于一组相关的常量，应使用枚举类型。
4. **避免硬编码**：避免在代码中直接使用字面常量，应定义为具名常量。

## 7. 实际应用示例

### 7.1 示例 1：学生信息管理

```java
 public class Student {
  // 成员变量
  private String name;
  private int age;
  private double score;
  // 构造方法
  public Student(String name, int age, double score) {
  this.name = name;
  this.age = age;
  this.score = score;
  }
  // 方法
  public void display() {
  System.out.println("Name: " + name);
  System.out.println("Age: " + age);
  System.out.println("Score: " + score);
  }
  public static void main(String[] args) {
  // 创建学生对象
  Student student1 = new Student("John", 18, 95.5);
  Student student2 = new Student("Jane", 17, 92.0);
  // 显示学生信息
  System.out.println("Student 1:");
  student1.display();
  System.out.println("\nStudent 2:");
  student2.display();
  }
 }
```

### 7.2 示例 2：使用常量和枚举

```java
 public class ConstantsDemo {
  // 常量定义
  public static final double PI = 3.1415926535;
  public static final int MAX_STUDENTS = 50;
  public static final String SCHOOL_NAME = "ABC School";
  // 枚举定义
  public enum Grade {
  A, B, C, D, F
  }
  public static void main(String[] args) {
  // 使用常量
  System.out.println("PI: " + PI);
  System.out.println("Max Students: " + MAX_STUDENTS);
  System.out.println("School Name: " + SCHOOL_NAME);
  // 使用枚举
  Grade studentGrade = Grade.A;
  System.out.println("Student Grade: " + studentGrade);
  // 计算圆的面积
  double radius = 5.0;
  double area = PI * radius * radius;
  System.out.println("Circle Area: " + area);
  }
 }
```

### 7.3 示例 3：使用 var 类型推断

```java
 import java.util.ArrayList;
 import java.util.HashMap;
 public class VarDemo {
  public static void main(String[] args) {
  // 基本类型
  var count = 10;
  var price = 3.14;
  var flag = true;
  var name = "Java";
  System.out.println("Count: " + count);
  System.out.println("Price: " + price);
  System.out.println("Flag: " + flag);
  System.out.println("Name: " + name);
  // 引用类型
  var list = new ArrayList<String>();
  list.add("Apple");
  list.add("Banana");
  list.add("Orange");
  System.out.println("\nFruits:");
  for (var fruit : list) {
  System.out.println(fruit);
  }
  // 映射
  var map = new HashMap<String, Integer>();
  map.put("John", 25);
  map.put("Jane", 30);
  map.put("Bob", 35);
  System.out.println("\nAges:");
  for (var entry : map.entrySet()) {
  System.out.println(entry.getKey() + ": " + entry.getValue());
  }
  }
 }
```

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

## 参考文献



Oracle Java 官方文档：https://docs.oracle.com/en/java/
OpenJDK 项目：https://openjdk.org/
Java 语言规范：https://docs.oracle.com/javase/specs/
Spring 官方文档：https://spring.io/projects/spring-boot
Baeldung 教程站：https://www.baeldung.com/
Maven 官方文档：https://maven.apache.org/guides/

## 延伸阅读



Java 并发与 JUC，见 013-java 模块并发文档。
JVM 内存与 GC 调优，见 013-java 模块 JVM 文档。
Spring Boot 微服务与 Kubernetes，见 013-java/041-JavaKubernetes 文档。
数据库访问（JDBC/JPA），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Java 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Java 进阶课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Java 概述与开发环境 | 001-JavaOverviewDevEnv | 本文的前置基础 |
| 快速入门 | 002-QuickStart | 本文的前置基础 |
| 程序结构与基本语法 | 003-ProgramStructureBasicSyntax | 本文的并列主题 |
| 数据类型与类型转换 | 004-DataTypeConversion | 本文的并列主题 |
| 变量与常量 | 005-VariableConstant | 本文自身 |
| 枚举与注解 | 006-JavaAnnotationsTutorial | 本文的并列主题 |
| 泛型进阶 | 007-JavaGenericsTutorial | 本文的并列主题 |
| 并发编程基础 | 008-ConcurrencyBasics | 本文的前置基础 |
| JUC并发包 | 009-JUCConcurrency | 本文的并列主题 |
| JVM类加载机制 | 010-JVMClassLoadingMechanism | 本文的原理深化 |
| JVM垃圾回收 | 011-JVMGC | 本文的并列主题 |
| Java反射 | 012-JavaReflection | 本文的并列主题 |
| Java序列化 | 013-JavaSerialization | 本文的并列主题 |
| JavaIO与NIO | 014-JavaIONIO | 本文的并列主题 |
| Java新特性 | 015-JavaNewFeatures | 本文的并列主题 |
| 运算符与表达式 | 016-OperatorExpression | 本文的并列主题 |
| Spring 基础：IoC 容器、AOP、Bean 生命周期与企业级开发核心 | 017-SpringBasicsIoCAOPBeanLifecycle | 本文的前置基础 |
| SpringBoot进阶 | 018-SpringBootAdvanced | 本文的并列主题 |
| SpringBoot安全 | 019-SpringBootSecurity | 本文的安全延伸 |
| SpringBoot数据访问 | 020-SpringBootDataAccess | 本文的并列主题 |
| Java设计模式 | 021-JavaDesignPattern | 本文的并列主题 |
| Java函数式编程 | 022-JavaFunctionalProgramming | 本文的并列主题 |
| Java网络编程 | 023-JavaNetworkProgramming | 本文的并列主题 |
| Java日志系统 | 024-JavaLogSystem | 本文的并列主题 |
| Java单元测试 | 025-JavaUnitTest | 本文的并列主题 |
| Java构建工具 | 026-JavaBuildTool | 本文的并列主题 |
| 控制流 | 027-ControlFlow | 本文的并列主题 |
| Java与微服务 | 028-JavaMicroservice | 本文的并列主题 |
| Java与消息队列 | 029-JavaMessageQueue | 本文的并列主题 |
| Java与Redis | 030-JavaRedis | 本文的并列主题 |
| Java与Docker | 031-JavaDocker | 本文的并列主题 |
| Java与GraphQL | 032-JavaGraphQL | 本文的并列主题 |
| Java性能调优 | 033-JavaPerformanceTuning | 本文的性能延伸 |
| Java与AI | 034-JavaAI | 本文的并列主题 |
| Java与安全 | 035-JavaSecurity | 本文的安全延伸 |
| Java与WebAssembly | 036-JavaWebAssembly | 本文的并列主题 |
| Java与响应式编程 | 037-JavaReactiveProgramming | 本文的并列主题 |
| 方法详解 | 038-MethodDetailed | 本文的并列主题 |
| Java与虚拟线程 | 039-JavaVirtualThread | 本文的并列主题 |
| Java与GraalVM | 040-JavaGraalVM | 本文的并列主题 |
| Java与Kubernetes | 041-JavaKubernetes | 本文的并列主题 |
| Java记录类 | 042-JavaRecordClass | 本文的并列主题 |
| Java文本块 | 043-JavaTextBlock | 本文的并列主题 |
| Java模块系统 | 044-JavaModuleSystem | 本文的并列主题 |
| Java与数据库连接 | 045-JavaDatabaseConnection | 本文的并列主题 |
| Java 新特性与生态 | 046-JavaNewFeaturesEcosystem | 本文的并列主题 |
| 数组详解 | 047-ArrayDetailed | 本文的并列主题 |
| JVM调优 | 048-JVMtuning | 本文的性能延伸 |
| 集合框架详解 | 049-CollectionFrameworkDetailed | 本文的并列主题 |
| 并发编程详解 | 050-ConcurrencyDetailed | 本文的并列主题 |
| CompletableFuture异步编排 | 051-CompletableFutureAsync | 本文的并列主题 |
| ThreadLocal内存泄漏 | 052-ThreadLocalMemoryLeak | 本文的并列主题 |
| 反射与动态代理 | 053-ReflectionDynamicProxy | 本文的并列主题 |
| 注解处理器 | 054-AnnotationProcessor | 本文的并列主题 |
| 分代ZGC详解 | 055-GenerationalZGCDetailed | 本文的并列主题 |
| 面向对象编程 | 056-OOP | 本文的并列主题 |
| 抽象类与接口 | 057-AbstractClassInterface | 本文的并列主题 |
| 异常处理机制 | 058-ExceptionHandlingMechanism | 本文的原理深化 |
| 泛型详解 | 059-GenericDetailed | 本文的并列主题 |
| I/O 流与文件操作 | 060-IOStreamFileOperation | 本文的并列主题 |
| 多线程基础 | 061-MultithreadingBasics | 本文的前置基础 |
| JVM 内存模型 | 062-JVMMemoryModel | 本文的并列主题 |
| Lambda与函数式编程 | 063-LambdaFunctionalProgramming | 本文的并列主题 |
| Stream API | 064-StreamAPI | 本文的并列主题 |
| Spring Boot 学习笔记 | 065-SpringBootNotes | 本文的并列主题 |
| 网络编程 | 066-NetworkProgramming | 本文的并列主题 |
| Spring Cloud 微服务开发 | 067-SpringCloudMicroserviceDevelopment | 本文的并列主题 |
| Java Swing 图形界面 | 068-JavaSwingGUI | 本文的并列主题 |
| Java 项目示例：图书管理系统 | 069-JavaProjectExampleLibrarySystem | 本文的综合应用 |
| Java 理论知识点：JVM 原理、类加载机制与内存管理 | 070-JavaTheoryJVMClassLoadingMemory | 本文的原理深化 |
| Java NIO 通道与缓冲区 | 071-JavaNIOChannelBuffer | 本文的并列主题 |
| Java JDBC 数据库连接 | 072-JDBCDatabaseConnection | 本文的并列主题 |
| Java Optional 类 | 073-JavaOptionalClass | 本文的并列主题 |
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文的并列主题 |
| Java Path 与 Files 语法速查手册 | 075-JavaPathFiles | 本文的并列主题 |
| 启动 REPL 交互环境 | 076-JavaJshellJpackage | 本文的前置基础 |
| Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册 | 077-JavaCountDownLatchCyclicBarrier | 本文的并列主题 |
| Java 阻塞队列 BlockingQueue 语法速查手册 | 078-JavaBlockingQueue | 本文的并列主题 |
| Java try-with-resources 与异常链语法速查手册 | 079-JavaTryWithResources | 本文的并列主题 |
| Java HttpClient 与 WebSocket 语法速查手册 | 080-JavaHttpClientWebSocket | 本文的并列主题 |
| Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册 | 081-JavaTimeFormatting | 本文的并列主题 |
| Java 类型擦除与桥接方法语法速查手册 | 082-JavaTypeErasure | 本文的并列主题 |
| Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册 | 083-JavaEnumAdvanced | 本文的并列主题 |
| Java Iterator/Iterable/Spliterator 语法速查手册 | 084-JavaIteratorIterable | 本文的并列主题 |
| Java Comparator/Comparable 语法速查手册 | 085-JavaComparatorComparable | 本文的并列主题 |
| Java String.format/printf/MessageFormat 语法速查手册 | 086-JavaStringFormat | 本文的并列主题 |
| Java Arrays 工具类语法速查手册 | 087-JavaArraysUtility | 本文的并列主题 |
| Java Objects 工具类语法速查手册 | 088-JavaObjectsUtility | 本文的并列主题 |
| Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册 | 089-JavaCommandLineTools | 本文的并列主题 |
| Maven pom.xml 配置语法速查手册 | 090-MavenPomConfiguration | 本文的并列主题 |
| Gradle build.gradle 配置语法速查手册 | 091-GradleBuildConfiguration | 本文的并列主题 |
