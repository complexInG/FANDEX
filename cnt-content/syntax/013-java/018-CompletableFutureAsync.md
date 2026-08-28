# Java CompletableFuture 异步编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 CompletableFuture

**基本写法：supplyAsync 异步执行**
`CompletableFuture.supplyAsync(<Supplier>);`
```java
// 异步执行并返回结果
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "Result";
});
```

---

**基本写法：runAsync 无返回值**
`CompletableFuture.runAsync(<Runnable>);`
```java
// 异步执行无返回值任务
CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
    System.out.println("Running");
});
```

---

**基本写法：completedFuture 已完成**
`CompletableFuture.completedFuture(<值>);`
```java
// 创建已完成的 Future
CompletableFuture<String> future = CompletableFuture.completedFuture("Done");
```

---

## 获取结果

**基本写法：get 阻塞获取**
`<future>.get();`
```java
// 阻塞等待结果
String result = future.get();
```

---

**基本写法：get 超时获取**
`<future>.get(<超时>, <时间单位>);`
```java
// 最多等待 1 秒
String result = future.get(1, TimeUnit.SECONDS);
```

---

**基本写法：join 阻塞获取（不抛受检异常）**
`<future>.join();`
```java
// 阻塞获取结果
String result = future.join();
```

---

**基本写法：getNow 立即获取**
`<future>.getNow(<默认值>);`
```java
// 未完成则返回默认值
String result = future.getNow("Default");
```

---

## 结果处理

**基本写法：thenApply 转换结果**
`<future>.thenApply(<Function>);`
```java
// 转换结果类型
CompletableFuture<Integer> next = future.thenApply(String::length);
```

---

**基本写法：thenAccept 消费结果**
`<future>.thenAccept(<Consumer>);`
```java
// 消费结果（无返回值）
CompletableFuture<Void> next = future.thenAccept(System.out::println);
```

---

**基本写法：thenRun 不使用结果**
`<future>.thenRun(<Runnable>);`
```java
// 结果完成后执行其他操作
CompletableFuture<Void> next = future.thenRun(() -> {
    System.out.println("Done");
});
```

---

## 异步组合

**基本写法：thenCompose 串联**
`<future>.thenCompose(<Function>);`
```java
// 串联两个异步任务
CompletableFuture<String> next = future.thenCompose(s -> CompletableFuture.supplyAsync(() -> s + "!"));
```

---

**基本写法：thenCombine 合并两个**
`<future>.thenCombine(<other>, <BiFunction>);`
```java
// 合并两个独立 Future 的结果
CompletableFuture<String> combined = future1.thenCombine(future2, (s1, s2) -> s1 + s2);
```

---

**基本写法：allOf 等待全部完成**
`CompletableFuture.allOf(<future1>, <future2>, ...);`
```java
// 等待所有任务完成
CompletableFuture<Void> all = CompletableFuture.allOf(f1, f2, f3);
all.join();
```

---

**基本写法：anyOf 任一完成**
`CompletableFuture.anyOf(<future1>, <future2>, ...);`
```java
// 任一任务完成即返回
CompletableFuture<Object> any = CompletableFuture.anyOf(f1, f2);
Object result = any.get();
```

---

## 异常处理

**基本写法：exceptionally 异常恢复**
`<future>.exceptionally(<Function>);`
```java
// 发生异常时返回默认值
CompletableFuture<String> safe = future.exceptionally(ex -> "Fallback");
```

---

**基本写法：handle 处理结果与异常**
`<future>.handle(<BiFunction>);`
```java
// 同时处理正常结果与异常
CompletableFuture<String> handled = future.handle((result, ex) -> {
    if (ex != null) return "Error";
    return result;
});
```

---

**基本写法：whenComplete 完成时执行**
`<future>.whenComplete(<BiConsumer>);`
```java
// 完成时执行副作用（不改变结果）
CompletableFuture<String> next = future.whenComplete((result, ex) -> {
    if (ex != null) {
        log.error("Failed", ex);
    }
});
```

---

## 线程池控制

**基本写法：指定线程池**
`CompletableFuture.supplyAsync(<Supplier>, <Executor>);`
```java
// 使用自定义线程池
ExecutorService executor = Executors.newFixedThreadPool(10);
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> "Result", executor);
```

---

**基本写法：thenApplyAsync 异步转换**
`<future>.thenApplyAsync(<Function>, [<Executor>]);`
```java
// 在默认或指定线程池中异步执行
CompletableFuture<Integer> next = future.thenApplyAsync(String::length, executor);
```

---

## 多任务编排

**基本写法：thenAcceptBoth 消费两个结果**
`<future>.thenAcceptBoth(<other>, <BiConsumer>);`
```java
// 消费两个 Future 的结果
future1.thenAcceptBoth(future2, (s1, s2) -> {
    System.out.println(s1 + s2);
});
```

---

**基本写法：runAfterBoth 都完成后执行**
`<future>.runAfterBoth(<other>, <Runnable>);`
```java
// 两个 Future 都完成后执行
future1.runAfterBoth(future2, () -> {
    System.out.println("Both done");
});
```

---

**基本写法：runAfterEither 任一完成后执行**
`<future>.runAfterEither(<other>, <Runnable>);`
```java
// 任一 Future 完成后执行
future1.runAfterEither(future2, () -> {
    System.out.println("One done");
});
```

---

**基本写法：applyToEither 取先完成的结果**
`<future>.applyToEither(<other>, <Function>);`
```java
// 取先完成的 Future 结果转换
CompletableFuture<String> next = future1.applyToEither(future2, s -> s + "!");
```
