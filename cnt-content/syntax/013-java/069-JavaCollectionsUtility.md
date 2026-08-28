# Java Collections 工具类语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 排序与打乱

**基本写法：排序**
`Collections.sort(<list>);`
```java
// 对 List 自然排序
Collections.sort(list);
```

---

**基本写法：自定义排序**
`Collections.sort(<list>, <比较器>);`
```java
// 用比较器排序
Collections.sort(list, Comparator.reverseOrder());
```

---

**基本写法：打乱顺序**
`Collections.shuffle(<list>);`
```java
// 随机打乱列表
Collections.shuffle(list);
```

---

**基本写法：指定随机源**
`Collections.shuffle(<list>, <Random>);`
```java
// 用指定随机数打乱
Collections.shuffle(list, new Random(42));
```

---

**基本写法：反转**
`Collections.reverse(<list>);`
```java
// 反转列表顺序
Collections.reverse(list);
```

---

**基本写法：旋转**
`Collections.rotate(<list>, <距离>);`
```java
// 循环移动元素
Collections.rotate(list, 2);
```

---

## 查找与替换

**基本写法：二分查找**
`Collections.binarySearch(<list>, <key>);`
```java
// 在已排序列表中查找
int idx = Collections.binarySearch(sortedList, "b");
```

---

**基本写法：最大值**
`Collections.max(<collection>);`
```java
// 自然顺序最大值
String max = Collections.max(list);
```

---

**基本写法：最小值**
`Collections.min(<collection>);`
```java
// 自然顺序最小值
String min = Collections.min(list);
```

---

**基本写法：替换全部**
`Collections.replaceAll(<list>, <旧值>, <新值>);`
```java
// 把所有旧值替换为新值
Collections.replaceAll(list, "old", "new");
```

---

**基本写法：查找子列表**
`Collections.indexOfSubList(<list>, <子列表>);`
```java
// 查找子列表首次出现位置
int idx = Collections.indexOfSubList(list, sub);
```

---

**基本写法：频率**
`Collections.frequency(<collection>, <元素>);`
```java
// 统计元素出现次数
int n = Collections.frequency(list, "a");
```

---

**基本写法：不相交**
`Collections.disjoint(<c1>, <c2>);`
```java
// 判断两个集合是否无交集
boolean no = Collections.disjoint(c1, c2);
```

---

## 不可变包装

**基本写法：不可变 List**
`Collections.unmodifiableList(<list>);`
```java
// 包装为不可变 List
List<String> imm = Collections.unmodifiableList(list);
```

---

**基本写法：不可变 Set**
`Collections.unmodifiableSet(<set>);`
```java
// 包装为不可变 Set
Set<String> imm = Collections.unmodifiableSet(set);
```

---

**基本写法：不可变 Map**
`Collections.unmodifiableMap(<map>);`
```java
// 包装为不可变 Map
Map<String, Integer> imm = Collections.unmodifiableMap(map);
```

---

## 同步包装

**基本写法：同步 List**
`Collections.synchronizedList(<list>);`
```java
// 包装为线程安全 List
List<String> sync = Collections.synchronizedList(list);
```

---

**基本写法：同步 Set**
`Collections.synchronizedSet(<set>);`
```java
// 包装为线程安全 Set
Set<String> sync = Collections.synchronizedSet(set);
```

---

**基本写法：同步 Map**
`Collections.synchronizedMap(<map>);`
```java
// 包装为线程安全 Map
Map<String, Integer> sync = Collections.synchronizedMap(map);
```

---

## 类型检查视图

**基本写法：类型检查 List**
`Collections.checkedList(<list>, <元素类>);`
```java
// 运行时类型检查防止污染
List<String> safe = Collections.checkedList(new ArrayList<>(), String.class);
```

---

## 空与单例集合

**基本写法：空列表**
`Collections.emptyList();`
```java
// 返回不可变空 List
List<String> empty = Collections.emptyList();
```

---

**基本写法：单例列表**
`Collections.singletonList(<元素>);`
```java
// 只含一个元素的不可变 List
List<String> one = Collections.singletonList("a");
```

---

**基本写法：单例 Set**
`Collections.singleton(<元素>);`
```java
// 只含一个元素的不可变 Set
Set<String> one = Collections.singleton("a");
```

---

**基本写法：单例 Map**
`Collections.singletonMap(<键>, <值>);`
```java
// 只含一个键值对的不可变 Map
Map<String, Integer> one = Collections.singletonMap("k", 1);
```

---

## 添加元素

**基本写法：添加全部**
`Collections.addAll(<collection>, <元素>...);`
```java
// 批量添加元素
Collections.addAll(list, "a", "b", "c");
```

---

## 不可变集合工厂

**基本写法：List.of**
`List.of(<元素>...);`
```java
// Java 9+ 创建不可变 List
List<String> imm = List.of("a", "b");
```

---

**基本写法：Set.of**
`Set.of(<元素>...);`
```java
// Java 9+ 创建不可变 Set
Set<String> imm = Set.of("a", "b");
```

---

**基本写法：Map.of**
`Map.of(<键1>, <值1>, <键2>, <值2>);`
```java
// Java 9+ 创建不可变 Map
Map<String, Integer> imm = Map.of("a", 1, "b", 2);
```

---

**基本写法：Map.entry**
`Map.entry(<键>, <值>);`
```java
// 创建不可变 entry
Map.Entry<String, Integer> e = Map.entry("k", 1);
Map<String, Integer> m = Map.ofEntries(e);
```

---
