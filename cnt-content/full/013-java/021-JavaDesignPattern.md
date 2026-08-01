---
order: 65
title: Java设计模式
module: java
category: Java
difficulty: intermediate
description: GoF设计模式Java实现
author: fanquanpp
updated: '2026-08-01'
related:
  - java/SpringBoot安全
  - java/SpringBoot数据访问
  - java/Java函数式编程
  - java/Java网络编程
prerequisites:
  - java/概述与开发环境
---

## 概述

设计模式是针对软件设计中常见问题的可复用解决方案。1994 年，四位作者（被称为 GoF，Gang of Four）在《设计模式》一书中总结了 23 种经典设计模式，分为创建型、结构型和行为型三大类。

学习设计模式的目的不是生搬硬套，而是理解每种模式解决的问题和背后的设计思想。当你遇到类似的场景时，可以快速想到合适的解决方案。过度使用设计模式会让代码变得复杂，适度使用则能让代码更灵活、更易维护。

## 基础概念

### 三大类设计模式

- **创建型**：关注对象的创建方式，将对象的创建与使用分离。包括单例、工厂方法、抽象工厂、建造者、原型
- **结构型**：关注类和对象的组合方式，形成更大的结构。包括适配器、桥接、组合、装饰器、外观、享元、代理
- **行为型**：关注对象之间的通信和职责分配。包括策略、观察者、模板方法、命令、迭代器、中介者、备忘录、状态、职责链、访问者、解释器

### 设计原则

设计模式遵循的核心原则包括：

- 开闭原则：对扩展开放，对修改关闭
- 单一职责：一个类只做一件事
- 依赖倒置：依赖抽象而非具体实现
- 里氏替换：子类可以替换父类
- 接口隔离：接口要小而专

## 快速上手

### 单例模式

确保一个类只有一个实例，并提供全局访问点：

```java
// 方式一：枚举单例（最简洁、最安全）
public enum Singleton {
    INSTANCE;

    public void doSomething() {
        System.out.println("执行单例方法");
    }
}

// 使用
Singleton.INSTANCE.doSomething();

// 方式二：双重检查锁定（延迟初始化）
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}  // 私有构造函数，防止外部实例化

    public static Singleton getInstance() {
        if (instance == null) {                  // 第一次检查（无锁）
            synchronized (Singleton.class) {
                if (instance == null) {          // 第二次检查（有锁）
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

### 工厂方法模式

定义创建对象的接口，让子类决定实例化哪个类：

```java
// 产品接口
interface Transport {
    void deliver();
}

// 具体产品
class Truck implements Transport {
    public void deliver() {
        System.out.println("卡车运输货物");
    }
}

class Ship implements Transport {
    public void deliver() {
        System.out.println("轮船运输货物");
    }
}

// 工厂接口
interface TransportFactory {
    Transport create();
}

// 具体工厂
class TruckFactory implements TransportFactory {
    public Transport create() {
        return new Truck();
    }
}

class ShipFactory implements TransportFactory {
    public Transport create() {
        return new Ship();
    }
}

// 使用
TransportFactory factory = new TruckFactory();
Transport transport = factory.create();
transport.deliver();  // 输出: 卡车运输货物
```

## 详细用法

### 1. 建造者模式

当对象有很多可选参数时，使用建造者模式可以避免构造函数参数过多：

```java
// 使用 Lombok 的 @Builder 注解可以自动生成（推荐）
// @Builder
// public class User { ... }

// 手动实现建造者
public class User {
    private final String name;    // 必填
    private final int age;        // 必填
    private final String email;   // 可选
    private final String phone;   // 可选

    private User(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
        this.email = builder.email;
        this.phone = builder.phone;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private String name;
        private int age;
        private String email;
        private String phone;

        public Builder name(String name) {
            this.name = name;
            return this;  // 返回 this 实现链式调用
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder email(String email) {
            this.email = email;
            return this;
        }

        public Builder phone(String phone) {
            this.phone = phone;
            return this;
        }

        public User build() {
            // 可以在这里添加参数校验
            if (name == null || name.isEmpty()) {
                throw new IllegalStateException("姓名不能为空");
            }
            return new User(this);
        }
    }
}

// 使用：链式调用，清晰易读
User user = User.builder()
    .name("Alice")
    .age(25)
    .email("alice@example.com")
    .build();
```

### 2. 策略模式

定义一系列算法，将每个算法封装起来，使它们可以互相替换：

```java
// 策略接口
interface PaymentStrategy {
    void pay(double amount);
}

// 具体策略
class CreditCardPayment implements PaymentStrategy {
    private String cardNumber;

    public CreditCardPayment(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public void pay(double amount) {
        System.out.println("信用卡支付: " + amount + " 元，卡号: " + cardNumber);
    }
}

class WechatPayment implements PaymentStrategy {
    public void pay(double amount) {
        System.out.println("微信支付: " + amount + " 元");
    }
}

// 上下文
class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.paymentStrategy = strategy;
    }

    public void checkout(double amount) {
        paymentStrategy.pay(amount);
    }
}

// 使用
ShoppingCart cart = new ShoppingCart();
cart.setPaymentStrategy(new CreditCardPayment("6222****1234"));
cart.checkout(99.9);  // 信用卡支付: 99.9 元

cart.setPaymentStrategy(new WechatPayment());
cart.checkout(49.9);  // 微信支付: 49.9 元
```

### 3. 观察者模式

定义对象间一对多的依赖关系，当一个对象状态改变时，所有依赖它的对象都会收到通知：

```java
import java.util.ArrayList;
import java.util.List;

// 观察者接口
interface OrderListener {
    void onOrderCreated(Order order);
}

// 被观察者
class OrderService {
    private List<OrderListener> listeners = new ArrayList<>();

    // 注册观察者
    public void addListener(OrderListener listener) {
        listeners.add(listener);
    }

    // 移除观察者
    public void removeListener(OrderListener listener) {
        listeners.remove(listener);
    }

    // 创建订单时通知所有观察者
    public void createOrder(Order order) {
        // 保存订单到数据库...
        System.out.println("订单已创建: " + order.getId());

        // 通知所有观察者
        for (OrderListener listener : listeners) {
            listener.onOrderCreated(order);
        }
    }
}

// 具体观察者
class EmailNotifier implements OrderListener {
    public void onOrderCreated(Order order) {
        System.out.println("发送邮件通知: 订单 " + order.getId() + " 已创建");
    }
}

class InventoryUpdater implements OrderListener {
    public void onOrderCreated(Order order) {
        System.out.println("更新库存: 扣减商品数量");
    }
}

// 使用
OrderService orderService = new OrderService();
orderService.addListener(new EmailNotifier());
orderService.addListener(new InventoryUpdater());
orderService.createOrder(new Order("1001"));
```

### 4. 模板方法模式

在父类中定义算法的骨架，将某些步骤延迟到子类实现：

```java
// 抽象模板类
abstract class DataProcessor {

    // 模板方法：定义处理流程的骨架（用 final 防止子类覆盖）
    public final void process() {
        readData();
        transformData();
        writeData();
    }

    // 具体方法：所有子类共用的实现
    private void readData() {
        System.out.println("读取原始数据");
    }

    // 抽象方法：由子类实现不同的转换逻辑
    protected abstract void transformData();

    // 具体方法
    private void writeData() {
        System.out.println("写入处理后的数据");
    }
}

// 具体子类
class JsonProcessor extends DataProcessor {
    @Override
    protected void transformData() {
        System.out.println("将数据转换为 JSON 格式");
    }
}

class XmlProcessor extends DataProcessor {
    @Override
    protected void transformData() {
        System.out.println("将数据转换为 XML 格式");
    }
}

// 使用
DataProcessor processor = new JsonProcessor();
processor.process();
// 输出:
// 读取原始数据
// 将数据转换为 JSON 格式
// 写入处理后的数据
```

### 5. 适配器模式

将一个类的接口转换成客户端期望的另一个接口，使原本不兼容的类可以协同工作：

```java
// 目标接口（客户端期望的接口）
interface MediaPlayer {
    void play(String filename);
}

// 已有的类（接口不兼容）
class AdvancedMediaPlayer {
    public void playVlc(String filename) {
        System.out.println("播放 VLC 文件: " + filename);
    }

    public void playMp4(String filename) {
        System.out.println("播放 MP4 文件: " + filename);
    }
}

// 适配器：将 AdvancedMediaPlayer 适配为 MediaPlayer
class MediaAdapter implements MediaPlayer {
    private AdvancedMediaPlayer advancedPlayer;

    public MediaAdapter() {
        this.advancedPlayer = new AdvancedMediaPlayer();
    }

    @Override
    public void play(String filename) {
        if (filename.endsWith(".vlc")) {
            advancedPlayer.playVlc(filename);
        } else if (filename.endsWith(".mp4")) {
            advancedPlayer.playMp4(filename);
        }
    }
}

// 使用
MediaPlayer player = new MediaAdapter();
player.play("movie.mp4");  // 播放 MP4 文件: movie.mp4
```

### 6. 装饰器模式

动态地给对象添加额外的职责，比继承更灵活：

```java
// 组件接口
interface Coffee {
    String getDescription();
    double getCost();
}

// 基础组件
class SimpleCoffee implements Coffee {
    public String getDescription() { return "普通咖啡"; }
    public double getCost() { return 10.0; }
}

// 装饰器基类
abstract class CoffeeDecorator implements Coffee {
    protected Coffee coffee;

    public CoffeeDecorator(Coffee coffee) {
        this.coffee = coffee;
    }
}

// 具体装饰器
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) { super(coffee); }
    public String getDescription() { return coffee.getDescription() + " + 牛奶"; }
    public double getCost() { return coffee.getCost() + 3.0; }
}

class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee coffee) { super(coffee); }
    public String getDescription() { return coffee.getDescription() + " + 糖"; }
    public double getCost() { return coffee.getCost() + 1.0; }
}

// 使用：可以自由组合装饰器
Coffee coffee = new SimpleCoffee();             // 普通咖啡, 10.0
coffee = new MilkDecorator(coffee);             // 普通咖啡 + 牛奶, 13.0
coffee = new SugarDecorator(coffee);            // 普通咖啡 + 牛奶 + 糖, 14.0
System.out.println(coffee.getDescription() + " = " + coffee.getCost());
```

### 7. 代理模式

为另一个对象提供替身或占位符，控制对原对象的访问：

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

// 接口
interface UserService {
    User getUser(Long id);
}

// 实际实现
class UserServiceImpl implements UserService {
    public User getUser(Long id) {
        System.out.println("从数据库查询用户: " + id);
        return new User(id, "Alice");
    }
}

// JDK 动态代理：添加缓存功能
class CacheProxy implements InvocationHandler {
    private Object target;
    private Map<String, Object> cache = new HashMap<>();

    public CacheProxy(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        String key = method.getName() + ":" + args[0];
        if (cache.containsKey(key)) {
            System.out.println("从缓存返回结果: " + key);
            return cache.get(key);
        }
        Object result = method.invoke(target, args);
        cache.put(key, result);
        return result;
    }
}

// 使用
UserService original = new UserServiceImpl();
UserService proxied = (UserService) Proxy.newProxyInstance(
    original.getClass().getClassLoader(),
    original.getClass().getInterfaces(),
    new CacheProxy(original)
);

proxied.getUser(1L);  // 从数据库查询用户: 1
proxied.getUser(1L);  // 从缓存返回结果: getUser:1
```

## 常见场景

### 场景一：Spring 中的设计模式

Spring 框架大量使用了设计模式：

- **工厂模式**：BeanFactory 和 ApplicationContext 创建 Bean
- **单例模式**：Spring Bean 默认是单例的
- **代理模式**：AOP 使用动态代理实现
- **模板方法**：JdbcTemplate、RestTemplate 等模板类
- **观察者模式**：ApplicationEvent 和 ApplicationListener
- **适配器模式**：HandlerAdapter 适配不同的 Controller

### 场景二：使用函数式接口简化策略模式

Java 8 的 Lambda 表达式可以简化很多设计模式的实现：

```java
import java.util.function.DoubleUnaryOperator;

// 用函数式接口代替策略接口
class Calculator {
    private DoubleUnaryOperator strategy;

    public Calculator(DoubleUnaryOperator strategy) {
        this.strategy = strategy;
    }

    public double calculate(double input) {
        return strategy.applyAsDouble(input);
    }
}

// 使用 Lambda 代替具体的策略类
Calculator square = new Calculator(x -> x * x);
Calculator cube = new Calculator(x -> x * x * x);

System.out.println(square.calculate(3));  // 9.0
System.out.println(cube.calculate(3));    // 27.0
```

## 注意事项与常见错误

### 不要为了用模式而用模式

设计模式是解决问题的工具，不是目标。如果一个简单的 if-else 就能解决问题，不需要引入策略模式。过度设计比没有设计更糟糕。

### 单例模式的陷阱

单例模式在测试中很难 mock，而且全局状态会导致隐式依赖。在 Spring 应用中，让 Spring 管理单例 Bean 比自己实现单例模式更好。

### 建造者模式与构造函数的选择

如果对象只有 2-3 个必填参数，直接用构造函数即可。只有当参数很多且大部分可选时，建造者模式才有价值。

### 代理模式的性能

动态代理（JDK Proxy、CGLIB）会带来微小的性能开销。在性能敏感的场景中，需要评估代理的影响。

## 进阶用法

### 事件总线（观察者模式的进阶）

在大型应用中，可以使用事件总线来解耦组件之间的通信：

```java
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.concurrent.ConcurrentHashMap;

// 简单的事件总线实现
class EventBus {
    private Map<Class<?>, List<Object>> listeners = new ConcurrentHashMap<>();

    // 注册监听器
    public <T> void register(Class<T> eventType, Object listener) {
        listeners.computeIfAbsent(eventType, k -> new ArrayList<>()).add(listener);
    }

    // 发布事件
    @SuppressWarnings("unchecked")
    public <T> void publish(T event) {
        List<Object> handlers = listeners.get(event.getClass());
        if (handlers != null) {
            for (Object handler : handlers) {
                ((java.util.function.Consumer<T>) handler).accept(event);
            }
        }
    }
}

// 使用
EventBus bus = new EventBus();
bus.register(OrderCreatedEvent.class, (OrderCreatedEvent e) -> {
    System.out.println("处理订单: " + e.getOrderId());
});
bus.publish(new OrderCreatedEvent("1001"));
```

### 组合模式

将对象组合成树形结构，统一处理单个对象和组合对象：

```java
import java.util.ArrayList;
import java.util.List;

// 组件接口
interface FileSystemComponent {
    long getSize();
    void print(String indent);
}

// 叶子节点
class File implements FileSystemComponent {
    private String name;
    private long size;

    public File(String name, long size) {
        this.name = name;
        this.size = size;
    }

    public long getSize() { return size; }
    public void print(String indent) {
        System.out.println(indent + "- " + name + " (" + size + "KB)");
    }
}

// 组合节点
class Directory implements FileSystemComponent {
    private String name;
    private List<FileSystemComponent> children = new ArrayList<>();

    public Directory(String name) { this.name = name; }

    public void add(FileSystemComponent component) {
        children.add(component);
    }

    public long getSize() {
        return children.stream().mapToLong(FileSystemComponent::getSize).sum();
    }

    public void print(String indent) {
        System.out.println(indent + "+ " + name + "/");
        for (FileSystemComponent child : children) {
            child.print(indent + "  ");
        }
    }
}

// 使用
Directory root = new Directory("项目");
root.add(new File("pom.xml", 5));
Directory src = new Directory("src");
src.add(new File("Main.java", 3));
src.add(new File("Utils.java", 2));
root.add(src);
root.print("");  // 打印目录树
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
| Java设计模式 | 021-JavaDesignPattern | 本文自身 |
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
