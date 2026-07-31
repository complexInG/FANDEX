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
