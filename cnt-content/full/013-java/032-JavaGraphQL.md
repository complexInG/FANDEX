---
order: 75
title: Java与GraphQL
module: java
category: Java
difficulty: intermediate
description: 'GraphQL API开发'
author: fanquanpp
updated: '2026-08-01'
related:
  - java/Java与Redis
  - java/Java与Docker
  - java/Java性能调优
  - java/Java与AI
prerequisites:
  - java/概述与开发环境
---

## 概述

GraphQL 是一种 API 查询语言，由 Facebook 在 2015 年开源。与 REST 不同，GraphQL 允许客户端精确指定需要哪些数据，避免了过度获取（返回太多不需要的数据）和不足获取（需要多次请求才能拿到所有数据）的问题。

在 Java 生态中，Spring for GraphQL 是官方推荐的方案，它将 GraphQL 的能力与 Spring Boot 的开发体验结合在一起。你只需要定义 Schema、编写数据获取器（DataFetcher），Spring 就会帮你处理请求路由、参数解析、异常处理等细节。

## 基础概念

### GraphQL 核心概念

- **Schema**：GraphQL 的类型定义文件，描述了有哪些类型、查询和变更。Schema 是前后端的契约
- **Query**：查询操作，相当于 REST 的 GET，只读不修改数据
- **Mutation**：变更操作，相当于 REST 的 POST/PUT/DELETE，会修改数据
- **Subscription**：订阅操作，基于 WebSocket 实现实时数据推送
- **Resolver / DataFetcher**：解析器，为 Schema 中的每个字段提供数据获取逻辑

### GraphQL 与 REST 的区别

REST 按资源设计多个端点（/users、/users/1/posts），GraphQL 只有一个端点（/graphql），客户端通过查询语句决定返回什么数据。这意味着前端不需要后端新增接口就能获取不同组合的数据，减少了沟通成本。

### 类型系统

GraphQL 有自己的类型系统，包括标量类型（Int、String、Boolean、ID）和自定义对象类型。类型之间可以互相引用，形成图状结构，这也是 GraphQL 名称的由来。

## 快速上手

### 添加依赖

Maven 项目中添加 Spring for GraphQL 依赖：

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-graphql</artifactId>
</dependency>
```

Gradle 项目中：

```groovy
implementation 'org.springframework.boot:spring-boot-starter-graphql'
```

### 定义 Schema

在 src/main/resources/graphql/ 目录下创建 Schema 文件：

```graphql
# src/main/resources/graphql/schema.graphqls

# 定义用户类型
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

# 定义文章类型
type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

# 查询入口
type Query {
  user(id: ID!): User
  users: [User!]!
  post(id: ID!): Post
}

# 变更入口
type Mutation {
  createUser(name: String!, email: String!): User!
  createPost(title: String!, content: String!, authorId: ID!): Post!
}
```

### 编写数据获取器

```java
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.graphql.data.method.annotation.SchemaMapping;
import org.springframework.stereotype.Controller;

@Controller
public class UserGraphQLController {

    private final UserService userService;
    private final PostService postService;

    public UserGraphQLController(UserService userService, PostService postService) {
        this.userService = userService;
        this.postService = postService;
    }

    // 处理 Query.user 查询
    @QueryMapping
    public User user(@Argument Long id) {
        return userService.getUser(id);
    }

    // 处理 Query.users 查询
    @QueryMapping
    public List<User> users() {
        return userService.getAllUsers();
    }

    // 处理 User.posts 字段（当查询用户的文章时调用）
    @SchemaMapping
    public List<Post> posts(User user) {
        return postService.getByUserId(user.getId());
    }
}
```

### 测试查询

启动应用后，访问 /graphql 端点，发送以下查询：

```json
{
  "query": "{ user(id: 1) { name email posts { title } } }"
}
```

返回结果只包含你请求的字段：

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com",
      "posts": [{ "title": "First Post" }, { "title": "Second Post" }]
    }
  }
}
```

## 详细用法

### 1. Mutation 变更操作

Mutation 用于创建、更新、删除数据：

```java
import org.springframework.graphql.data.method.annotation.MutationMapping;

@Controller
public class UserGraphQLController {

    // 处理 Mutation.createUser
    @MutationMapping
    public User createUser(@Argument String name, @Argument String email) {
        User user = new User();
        user.setName(name);
        user.setEmail(email);
        return userService.save(user);
    }

    // 处理 Mutation.createPost
    @MutationMapping
    public Post createPost(
            @Argument String title,
            @Argument String content,
            @Argument Long authorId) {
        Post post = new Post();
        post.setTitle(title);
        post.setContent(content);
        post.setAuthorId(authorId);
        return postService.save(post);
    }
}
```

客户端调用 Mutation：

```graphql
mutation {
  createUser(name: "Bob", email: "bob@example.com") {
    id
    name
  }
}
```

### 2. 输入类型 Input Type

当 Mutation 的参数较多时，使用 Input Type 封装：

```graphql
# Schema 中定义输入类型
input CreateUserInput {
  name: String!
  email: String!
  age: Int
}

type Mutation {
  createUser(input: CreateUserInput!): User!
}
```

```java
// Java 中用记录类接收输入参数
public record CreateUserInput(String name, String email, Integer age) {}

@Controller
public class UserGraphQLController {

    @MutationMapping
    public User createUser(@Argument CreateUserInput input) {
        User user = new User();
        user.setName(input.name());
        user.setEmail(input.email());
        user.setAge(input.age());
        return userService.save(user);
    }
}
```

### 3. 分页查询

GraphQL 社区定义了分页规范（Cursor Connection），Spring for GraphQL 支持开箱即用：

```graphql
# Schema 中定义分页
type Query {
  users(first: Int, after: String): UserConnection!
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
}

type UserEdge {
  node: User!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  endCursor: String
}
```

```java
import org.springframework.data.domain.ScrollPosition;
import org.springframework.data.domain.Window;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;

@Controller
public class UserGraphQLController {

    @QueryMapping
    public Window<User> users(
            @Argument int first,
            @Argument String after) {
        // Spring Data 的 Window 类型自动映射为 Connection
        ScrollPosition position = after != null
            ? ScrollPosition.keyset(after)
            : ScrollPosition.keyset();
        return userRepository.findTop10By(position);
    }
}
```

### 4. 异常处理

GraphQL 的错误处理与 REST 不同，即使部分字段出错，也会返回 HTTP 200，错误信息放在 errors 数组中：

```java
import graphql.GraphQLError;
import graphql.GraphqlErrorBuilder;
import org.springframework.graphql.execution.DataFetcherExceptionResolver;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
public class GraphQLExceptionResolver implements DataFetcherExceptionResolver {

    @Override
    public List<GraphQLError> resolveException(Throwable exception) {
        // 将业务异常转换为 GraphQL 错误
        if (exception instanceof UserNotFoundException) {
            GraphQLError error = GraphqlErrorBuilder.newError()
                .message("用户不存在: " + exception.getMessage())
                .errorType(ErrorType.NOT_FOUND)
                .build();
            return List.of(error);
        }

        // 未处理的异常返回 null，由默认处理器处理
        return null;
    }
}
```

### 5. 自定义标量类型

GraphQL 默认不支持 Date 类型，需要注册自定义标量：

```java
import graphql.schema.GraphQLScalarType;
import graphql.schema.Coercing;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

@Bean
public GraphQLScalarType dateScalar() {
    return GraphQLScalarType.newScalar()
        .name("Date")
        .description("日期类型，格式 yyyy-MM-dd")
        .coercing(new Coercing<LocalDate, String>() {
            @Override
            public String serialize(Object dataFetcherResult) {
                // 将 LocalDate 序列化为字符串
                return ((LocalDate) dataFetcherResult)
                    .format(DateTimeFormatter.ISO_LOCAL_DATE);
            }

            @Override
            public LocalDate parseValue(Object input) {
                // 从字符串解析为 LocalDate
                return LocalDate.parse(input.toString());
            }

            @Override
            public LocalDate parseLiteral(Object input) {
                // 从 GraphQL 字面量解析
                return LocalDate.parse(input.toString());
            }
        })
        .build();
}
```

在 Schema 中使用自定义标量：

```graphql
scalar Date

type User {
  name: String!
  birthday: Date
}
```

## 常见场景

### 场景一：多表关联查询

GraphQL 的优势在于关联查询，一次请求获取多层关联数据：

```graphql
# 一次请求获取用户及其文章和评论
query {
  user(id: 1) {
    name
    posts {
      title
      comments {
        content
        author {
          name
        }
      }
    }
  }
}
```

### 场景二：接口联合类型

当查询可能返回不同类型时，使用接口或联合类型：

```graphql
interface Node {
  id: ID!
}

type User implements Node {
  id: ID!
  name: String!
}

type Post implements Node {
  id: ID!
  title: String!
}

type Query {
  node(id: ID!): Node
}
```

```java
@QueryMapping
public Node node(@Argument Long id) {
    // 根据ID前缀判断返回哪种类型
    if (id.startsWith("user:")) {
        return userService.getUser(extractId(id));
    } else {
        return postService.getPost(extractId(id));
    }
}
```

## 注意事项与常见错误

### N+1 查询问题

GraphQL 最常见的问题是 N+1 查询：查询 10 个用户，每个用户再查文章，就会执行 1+10 次数据库查询。解决方法是使用 DataLoader 批量加载：

```java
import org.dataloader.DataLoader;
import org.dataloader.DataLoaderRegistry;
import java.util.concurrent.CompletableFuture;

// 注册 DataLoader
@Bean
public DataLoaderRegistry dataLoaderRegistry() {
    DataLoaderRegistry registry = new DataLoaderRegistry();
    registry.register("posts", DataLoader.newMappedDataLoader(userIds -> {
        // 一次性查询所有用户的文章，避免 N+1
        Map<Long, List<Post>> postsByUserId = postService.findByUserIds(userIds);
        return CompletableFuture.completedFuture(postsByUserId);
    }));
    return registry;
}

// 在 Controller 中使用 DataLoader
@SchemaMapping
public CompletableFuture<List<Post>> posts(User user, DataLoader<Long, List<Post>> dataLoader) {
    return dataLoader.load(user.getId());
}
```

### Schema 设计原则

Schema 应该以业务领域为中心设计，而不是照搬数据库表结构。GraphQL 类型可以和数据库实体不同，一个 GraphQL 字段可能聚合多个数据源的数据。

### 不要把 GraphQL 当数据库查询语言

GraphQL 查询的深度和复杂度需要限制，否则客户端可能发送极其复杂的查询导致服务端资源耗尽。可以通过配置最大查询深度来防护：

```yaml
spring:
  graphql:
    schema:
      max-query-depth: 10 # 限制查询最大深度
```

## 进阶用法

### Subscription 实时数据

GraphQL Subscription 基于 WebSocket，适合实时通知、聊天等场景：

```graphql
type Subscription {
  onNewPost: Post!
}
```

```java
import org.springframework.graphql.data.method.annotation.SubscriptionMapping;
import reactor.core.publisher.Flux;

@Controller
public class PostSubscriptionController {

    @SubscriptionMapping
    public Flux<Post> onNewPost() {
        return postService.newPostStream();
    }
}
```

### 批量加载 @BatchMapping

Spring for GraphQL 提供了 @BatchMapping 注解，简化 DataLoader 的使用：

```java
import org.springframework.graphql.data.method.annotation.BatchMapping;
import java.util.List;
import java.util.Map;

// 批量加载用户文章，自动处理 N+1 问题
@BatchMapping
public Map<User, List<Post>> posts(List<User> users) {
    // 一次查询所有用户的文章
    List<Long> userIds = users.stream().map(User::getId).toList();
    Map<Long, List<Post>> postsByUserId = postService.findByUserIds(userIds);

    // 返回用户到文章列表的映射
    return users.stream().collect(java.util.stream.Collectors.toMap(
        user -> user,
        user -> postsByUserId.getOrDefault(user.getId(), List.of())
    ));
}
```

### GraphQL Federation

在微服务架构中，GraphQL Federation 允许多个服务各自定义 Schema 的一部分，由网关合并为统一的 Schema。Spring for GraphQL 支持 Federation 规范，适合大型微服务项目的 API 统一。

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
| Java与GraphQL | 032-JavaGraphQL | 本文自身 |
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
