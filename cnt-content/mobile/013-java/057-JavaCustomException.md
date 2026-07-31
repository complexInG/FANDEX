# Java 自定义异常语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 自定义受检异常

**基本写法：继承 Exception**
```java
public class <名称> extends Exception {
  public <名称>(String msg) { super(msg); }
  public <名称>(String msg, Throwable cause) { super(msg, cause); }
}
```
```java
// 受检异常必须声明或捕获
public class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String msg) { super(msg); }
    public InsufficientFundsException(String msg, Throwable cause) { super(msg, cause); }
}
```

---

## 自定义非受检异常

**基本写法：继承 RuntimeException**
```java
public class <名称> extends RuntimeException {
  public <名称>(String msg) { super(msg); }
}
```
```java
// 运行时异常无需声明
public class BusinessException extends RuntimeException {
    public BusinessException(String msg) { super(msg); }
    public BusinessException(String msg, Throwable cause) { super(msg, cause); }
}
```

---

## 带字段的自定义异常

**基本写法：携带业务字段**
```java
public class <名称> extends RuntimeException {
  private final <类型> <字段>;
  public <名称>(<类型> <字段>, String msg) { super(msg); this.<字段> = <字段>; }
  public <类型> get<Field>() { return <字段>; }
}
```
```java
// 异常携带错误码与上下文
public class OrderException extends RuntimeException {
    private final int code;
    public OrderException(int code, String msg) {
        super(msg);
        this.code = code;
    }
    public int getCode() { return code; }
}
```

---

## 抛出自定义异常

**基本写法：抛出异常**
`throw new <异常>(<消息>);`
```java
// 抛出自定义异常
if (balance < 0) {
    throw new BusinessException("余额不能为负");
}
```

---

**基本写法：带原因抛出**
`throw new <异常>(<消息>, <原因>);`
```java
// 包装原始异常抛出
try { ... }
catch (IOException e) { throw new BusinessException("IO 失败", e); }
```

---

## 声明受检异常

**基本写法：方法声明 throws**
`public <返回> <方法>() throws <异常1>, <异常2> {}`
```java
// 方法声明可能抛出的受检异常
public void withdraw(double amt) throws InsufficientFundsException {
    if (amt > balance) throw new InsufficientFundsException("余额不足");
}
```

---

## 异常断言

**基本写法：断言**
`assert <条件> : <消息>;`
```java
// 启用 -ea 后生效
assert amount > 0 : "金额必须大于 0";
```

---

## 异常工具方法

**基本写法：Objects.requireNonNull**
`Objects.requireNonNull(<对象>, <消息>);`
```java
// 参数非空校验
public void set(String name) {
    this.name = Objects.requireNonNull(name, "name 不能为空");
}
```

---

**基本写法：检查索引**
`Objects.checkIndex(<索引>, <长度>);`
```java
// 检查索引是否在 [0, length) 范围
int i = Objects.checkIndex(5, 10);
```

---

## 异常匹配

**基本写法：模式匹配捕获**
```java
try { ... }
catch (Throwable t) {
  if (t instanceof IOException io) { handleIO(io); }
  else if (t instanceof SQLException sql) { handleSql(sql); }
}
```
```java
// Java 16+ instanceof 模式匹配
catch (Throwable t) {
    if (t instanceof IOException io) {
        System.out.println("IO: " + io.getMessage());
    }
}
```

---
