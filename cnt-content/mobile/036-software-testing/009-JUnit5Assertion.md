# JUnit5 断言与假设

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## assertEquals 相等断言

**基本写法：断言两值相等**
`assertEquals(<期望>, <实际>[, <消息>])`

```java
# 断言两值相等
import static org.junit.jupiter.api.Assertions.*;

@Test
void testEqual() {
    assertEquals(5, 2 + 3);
    assertEquals("hello", "hello", "字符串应相等");
}
```

---

## assertNotEquals 不等断言

**基本写法：断言两值不等**
`assertNotEquals(<意外值>, <实际>[, <消息>])`

```java
# 断言两值不相等
@Test
void testNotEqual() {
    assertNotEquals(0, 1 + 1);
}
```

---

## assertTrue / assertFalse

**基本写法：断言布尔条件**
`assertTrue(<条件>[, <消息>])`
`assertFalse(<条件>[, <消息>])`

```java
# 断言条件为真或为假
@Test
void testBoolean() {
    assertTrue(5 > 3);
    assertFalse(2 > 5, "2 不应大于 5");
}
```

---

## assertNull / assertNotNull

**基本写法：断言对象为空或非空**
`assertNull(<对象>[, <消息>])`
`assertNotNull(<对象>[, <消息>])`

```java
# 断言对象为 null 或非 null
@Test
void testNull() {
    assertNull(null);
    assertNotNull(new Object());
}
```

---

## assertSame / assertNotSame

**基本写法：断言同一对象引用**
`assertSame(<期望>, <实际>[, <消息>])`
`assertNotSame(<意外>, <实际>[, <消息>])`

```java
# 断言两引用指向同一对象
@Test
void testSame() {
    String a = "x";
    String b = a;
    assertSame(a, b);
}
```

---

## assertArrayEquals 数组断言

**基本写法：断言数组内容相等**
`assertArrayEquals(<期望数组>, <实际数组>[, <消息>])`

```java
# 断言数组元素相等
@Test
void testArray() {
    assertArrayEquals(new int[]{1, 2, 3}, new int[]{1, 2, 3});
}
```

---

## assertIterableEquals 迭代断言

**基本写法：断言可迭代对象相等**
`assertIterableEquals(<期望>, <实际>[, <消息>])`

```java
# 断言 List 等可迭代对象相等
@Test
void testList() {
    assertIterableEquals(
        List.of(1, 2, 3),
        List.of(1, 2, 3)
    );
}
```

---

## assertLinesMatch 行匹配

**基本写法：断言文本行匹配**
`assertLinesMatch(<期望行列表>, <实际行列表>)`

```java
# 断言多行文本匹配，支持正则
@Test
void testLines() {
    assertLinesMatch(
        List.of("header", ".*", "footer"),
        Files.readAllLines(Path.of("file.txt"))
    );
}
```

---

## assertThrows 异常断言

**换行写法：断言抛出异常**
`assertThrows(<异常类>.class, () -> <调用>)`
`Exception e = assertThrows(<异常类>.class, () -> <调用>);`

```java
# 断言代码块抛出指定异常
@Test
void testException() {
    ArithmeticException e = assertThrows(
        ArithmeticException.class,
        () -> { int x = 1 / 0; }
    );
    assertEquals("/ by zero", e.getMessage());
}
```

---

## assertDoesNotThrow 无异常断言

**基本写法：断言不抛异常**
`assertDoesNotThrow(() -> <调用>)`

```java
# 断言代码块不抛出任何异常
@Test
void testNoException() {
    assertDoesNotThrow(() -> Integer.parseInt("42"));
}
```

---

## assertTimeout 超时断言

**换行写法：断言在超时内完成**
`assertTimeout(<Duration>, () -> <调用>)`
`assertTimeoutPreemptively(<Duration>, () -> <调用>)`

```java
# 断言代码在指定时间内完成
import java.time.Duration;

@Test
void testTimeout() {
    assertTimeout(Duration.ofMillis(100), () -> {
        Thread.sleep(50);
    });
}

@Test
void testPreemptiveTimeout() {
    assertTimeoutPreemptively(Duration.ofSeconds(1), () -> {
        fastOperation();
    });
}
```

---

## assertAll 分组断言

**换行写法：一次性执行多个断言**
`assertAll("<标题>", () -> <断言1>, () -> <断言2>, ...)`

```java
# 分组断言全部执行后统一报告
@Test
void testAll() {
    assertAll("用户校验",
        () -> assertEquals("Alice", user.getName()),
        () -> assertTrue(user.getAge() > 0),
        () -> assertNotNull(user.getId())
    );
}
```

---

## assumeTrue 假设

**基本写法：假设成立才继续**
`assumeTrue(<条件>[, <消息>])`

```java
# 假设条件不满足时测试被跳过
import static org.junit.jupiter.api.Assumptions.*;

@Test
void testOnLinux() {
    assumeTrue(System.getProperty("os.name").contains("Linux"));
    assertEquals(0, runLinuxCommand());
}
```

---

## assumingThat 条件执行

**基本写法：条件成立时执行断言**
`assumingThat(<条件>, () -> <断言>)`

```java
# 条件成立时执行，不成立不报错
@Test
void testConditional() {
    assumingTrue(System.getProperty("os.arch").contains("64"),
        () -> assertEquals(8, pointerSize()));
}
```
