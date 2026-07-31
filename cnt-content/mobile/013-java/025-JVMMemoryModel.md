# Java JVM 内存模型速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 运行时数据区

**基本写法：堆内存 Heap**
`-Xmx<size>`
```java
// 所有对象实例与数组存放区域，GC 主战场
// -Xmx2g 设置最大堆为 2GB
ArrayList<String> list = new ArrayList<>();
```

---

**基本写法：方法区 Method Area**
`-XX:MaxMetaspaceSize=<size>`
```java
// 存储类元信息、常量池、静态变量（JDK 8+ 为 Metaspace）
// -XX:MaxMetaspaceSize=256m
```

---

**基本写法：虚拟机栈 VM Stack**
`-Xss<size>`
```java
// 每个线程私有，存储栈帧（局部变量、操作数栈）
// -Xss512k 设置每个线程栈大小
```

---

**基本写法：本地方法栈 Native Method Stack**
`-Xss<size>`
```java
// Native 方法调用使用，与 VM Stack 类似
```

---

**基本写法：程序计数器 PC Register**
`<线程私有>`
```java
// 当前线程执行字节码的行号指示器，线程私有无 OOM
```

---

## 堆内存分代

**基本写法：新生代 Young Generation**
`-Xmn<size>`
```java
// Eden + Survivor0 + Survivor1，对象出生地
// -Xmn512m 设置新生代大小
```

---

**基本写法：老年代 Old Generation**
`-XX:NewRatio=<ratio>`
```java
// 新生代:老年代 = 1:2（NewRatio=2 时）
// -XX:NewRatio=2
```

---

**基本写法：Eden 与 Survivor 比例**
`-XX:SurvivorRatio=<ratio>`
```java
// Eden:Survivor = 8:1:1（SurvivorRatio=8 时）
// -XX:SurvivorRatio=8
```

---

## GC 垃圾回收器

**基本写法：G1 回收器（JDK 9+ 默认）**
`-XX:+UseG1GC`
```java
// 面向大堆的 Region 化回收器
// java -XX:+UseG1GC -Xmx4g -jar app.jar
```

---

**基本写法：ZGC 低延迟回收器**
`-XX:+UseZGC`
```java
// 亚毫秒级停顿（JDK 15+ 生产可用）
// java -XX:+UseZGC -Xmx16g -jar app.jar
```

---

**基本写法：设置 GC 日志**
`-Xlog:gc*:<file>`
```java
// JDK 9+ 统一日志格式
// -Xlog:gc*:file=gc.log:time,uptime,level,tags
```

---

**基本写法：设置期望停顿时间**
`-XX:MaxGCPauseMillis=<ms>`
```java
// G1/ZGC 设置目标停顿时间
// -XX:MaxGCPauseMillis=200
```

---

## 对象生命周期

**基本写法：对象分配在 Eden**
`new <类型>()`
```java
// 新对象优先在 Eden 区分配
Object obj = new Object();
```

---

**基本写法：进入 Survivor**
`<对象> 经历 Minor GC`
```java
// Eden 满时触发 Minor GC，存活对象进入 Survivor
// 每经历一次 GC 年龄 +1
```

---

**基本写法：晋升老年代**
`-XX:MaxTenuringThreshold=<年龄>`
```java
// 对象年龄达到阈值进入老年代
// -XX:MaxTenuringThreshold=15
```

---

**基本写法：大对象直接进老年代**
`-XX:PretenureSizeThreshold=<size>`
```java
// 超过阈值的对象直接分配到老年代
// -XX:PretenureSizeThreshold=1048576（1MB）
```

---

## 内存溢出排查

**基本写法：堆 OOM 转储**
`-XX:+HeapDumpOnOutOfMemoryError`
```java
// OOM 时自动生成堆转储文件
// -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/dump.hprof
```

---

**基本写法：手动触发堆转储**
`jcmd <pid> GC.heap_dump <file>`
```java
// 运行时手动生成堆 dump
// jcmd 12345 GC.heap_dump /tmp/heap.hprof
```

---

**基本写法：jmap 查看堆概况**
`jmap -heap <pid>`
```java
// 查看堆配置与使用情况
// jmap -heap 12345
```

---

**基本写法：查看对象统计**
`jmap -histo <pid>`
```java
// 按对象大小排序统计
// jmap -histo 12345 | head -20
```

---

## 内存监控工具

**基本写法：jstat 查看 GC 统计**
`jstat -gcutil <pid> <间隔>`
```java
// 每 1 秒打印一次各区使用率
// jstat -gcutil 12345 1000
```

---

**基本写法：jcmd 列出进程命令**
`jcmd <pid> <command>`
```java
// 查看支持的命令
// jcmd 12345 help
```

---

**基本写法：JFR 录制**
`jcmd <pid> JFR.start duration=60s filename=<file>`
```java
// 录制 60 秒 Java Flight Recorder 数据
// jcmd 12345 JFR.start duration=60s filename=/tmp/rec.jfr
```

---

## 内存可见性

**基本写法：volatile 保证可见性**
`volatile <类型> <字段>`
```java
// 写入立即对其他线程可见，禁止指令重排
private volatile boolean running = true;
```

---

**基本写法：happens-before 规则**
`<线程A> happens-before <线程B>`
```java
// 锁释放 happens-before 后续锁获取
// volatile 写 happens-before 后续 volatile 读
// 线程启动 happens-before 其 run 方法
```

---

## 常用 JVM 参数

**基本写法：设置堆初始与最大值**
`-Xms<size> -Xmx<size>`
```java
// 推荐初始与最大值相同避免动态扩容
// -Xms2g -Xmx2g
```

---

**基本写法：设置元空间**
`-XX:MetaspaceSize=<size> -XX:MaxMetaspaceSize=<size>`
```java
// 元空间初始与最大值
// -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=256m
```

---

**基本写法：开启压缩指针**
`-XX:+UseCompressedOops`
```java
// 堆小于 32G 时开启可节省内存（默认开启）
// -XX:+UseCompressedOops
```

---

**基本写法：禁用偏向锁**
`-XX:-UseBiasedLocking`
```java
// JDK 15+ 弃用偏向锁，高并发场景可禁用
// -XX:-UseBiasedLocking
```

---

## 字符串常量池

**基本写法：字符串驻留**
`<string>.intern()`
```java
// 将字符串放入常量池并返回引用
String s = new String("hello").intern();
```

---

**基本写法：调整字符串表大小**
`-XX:StringTableSize=<buckets>`
```java
// 调整常量池哈希桶数量
// -XX:StringTableSize=65536
```

---

## 直接内存

**基本写法：分配直接内存**
`ByteBuffer.allocateDirect(<size>)`
```java
// 堆外内存，不受 GC 控制，NIO 使用
ByteBuffer buf = ByteBuffer.allocateDirect(1024 * 1024);
```

---

**基本写法：设置直接内存上限**
`-XX:MaxDirectMemorySize=<size>`
```java
// 限制堆外内存使用
// -XX:MaxDirectMemorySize=512m
```

---

## 类加载机制

**基本写法：双亲委派模型**
`<ClassLoader>.loadClass(<name>)`
```java
// 先委托父加载器加载，失败才自己加载
ClassLoader cl = ClassLoader.getSystemClassLoader();
Class<?> clazz = cl.loadClass("com.example.App");
```

---

**基本写法：自定义类加载器**
`extends ClassLoader`
```java
// 重写 findClass 实现自定义加载
class MyLoader extends ClassLoader {
    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        byte[] bytes = loadClassData(name);
        return defineClass(name, bytes, 0, bytes.length);
    }
}
```

---

## 内存模型三大特性

**基本写法：原子性**
`synchronized` / `AtomicInteger`
```java
// 通过锁或原子类保证操作原子性
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();
```

---

**基本写法：可见性**
`volatile` / `synchronized`
```java
// 通过 volatile 保证变量修改对所有线程可见
private volatile boolean flag = false;
```

---

**基本写法：有序性**
`volatile` / `happens-before`
```java
// volatile 写之前的操作不会被重排到写之后
private int x = 0;
private volatile boolean ready = false;
public void writer() { x = 42; ready = true; }
```
