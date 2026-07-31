# Java 日志 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## JUL java.util.logging

**基本写法：获取 Logger**
`Logger.getLogger("<名称>");`
```java
// 获取 JDK 内置 Logger
Logger log = Logger.getLogger("com.example.App");
```

---

**基本写法：日志级别**
`<logger>.info("<消息>");`
```java
// 输出 INFO 级别日志
log.info("started");
```

---

**基本写法：带异常**
`<logger>.log(<级别>, "<消息>", <异常>);`
```java
// 输出异常堆栈
log.log(Level.SEVERE, "error", e);
```

---

**基本写法：设置级别**
`<logger>.setLevel(<级别>);`
```java
// 设置日志级别
log.setLevel(Level.FINE);
```

---

**基本写法：配置 ConsoleHandler**
`ConsoleHandler h = new ConsoleHandler(); h.setLevel(<级别>);`
```java
// 配置控制台处理器级别
ConsoleHandler h = new ConsoleHandler();
h.setLevel(Level.ALL);
log.addHandler(h);
```

---

## SLF4J 门面

**基本写法：通过 LoggerFactory 获取**
`LoggerFactory.getLogger(<类>.class);`
```java
// 使用 SLF4J 获取 Logger
Logger log = LoggerFactory.getLogger(App.class);
```

---

**基本写法：占位符日志**
`<logger>.info("<模板>", <参数>...);`
```java
// 占位符方式输出
log.info("user={} age={}", name, age);
```

---

**基本写法：异常日志**
`<logger>.error("<消息>", <异常>);`
```java
// 最后一个参数为异常
log.error("failed", e);
```

---

**基本写法：MDC 上下文**
`MDC.put("<键>", <值>);`
```java
// 设置诊断上下文
MDC.put("traceId", "abc123");
```

---

**基本写法：移除 MDC**
`MDC.remove("<键>");`
```java
// 清理上下文避免泄漏
MDC.remove("traceId");
```

---

## Logback 配置

**基本写法：logback.xml 控制台输出**
`<appender class="ch.qos.logback.core.ConsoleAppender">`
```xml
<!-- 控制台输出配置 -->
<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
  <encoder>
    <pattern>%d{HH:mm:ss} %-5level %logger{20} - %msg%n</pattern>
  </encoder>
</appender>
```

---

**基本写法：滚动文件输出**
`<appender class="ch.qos.logback.core.rolling.RollingFileAppender">`
```xml
<!-- 按日期滚动文件 -->
<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
  <file>app.log</file>
  <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <fileNamePattern>app.%d{yyyy-MM-dd}.log</fileNamePattern>
    <maxHistory>30</maxHistory>
  </rollingPolicy>
  <encoder><pattern>%msg%n</pattern></encoder>
</appender>
```

---

**基本写法：设置 Logger 级别**
`<logger name="<包名>" level="<级别>"/>`
```xml
<!-- 为指定包设置级别 -->
<logger name="com.example" level="DEBUG"/>
<root level="INFO">
  <appender-ref ref="STDOUT"/>
</root>
```

---

## Log4j2 配置

**基本写法：log4j2.xml Configuration**
`<Configuration status="WARN">`
```xml
<!-- Log4j2 根配置 -->
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d %p %c - %m%n"/>
    </Console>
  </Appenders>
</Configuration>
```

---

**基本写法：Loggers 配置**
`<Loggers> <Logger name="<包>" level="<级别>"/> <Root level="<级别>">`
```xml
<!-- 日志器与根配置 -->
<Loggers>
  <Logger name="com.example" level="debug" additivity="false">
    <AppenderRef ref="Console"/>
  </Logger>
  <Root level="info">
    <AppenderRef ref="Console"/>
  </Root>
</Loggers>
```

---

## System.Logger（Java 9+）

**基本写法：获取 SystemLogger**
`System.getLogger("<名称>");`
```java
// JDK 9+ 统一日志门面
System.Logger log = System.getLogger("app");
```

---

**基本写法：记录日志**
`<logger>.log(<级别>, "<消息>");`
```java
// 通过 System.Logger 输出
log.log(System.Logger.Level.INFO, "started");
```

---

**基本写法：带 Supplier 延迟求值**
`<logger>.log(<级别>, <Supplier>);`
```java
// 仅当日志级别开启时求值
log.log(System.Logger.Level.DEBUG, () -> "expensive: " + compute());
```

---

## 异步日志

**基本写法：Log4j2 异步配置**
`<AsyncLogger name="<包>" level="<级别>"/>`
```xml
<!-- 全异步日志提升性能 -->
<Loggers>
  <AsyncLogger name="com.example" level="info"/>
  <AsyncRoot level="info">
    <AppenderRef ref="Console"/>
  </AsyncRoot>
</Loggers>
```

---

## Logback AsyncAppender

**基本写法：包装异步**
`<appender class="ch.qos.logback.classic.AsyncAppender">`
```xml
<!-- 异步 Appender 包装 -->
<appender name="ASYNC" class="ch.qos.logback.classic.AsyncAppender">
  <appender-ref ref="FILE"/>
  <queueSize>1024</queueSize>
  <neverBlock>true</neverBlock>
</appender>
```

---

## 结构化日志（JSON）

**基本写法：Logback JSON 编码器**
`<encoder class="net.logstash.logback.encoder.LogstashEncoder">`
```xml
<!-- 输出 JSON 格式日志 -->
<appender name="JSON" class="ch.qos.logback.core.ConsoleAppender">
  <encoder class="net.logstash.logback.encoder.LogstashEncoder"/>
</appender>
```

---

## 日志参数化最佳实践

**基本写法：避免字符串拼接**
`<logger>.debug("<模板>", <参数>);`
```java
// 使用占位符而非字符串拼接
log.debug("value={}", value);
```

---

**基本写法：惰性求值**
`if (<logger>.isDebugEnabled()) { <logger>.debug(<计算>); }`
```java
// 开销大时先判断级别
if (log.isDebugEnabled()) {
    log.debug("data={}", expensiveSerialize());
}
```
