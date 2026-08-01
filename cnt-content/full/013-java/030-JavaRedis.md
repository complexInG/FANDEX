---
order: 73
title: Java与Redis
module: java
category: Java
difficulty: intermediate
description: Redis缓存与数据结构
author: fanquanpp
updated: '2026-08-01'
related:
  - java/Java与微服务
  - java/Java与消息队列
  - java/Java与Docker
  - java/Java与GraphQL
prerequisites:
  - java/概述与开发环境
---

## 概述

Redis 是一个基于内存的键值存储系统，支持多种数据结构（字符串、哈希、列表、集合、有序集合等），读写速度极快，单机可达每秒十万次操作。在 Java 应用中，Redis 主要用于缓存、会话管理、排行榜、消息队列等场景。

Java 生态中操作 Redis 的方式主要有三种：Jedis（传统同步客户端）、Lettuce（现代异步客户端）、Spring Data Redis（Spring 生态的抽象层）。对于新项目，推荐使用 Spring Data Redis + Lettuce 的组合，既享受 Spring 的便捷抽象，又获得 Lettuce 的异步性能。

## 基础概念

### Redis 数据结构

Redis 不是简单的 key-value 存储，它支持多种数据结构，每种结构适合不同的场景：

- **String**：最基础的类型，可以存字符串、数字、甚至二进制数据（如图片）
- **Hash**：键值对集合，类似 Java 的 HashMap，适合存储对象
- **List**：有序列表，支持从两端插入和弹出，适合消息队列
- **Set**：无序集合，元素唯一，适合去重和交集运算
- **Sorted Set**：有序集合，每个元素关联一个分数，适合排行榜

### 连接方式

Redis 支持单机连接、哨兵模式（Sentinel）和集群模式（Cluster）。开发环境通常用单机，生产环境推荐哨兵或集群以保证高可用。

### 缓存策略

使用 Redis 做缓存时，需要考虑缓存策略：缓存何时失效、缓存和数据库如何保持一致、缓存穿透和雪崩如何防止。这些不是 Redis 本身的功能，而是使用 Redis 时必须面对的架构问题。

## 快速上手

### 添加依赖

Maven 项目中添加 Spring Data Redis 依赖：

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

Gradle 项目中：

```groovy
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

### 配置连接

在 application.yml 中配置 Redis 连接信息：

```yaml
spring:
  data:
    redis:
      host: localhost
      port: 6379
      password: your_password
      database: 0
      lettuce:
        pool:
          max-active: 8 # 连接池最大连接数
          max-idle: 8 # 连接池最大空闲连接数
          min-idle: 2 # 连接池最小空闲连接数
```

### 最简示例

```java
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CacheService {

    @Autowired
    private StringRedisTemplate redisTemplate;

    // 存入字符串
    public void set(String key, String value) {
        redisTemplate.opsForValue().set(key, value);
    }

    // 读取字符串
    public String get(String key) {
        return redisTemplate.opsForValue().get(key);
    }
}
```

## 详细用法

### 1. String 操作

String 是最常用的类型，适合缓存简单值：

```java
@Autowired
private StringRedisTemplate redisTemplate;

// 基本存取
redisTemplate.opsForValue().set("user:name", "Alice");
String name = redisTemplate.opsForValue().get("user:name");

// 设置过期时间（60秒后自动删除）
redisTemplate.opsForValue().set("verify:code", "123456", Duration.ofSeconds(60));

// 仅当 key 不存在时设置（防止覆盖）
Boolean created = redisTemplate.opsForValue().setIfAbsent("lock:order:1001", "locked", Duration.ofSeconds(30));

// 数值递增（适合计数器）
redisTemplate.opsForValue().set("page:views", "0");
redisTemplate.opsForValue().increment("page:views");     // 变为 1
redisTemplate.opsForValue().increment("page:views", 5);  // 变为 6
```

### 2. Hash 操作

Hash 适合存储对象，每个字段可以独立读写：

```java
// 存储用户信息
redisTemplate.opsForHash().put("user:1001", "name", "Alice");
redisTemplate.opsForHash().put("user:1001", "age", "25");
redisTemplate.opsForHash().put("user:1001", "email", "alice@example.com");

// 读取单个字段
String email = (String) redisTemplate.opsForHash().get("user:1001", "email");

// 读取所有字段
Map<Object, Object> user = redisTemplate.opsForHash().entries("user:1001");

// 只更新某个字段（不影响其他字段）
redisTemplate.opsForHash().put("user:1001", "age", "26");

// 删除某个字段
redisTemplate.opsForHash().delete("user:1001", "email");
```

### 3. List 操作

List 适合实现队列或最新列表：

```java
// 从左侧推入（最新消息在前）
redisTemplate.opsForList().leftPush("notifications:user:1001", "你有新消息");
redisTemplate.opsForList().leftPush("notifications:user:1001", "系统升级通知");

// 获取列表范围（0到-1表示全部）
List<String> notifications = redisTemplate.opsForList().range("notifications:user:1001", 0, -1);

// 从右侧弹出（实现先进先出队列）
String oldest = redisTemplate.opsForList().rightPop("notifications:user:1001");

// 获取列表长度
Long count = redisTemplate.opsForList().size("notifications:user:1001");
```

### 4. Set 操作

Set 适合去重和集合运算：

```java
// 添加元素
redisTemplate.opsForSet().add("tags:article:1", "Java", "Redis", "Spring");
redisTemplate.opsForSet().add("tags:article:2", "Java", "MySQL", "Spring");

// 获取所有元素
Set<String> tags = redisTemplate.opsForSet().members("tags:article:1");

// 求交集（两篇文章的共同标签）
Set<String> common = redisTemplate.opsForSet().intersect("tags:article:1", "tags:article:2");

// 判断元素是否存在
Boolean exists = redisTemplate.opsForSet().isMember("tags:article:1", "Java");

// 随机弹出一个元素（适合抽奖场景）
String winner = redisTemplate.opsForSet().pop("lottery:users");
```

### 5. Sorted Set 操作

Sorted Set 适合排行榜：

```java
// 添加元素（带分数）
redisTemplate.opsForZSet().add("leaderboard", "Alice", 95.0);
redisTemplate.opsForZSet().add("leaderboard", "Bob", 88.5);
redisTemplate.opsForZSet().add("leaderboard", "Charlie", 92.0);

// 按分数从高到低获取排名（0表示最高分）
Set<String> top3 = redisTemplate.opsForZSet().reverseRange("leaderboard", 0, 2);

// 获取某个人的排名（从0开始）
Long rank = redisTemplate.opsForZSet().reverseRank("leaderboard", "Alice");

// 获取某个人的分数
Double score = redisTemplate.opsForZSet().score("leaderboard", "Alice");

// 增加分数
redisTemplate.opsForZSet().incrementScore("leaderboard", "Bob", 5.0);
```

### 6. 使用 @Cacheable 注解

Spring 提供了声明式缓存注解，无需手动操作 Redis：

```java
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    // 查询时先查缓存，缓存未命中再查数据库并写入缓存
    @Cacheable(value = "users", key = "#id")
    public User getUser(Long id) {
        // 这个方法只在缓存未命中时执行
        System.out.println("从数据库查询用户: " + id);
        return userRepository.findById(id).orElse(null);
    }

    // 更新数据时同时更新缓存
    @CachePut(value = "users", key = "#user.id")
    public User updateUser(User user) {
        userRepository.save(user);
        return user;
    }

    // 删除数据时同时清除缓存
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }

    // 清除该缓存下的所有条目
    @CacheEvict(value = "users", allEntries = true)
    public void clearAllUserCache() {
        // 不需要实际操作，注解会自动清除缓存
    }
}
```

使用缓存注解前，需要在启动类上添加 @EnableCaching：

```java
@EnableCaching
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### 7. 配置缓存序列化

默认情况下 Spring Cache 使用 Java 序列化存储对象，可读性差。建议配置 JSON 序列化：

```java
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.StringRedisSerializer;
import java.time.Duration;

@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public RedisCacheConfiguration cacheConfiguration() {
        return RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(30)) // 默认过期时间30分钟
            .serializeKeysWith(RedisSerializationContext.SerializationPair
                .fromSerializer(new StringRedisSerializer()))
            .serializeValuesWith(RedisSerializationContext.SerializationPair
                .fromSerializer(new GenericJackson2JsonRedisSerializer()));
    }
}
```

## 常见场景

### 场景一：验证码存储

验证码需要设置短时间过期，Redis 的 TTL 功能天然适合：

```java
@Service
public class VerifyCodeService {

    @Autowired
    private StringRedisTemplate redisTemplate;

    // 生成并存储验证码，5分钟有效
    public void sendCode(String phone) {
        String code = String.valueOf((int)((Math.random() * 9 + 1) * 100000));
        redisTemplate.opsForValue().set("code:" + phone, code, Duration.ofMinutes(5));
        // 发送短信...
        System.out.println("验证码已发送: " + code);
    }

    // 验证验证码
    public boolean verifyCode(String phone, String inputCode) {
        String key = "code:" + phone;
        String savedCode = redisTemplate.opsForValue().get(key);
        if (savedCode != null && savedCode.equals(inputCode)) {
            redisTemplate.delete(key); // 验证成功后删除，防止重复使用
            return true;
        }
        return false;
    }
}
```

### 场景二：分布式锁

在分布式系统中，多个实例可能同时操作同一资源，需要用 Redis 实现分布式锁：

```java
@Service
public class OrderService {

    @Autowired
    private StringRedisTemplate redisTemplate;

    public boolean createOrder(String orderId) {
        String lockKey = "lock:order:" + orderId;
        // 尝试获取锁，30秒后自动释放
        Boolean locked = redisTemplate.opsForValue()
            .setIfAbsent(lockKey, "locked", Duration.ofSeconds(30));

        if (Boolean.TRUE.equals(locked)) {
            try {
                // 执行业务逻辑
                doCreateOrder(orderId);
                return true;
            } finally {
                // 释放锁
                redisTemplate.delete(lockKey);
            }
        }
        return false; // 获取锁失败，说明其他实例正在处理
    }

    private void doCreateOrder(String orderId) {
        // 实际的订单创建逻辑
    }
}
```

### 场景三：限流

使用 Redis 实现简单的滑动窗口限流：

```java
@Service
public class RateLimitService {

    @Autowired
    private StringRedisTemplate redisTemplate;

    // 检查是否超过限制（每分钟最多60次请求）
    public boolean isAllowed(String userId) {
        String key = "rate:" + userId;
        Long count = redisTemplate.opsForValue().increment(key);
        if (count != null && count == 1) {
            // 第一次请求，设置过期时间
            redisTemplate.expire(key, Duration.ofMinutes(1));
        }
        return count != null && count <= 60;
    }
}
```

## 注意事项与常见错误

### 缓存穿透

查询一个数据库中不存在的数据，每次请求都会穿透到数据库。解决方案是缓存空值：

```java
@Cacheable(value = "users", key = "#id")
public User getUser(Long id) {
    User user = userRepository.findById(id).orElse(null);
    if (user == null) {
        // 缓存空对象，设置较短的过期时间
        redisTemplate.opsForValue().set("users::" + id, "NULL", Duration.ofMinutes(5));
    }
    return user;
}
```

### 缓存雪崩

大量缓存同时过期，导致请求全部打到数据库。解决方案是给过期时间加随机偏移：

```java
// 不要让所有缓存同时过期
long baseTtl = 30; // 基础过期时间30分钟
long randomTtl = baseTtl + (long)(Math.random() * 10); // 加0-10分钟随机偏移
redisTemplate.opsForValue().set(key, value, Duration.ofMinutes(randomTtl));
```

### 序列化问题

使用 Spring Data Redis 存储对象时，对象必须实现 Serializable 接口（如果使用 Java 默认序列化）。建议配置 JSON 序列化来避免这个问题，同时提高可读性。

### 连接泄漏

使用 Jedis 时，忘记归还连接会导致连接泄漏。Lettuce 基于 Netty 的异步模型，不存在这个问题，这也是推荐 Lettuce 的原因之一。

## 进阶用法

### Redis Stream 消息队列

Redis 5.0 引入了 Stream 数据类型，可以作为轻量级消息队列使用：

```java
// 生产消息
MapRecord<String, String, String> record = StreamRecords.newRecord()
    .ofMap(Map.of("orderId", "1001", "action", "created"))
    .withStreamKey("order-events");

RecordId id = redisTemplate.opsForStream().add(record);

// 消费消息
List<MapRecord<String, String, String>> messages = redisTemplate.opsForStream()
    .read(StreamOffset.fromLast("order-events"));
```

### Redis Pipeline 批量操作

当需要执行大量 Redis 命令时，使用 Pipeline 可以减少网络往返：

```java
redisTemplate.executePipelined((RedisCallback<Object>) connection -> {
    for (int i = 0; i < 1000; i++) {
        connection.stringCommands().set(
            ("key:" + i).getBytes(),
            ("value:" + i).getBytes()
        );
    }
    return null; // Pipeline 模式下返回值由框架收集
});
```

### Redis 事务

Redis 支持简单的事务，保证一组命令顺序执行不被打断：

```java
redisTemplate.execute(new SessionCallback<Object>() {
    @Override
    public Object execute(RedisOperations operations) throws DataAccessException {
        operations.multi(); // 开启事务
        operations.opsForValue().set("account:A", "900");
        operations.opsForValue().set("account:B", "1100");
        return operations.exec(); // 提交事务
    }
});
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
| Java与Redis | 030-JavaRedis | 本文自身 |
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
