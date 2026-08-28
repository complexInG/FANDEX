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
