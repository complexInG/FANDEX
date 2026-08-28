# Kotlin 测试

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## kotlin.test 基础

**基本写法：简单测试**
`@Test fun <方法名>() { }`
```kotlin
// 使用 @Test 注解标记测试
class MyTest {
    @Test fun sumWorks() = assertEquals(4, 2 + 2)
}
```

---

**基本写法：断言相等**
`assertEquals(<期望>, <实际>)`
```kotlin
// 断言两值相等
assertEquals(10, calc())
```

---

**基本写法：断言不相等**
`assertNotEquals(<值1>, <值2>)`
```kotlin
// 断言两值不等
assertNotEquals(0, count)
```

---

**基本写法：断言为真**
`assertTrue(<条件>)`
```kotlin
// 断言条件为真
assertTrue(list.isEmpty())
```

---

**基本写法：断言为假**
`assertFalse(<条件>)`
```kotlin
// 断言条件为假
assertFalse(list.isNotEmpty())
```

---

**基本写法：断言为 null**
`assertNull(<值>)`
```kotlin
// 断言值为 null
assertNull(findUser(-1))
```

---

**基本写法：断言非 null**
`assertNotNull(<值>)`
```kotlin
// 断言值非 null
assertNotNull(findUser(1))
```

---

**基本写法：断言抛异常**
`assertFailsWith<<异常类型>> { }`
```kotlin
// 断言代码块抛指定异常
assertFailsWith<IllegalArgumentException> { parse("") }
```

---

## kotlin.test 框架适配

**基本写法：Test 注解导入**
`import kotlin.test.Test`
```kotlin
// 跨平台测试注解
import kotlin.test.Test
import kotlin.test.assertEquals
```

---

## JUnit 5 注解

**基本写法：BeforeEach 初始化**
`@BeforeEach fun <方法>() { }`
```kotlin
// 每个测试前执行
class DbTest {
    @BeforeEach fun setup() { db = open() }
}
```

---

**基本写法：AfterEach 清理**
`@AfterEach fun <方法>() { }`
```kotlin
// 每个测试后执行
@AfterEach fun teardown() { db.close() }
```

---

**基本写法：BeforeAll 一次性初始化**
`@BeforeAll fun <方法>() { }`
```kotlin
// 所有测试前执行一次
companion object {
    @BeforeAll @JvmStatic fun init() { }
}
```

---

**基本写法：Disabled 禁用**
`@Disabled("<原因>") @Test fun <方法>() { }`
```kotlin
// 禁用测试用例
@Disabled("待实现")
@Test fun todo() { }
```

---

**基本写法：DisplayName**
`@DisplayName("<名称>") @Test fun <方法>() { }`
```kotlin
// 自定义测试显示名
@DisplayName("用户登录成功")
@Test fun login() { }
```

---

## 参数化测试

**基本写法：ValueSource**
`@ParameterizedTest @ValueSource(strings = ["a", "b"])`
```kotlin
// 多组参数运行测试
@ParameterizedTest
@ValueSource(strings = ["a", "b"])
fun test(s: String) { }
```

---

**基本写法：CsvSource**
`@ParameterizedTest @CsvSource(["1,2,3"])`
```kotlin
// CSV 多参数
@ParameterizedTest
@CsvSource(["1,2,3", "4,5,9"])
fun sum(a: Int, b: Int, expected: Int) { assertEquals(expected, a + b) }
```

---

**基本写法：MethodSource**
`@ParameterizedTest @MethodSource("<方法>")`
```kotlin
// 从静态方法获取参数
@ParameterizedTest
@MethodSource("cases")
fun test(c: Case) { }
companion object {
    @JvmStatic fun cases() = listOf(Case(1, 2))
}
```

---

## 协程测试

**基本写法：runTest 测试协程**
`runTest { }`
```kotlin
// 协程测试运行器
@Test fun test() = runTest {
    val r = fetch()
    assertEquals("ok", r)
}
```

---

**基本写法：测试延迟跳过**
`runTest { delay(1000) }`
```kotlin
// 虚拟时间跳过延迟
runTest {
    delay(1000) // 不实际等待
    launch { }
}
```

---

**基本写法：Turbine 测试 Flow**
`<flow>.test { }`
```kotlin
// 使用 Turbine 测试 Flow
nums().test {
    assertEquals(1, awaitItem())
    awaitComplete()
}
```

---

## MockK 模拟

**基本写法：mockk 模拟对象**
`mockk<<类型>>()`
```kotlin
// 创建 mock 对象
val repo = mockk<UserRepository>()
```

---

**基本写法：mockk relax**
`mockk<<类型>>(relaxed = true)`
```kotlin
// 宽松 mock 自动返回默认值
val repo = mockk<UserRepository>(relaxed = true)
```

---

**基本写法：every 打桩**
`every { <调用> } returns <值>`
```kotlin
// 配置 mock 返回值
every { repo.find(1) } returns User("Alice")
```

---

**基本写法：verify 验证**
`verify { <调用> }`
```kotlin
// 验证方法被调用
verify { repo.find(1) }
```

---

**基本写法：验证调用次数**
`verify(exactly = <次数>) { }`
```kotlin
// 验证调用次数
verify(exactly = 2) { repo.find(any()) }
```

---

**基本写法：coEvery 协程打桩**
`coEvery { <挂起调用> } returns <值>`
```kotlin
// 协程方法打桩
coEvery { repo.fetch() } returns "ok"
```

---

**基本写法：coVerify 协程验证**
`coVerify { <挂起调用> }`
```kotlin
// 验证协程方法调用
coVerify { repo.fetch() }
```

---

## kotest 风格

**基本写法：StringSpec**
`class <类> : StringSpec({ })`
```kotlin
// kotest 字符串风格
class MyTest : StringSpec({
    "sum should work" { 2 + 2 shouldBe 4 }
})
```

---

**基本写法：shouldBe 断言**
`<值> shouldBe <期望>`
```kotlin
// kotest 断言
result shouldBe "hello"
```

---

**基本写法：shouldThrow**
`shouldThrow<<异常>> { }`
```kotlin
// 断言抛异常
shouldThrow<IllegalArgumentException> { parse("") }
```

---

## Gradle 配置

**基本写法：测试依赖**
`testImplementation("<坐标>")`
```kotlin
// build.gradle.kts 测试依赖
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("io.mockk:mockk:1.13.12")
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.9.0")
}
```

---

**基本写法：运行测试**
`./gradlew test`
```bash
# 运行所有测试
./gradlew test
```

---

**基本写法：运行特定测试**
`./gradlew test --tests "<类>.<方法>"`
```bash
# 运行指定测试方法
./gradlew test --tests "com.example.MyTest.sumWorks"
```
