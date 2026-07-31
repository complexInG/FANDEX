# Spring 框架核心注解速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 组件注册

**基本写法：@Component 通用组件**
`@Component [("<bean名称>")]`
```java
// 注册为 Spring Bean
@Component
public class UserService { }
```

---

**基本写法：@Service 业务层**
`@Service [("<bean名称>")]`
```java
// 标记业务逻辑层组件
@Service
public class UserService { }
```

---

**基本写法：@Repository 持久层**
`@Repository [("<bean名称>")]`
```java
// 标记数据访问层组件
@Repository
public class UserRepository { }
```

---

**基本写法：@Controller 控制层**
`@Controller [("<bean名称>")]`
```java
// 标记 MVC 控制器
@Controller
public class HomeController { }
```

---

**基本写法：@RestController REST 控制器**
`@RestController`
```java
// 等同于 @Controller + @ResponseBody
@RestController
public class ApiController { }
```

---

**基本写法：@Configuration 配置类**
`@Configuration`
```java
// 声明配置类
@Configuration
public class AppConfig { }
```

---

**基本写法：@Bean 声明 Bean**
`@Bean [("<名称>")]`
```java
// 在配置类中声明 Bean
@Bean
public DataSource dataSource() {
    return new HikariDataSource();
}
```

---

## 依赖注入

**基本写法：@Autowired 按类型注入**
`@Autowired`
```java
// 按类型自动注入
@Autowired
private UserRepository userRepository;
```

---

**基本写法：@Autowired 构造方法注入**
`@Autowired` （构造方法上方）
```java
// 推荐的构造方法注入
@Autowired
public UserService(UserRepository userRepository) {
    this.userRepository = userRepository;
}
```

---

**基本写法：@Qualifier 按名称注入**
`@Qualifier("<bean名称>")`
```java
// 指定注入的 Bean 名称
@Autowired
@Qualifier("primaryDataSource")
private DataSource dataSource;
```

---

**基本写法：@Resource 按名称注入**
`@Resource(name = "<bean名称>")`
```java
// JSR-250 标准注解
@Resource(name = "userRepository")
private UserRepository userRepository;
```

---

**基本写法：@Value 注入配置值**
`@Value("${<属性键>}")`
```java
// 注入配置文件中的值
@Value("${app.name}")
private String appName;
```

---

## 作用域

**基本写法：@Scope 单例**
`@Scope("singleton")`
```java
// 单例作用域（默认）
@Scope("singleton")
@Component
public class SingletonService { }
```

---

**基本写法：@Scope 原型**
`@Scope("prototype")`
```java
// 每次注入都创建新实例
@Scope("prototype")
@Component
public class PrototypeService { }
```

---

## AOP 切面

**基本写法：@Aspect 声明切面**
`@Aspect`
```java
// 声明切面类
@Aspect
@Component
public class LogAspect { }
```

---

**基本写法：@Pointcut 切入点**
`@Pointcut("<切入点表达式>")`
```java
// 定义切入点
@Pointcut("execution(* com.example.service.*.*(..))")
public void serviceMethods() { }
```

---

**基本写法：@Before 前置通知**
`@Before("<切入点>")`
```java
// 方法执行前执行
@Before("serviceMethods()")
public void beforeLog(JoinPoint jp) {
    System.out.println("Before: " + jp.getSignature());
}
```

---

**基本写法：@After 后置通知**
`@After("<切入点>")`
```java
// 方法执行后执行（无论是否异常）
@After("serviceMethods()")
public void afterLog() { }
```

---

**基本写法：@AfterReturning 返回通知**
`@AfterReturning(pointcut = "<切入点>", returning = "<结果变量>")`
```java
// 方法成功返回后执行
@AfterReturning(pointcut = "serviceMethods()", returning = "result")
public void afterReturning(Object result) { }
```

---

**基本写法：@AfterThrowing 异常通知**
`@AfterThrowing(pointcut = "<切入点>", throwing = "<异常变量>")`
```java
// 方法抛出异常后执行
@AfterThrowing(pointcut = "serviceMethods()", throwing = "ex")
public void afterThrowing(Exception ex) { }
```

---

**基本写法：@Around 环绕通知**
`@Around("<切入点>")`
```java
// 环绕通知（最强大）
@Around("serviceMethods()")
public Object around(ProceedingJoinPoint pjp) throws Throwable {
    long start = System.currentTimeMillis();
    Object result = pjp.proceed();
    System.out.println("Cost: " + (System.currentTimeMillis() - start));
    return result;
}
```

---

## 生命周期

**基本写法：@PostConstruct 初始化**
`@PostConstruct`
```java
// Bean 初始化完成后执行
@PostConstruct
public void init() {
    System.out.println("Initialized");
}
```

---

**基本写法：@PreDestroy 销毁前**
`@PreDestroy`
```java
// Bean 销毁前执行
@PreDestroy
public void cleanup() {
    System.out.println("Cleanup");
}
```

---

## 条件装配

**基本写法：@Conditional 条件注册**
`@Conditional(<条件类>.class)`
```java
// 满足条件才注册 Bean
@Bean
@Conditional(OnLinuxCondition.class)
public DataSource linuxDataSource() { }
```

---

**基本写法：@Profile 环境配置**
`@Profile("<环境>")`
```java
// 仅在指定环境生效
@Bean
@Profile("dev")
public DataSource devDataSource() { }
```

---

**基本写法：@ConditionalOnProperty 属性条件**
`@ConditionalOnProperty(name = "<属性>", havingValue = "<值>")`
```java
// 配置属性满足条件时注册
@Bean
@ConditionalOnProperty(name = "cache.enabled", havingValue = "true")
public CacheService cacheService() { }
```
