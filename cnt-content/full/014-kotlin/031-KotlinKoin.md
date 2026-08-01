---
order: 70
title: Kotlin与Koin
module: kotlin
category: Kotlin
difficulty: intermediate
description: Koin依赖注入
author: fanquanpp
updated: '2026-08-01'
related:
  - kotlin/Kotlin与Ktor
  - kotlin/Kotlin与Exposed
  - 'kotlin/Kotlin与ktor-client'
  - kotlin/Kotlin与测试
prerequisites:
  - kotlin/概述与环境配置
---

## 概述

Koin 是一个轻量级的 Kotlin 依赖注入框架。与 Dagger、Hilt 等基于代码生成的框架不同，Koin 完全基于 Kotlin 的 DSL 和运行时解析，不需要注解处理器，配置简单直观。如果你觉得 Dagger 太复杂，Koin 是一个很好的替代选择。

依赖注入（Dependency Injection，DI）的核心思想是：一个类不应该自己创建它依赖的对象，而是由外部提供。这样做的好处是代码松耦合、方便测试、易于维护。

## 基础概念

- **Module（模块）**：用 `module { }` 定义的容器，声明各种依赖关系
- **single**：单例，整个应用生命周期只创建一个实例
- **factory**：工厂，每次请求都创建新实例
- **viewModel**：Android ViewModel 专用声明方式
- **get()**：在模块内部获取已声明的依赖，用于自动装配
- **startKoin**：启动 Koin，注册所有模块

## 快速上手

添加依赖：

```kotlin
// build.gradle.kts
dependencies {
    // 核心库
    implementation("io.insert-koin:koin-core:3.5.6")
    // 如果是 Android 项目
    implementation("io.insert-koin:koin-android:3.5.6")
    // 如果是 Ktor 项目
    implementation("io.insert-koin:koin-ktor:3.5.6")
}
```

最简单的使用：

```kotlin
import org.koin.core.module.dsl.singleOf
import org.koin.dsl.module
import org.koin.core.context.startKoin
import org.koin.java.KoinJavaComponent.getKoinInstance

// 定义服务类
class UserRepository {
    fun findUser(id: String): String = "User_$id"
}

class UserService(private val repo: UserRepository) {
    fun getUser(id: String): String = repo.findUser(id)
}

// 定义模块：声明依赖关系
val appModule = module {
    // 单例：UserRepository 全局只有一个实例
    single { UserRepository() }
    // 单例：UserService 全局只有一个实例，自动注入 UserRepository
    single { UserService(get()) }
}

fun main() {
    // 启动 Koin
    startKoin {
        modules(appModule)
    }

    // 获取 UserService 实例
    val userService: UserService = getKoinInstance(UserService::class.java)
    println(userService.getUser("1"))  // User_1
}
```

## 详细用法

### 声明依赖的三种方式

```kotlin
import org.koin.core.module.dsl.singleOf
import org.koin.core.module.dsl.factoryOf
import org.koin.dsl.module

val demoModule = module {
    // 方式一：用 lambda 声明，手动调用 get() 注入依赖
    single { UserRepository() }
    single { UserService(get()) }  // get() 获取 UserRepository

    // 方式二：用构造器引用，自动解析依赖
    singleOf(::UserRepository)
    singleOf(::UserService)

    // 方式三：factory，每次获取都创建新实例
    factory { UserViewModel(get()) }
    factoryOf(::UserViewModel)
}
```

### 带接口的依赖注入

```kotlin
// 定义接口和实现
interface Repository {
    fun getData(): String
}

class RepositoryImpl : Repository {
    override fun getData(): String = "Hello from Repository"
}

class MyService(private val repository: Repository) {
    fun process(): String = repository.getData()
}

val module = module {
    // 绑定接口到实现
    single<Repository> { RepositoryImpl() }
    // 或者使用 bind 关键字
    single { RepositoryImpl() } bind Repository::class
    // MyService 自动注入 Repository
    single { MyService(get()) }
}
```

### 带参数的依赖

```kotlin
class UserViewModel(private val userId: String, private val service: UserService)

val module = module {
    // 声明带参数的依赖
    factory { (userId: String) ->
        UserViewModel(userId, get())
    }
}

// 获取时传入参数
fun main() {
    startKoin { modules(module) }
    val viewModel: UserViewModel by inject { parametersOf("user_123") }
}
```

### 命名依赖

当同一个类型有多个实现时，用命名区分：

```kotlin
interface DataSource {
    fun read(): String
}

class LocalDataSource : DataSource {
    override fun read() = "本地数据"
}

class RemoteDataSource : DataSource {
    override fun read() = "远程数据"
}

val module = module {
    // 用 named 区分同类型的不同实现
    single<DataSource>(named("local")) { LocalDataSource() }
    single<DataSource>(named("remote")) { RemoteDataSource() }

    // 注入时指定名称
    factory { DataProcessor(get(named("remote"))) }
}
```

### Android 中的使用

```kotlin
// 定义 ViewModel
class MainViewModel(private val userService: UserService) : ViewModel() {
    fun loadUser() = userService.getUser("1")
}

// 定义模块
val appModule = module {
    single { UserRepository() }
    single { UserService(get()) }
    // 使用 viewModel 声明，自动与生命周期绑定
    viewModel { MainViewModel(get()) }
}

// 在 Application 中启动
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        startKoin {
            androidContext(this@MyApp)
            modules(appModule)
        }
    }
}

// 在 Activity 中注入
class MainActivity : AppCompatActivity() {
    // 懒注入
    private val viewModel: MainViewModel by viewModel()
}
```

## 常见场景

### 分层架构的依赖注入

```kotlin
// 数据层
class UserRepositoryImpl(private val api: ApiClient) : UserRepository {
    override suspend fun getUser(id: String) = api.fetchUser(id)
}

// 领域层
class GetUserUseCase(private val repo: UserRepository) {
    suspend operator fun invoke(id: String) = repo.getUser(id)
}

// 表现层
class UserViewModel(private val getUserUseCase: GetUserUseCase) : ViewModel() {
    private val _user = MutableStateFlow<User?>(null)
    val user: StateFlow<User?> = _user

    fun load(id: String) {
        viewModelScope.launch {
            _user.value = getUserUseCase(id)
        }
    }
}

// 模块声明
val dataModule = module {
    single { ApiClient() }
    single<UserRepository> { UserRepositoryImpl(get()) }
}

val domainModule = module {
    factory { GetUserUseCase(get()) }
}

val presentationModule = module {
    viewModel { UserViewModel(get()) }
}

// 启动时注册所有模块
startKoin {
    modules(dataModule, domainModule, presentationModule)
}
```

### Ktor 服务端集成

```kotlin
import io.ktor.server.application.*
import org.koin.ktor.plugin.koin
import org.koin.logger.slf4jLogger

fun Application.module() {
    // 在 Ktor 中安装 Koin
    install(Koin) {
        slf4jLogger()
        modules(appModule)
    }

    // 在路由中注入
    routing {
        val userService: UserService by inject()
        get("/users/{id}") {
            val id = call.parameters["id"]!!
            call.respond(userService.getUser(id))
        }
    }
}
```

### 测试中替换依赖

```kotlin
import org.koin.test.KoinTest
import org.koin.test.inject
import org.koin.test.mock.declareMock

class UserServiceTest : KoinTest {
    private val userService: UserService by inject()

    @BeforeEach
    fun setup() {
        startKoin {
            modules(module {
                single<UserRepository> { mockk() }
                single { UserService(get()) }
            })
        }
    }

    @Test
    fun `test with mock repository`() {
        // 用 mock 替换真实依赖
        declareMock<UserRepository> {
            every { findUser("1") } returns "MockUser"
        }
        assertEquals("MockUser", userService.getUser("1"))
    }

    @AfterEach
    fun tearDown() {
        stopKoin()
    }
}
```

## 注意事项

- **没有编译期检查**：Koin 在运行时解析依赖，如果依赖缺失，运行时才会报错。Dagger 在编译期就能发现
- **get() 的位置**：`get()` 只能在模块声明的 lambda 中使用，不能在任意位置调用
- **循环依赖**：Koin 不支持循环依赖，如果 A 依赖 B，B 又依赖 A，启动时会报错
- **性能**：由于运行时解析，Koin 的启动速度比 Dagger 略慢，但对大多数应用来说差异可以忽略
- **模块顺序**：模块的注册顺序不影响依赖解析，Koin 会在所有模块中查找

## 进阶用法

### 模块包含（Module Inclusion）

```kotlin
// 基础模块
val coreModule = module {
    single { HttpClient() }
    single { JsonConfig() }
}

// 业务模块包含基础模块
val featureModule = module {
    includes(coreModule)
    single { UserService(get()) }
}

// 启动时只需注册业务模块
startKoin {
    modules(featureModule)  // coreModule 会自动包含
}
```

### Scope（作用域）

```kotlin
class ScopeService(private val scopeId: String) {
    fun process() = "Processing in scope $scopeId"
}

val module = module {
    // 声明作用域
    scope<ScopeActivity> {
        // 依赖只在 ScopeActivity 的作用域内存在
        scoped { ScopeService("activity-scope") }
    }
}

// 在 Activity 中使用
class ScopeActivity : AppCompatActivity() {
    // 创建作用域
    val scope = createScope(this)

    fun useService() {
        // 从作用域获取依赖
        val service = scope.get<ScopeService>()
        println(service.process())
    }

    override fun onDestroy() {
        super.onDestroy()
        // 关闭作用域，释放依赖
        scope.close()
    }
}
```

### 检查模块配置

```kotlin
// 在测试中验证模块配置是否正确
class ModuleCheckTest : KoinTest {
    @Test
    fun verifyKoinConfiguration() {
        // 检查所有依赖是否都能正确解析
        koinApplication {
            modules(appModule)
            checkModules()
        }
    }
}
```

## 参考文献

Kotlin 官方文档：https://kotlinlang.org/docs/home.html
Kotlin 协程指南：https://kotlinlang.org/docs/coroutines-guide.html
Compose Multiplatform：https://www.jetbrains.com/compose-multiplatform/
Ktor 框架：https://ktor.io/
Android 开发者文档：https://developer.android.com/kotlin

## 延伸阅读

Kotlin 基础语法精讲，见 014-kotlin/002-KotlinBasicSyntax 文档。
协程与 Flow，见 014-kotlin 模块协程文档。
Android 与 HarmonyOS 应用开发，见 018-harmonyos 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Kotlin 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 协程调度与 Flow 背压

协程调度器决定线程切换：Dispatchers.Main 走 Android 主线程，IO 用于阻塞 I/O，Default 用于 CPU 密集；withContext 切换上下文而不阻塞调用方。
Flow 是冷流：每次收集重新执行；`flowOn` 切换上游上下文，`buffer` 缓冲背压，`conflate` 丢弃中间值。
StateFlow 持有最新值并去重，适合 UI 状态；SharedFlow 支持多订阅与事件广播。
取消协作：挂起点检查取消状态并抛出 CancellationException；耗时计算需周期调用 ensureActive。

### 13.2 KMP 多平台架构

KMP 项目以 kotlin-multiplatform 插件定义 targets（jvm、iosArm64、js 等）；commonMain 中 expect 声明，平台源集 actual 实现。
依赖管理：commonMain 使用 kotlinx 库（coroutines、serialization、datetime），平台差异库放对应源集。
与 Compose Multiplatform 组合时，UI 逻辑共享、平台能力通过 expect/actual 隔离。
构建产物：Android 输出 AAR，iOS 输出 framework；通过 CocoaPods 或 Swift Package 集成。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Kotlin 概述与环境配置 | 001-KotlinOverviewEnvSetup | 本文的前置基础 |
| Kotlin 基础语法 | 002-KotlinBasicSyntax | 本文的前置基础 |
| Kotlin 函数与 Lambda | 003-KotlinFunctionAndLambda | 本文的并列主题 |
| Kotlin 类与对象 | 004-KotlinClassObject | 本文的并列主题 |
| Kotlin 泛型与类型系统 | 005-KotlinGenericTypeSystem | 本文的并列主题 |
| Kotlin 集合与协程 | 006-KotlinCollectionCoroutine | 本文的并列主题 |
| Kotlin 协程进阶 | 007-KotlinCoroutineAdvanced | 本文的并列主题 |
| Kotlin 多平台 | 008-KotlinMultiplatform | 本文的并列主题 |
| Kotlin DSL 与领域特定语言 | 009-KotlinDSLDomainSpecificLanguage | 本文的并列主题 |
| Kotlin 测试与最佳实践 | 010-KotlinTestBestPractice | 本文的并列主题 |
| Kotlin与协程Channel | 011-KotlinCoroutineChannel | 本文的并列主题 |
| 空安全详解 | 012-NullSafetyDetailed | 本文的安全延伸 |
| 密封类与代数数据类型 | 013-SealedClassAlgebraicDataType | 本文的并列主题 |
| 委托属性 | 014-DelegateProperty | 本文的并列主题 |
| 扩展函数 | 015-ExtensionFunction | 本文的并列主题 |
| 协程基础 | 016-CoroutineBasics | 本文的前置基础 |
| Flow与响应式流 | 017-FlowReactiveStream | 本文的并列主题 |
| Kotlin作用域函数 | 018-KotlinScopeFunction | 本文的并列主题 |
| Kotlin集合操作 | 019-KotlinCollectionOperation | 本文的并列主题 |
| Kotlin内联类 | 020-KotlinInlineClass | 本文的并列主题 |
| Kotlin 契约（Contracts） | 021-KotlinContractContracts | 本文的并列主题 |
| Kotlin与DSL | 022-KotlinDSL | 本文的并列主题 |
| Kotlin序列化 | 023-KotlinSerialization | 本文的并列主题 |
| Kotlin与Android | 024-KotlinAndroid | 本文的并列主题 |
| Kotlin与Spring | 025-KotlinSpring | 本文的并列主题 |
| Kotlin类型系统 | 026-KotlinTypeSystem | 本文的并列主题 |
| Kotlin与Compose | 027-KotlinCompose | 本文的并列主题 |
| Kotlin与Arrow | 028-KotlinArrow | 本文的并列主题 |
| Kotlin与Ktor | 029-KotlinKtor | 本文的并列主题 |
| Kotlin与Exposed | 030-KotlinExposed | 本文的并列主题 |
| Kotlin与Koin | 031-KotlinKoin | 本文自身 |
| Kotlin与ktor-client | 032-KotlinKtorClient | 本文的并列主题 |
| Kotlin与测试 | 033-KotlinTest | 本文的并列主题 |
| Kotlin与编译器插件 | 034-KotlinCompilerPlugin | 本文的并列主题 |
| Kotlin与Gradle | 035-KotlinGradle | 本文的并列主题 |
| Kotlin与原子操作 | 036-KotlinAtomicOperation | 本文的并列主题 |
| Kotlin与Benchmark | 037-KotlinBenchmark | 本文的并列主题 |
| Kotlin与IO | 038-KotlinIO | 本文的并列主题 |
| Kotlin 与正则表达式 | 039-KotlinRegex | 本文的并列主题 |
| Kotlin与时间 | 040-KotlinTime | 本文的并列主题 |
| Kotlin与并发安全 | 041-KotlinConcurrencySafety | 本文的安全延伸 |
| Kotlin与WebSocket | 042-KotlinWebSocket | 本文的并列主题 |
| Kotlin与安全 | 043-KotlinSecurity | 本文的安全延伸 |
| 协程调度器与上下文 | 044-CoroutineDispatcherContext | 本文的并列主题 |
| Flow冷流与SharedFlow和StateFlow | 045-FlowColdSharedState | 本文的并列主题 |
| Channel与BroadcastChannel | 046-ChannelBroadcastChannel | 本文的并列主题 |
| 密封类与密封接口 | 047-SealedClassSealedInterface | 本文的并列主题 |
| 内联类 | 048-InlineClass | 本文的并列主题 |
| 扩展函数的编译原理 | 049-ExtensionFunctionCompilePrinciple | 本文的原理深化 |
| 作用域函数区别 | 050-ScopeFunctionDifference | 本文的并列主题 |
| 协程异常处理 | 051-CoroutineExceptionHandling | 本文的并列主题 |
| Kotlin跨平台 | 052-KotlinCrossPlatform | 本文的并列主题 |
| Kotlin Flow 进阶 | 053-FlowAdvanced | 本文的并列主题 |
