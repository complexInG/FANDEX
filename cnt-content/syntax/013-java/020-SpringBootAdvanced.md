# Java SpringBoot 进阶配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## application.yml 基础配置

**基本写法：服务端口与上下文配置**
`server.port: <端口>`
```java
// application.yml
server:
  port: 8081
  servlet:
    context-path: /api
```

---

**基本写法：应用名称配置**
`spring.application.name: <名称>`
```java
// 应用名称（SpringBoot 2.7+ 推荐写法）
spring:
  application:
    name: my-app
```

---

**基本写法：多环境配置**
`spring.profiles.active: <profile>`
```java
// 激活 dev 环境
spring:
  profiles:
    active: dev
```

---

**基本写法：自定义配置项**
`<前缀>.<字段>: <值>`
```java
// application.yml 自定义属性
app:
  cache:
    ttl: 3600
    maxSize: 1000
```

---

## 读取配置

**基本写法：使用 @Value 注入**
`@Value("${<属性名>}")`
```java
// 注入单个配置项
@Value("${app.cache.ttl}")
private long cacheTtl;
```

---

**基本写法：使用 @ConfigurationProperties 绑定**
`@ConfigurationProperties(prefix = "<前缀>")`
```java
// 批量绑定配置到对象
@Component
@ConfigurationProperties(prefix = "app.cache")
public class CacheProperties {
    private long ttl;
    private int maxSize;
}
```

---

**基本写法：注入 Environment**
`@Autowired Environment <env>`
```java
// 通过 Environment 动态读取配置
@Autowired
private Environment env;
String ttl = env.getProperty("app.cache.ttl");
```

---

## 核心注解

**基本写法：启动类注解**
`@SpringBootApplication`
```java
// 标记 SpringBoot 启动类
@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
```

---

**基本写法：自定义 Component 扫描**
`@ComponentScan(basePackages = {"<包1>", "<包2>"})`
```java
// 指定扫描的包路径
@SpringBootApplication
@ComponentScan(basePackages = {"com.example.service", "com.example.dao"})
public class App { }
```

---

**基本写法：排除自动配置**
`@SpringBootApplication(exclude = {<配置类>.class})`
```java
// 排除数据源自动配置
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class App { }
```

---

**基本写法：定义 Bean**
`@Bean`
```java
// 在配置类中声明 Bean
@Configuration
public class AppConfig {
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

---

**基本写法：条件化 Bean**
`@ConditionalOnProperty(name = "<属性>", havingValue = "<值>")`
```java
// 仅在配置项匹配时生效
@Bean
@ConditionalOnProperty(name = "app.cache.enabled", havingValue = "true")
public CacheManager cacheManager() {
    return new ConcurrentMapCacheManager();
}
```

---

**基本写法：缺失时创建**
`@ConditionalOnMissingBean(<类型>.class)`
```java
// 容器中无该类型 Bean 时才创建
@Bean
@ConditionalOnMissingBean(RestTemplate.class)
public RestTemplate defaultRestTemplate() {
    return new RestTemplate();
}
```

---

## 自动配置机制

**基本写法：自定义 AutoConfiguration**
`@AutoConfiguration`
```java
// SpringBoot 2.7+ 自动配置类写法
@AutoConfiguration
@ConditionalOnClass(RestTemplate.class)
public class MyAutoConfiguration {
    @Bean
    @ConditionalOnMissingBean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

---

**基本写法：注册自动配置**
`META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`
```java
// 文件内每行写一个全限定类名
com.example.MyAutoConfiguration
com.example.OtherAutoConfiguration
```

---

## Profile 环境

**基本写法：声明 Profile Bean**
`@Profile("<名称>")`
```java
// 仅在 dev 环境生效
@Bean
@Profile("dev")
public DataSource devDataSource() {
    return new HikariDataSource();
}
```

---

**基本写法：Profile 配置文件**
`application-<profile>.yml`
```java
// 文件名约定：application-dev.yml、application-prod.yml
// 激活 dev 后会合并 application.yml 与 application-dev.yml
```

---

## 条件装配

**基本写法：类路径存在时生效**
`@ConditionalOnClass(<类>.class)`
```java
// 类路径存在该类时配置才生效
@Configuration
@ConditionalOnClass(RestTemplate.class)
public class WebConfig { }
```

---

**基本写法：Bean 存在时生效**
`@ConditionalOnBean(<类型>.class)`
```java
// 容器中存在 DataSource 时生效
@Bean
@ConditionalOnBean(DataSource.class)
public JdbcTemplate jdbcTemplate(DataSource ds) {
    return new JdbcTemplate(ds);
}
```

---

## 常用 Starter 依赖

**基本写法：Web Starter**
`spring-boot-starter-web`
```java
// pom.xml 引入后自动配置 Tomcat + Spring MVC
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

---

**基本写法：数据访问 Starter**
`spring-boot-starter-data-jpa`
```java
// 引入后自动配置 Hibernate + JPA
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

---

## 启动与运行

**基本写法：以编程方式启动**
`SpringApplication.run(<配置类>.class, <args>)`
```java
// 通过 API 启动并定制
new SpringApplicationBuilder(App.class)
    .bannerMode(Banner.Mode.OFF)
    .logStartupInfo(false)
    .run(args);
```

---

**基本写法：命令行传参**
`--<属性名>=<值>`
```java
// 启动时覆盖配置
java -jar app.jar --server.port=9090 --spring.profiles.active=prod
```

---

**基本写法：CommandLineRunner 初始化**
`@Bean CommandLineRunner <方法>`
```java
// 启动完成后执行
@Bean
public CommandLineRunner init(DataService service) {
    return args -> service.loadData();
}
```

---

## 外部化配置加载顺序

**基本写法：命令行参数优先级最高**
`java -jar <jar> --<属性>=<值>`
```java
// 优先级（从高到低）：
// 命令行参数 > 环境变量 > application-{profile}.yml > application.yml
java -jar app.jar --server.port=9090
```
