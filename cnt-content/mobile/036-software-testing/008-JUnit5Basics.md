# JUnit5 基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## @Test 注解

**基本写法：标记测试方法**
`@Test`
`void <方法名>() { <断言> }`

```java
# 使用 @Test 标记测试方法
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    @Test
    void testAdd() {
        assertEquals(5, 2 + 3);
    }
}
```

---

## @DisplayName 显示名

**基本写法：设置测试显示名称**
`@DisplayName("<名称>")`

```java
# 为测试类或方法设置友好显示名
@DisplayName("计算器测试")
class CalculatorTest {
    @Test
    @DisplayName("加法应返回正确结果")
    void testAdd() {
        assertEquals(5, 2 + 3);
    }
}
```

---

## @BeforeEach / @AfterEach

**基本写法：每个测试方法前后执行**
`@BeforeEach`
`void <方法>() { <setup> }`
`@AfterEach`
`void <方法>() { <teardown> }`

```java
# 每个测试方法前后执行
import org.junit.jupiter.api.*;

class DatabaseTest {
    @BeforeEach
    void setUp() {
        db = createConnection();
    }

    @AfterEach
    void tearDown() {
        db.close();
    }
}
```

---

## @BeforeAll / @AfterAll

**基本写法：所有测试方法前后执行一次**
`@BeforeAll`
`static void <方法>() { <setup> }`
`@AfterAll`
`static void <方法>() { <teardown> }`

```java
# 所有测试前后执行一次，方法必须为 static
class ServerTest {
    @BeforeAll
    static void startServer() {
        server.start();
    }

    @AfterAll
    static void stopServer() {
        server.stop();
    }
}
```

---

## 生命周期执行顺序

**基本写法：JUnit5 生命周期顺序**
`@BeforeAll → @BeforeEach → @Test → @AfterEach → @AfterAll`

```java
# 生命周期钩子执行顺序示例
class LifecycleTest {
    @BeforeAll  static void initAll() {}
    @BeforeEach void init() {}
    @Test       void test() {}
    @AfterEach  void cleanup() {}
    @AfterAll   static void cleanupAll() {}
}
```

---

## @Disabled 禁用测试

**基本写法：禁用测试方法或类**
`@Disabled(["<原因>"])`

```java
# 禁用测试方法或整个测试类
@Disabled("未实现")
@Test
void testFuture() {
}

@Disabled("维护中")
class MaintenanceTest {
}
```

---

## @Tag 标签过滤

**基本写法：为测试打标签**
`@Tag("<标签名>")`

```java
# 使用标签筛选运行的测试
@Tag("slow")
class LargeDataTest {
    @Test
    @Tag("integration")
    void testLargeQuery() {
    }
}

# 运行: mvn test -Dgroups="slow"
```

---

## @Nested 嵌套测试

**基本写法：嵌套组织测试类**
`@Nested`
`class <内部类> { <测试方法> }`

```java
# 嵌套测试类表达层级关系
class ListTest {
    @Nested
    class WhenEmpty {
        @Test
        void isEmpty() {
            assertTrue(new ArrayList<>().isEmpty());
        }
    }
}
```

---

## @RepeatedTest 重复测试

**基本写法：重复运行测试**
`@RepeatedTest(<次数>[, name="<名称>"])`

```java
# 重复运行同一测试多次
@RepeatedTest(value = 5, name = "重复 {currentRepetition}/{totalRepetitions}")
void testFlaky() {
    assertEquals(4, 2 + 2);
}
```

---

## @ParameterizedTest 参数化

**换行写法：参数化测试**
`@ParameterizedTest`
`@<来源注解>`
`void test_<名称>(<参数>) { <断言> }`

```java
# 参数化测试配合数据来源
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

@ParameterizedTest
@ValueSource(strings = {"", "  "})
void testBlank(String input) {
    assertTrue(input.isBlank());
}
```

---

## @ValueSource 值来源

**基本写法：提供简单值数组**
`@ValueSource(strings = {<值>})`
`@ValueSource(ints = {<值>})`

```java
# 提供基本类型值数组
@ParameterizedTest
@ValueSource(ints = {1, 2, 3})
void testPositive(int n) {
    assertTrue(n > 0);
}
```

---

## @CsvSource CSV 来源

**换行写法：CSV 格式多参数**
`@CsvSource({`
`    "<值1>,<值2>,<期望>",`
`    "<值1>,<值2>,<期望>"`
`})`

```java
# CSV 格式提供多参数
@ParameterizedTest
@CsvSource({
    "1, 2, 3",
    "0, 0, 0",
    "-1, 1, 0"
})
void testAdd(int a, int b, int expected) {
    assertEquals(expected, a + b);
}
```

---

## @MethodSource 方法来源

**换行写法：从工厂方法获取参数**
`@MethodSource("<方法名>")`
`static Stream<Arguments> <方法名>() { return Stream.of(<参数>); }`

```java
# 从静态工厂方法获取复杂参数
@ParameterizedTest
@MethodSource("provideData")
void testAdd(int a, int b, int expected) {
    assertEquals(expected, a + b);
}

static Stream<Arguments> provideData() {
    return Stream.of(
        Arguments.of(1, 2, 3),
        Arguments.of(0, 0, 0)
    );
}
```

---

## AssertAll 分组断言

**基本写法：分组断言一次性报告**
`assertAll(<Executable>...)`

```java
# 分组断言，即使部分失败也全部执行
import static org.junit.jupiter.api.Assertions.*;

@Test
void testUser() {
    User user = new User("Alice", 30);
    assertAll("用户属性",
        () -> assertEquals("Alice", user.getName()),
        () -> assertEquals(30, user.getAge()),
        () -> assertNotNull(user.getEmail())
    );
}
```
