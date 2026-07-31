# Java JVM 调优命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## jps 进程查询

**基本写法：列出 Java 进程**
`jps [-l]`
```bash
# 列出所有 Java 进程及主类全名
jps -l
```

---

**基本写法：查看 JVM 启动参数**
`jps -v`
```bash
# 显示各 Java 进程的 JVM 参数
jps -v
```

---

**基本写法：仅显示 PID**
`jps -q`
```bash
# 只输出进程 ID
jps -q
```

---

## jstat 统计监控

**基本写法：监控 GC 状态**
`jstat -gc <pid> [间隔ms] [次数]`
```bash
# 每 250ms 输出一次 GC 情况，共 4 次
jstat -gc 12345 250 4
```

---

**基本写法：监控类加载**
`jstat -class <pid>`
```bash
# 查看类加载统计
jstat -class 12345
```

---

**基本写法：带时间戳输出**
`jstat -gc -t <pid>`
```bash
# 显示程序运行时间戳的 GC 信息
jstat -gc -t 12345
```

---

**基本写法：周期性输出表头**
`jstat -gc -h<行数> <pid> <间隔>`
```bash
# 每 5 行重新输出表头
jstat -gc -h5 12345 1000
```

---

## jmap 内存映像

**基本写法：堆转储**
`jmap -dump:format=b,file=<文件名> <pid>`
```bash
# 生成堆转储 hprof 文件
jmap -dump:format=b,file=heap.hprof 12345
```

---

**基本写法：对象直方图**
`jmap -histo <pid>`
```bash
# 输出堆中对象统计直方图
jmap -histo 12345
```

---

**基本写法：仅存活对象**
`jmap -histo:live <pid>`
```bash
# 触发 GC 后统计存活对象
jmap -histo:live 12345
```

---

**基本写法：堆配置信息**
`jmap -heap <pid>`
```bash
# 查看堆内存配置和使用情况
jmap -heap 12345
```

---

## jstack 线程栈

**基本写法：导出线程栈**
`jstack <pid>`
```bash
# 输出所有线程堆栈
jstack 12345
```

---

**基本写法：检测死锁**
`jstack -l <pid>`
```bash
# 输出线程栈及锁信息
jstack -l 12345
```

---

**基本写法：强制输出**
`jstack -F <pid>`
```bash
# 进程无响应时强制输出栈
jstack -F 12345
```

---

## jcmd 诊断命令

**基本写法：列出进程**
`jcmd -l`
```bash
# 列出所有 Java 进程
jcmd -l
```

---

**基本写法：查看可用命令**
`jcmd <pid> help`
```bash
# 列出该进程支持的诊断命令
jcmd 12345 help
```

---

**基本写法：生成堆转储**
`jcmd <pid> GC.heap_dump <文件名>`
```bash
# 通过 jcmd 生成堆转储
jcmd 12345 GC.heap_dump heap.hprof
```

---

**基本写法：查看 JVM 参数**
`jcmd <pid> VM.flags`
```bash
# 查看进程实际生效的 JVM 参数
jcmd 12345 VM.flags
```

---

**基本写法：查看系统属性**
`jcmd <pid> VM.system_properties`
```bash
# 输出 JVM 系统属性
jcmd 12345 VM.system_properties
```

---

**基本写法：触发 GC**
`jcmd <pid> GC.run`
```bash
# 显式触发一次垃圾回收
jcmd 12345 GC.run
```

---

**基本写法：查看类直方图**
`jcmd <pid> GC.class_histogram`
```bash
# 输出类实例直方图
jcmd 12345 GC.class_histogram
```

---

## jinfo 配置信息

**基本写法：查看 JVM 参数**
`jinfo -flags <pid>`
```bash
# 查看进程所有 JVM 标志
jinfo -flags 12345
```

---

**基本写法：查看系统属性**
`jinfo -sysprops <pid>`
```bash
# 查看进程系统属性
jinfo -sysprops 12345
```

---

**基本写法：动态设置参数**
`jinfo -flag <名称>=<值> <pid>`
```bash
# 运行时设置布尔型 JVM 标志
jinfo -flag +PrintGCDetails 12345
```

---

## 常用 JVM 启动参数

**基本写法：设置堆大小**
`-Xms<大小> -Xmx<大小>`
```bash
# 设置初始堆和最大堆均为 2g
java -Xms2g -Xmx2g -jar app.jar
```

---

**基本写法：设置年轻代大小**
`-Xmn<大小>`
```bash
# 设置年轻代大小为 512m
java -Xmn512m -jar app.jar
```

---

**基本写法：设置元空间大小**
`-XX:MetaspaceSize=<大小> -XX:MaxMetaspaceSize=<大小>`
```bash
# 设置元空间初始和最大值
java -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=512m -jar app.jar
```

---

**基本写法：选择 GC 收集器**
`-XX:+UseG1GC`
```bash
# 启用 G1 垃圾收集器
java -XX:+UseG1GC -jar app.jar
```

---

**基本写法：启用 ZGC**
`-XX:+UseZGC`
```bash
# 启用低延迟 ZGC 收集器
java -XX:+UseZGC -jar app.jar
```

---

**基本写法：GC 日志**
`-Xlog:gc*:<文件>:time`
```bash
# JDK 9+ 统一日志输出 GC 日志
java -Xlog:gc*:gc.log:time -jar app.jar
```

---

**基本写法：堆溢出转储**
`-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=<路径>`
```bash
# OOM 时自动生成堆转储
java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/var/log/dump -jar app.jar
```

---

## JFR 飞行记录器

**基本写法：启动并录制**
`jcmd <pid> JFR.start duration=<时长>s filename=<文件>`
```bash
# 启动 60 秒的 JFR 录制
jcmd 12345 JFR.start duration=60s filename=rec.jfr
```

---

**基本写法：查看录制状态**
`jcmd <pid> JFR.check`
```bash
# 检查 JFR 录制状态
jcmd 12345 JFR.check
```

---

**基本写法：停止录制**
`jcmd <pid> JFR.stop filename=<文件>`
```bash
# 停止并保存录制
jcmd 12345 JFR.stop filename=rec.jfr
```
