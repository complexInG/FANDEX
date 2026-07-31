# Java ThreadLocal 与内存泄漏

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 ThreadLocal

**基本写法：创建 ThreadLocal**
`ThreadLocal.<类型>withInitial(() -> <初始值>);`
```java
// 创建带初始值的 ThreadLocal
ThreadLocal<Integer> counter = ThreadLocal.withInitial(() -> 0);
```

---

**基本写法：匿名内部类创建**
`new ThreadLocal<<类型>>() { protected <类型> initialValue() {} }`
```java
// 重写 initialValue 创建
ThreadLocal<List<String>> ctx = new ThreadLocal<>() {
    @Override
    protected List<String> initialValue() { return new ArrayList<>(); }
};
```

---

## 读写操作

**基本写法：设置值**
`<threadLocal>.set(<值>);`
```java
// 为当前线程设置值
counter.set(10);
```

---

**基本写法：获取值**
`<threadLocal>.get();`
```java
// 获取当前线程的值
int v = counter.get();
```

---

**基本写法：移除值**
`<threadLocal>.remove();`
```java
// 移除当前线程的值，防止内存泄漏
counter.remove();
```

---

## InheritableThreadLocal 子线程继承

**基本写法：创建可继承 ThreadLocal**
`new InheritableThreadLocal<<类型>>();`
```java
// 子线程可继承父线程的值
InheritableThreadLocal<String> itl = new InheritableThreadLocal<>();
itl.set("parent");
```

---

**基本写法：自定义子线程值**
`new InheritableThreadLocal<<类型>>() { protected <类型> childValue(<类型> p) {} }`
```java
// 子线程继承时对值做转换
InheritableThreadLocal<String> itl = new InheritableThreadLocal<>() {
    @Override
    protected String childValue(String parent) { return parent + "-child"; }
};
```

---

## TransmittableThreadLocal 跨线程池传递

**基本写法：使用 TransmittableThreadLocal（阿里 TTL 库）**
`new TransmittableThreadLocal<<类型>>();`
```java
// 线程池场景下传递上下文
TransmittableThreadLocal<String> ttl = new TransmittableThreadLocal<>();
ttl.set("ctx");
```

---

**基本写法：包装 Runnable**
`TtlRunnable.get(<runnable>);`
```java
// 提交任务时包装以传递上下文
executor.submit(TtlRunnable.get(() -> doWork(ttl.get())));
```

---

## ScopedValue（Java 21+ 预览）

**基本写法：创建 ScopedValue**
`private static final ScopedValue<<类型>> NAME = ScopedValue.newInstance();`
```java
// 创建不可变作用域值
static final ScopedValue<String> USER = ScopedValue.newInstance();
```

---

**基本写法：绑定并执行**
`ScopedValue.where(<sv>, <值>).run(() -> <方法>);`
```java
// 在作用域内绑定值并执行
ScopedValue.where(USER, "Alice").run(() -> {
    System.out.println(USER.get());
});
```

---

**基本写法：返回结果**
`ScopedValue.where(<sv>, <值>).call(() -> <表达式>);`
```java
// 作用域内执行并返回值
String r = ScopedValue.where(USER, "Alice").call(() -> "hello " + USER.get());
```

---

## 内存泄漏原理与排查

**基本写法：try-finally 清理**
`try { <tl>.set(<值>); ... } finally { <tl>.remove(); }`
```java
// 标准清理模式防止线程池泄漏
try {
    ctx.set(request);
    handle();
} finally {
    ctx.remove();
}
```

---

## 与线程池配合

**基本写法：装饰 Runnable 自动清理**
`Runnable wrapped = () -> { try { <tl>.set(v); run(); } finally { <tl>.remove(); } };`
```java
// 线程池任务包装自动清理 ThreadLocal
Runnable task = () -> {
    try { counter.set(1); doWork(); }
    finally { counter.remove(); }
};
```

---

## ThreadLocalRandom 随机数

**基本写法：获取当前线程随机数**
`ThreadLocalRandom.current().nextInt(<上界>);`
```java
// 线程本地随机数生成器
int n = ThreadLocalRandom.current().nextInt(100);
```

---

**基本写法：指定范围**
`ThreadLocalRandom.current().nextInt(<起>, <止>);`
```java
// 生成区间内随机数
int n = ThreadLocalRandom.current().nextInt(10, 20);
```

---

## ThreadLocal 与虚拟线程

**基本写法：虚拟线程下使用 ThreadLocal**
`Thread.ofVirtual().start(() -> { <tl>.set(v); ... });`
```java
// 虚拟线程下使用 ThreadLocal（不推荐大量使用）
Thread.ofVirtual().start(() -> {
    ctx.set("v");
    try { work(); } finally { ctx.remove(); }
});
```
