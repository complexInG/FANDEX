# Java 原子变量 AtomicInteger/AtomicReference/LongAdder 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## AtomicInteger 原子整数

**基本写法：创建原子整数**
`new AtomicInteger(<初始值>);`
```java
// 创建初始值为 0 的原子整数
AtomicInteger ai = new AtomicInteger(0);
```

---

**基本写法：获取值**
`<ai>.get();`
```java
// 原子读取当前值
int v = ai.get();
```

---

**基本写法：设置值**
`<ai>.set(<值>);`
```java
// 原子设置新值
ai.set(10);
```

---

**基本写法：原子自增**
`<ai>.incrementAndGet();`
```java
// 先自增再获取
int v = ai.incrementAndGet();
```

---

**基本写法：原子自减**
`<ai>.decrementAndGet();`
```java
// 先自减再获取
int v = ai.decrementAndGet();
```

---

**基本写法：CAS 比较交换**
`<ai>.compareAndSet(<期望>, <新值>);`
```java
// 当值等于期望时更新
boolean ok = ai.compareAndSet(10, 20);
```

---

**基本写法：原子更新**
`<ai>.updateAndGet(<IntUnaryOperator>);`
```java
// 用函数更新值
int v = ai.updateAndGet(x -> x * 2);
```

---

**基本写法：原子累加**
`<ai>.getAndAccumulate(<增量>, <IntBinaryOperator>);`
```java
// 用函数累积并返回旧值
int old = ai.getAndAccumulate(5, Integer::sum);
```

---

## AtomicReference 原子引用

**基本写法：创建原子引用**
`new AtomicReference<<类型>>(<初始值>);`
```java
// 创建原子引用
AtomicReference<String> ref = new AtomicReference<>("init");
```

---

**基本写法：CAS 更新**
`<ref>.compareAndSet(<期望>, <新值>);`
```java
// 比较并设置
boolean ok = ref.compareAndSet("init", "new");
```

---

**基本写法：函数更新**
`<ref>.updateAndGet(<UnaryOperator>);`
```java
// 用函数更新引用
String v = ref.updateAndGet(s -> s.toUpperCase());
```

---

## AtomicStampedReference 防止 ABA

**基本写法：带版本号 CAS**
`new AtomicStampedReference<<类型>>(<初始值>, <初始版本>);`
```java
// 创建带版本戳的原子引用
AtomicStampedReference<String> ref = new AtomicStampedReference<>("a", 0);
int[] stamp = new int[1];
String cur = ref.get(stamp);
ref.compareAndSet(cur, "b", stamp[0], stamp[0] + 1);
```

---

## LongAdder 高并发累加器

**基本写法：创建累加器**
`new LongAdder();`
```java
// 高并发场景下比 AtomicLong 更高效
LongAdder adder = new LongAdder();
```

---

**基本写法：递增**
`<adder>.increment();`
```java
// 自增 1
adder.increment();
```

---

**基本写法：累加**
`<adder>.add(<值>);`
```java
// 累加指定值
adder.add(10);
```

---

**基本写法：求和**
`<adder>.sum();`
```java
// 返回当前总和
long total = adder.sum();
```

---

**基本写法：重置**
`<adder>.reset();`
```java
// 重置为 0
adder.reset();
```

---

## LongAccumulator 通用累加器

**基本写法：创建累加器**
`new LongAccumulator(<LongBinaryOperator>, <初始值>);`
```java
// 创建求最大值的累加器
LongAccumulator max = new LongAccumulator(Long::max, Long.MIN_VALUE);
```

---

**基本写法：累加**
`<acc>.accumulate(<值>);`
```java
// 用函数累加
max.accumulate(42);
```

---
