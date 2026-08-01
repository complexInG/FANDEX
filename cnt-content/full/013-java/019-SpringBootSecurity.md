---
order: 63
title: SpringBoot安全
module: java
category: Java
difficulty: intermediate
description: 'Spring Security与认证授权'
author: fanquanpp
updated: '2026-08-01'
related:
  - java/Spring基础
  - java/SpringBoot进阶
  - java/SpringBoot数据访问
  - java/Java设计模式
prerequisites:
  - java/概述与开发环境
---

## 概述

Spring Security 是 Spring 生态中的安全框架，负责处理认证（Authentication，你是谁）和授权（Authorization，你能做什么）两大核心问题。在 Web 应用中，安全是基础需求：未登录的用户不能访问受保护的页面，普通用户不能执行管理员的操作，API 接口需要防止被恶意调用。

Spring Security 的设计理念是"默认安全"：引入依赖后，所有接口都需要认证才能访问。你需要显式地配置哪些路径可以公开访问、哪些需要特定角色。这种设计避免了因疏忽导致的未授权访问。

## 基础概念

### 认证与授权

- **认证（Authentication）**：验证用户身份，确认"你是谁"。常见方式有用户名密码登录、OAuth2 登录、JWT 令牌验证
- **授权（Authorization）**：验证用户权限，确认"你能做什么"。常见方式有基于角色的访问控制（RBAC）、基于权限的细粒度控制

### 过滤器链

Spring Security 的核心是一组过滤器链（Filter Chain）。每个 HTTP 请求都会经过这些过滤器，依次完成会话检查、认证、授权等步骤。如果某个过滤器认为请求不合法（如未登录），可以直接返回错误响应，请求不会到达 Controller。

### SecurityContext

认证成功后，用户信息存储在 SecurityContext 中，可以通过 SecurityContextHolder 在应用的任何地方获取当前登录用户的信息。

## 快速上手

### 添加依赖

Maven 项目中添加 Spring Security 依赖：

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

Gradle 项目中：

```groovy
implementation 'org.springframework.boot:spring-boot-starter-security'
```

### 最简配置

添加依赖后，所有接口都需要认证。Spring Security 会自动生成一个密码（在控制台输出），用户名为 user：

```yaml
# application.yml 中自定义用户名密码
spring:
  security:
    user:
      name: admin
      password: admin123
```

### 基本安全配置

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            // 配置路径权限
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/public/**").permitAll()    // 公开路径，无需认证
                .requestMatchers("/admin/**").hasRole("ADMIN") // 需要 ADMIN 角色
                .anyRequest().authenticated()                  // 其他路径需要认证
            )
            // 启用表单登录
            .formLogin(form -> form
                .loginPage("/login")          // 自定义登录页面
                .permitAll()                   // 登录页面本身可以公开访问
            )
            // 启用 OAuth2 登录
            .oauth2Login(oauth2 -> oauth2
                .loginPage("/login")
            );
        return http.build();
    }
}
```

## 详细用法

### 1. 基于数据库的用户认证

实际项目中，用户信息存储在数据库中，需要自定义 UserDetailsService：

```java
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class CustomUserDetailsService implements UserDetailsService {

    private final UserRepository userRepository;

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // 从数据库查询用户
        UserEntity user = userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("用户不存在: " + username));

        // 构建 Spring Security 的 UserDetails 对象
        return User.builder()
            .username(user.getUsername())
            .password(user.getPassword())  // 数据库中存储的是加密后的密码
            .roles(user.getRoles().toArray(new String[0]))  // 用户角色
            .build();
    }
}
```

### 2. 密码加密

永远不要在数据库中存储明文密码。Spring Security 提供了 BCryptPasswordEncoder：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class PasswordConfig {

    @Bean
    public PasswordEncoder passwordEncoder() {
        // BCrypt 是目前推荐的密码哈希算法
        // 每次加密结果不同（因为内置了随机盐），但验证时可以正确匹配
        return new BCryptPasswordEncoder();
    }
}

// 注册用户时加密密码
@Service
public class RegistrationService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public RegistrationService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public void register(String username, String rawPassword) {
        // 加密密码后存储
        String encodedPassword = passwordEncoder.encode(rawPassword);
        UserEntity user = new UserEntity();
        user.setUsername(username);
        user.setPassword(encodedPassword);
        userRepository.save(user);
    }
}
```

### 3. JWT 令牌认证

前后端分离项目中，通常使用 JWT（JSON Web Token）进行认证：

```java
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import javax.crypto.SecretKey;
import java.util.Date;

@Service
public class JwtService {

    // 密钥（生产环境应从配置文件读取）
    private static final SecretKey KEY = Keys.hmacShaKeyFor(
        "my-secret-key-that-is-at-least-32-bytes-long".getBytes()
    );

    // 生成 JWT 令牌
    public String generateToken(String username) {
        return Jwts.builder()
            .subject(username)                          // 主题（用户名）
            .issuedAt(new Date())                      // 签发时间
            .expiration(new Date(System.currentTimeMillis() + 86400000))  // 过期时间（24小时）
            .signWith(KEY)                             // 签名
            .compact();
    }

    // 从 JWT 令牌中提取用户名
    public String extractUsername(String token) {
        return Jwts.parser()
            .verifyWith(KEY)
            .build()
            .parseSignedClaims(token)
            .getPayload()
            .getSubject();
    }

    // 验证令牌是否有效
    public boolean isTokenValid(String token) {
        try {
            Jwts.parser().verifyWith(KEY).build().parseSignedClaims(token);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
```

JWT 认证过滤器：

```java
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.filter.OncePerRequestFilter;
import java.io.IOException;

@Component
public class JwtAuthFilter extends OncePerRequestFilter {

    private final JwtService jwtService;
    private final UserDetailsService userDetailsService;

    public JwtAuthFilter(JwtService jwtService, UserDetailsService userDetailsService) {
        this.jwtService = jwtService;
        this.userDetailsService = userDetailsService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {
        // 从请求头中获取令牌
        String authHeader = request.getHeader("Authorization");
        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            filterChain.doFilter(request, response);
            return;
        }

        String token = authHeader.substring(7);  // 去掉 "Bearer " 前缀
        String username = jwtService.extractUsername(token);

        // 如果用户名不为空且当前没有认证信息
        if (username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
            UserDetails userDetails = userDetailsService.loadUserByUsername(username);

            if (jwtService.isTokenValid(token)) {
                // 设置认证信息到 SecurityContext
                UsernamePasswordAuthenticationToken authToken =
                    new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }

        filterChain.doFilter(request, response);
    }
}
```

### 4. 方法级安全控制

除了 URL 级别的控制，Spring Security 还支持在方法级别进行权限控制：

```java
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.access.prepost.PostAuthorize;
import org.springframework.stereotype.Service;

@Service
public class DocumentService {

    // 只有 ADMIN 角色才能调用此方法
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteDocument(Long id) {
        // 删除文档...
    }

    // 只有文档的作者才能查看
    @PostAuthorize("returnObject.author == authentication.name")
    public Document getDocument(Long id) {
        return documentRepository.findById(id).orElse(null);
    }

    // 使用 SpEL 表达式进行复杂权限判断
    @PreAuthorize("hasRole('ADMIN') or #userId == authentication.principal.id")
    public User getUserProfile(Long userId) {
        return userRepository.findById(userId).orElse(null);
    }
}
```

启用方法级安全控制需要在配置类上添加注解：

```java
@Configuration
@EnableMethodSecurity  // Spring Security 6 的新注解
public class SecurityConfig {
    // ...
}
```

### 5. 获取当前登录用户

在业务代码中获取当前登录用户的信息：

```java
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

@Service
public class SomeBusinessService {

    public void doSomething() {
        // 方式一：通过 SecurityContextHolder 获取
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        String username = auth.getName();  // 当前登录用户的用户名

        // 方式二：在 Controller 方法中注入
        // public ResponseEntity<?> api(@AuthenticationPrincipal UserDetails user) { ... }

        // 方式三：转换为自定义的用户对象
        if (auth.getPrincipal() instanceof UserDetails) {
            UserDetails userDetails = (UserDetails) auth.getPrincipal();
            String name = userDetails.getUsername();
            // userDetails.getAuthorities() 获取权限列表
        }
    }
}
```

## 常见场景

### 场景一：OAuth2 社交登录

集成 GitHub、Google 等第三方登录：

```yaml
# application.yml
spring:
  security:
    oauth2:
      client:
        registration:
          github:
            client-id: your-client-id
            client-secret: your-client-secret
          google:
            client-id: your-client-id
            client-secret: your-client-secret
```

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/", "/login/**", "/error").permitAll()
                .anyRequest().authenticated()
            )
            .oauth2Login(oauth2 -> oauth2
                .loginPage("/login")
                .defaultSuccessUrl("/home", true)
            );
        return http.build();
    }
}
```

### 场景二：CORS 配置

前后端分离项目中，需要配置 CORS 允许前端跨域访问：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import java.util.List;

@Configuration
public class CorsConfig {

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowedOrigins(List.of("https://myapp.com"));  // 允许的来源
        config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE"));  // 允许的 HTTP 方法
        config.setAllowedHeaders(List.of("*"));  // 允许的请求头
        config.setAllowCredentials(true);  // 允许携带 Cookie

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", config);  // 只对 API 路径生效
        return source;
    }
}
```

## 注意事项与常见错误

### CSRF 防护

Spring Security 默认开启 CSRF 防护，这会阻止 POST/PUT/DELETE 请求。对于前后端分离的 API 项目（使用 JWT 认证），可以关闭 CSRF：

```java
http.csrf(csrf -> csrf.disable());  // 仅在使用 JWT 时关闭
```

对于传统的服务端渲染项目，应该保持 CSRF 防护开启。

### 不要在 URL 中传递敏感信息

密码、令牌等敏感信息不要放在 URL 参数中（会被浏览器历史记录和服务器日志记录），应该放在请求体或请求头中。

### 密码加密不能使用 MD5

MD5 已经不安全，容易被彩虹表破解。必须使用 BCrypt、SCrypt 或 Argon2 等自适应哈希算法。

### JWT 的安全问题

JWT 令牌一旦签发就无法撤销（直到过期）。如果用户修改密码或被禁用，已签发的令牌仍然有效。解决方案包括：缩短令牌有效期、使用黑名单、结合 Redis 存储令牌状态。

## 进阶用法

### 多因素认证

Spring Security 支持多因素认证（MFA），在用户名密码之外增加额外的验证步骤：

```java
// 配置两步验证
http
    .authorizeHttpRequests(auth -> auth
        .requestMatchers("/verify-2fa").permitAll()
        .anyRequest().hasAuthority("ROLE_2FA_VERIFIED")
    )
    .formLogin(form -> form
        .successHandler((request, response, authentication) -> {
            // 登录成功后跳转到二次验证页面
            response.sendRedirect("/verify-2fa");
        })
    );
```

### 审计日志

记录安全相关的事件（登录成功、登录失败、权限拒绝等）：

```java
import org.springframework.context.event.EventListener;
import org.springframework.security.authentication.event.AuthenticationSuccessEvent;
import org.springframework.security.authentication.event.AuthenticationFailureBadCredentialsEvent;
import org.springframework.security.authorization.event.AuthorizationDeniedEvent;
import org.springframework.stereotype.Component;

@Component
public class SecurityAuditLogger {

    @EventListener
    public void onLoginSuccess(AuthenticationSuccessEvent event) {
        String username = event.getAuthentication().getName();
        System.out.println("登录成功: " + username);
        // 记录到审计日志表...
    }

    @EventListener
    public void onLoginFailure(AuthenticationFailureBadCredentialsEvent event) {
        String username = (String) event.getAuthentication().getPrincipal();
        System.out.println("登录失败: " + username);
        // 记录到审计日志表，可能需要锁定账号...
    }
}
```

### 自定义访问拒绝处理

当用户权限不足时，返回友好的错误信息而不是默认的错误页面：

```java
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.web.access.AccessDeniedHandler;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@Component
public class CustomAccessDeniedHandler implements AccessDeniedHandler {

    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response,
                       AccessDeniedException ex) throws IOException {
        response.setStatus(HttpServletResponse.SC_FORBIDDEN);
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().write("{\"error\":\"权限不足\",\"message\":\"您没有执行此操作的权限\"}");
    }
}
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
| SpringBoot安全 | 019-SpringBootSecurity | 本文自身 |
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
