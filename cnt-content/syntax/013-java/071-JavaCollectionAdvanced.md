﻿# Java 集合进阶 EnumMap/IdentityHashMap/CopyOnWrite/ConcurrentHashMap 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## EnumMap 枚举映射

**基本写法：创建 EnumMap**
`new EnumMap<<枚举类型>, <值类型>>(<枚举类>.class);`
```java
// 以枚举作为键的高性能 Map
EnumMap<Color, String> map = new EnumMap<>(Color.class);
```

---

**基本写法：增改元素**
`<map>.put(<枚举键>, <值>);`
```java
// 添加或更新键值
map.put(Color.RED, "红色");
```

---

## EnumSet 枚举集合

**基本写法：包含所有枚举**
`EnumSet.allOf(<枚举类>.class);`
```java
// 创建包含全部枚举常量的集合
EnumSet<Color> all = EnumSet.allOf(Color.class);
```

---

**基本写法：指定元素集合**
`EnumSet.of(<枚举值>...);`
```java
// 创建包含指定枚举值的集合
EnumSet<Color> subset = EnumSet.of(Color.RED, Color.GREEN);
```

---

**基本写法：范围集合**
`EnumSet.range(<起>, <止>);`
```java
// 创建枚举区间集合
EnumSet<Color> range = EnumSet.range(Color.RED, Color.BLUE);
```

---

## IdentityHashMap 身份映射

**基本写法：基于引用相等创建**
`new IdentityHashMap<>();`
```java
// 使用 == 而非 equals 比较键
IdentityHashMap<String, Integer> ihm = new IdentityHashMap<>();
```

---

**基本写法：放入元素**
`<map>.put(<键>, <值>);`
```java
// 同字面量但不同对象会被视为不同键
ihm.put(new String("k"), 1);
ihm.put(new String("k"), 2); // 两个键共存
```

---

## CopyOnWriteArrayList

**基本写法：创建写时复制列表**
`new CopyOnWriteArrayList<>();`
```java
// 适合读多写少的并发场景
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
```

---

**基本写法：添加元素**
`<list>.add(<元素>);`
```java
// 每次写入都会复制底层数组
list.add("a");
```

---

**基本写法：弱一致迭代**
`<list>.iterator();`
```java
// 迭代器不会抛 ConcurrentModificationException
for (String s : list) {
    System.out.println(s);
}
```

---

## CopyOnWriteArraySet

**基本写法：创建写时复制集合**
`new CopyOnWriteArraySet<>();`
```java
// 基于 CopyOnWriteArrayList 实现的并发 Set
CopyOnWriteArraySet<String> set = new CopyOnWriteArraySet<>();
```

---

## ConcurrentHashMap

**基本写法：创建并发哈希映射**
`new ConcurrentHashMap<>();`
```java
// 线程安全的高并发哈希表
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
```

---

**基本写法：原子 absent 放入**
`<map>.putIfAbsent(<键>, <值>);`
```java
// 仅当键不存在时放入
map.putIfAbsent("k", 1);
```

---

**基本写法：原子计算**
`<map>.compute(<键>, <BiFunction>);`
```java
// 原子地重算指定键的值
map.compute("k", (k, v) -> v == null ? 1 : v + 1);
```

---

**基本写法：合并值**
`<map>.merge(<键>, <值>, <BiFunction>);`
```java
// 合并新旧值
map.merge("k", 1, Integer::sum);
```

---

**基本写法：批量遍历**
`<map>.forEach(<BiConsumer>);`
```java
// 并发安全遍历
map.forEach((k, v) -> System.out.println(k + ":" + v));
```

---

**基本写法：搜索所有条目**
`<map>.search(<并行阈值>, <BiFunction>);`
```java
// 并行搜索并返回首个非空结果
String r = map.search(2, (k, v) -> v > 1 ? k : null);
```

---

**基本写法：并行归约**
`<map>.reduce(<并行阈值>, <Mapper>, <Reducer>);`
```java
// 并行归约所有值
int sum = map.reduce(2, (k, v) -> v, Integer::sum);
```

---

## ConcurrentLinkedQueue

**基本写法：创建无界非阻塞队列**
`new ConcurrentLinkedQueue<>();`
```java
// 基于 CAS 的非阻塞并发队列
ConcurrentLinkedQueue<String> q = new ConcurrentLinkedQueue<>();
```

---

**基本写法：入队**
`<queue>.offer(<元素>);`
```java
// 非阻塞地添加到队尾
q.offer("a");
```

---

**基本写法：出队**
`<queue>.poll();`
```java
// 取出并移除队首元素，空队列返回 null
String head = q.poll();
```

---
