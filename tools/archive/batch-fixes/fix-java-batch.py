# -*- coding: utf-8 -*-
"""批量修复 013-java 下多个文件的 ASCII 图表。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\013-java")


def replace_block(path: pathlib.Path, marker: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx < 0:
        return False
    start = text.rfind("```", 0, idx)
    end = text.find("```", idx)
    if start < 0 or end < 0 or end < start:
        return False
    end += 3
    path.write_text(text[:start] + new + text[end:], encoding="utf-8")
    return True


results = []

# 051 CompletableFutureAsync：分层架构
p = ROOT / "051-CompletableFutureAsync.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    API[API 层（Controller）<br/>接收请求，返回 CompletableFuture&lt;Response&gt;] --> SVC[Service 层<br/>业务编排：thenCompose / thenCombine / allOf<br/>异常恢复：exceptionally / handle<br/>超时控制：orTimeout / completeOnTimeout]\n"
    "    SVC --> CL[Client 层（HTTP / DB / Redis）<br/>异步调用：supplyAsync(阻塞调用, ioPool)<br/>重试机制：exceptionallyCompose]\n"
    "    CL --> EX[Executor 层<br/>ioPool：IO 密集（200 线程）<br/>cpuPool：CPU 密集（N-1 线程）<br/>virtualThreadPool：JDK 21+ 虚拟线程]\n"
    "```"
)
results.append(("051-completable", replace_block(p, "API 层（Controller）", new)))

# 053 ReflectionDynamicProxy：时间线
p = ROOT / "053-ReflectionDynamicProxy.md"
new = (
    "```mermaid\ntimeline\n"
    "    title Java 反射发展时间线\n"
    "    1995: Java 1.0：无反射，仅通过 new 创建对象\n"
    "    1997: Java 1.1：引入反射 API（java.lang.reflect），Class.forName/getMethod/invoke，支持 JavaBeans、IDE 可视化设计\n"
    "    2002: J2SE 1.4：动态代理（java.lang.reflect.Proxy），支持 EJB、RMI stub 生成\n"
    "    2004: Java 5：泛型 + 注解，反射 API 支持泛型类型擦除信息，Annotation 反射读取\n"
    "    2006: Java 6：JAX-WS、JAXB 大量使用动态代理，ScriptEngine（JSR 223）通过反射调用脚本\n"
    "    2011: Java 7：invokedynamic + MethodHandle（JSR 292），Lambda 底层基于 invokedynamic\n"
    "    2014: Java 8：Lambda + MethodHandle，LambdaMetafactory 基于 invokedynamic，反射性能优化\n"
    "    2017: Java 9：模块系统，反射受模块封装限制（--add-opens）\n"
    "    2018: Java 11：VarHandle（JEP 193）替代 sun.misc.Unsafe 的字段访问\n"
    "    2021: Java 17：密封类、模式匹配，反射 API 支持 sealed 修饰符\n"
    "    2023: Java 21：虚拟线程，反射调用与虚拟线程兼容，Foreign Function & Memory API（FFM）\n"
    "    2024-2025: Java 22-25：进一步限制反射的非法访问，强封装（Strong Encapsulation by Default）\n"
    "```"
)
results.append(("053-reflection-timeline", replace_block(p, "1995 ──── Java 1.0", new)))

# 054 AnnotationProcessor：编译流程
p = ROOT / "054-AnnotationProcessor.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    A[源码读入] --> B[parse → AST（JCCompilationUnit）]\n"
    "    B --> C[enter → 符号表填充（Symbol）]\n"
    "    C --> D[Annotation Processing（JSR 269）<br/>调用 Processor.process<br/>生成的新源码加入下一轮<br/>重复直到无新源码]\n"
    "    D --> E[attribute → 类型检查 / 语义分析]\n"
    "    E --> F[flow → 数据流分析<br/>definite assignment, unreachable]\n"
    "    F --> G[desugar → Lambda → invokedynamic, 泛型擦除]\n"
    "    G --> H[gen → 字节码生成（.class）]\n"
    "```"
)
results.append(("054-annotation", replace_block(p, "源码读入", new)))

# 056 OOP：student 引用
p = ROOT / "056-OOP.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Stack[栈]\n"
    "        S[student]\n"
    "    end\n"
    "    subgraph Heap[堆]\n"
    "        O[name: null / age: 0 / major: null]\n"
    "    end\n"
    "    S --> O\n"
    "```"
)
results.append(("056-oop", replace_block(p, "│ age: 0 │", new)))

# 060 IOStream：流体系
p = ROOT / "060-IOStreamFileOperation.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    Byte[字节流] --> BI[InputStream]\n"
    "    Byte --> BO[OutputStream]\n"
    "    BI --> B1[FileInputStream]\n"
    "    BI --> B2[ByteArrayInputStream]\n"
    "    BI --> B3[BufferedInputStream]\n"
    "    BO --> B4[FileOutputStream]\n"
    "    BO --> B5[ByteArrayOutputStream]\n"
    "    BO --> B6[BufferedOutputStream]\n"
    "    Char[字符流] --> CI[Reader]\n"
    "    Char --> CO[Writer]\n"
    "    CI --> C1[FileReader]\n"
    "    CI --> C2[CharArrayReader]\n"
    "    CI --> C3[BufferedReader]\n"
    "    CO --> C4[FileWriter]\n"
    "    CO --> C5[CharArrayWriter]\n"
    "    CO --> C6[BufferedWriter]\n"
    "    Conv[转换流] --> CV1[InputStreamReader]\n"
    "    Conv --> CV2[OutputStreamWriter]\n"
    "    Obj[对象流] --> O1[ObjectInputStream]\n"
    "    Obj --> O2[ObjectOutputStream]\n"
    "```"
)
results.append(("060-io", replace_block(p, "InputStream │ OutputStream", new)))

# 061 Multithreading：线程状态机
p = ROOT / "061-MultithreadingBasics.md"
new = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> NEW\n"
    "    NEW --> RUNNABLE\n"
    "    RUNNABLE --> RUNNING\n"
    "    RUNNING --> WAITING: await() / wait() / join()\n"
    "    RUNNING --> TIMED_WAITING: sleep(timeout) / wait(timeout) / join(timeout)\n"
    "    RUNNING --> BLOCKED: 获取锁失败\n"
    "    WAITING --> RUNNABLE: 锁释放/通知\n"
    "    TIMED_WAITING --> RUNNABLE: 超时/唤醒\n"
    "    BLOCKED --> RUNNABLE: 获得锁\n"
    "    RUNNING --> TERMINATED\n"
    "    TERMINATED --> [*]\n"
    "```"
)
results.append(("061-thread-state", replace_block(p, "NEW │", new)))

# 062 JVMMemoryModel：堆布局
p = ROOT / "062-JVMMemoryModel.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Heap[Heap]\n"
    "        subgraph Young[Young Generation 1/3 heap]\n"
    "            Eden[Eden 80% young]\n"
    "            S0[Survivor 0 10% young]\n"
    "            S1[Survivor 1 10% young]\n"
    "        end\n"
    "        Old[Old Gen 2/3 heap]\n"
    "    end\n"
    "    Eden --> S0\n"
    "    S0 --> S1\n"
    "    S1 --> Old\n"
    "```"
)
results.append(("062-heap", replace_block(p, "Heap ─", new)))

# 062 JVMMemoryModel：栈帧
p = ROOT / "062-JVMMemoryModel.md"
new2 = (
    "```mermaid\nflowchart TD\n"
    "    Frame[栈帧 Stack Frame]\n"
    "    Frame --> LV[局部变量表<br/>this（非静态方法）<br/>方法参数<br/>方法内局部变量<br/>long/double 占 2 槽]\n"
    "    Frame --> OS[操作数栈<br/>字节码指令的工作区<br/>iadd/imul/invoke 用的栈]\n"
    "    Frame --> DL[动态链接<br/>指向运行时常量池的方法引用]\n"
    "    Frame --> RA[方法返回地址<br/>正常返回：调用者的 PC<br/>异常返回：异常表查找]\n"
    "```"
)
results.append(("062-stackframe", replace_block(p, "栈帧 (Stack Frame)", new2)))

# 062 JVMMemoryModel：对象布局
p = ROOT / "062-JVMMemoryModel.md"
new3 = (
    "```mermaid\nflowchart TD\n"
    "    Obj[对象 Object]\n"
    "    Obj --> OH[对象头 Object Header]\n"
    "    OH --> MW[Mark Word 64 bits<br/>hash、age、锁状态、GC 标记]\n"
    "    OH --> CP[Class Pointer 32/64 bits<br/>开启压缩为 32 位]\n"
    "    Obj --> ID[实例数据<br/>父类字段在前，子类字段在后<br/>相同宽度字段分配在一起<br/>字段对齐（8 字节边界）]\n"
    "    Obj --> PD[对齐填充<br/>对象起始地址 8 字节对齐]\n"
    "```"
)
results.append(("062-object", replace_block(p, "对象头 (Object Header)", new3)))

# 062 JVMMemoryModel：Mark Word 状态表
p = ROOT / "062-JVMMemoryModel.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    MW[Mark Word（64 bits）]\n"
    "    MW --> U[无锁：hash(25) / age(4) / 0 / 01]\n"
    "    MW --> B[偏向锁：thread(54) / epoch(2) / 1 / 01]\n"
    "    MW --> L[轻量锁：ptr_to_lock_record(62) / 00]\n"
    "    MW --> H[重量锁：ptr_to_heavy_monitor(62) / 10]\n"
    "    MW --> G[GC 标记：- / 11]\n"
    "```\n\n"
    "字段说明：\n"
    "- hash：对象 hashCode（延迟计算，调用 System.identityHashCode 后填充）\n"
    "- age：对象年龄（经历 Minor GC 次数，默认晋升阈值为 15）\n"
    "- thread：偏向线程 ID\n"
    "- epoch：偏向时间戳（用于批量撤销）\n"
    "- ptr_to_lock_record：指向线程栈中 Lock Record 的指针\n"
    "- ptr_to_heavy_monitor：指向 ObjectMonitor 的指针"
)
results.append(("062-markword", replace_block(p, "Mark Word (64 bits)", new4)))

# 062 JVMMemoryModel：新生代布局
p = ROOT / "062-JVMMemoryModel.md"
new5 = (
    "```mermaid\nflowchart LR\n"
    "    Eden[Eden<br/>80% of young] --- S0[Survivor 0<br/>10% young] --- S1[Survivor 1<br/>10% young]\n"
    "```"
)
results.append(("062-young", replace_block(p, "Eden        │  Survivor 0", new5)))

# 062 JVMMemoryModel：标记-清除
p = ROOT / "062-JVMMemoryModel.md"
new6 = (
    "```mermaid\nflowchart TD\n"
    "    A[标记前：占用块 + 空闲碎片] --> B[清除后：碎片残留]\n"
    "```"
)
results.append(("062-mark-sweep", replace_block(p, "标记前", new6)))

# 062 JVMMemoryModel：复制
p = ROOT / "062-JVMMemoryModel.md"
new7 = (
    "```mermaid\nflowchart TD\n"
    "    A[使用区 + 空闲区] --> B[复制后：紧凑排列]\n"
    "```"
)
results.append(("062-copy", replace_block(p, "使用区  空闲区", new7)))

# 062 JVMMemoryModel：标记-整理
p = ROOT / "062-JVMMemoryModel.md"
new8 = (
    "```mermaid\nflowchart TD\n"
    "    A[标记前：占用块 + 空闲区] --> B[整理后：无碎片]\n"
    "```"
)
results.append(("062-mark-compact", replace_block(p, "整理后（无碎片）", new8)))

# 062 JVMMemoryModel：G1 布局
p = ROOT / "062-JVMMemoryModel.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    G1[G1 Heap Layout<br/>Region（1-32MB）]\n"
    "    G1 --> R1[E / S / O / E / H / H / O / O]\n"
    "    G1 --> R2[O / E / O / S / O / E / O / -]\n"
    "    G1 --> R3[- / O / E / O / O / - / S / E]\n"
    "    Legend[E: Eden　S: Survivor　O: Old　H: Humongous　-: Free]\n"
    "```"
)
results.append(("062-g1", replace_block(p, "G1 Heap Layout", new9)))

# 062 JVMMemoryModel：ZGC 着色指针
p = ROOT / "062-JVMMemoryModel.md"
new10 = (
    "```mermaid\nflowchart LR\n"
    "    Color[4 bits Color] --- Addr[42 bits Address] --- Unused[18 bits Unused]\n"
    "```\n\n"
    "颜色位（4 bits）：\n"
    "- Marked0 (M0)：标记阶段 0\n"
    "- Marked1 (M1)：标记阶段 1\n"
    "- Remapped：转移完成\n"
    "- Finalizable：finalizer 可达"
)
results.append(("062-zgc-ptr", replace_block(p, "ZGC Colored Pointer", new10)))

# 062 JVMMemoryModel：ZGC 分代堆
p = ROOT / "062-JVMMemoryModel.md"
new11 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Heap[ZGC Generational Heap]\n"
    "        Young[Young Generation<br/>Small, frequent]\n"
    "        Old[Old Generation<br/>Large, infrequent GC]\n"
    "    end\n"
    "    Young --> YE[Eden]\n"
    "    Young --> YS[Survivor]\n"
    "    Old --> OR[Old Region]\n"
    "```"
)
results.append(("062-zgc-heap", replace_block(p, "ZGC Generational Heap", new11)))

# 065 SpringBootNotes：时间线
p = ROOT / "065-SpringBootNotes.md"
new12 = (
    "```mermaid\ntimeline\n"
    "    title Spring Boot 发展时间线\n"
    "    2002-2012: Spring Framework 兴起，配置冗长（XML 数千行），Rod Johnson《Expert One-on-One J2EE Development without EJB》\n"
    "    2013: Spring Boot 项目启动，Mike Youngstrom 提出约定优于配置，Phil Webb、Dave Syer 主导开发\n"
    "    2014: Spring Boot 1.0 GA（4 月），内嵌 Tomcat/Jetty，起步依赖，自动配置\n"
    "    2016: Spring Boot 1.4：Actuator 完善、@SpringBootTest\n"
    "    2018: Spring Boot 2.0 GA（3 月），基于 Spring Framework 5，响应式编程（WebFlux），Java 8+ 最低要求\n"
    "    2019: Spring Boot 2.1：Micrometer 集成、Java 11 支持\n"
    "    2020: Spring Boot 2.3：优雅停机、Docker 分层 JAR；2.4：配置文件重写（spring.config.import）\n"
    "    2022: Spring Boot 3.0 GA（11 月），基于 Spring Framework 6，Jakarta EE 9+，GraalVM Native Image（AOT），Java 17 最低要求，Micrometer Tracing\n"
    "    2023: Spring Boot 3.1：Docker Compose 支持、ConnectionDetails 抽象；3.2：虚拟线程、JVM Checkpoint Restore（CRaC）\n"
    "    2024: Spring Boot 3.3：Native Image 优化、structured logging、Packet Capture\n"
    "    2025: Spring Boot 3.4 / 4.0 路线图，HTTP Interface Client 增强，更深入 AOT 优化\n"
    "```"
)
results.append(("065-spring-timeline", replace_block(p, "Spring Framework 兴起", new12)))

for name, ok in results:
    print(f"{name}: {ok}")
