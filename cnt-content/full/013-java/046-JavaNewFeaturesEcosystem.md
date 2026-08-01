---
order: 90
title: 'Java 新特性与生态'
module: java
category: 'Java Advanced'
difficulty: advanced
description: 'Java 21-24 新特性、模块系统、Spring Boot 3.x、构建工具与 GraalVM 原生镜像。'
author: fanquanpp
updated: '2026-08-01'
related:
  - java/Java模块系统
  - java/Java与数据库连接
  - java/数组详解
  - java/JVM调优
prerequisites:
  - java/概述与开发环境
---

## 1. Java 21-24 新特性概览

Java 自从切换到六个月发布周期后，每个 LTS 版本都带来了重要的语言和运行时改进。Java 21 是最新的 LTS 版本，Java 22 和 23 持续引入预览特性，Java 24 进一步巩固了这些改进。

| 版本    | 发布时间 | LTS | 关键特性                                                      |
| :------ | :------- | :-- | :------------------------------------------------------------ |
| Java 21 | 2023-09  | 是  | Virtual Threads、Record Patterns、Pattern Matching for switch |
| Java 22 | 2024-03  | 否  | Unnamed Variables & Patterns、Stream Gatherers(预览)          |
| Java 23 | 2024-09  | 否  | Primitive Types in Patterns(预览)、Module Import Declarations |
| Java 24 | 2025-03  | 否  | Stream Gatherers(正式)、Compact Object Headers                |

### 1.1 Virtual Threads（虚拟线程）

虚拟线程是 Project Loom 的核心成果，在 Java 21 中正式发布。它是一种轻量级线程，由 JVM 而非操作系统管理，使得创建百万级线程成为可能。

```java
// 传统平台线程 —— 每个线程占用约 1MB 栈空间
try (var executor = Executors.newFixedThreadPool(200)) {
    IntStream.range(0, 10_000).forEach(i -> {
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        });
    });
} // 200 个线程处理 10000 个任务，需要排队

// 虚拟线程 —— 几乎无限制的并发
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 1_000_000).forEach(i -> {
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        });
    });
} // 百万级虚拟线程同时运行
```

**关键注意事项：**

- 避免在虚拟线程中使用 `synchronized`，应改用 `ReentrantLock`（即"固定"问题）
- 虚拟线程适用于 I/O 密集型任务，不适用于 CPU 密集型计算
- 使用 `Thread.ofVirtual().name("my-vthread").start(runnable)` 自定义虚拟线程

```java
// 使用 ReentrantLock 替代 synchronized
private final ReentrantLock lock = new ReentrantLock();

public void safeMethod() {
    lock.lock();
    try {
        // 临界区逻辑
    } finally {
        lock.unlock();
    }
}
```

### 1.2 Record Patterns（记录模式）

Record Patterns 在 Java 21 正式发布，允许在 `instanceof` 和 `switch` 中解构记录类：

```java
record Point(int x, int y) {}
record Rectangle(Point upperLeft, Point lowerRight) {}

// instanceof 解构
if (obj instanceof Point(int x, int y)) {
    System.out.println("x = " + x + ", y = " + y);
}

// 嵌套解构
if (obj instanceof Rectangle(Point(int x1, int y1), Point(int x2, int y2))) {
    System.out.printf("矩形: (%d,%d) -> (%d,%d)%n", x1, y1, x2, y2);
}

// switch 中使用 Record Patterns
static String describeShape(Object shape) {
    return switch (shape) {
        case Point(int x, int y) when x == y -> "对角线上的点";
        case Point(int x, int y) -> "普通点 (%d, %d)".formatted(x, y);
        case Rectangle(Point ul, Point lr) -> "矩形";
        default -> "未知形状";
    };
}
```

### 1.3 Pattern Matching for switch

Java 21 正式发布了 switch 的模式匹配，结合 Record Patterns 和 Guarded Patterns 提供了强大的模式匹配能力：

```java
static String formatObject(Object obj) {
    return switch (obj) {
        case Integer i when i > 0  -> "正整数: %d".formatted(i);
        case Integer i             -> "非正整数: %d".formatted(i);
        case String s              -> "字符串(长度%d): %s".formatted(s.length(), s);
        case int[] arr             -> "int数组(长度%d)".formatted(arr.length);
        case null                  -> "null 值";
        default                    -> "其他类型: " + obj.getClass().getSimpleName();
    };
}
```

### 1.4 Sequenced Collections

Java 21 引入了 `SequencedCollection`、`SequencedSet` 和 `SequencedMap` 接口，统一了有序集合的访问方式：

```java
// 之前：不同集合获取首尾元素的方式不同
list.get(0);                // List
list.get(list.size() - 1);
deque.getFirst();           // Deque
deque.getLast();
sortedSet.first();          // SortedSet
sortedSet.last();

// 现在：统一接口
sequencedCollection.getFirst();
sequencedCollection.getLast();
sequencedCollection.reversed(); // 返回逆序视图

// SequencedMap
sequencedMap.firstEntry();
sequencedMap.lastEntry();
sequencedMap.reversed();
sequencedMap.sequencedEntrySet();
sequencedMap.sequencedValues();
```

### 1.5 String Templates（预览）

Java 21 引入了字符串模板的预览特性（注意：在后续版本中仍在演进）：

```java
// 使用 STR 模板处理器
String message = STR."欢迎 \{name}，你的余额为 \{balance} 元";

// 自定义模板处理器
var JSON = StringTemplate.RAW;
StringTemplate template = JSON."""
    {
        "name": "\{name}",
        "age": \{age}
    }
    """;
```

### 1.6 Unnamed Patterns & Variables

Java 22 正式引入了未命名模式和变量：

```java
// 未命名变量 —— 不需要的返回值
try {
    int result = riskyOperation();
} catch (Exception _) {  // 不需要异常对象
    log.error("操作失败");
}

// 未命名模式 —— 忽略 Record 中的某些组件
if (obj instanceof Point(int x, _)) {
    System.out.println("x = " + x); // 只关心 x
}

// switch 中的未命名模式
switch (shape) {
    case Rectangle(Point(int x, _), _) -> "矩形宽度: " + x;
    case Circle(_) -> "圆形";
}
```

## 2. Java 模块系统（JPMS）

Java 9 引入的模块系统（Project Jigsaw）在 Java 21+ 中已成为成熟特性。模块系统通过 `module-info.java` 显式声明依赖和导出，解决了 classpath 的脆弱性问题。

### 2.1 模块定义

```java
// src/com.example.app/module-info.java
module com.example.app {
    requires com.example.service;      // 声明依赖
    requires transitive com.example.util; // 传递依赖
    exports com.example.app.api;       // 导出包
    exports com.example.app.spi to com.example.impl; // 限定导出
    opens com.example.app.model to com.fasterxml.jackson.databind; // 反射访问
    uses com.example.service.Processor; // 声明服务消费
    provides com.example.service.Processor  // 声明服务提供
        with com.example.app.DefaultProcessor;
}
```

### 2.2 模块路径 vs 类路径

| 特性     | Classpath              | Module Path             |
| :------- | :--------------------- | :---------------------- |
| 可靠性   | 脆弱，容易冲突         | 可靠，显式声明依赖      |
| 封装性   | 所有 public 类都可访问 | 只有 exports 的包可访问 |
| 启动速度 | 较慢，需扫描所有 JAR   | 较快，按需加载模块      |
| 反射访问 | 无限制                 | 需要 opens 声明         |

### 2.3 实际迁移策略

```bash
# 使用 jdeps 分析依赖
jdeps --module-path mods -s myapp.jar

# 使用 jlink 创建自定义运行时
jlink --module-path mods \
      --add-modules com.example.app \
      --output custom-runtime \
      --strip-debug \
      --compress zip-6 \
      --no-header-files \
      --no-man-pages
```

## 3. Spring Boot 3.x 核心

Spring Boot 3.x 基于 Spring Framework 6，要求 Java 17+，全面拥抱 Jakarta EE 10 规范。

### 3.1 自动配置原理

Spring Boot 的自动配置基于 `@Conditional` 系列注解和 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 文件：

```java
// 自定义自动配置类
@AutoConfiguration
@ConditionalOnClass(DataSource.class)
@ConditionalOnMissingBean(DataSource.class)
@EnableConfigurationProperties(DataSourceProperties.class)
public class DataSourceAutoConfiguration {

    @Bean
    @ConfigurationProperties(prefix = "spring.datasource")
    public DataSource dataSource(DataSourceProperties props) {
        return DataSourceBuilder.create()
            .url(props.getUrl())
            .username(props.getUsername())
            .password(props.getPassword())
            .build();
    }
}
```

```properties
# META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports
com.example.config.DataSourceAutoConfiguration
```

### 3.2 Spring Boot Actuator

Actuator 提供生产级别的监控和管理端点：

```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus,env,beans
  endpoint:
    health:
      show-details: when-authorized
  metrics:
    export:
      prometheus:
        enabled: true
  info:
    env:
      enabled: true
    java:
      enabled: true
    os:
      enabled: true
```

```java
// 自定义 Health Indicator
@Component
public class DatabaseHealthIndicator extends AbstractHealthIndicator {

    private final DataSource dataSource;

    public DatabaseHealthIndicator(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    protected void doHealthCheck(Health.Builder builder) throws Exception {
        try (Connection conn = dataSource.getConnection()) {
            if (conn.isValid(1)) {
                builder.up().withDetail("database", "PostgreSQL")
                        .withDetail("validationQuery", "isValid()");
            }
        }
    }
}
```

### 3.3 Spring Security 6.x

Spring Security 6 全面采用组件化配置，废弃了 `WebSecurityConfigurerAdapter`：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt
                    .jwtAuthenticationConverter(jwtAuthenticationConverter())
                )
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            );
        return http.build();
    }

    @Bean
    public JwtAuthenticationConverter jwtAuthenticationConverter() {
        JwtAuthenticationConverter converter = new JwtAuthenticationConverter();
        converter.setJwtGrantedAuthoritiesConverter(jwt -> {
            List<String> roles = jwt.getClaimAsStringList("roles");
            return roles.stream()
                .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
                .collect(Collectors.toList());
        });
        return converter;
    }
}
```

## 4. 构建工具

### 4.1 Gradle 现代 Java 项目

Gradle 使用 Kotlin DSL 已成为主流选择：

```kotlin
// build.gradle.kts
plugins {
    java
    id("org.springframework.boot") version "3.3.0"
    id("io.spring.dependency-management") version "1.1.5"
}

group = "com.example"
version = "1.0.0"

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springframework.boot:spring-boot-starter-data-jpa")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
}

tasks.test {
    useJUnitPlatform()
    jvmArgs = listOf("--enable-preview")  // 启用预览特性
}

// GraalVM 原生镜像插件
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
```

### 4.2 Maven Central 发布

发布到 Maven Central 需要 Sonatype 账号和 GPG 签名：

```kotlin
// build.gradle.kts — 发布配置
publishing {
    publications {
        create<MavenPublication>("mavenJava") {
            from(components["java"])
            pom {
                name.set("My Library")
                description.set("A useful library")
                url.set("https://github.com/example/my-lib")
                licenses {
                    license {
                        name.set("Apache-2.0")
                        url.set("https://opensource.org/licenses/Apache-2.0")
                    }
                }
                developers {
                    developer {
                        id.set("fanquanpp")
                        name.set("Fan Quan")
                    }
                }
                scm {
                    url.set("https://github.com/example/my-lib")
                }
            }
        }
    }
}

signing {
    sign(publishing.publications["mavenJava"])
}
```

## 5. JPackage 打包

`jpackage` 工具可以将 Java 应用打包为平台原生安装包：

```bash
# 打包为 Windows 安装程序
jpackage \
  --name MyApp \
  --input target/libs \
  --main-jar myapp.jar \
  --main-class com.example.Main \
  --type msi \
  --app-version 1.0.0 \
  --vendor "Example Corp" \
  --win-dir-chooser \
  --win-menu \
  --win-shortcut \
  --java-options "--enable-preview"

# 打包为 macOS dmg
jpackage \
  --name MyApp \
  --input target/libs \
  --main-jar myapp.jar \
  --main-class com.example.Main \
  --type dmg \
  --app-version 1.0.0 \
  --vendor "Example Corp" \
  --mac-package-identifier com.example.myapp

# 打包为 Linux deb
jpackage \
  --name myapp \
  --input target/libs \
  --main-jar myapp.jar \
  --main-class com.example.Main \
  --type deb \
  --app-version 1.0.0 \
  --vendor "Example Corp"
```

结合 jlink 可以创建不含完整 JRE 的轻量安装包：

```bash
# 先用 jlink 创建自定义运行时
jlink --module-path target/modules \
      --add-modules com.example.app \
      --output target/custom-jre \
      --strip-debug --compress zip-6 \
      --no-header-files --no-man-pages

# 再用 jpackage 基于自定义运行时打包
jpackage \
  --name MyApp \
  --runtime-image target/custom-jre \
  --input target/libs \
  --main-jar myapp.jar \
  --main-class com.example.Main \
  --type app-image
```

## 6. GraalVM 原生镜像

GraalVM 的 Native Image 技术可以将 Java 应用编译为独立的原生可执行文件，显著提升启动速度和降低内存占用。

### 6.1 基本使用

```bash
# 安装 GraalVM
sdk install java 21-graal
sdk use java 21-graal

# 安装 native-image
gu install native-image

# 编译原生镜像
native-image -jar myapp.jar myapp

# 带优化的编译
native-image \
  --initialize-at-build-time \
  --no-fallback \
  -H:+ReportExceptionStackTraces \
  -H:Name=myapp \
  -jar myapp.jar
```

### 6.2 Spring Boot 原生镜像

Spring Boot 3.x 对 GraalVM 原生镜像提供了一等支持：

```bash
# 使用 Spring Boot Maven 插件
mvn -Pnative native:compile

# 使用 Spring Boot Gradle 插件
gradle nativeCompile

# 使用 buildpacks（无需本地安装 GraalVM）
mvn -Pnative spring-boot:build-image
```

```java
// Runtime Hints —— 为反射、代理等提供元数据
@Configuration
@ImportRuntimeHints(MyHints.class)
public class NativeConfig {}

class MyHints implements RuntimeHintsRegistrar {
    @Override
    public void registerHints(RuntimeHints hints, ClassLoader classLoader) {
        hints.reflection()
            .registerType(MyModel.class, MemberCategory.INVOKE_PUBLIC_METHODS)
            .registerType(MyModel.class, MemberCategory.DECLARED_FIELDS);

        hints.resources()
            .registerPattern("com/example/templates/*");

        hints.serialization()
            .registerType(MySerializable.class);

        hints.proxies()
            .registerJdkProxy(MyInterface.class);
    }
}
```

### 6.3 性能对比

| 指标         | 传统 JVM           | GraalVM Native Image |
| :----------- | :----------------- | :------------------- |
| 启动时间     | 1-3 秒             | 10-50 毫秒           |
| 首次请求延迟 | 较高（JIT 预热）   | 立即响应             |
| 内存占用     | 200-500 MB         | 30-80 MB             |
| 峰值吞吐量   | 更高（JIT 优化后） | 较低（AOT 限制）     |
| 生态兼容性   | 完全兼容           | 部分反射需配置       |

**适用场景：** 容器化微服务、Serverless 函数、CLI 工具、需要快速启动的云原生应用。

**不适用场景：** 长时间运行的重计算服务（JIT 的峰值性能更优）、重度依赖反射和动态代理的遗留应用。

## 7. 小结

Java 21+ 的新特性正在从根本上改变 Java 的编程范式：

- **Virtual Threads** 让 Java 回归"一请求一线程"的简单模型
- **Pattern Matching** 让条件逻辑更加声明式和安全
- **Record Classes + Sealed Classes** 构建了代数数据类型的基础
- **JPMS** 提供了强封装和可靠的依赖管理
- **GraalVM Native Image** 让 Java 在云原生场景中更具竞争力
- **Spring Boot 3.x** 全面拥抱现代 Java 特性，提供一流的开发体验

这些特性组合在一起，使得 Java 在保持向后兼容的同时，不断进化以适应现代软件开发的需求。

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
| 变量与常量 | 005-VariableConstant | 本文的并列主题 |
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
| Java 新特性与生态 | 046-JavaNewFeaturesEcosystem | 本文自身 |
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
