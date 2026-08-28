# Kotlin kotlinc 编译命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本编译

**基本写法：编译单文件**
`kotlinc <源文件> -include-runtime -d <输出jar>`
```bash
# 编译并打包为可执行 jar，附带运行时
kotlinc Main.kt -include-runtime -d app.jar
```

---

**基本写法：运行 jar**
`java -jar <jar文件>`
```bash
# 运行上一步生成的 jar
java -jar app.jar
```

---

**基本写法：编译模块**
`kotlinc <模块名> -include-runtime -d <输出>`
```bash
# 编译整个模块目录
kotlinc src/main/kotlin -include-runtime -d app.jar
```

---

**基本写法：仅编译不打包**
`kotlinc <源> -d <输出目录>`
```bash
# 输出 .class 文件到目录
kotlinc Main.kt -d out
```

---

## 输出目标

**基本写法：指定 JVM 版本**
`kotlinc -jvm-target <版本> -d <输出>`
```bash
# 指定生成的字节码版本
kotlinc Main.kt -jvm-target 21 -d app.jar
```

---

**基本写法：编译为 JavaScript**
`kotlinc -js <源文件> -output <输出js>`
```bash
# 编译为 JavaScript 文件
kotlinc -js Main.kt -output app.js
```

---

**基本写法：编译为 Native 二进制**
`kotlinc-native <源文件> -o <输出名>`
```bash
# 编译为 Kotlin/Native 可执行文件
kotlinc-native Main.kt -o app
```

---

**基本写法：生成 IR**
`kotlinc -js -ir <源> -output <输出>`
```bash
# 使用新 IR 编译器后端
kotlinc -js -ir Main.kt -output app.js
```

---

## 脚本与 REPL

**基本写法：启动 REPL**
`kotlinc`
```bash
# 进入 Kotlin 交互式 REPL
kotlinc
```

---

**基本写法：执行脚本**
`kotlinc -script <脚本.kts> [参数]`
```bash
# 执行 .kts 脚本文件
kotlinc -script build.kts release
```

---

**基本写法：交互式求值**
`kotlinc -e "<代码>"`
```bash
# 直接执行单段代码
kotlinc -e "println(1 + 2)"
```

---

## 依赖与类路径

**基本写法：指定类路径**
`kotlinc -cp <类路径> <源> -d <输出>`
```bash
# 引入 jar 依赖
kotlinc -cp "lib/*" Main.kt -d app.jar
```

---

**基本写法：模块路径**
`kotlinc -module-path <路径> <源>`
```bash
# Java 模块系统支持
kotlinc -module-path mods Main.kt -d out
```

---

**基本写法：生成 Java 模块**
`kotlinc --java-module-path <路径> -d <输出>`
```bash
# 输出 JPMS 兼容模块
kotlinc -module-path mods -java-module-name com.example -d out
```

---

## 编译选项

**基本写法：开启严格可空性**
`kotlinc -Xjsr305=strict <源>`
```bash
# 严格 JSR-305 可空检查
kotlinc -Xjsr305=strict Main.kt -d out
```

---

**基本写法：启用 expect/actual**
`kotlinc -Xmulti-platform <源>`
```bash
# 多平台项目编译
kotlinc -Xmulti-platform commonMain -d out
```

---

**基本写法：开启进阶优化**
`kotlinc -Xopt=kotlin.classes.aligned <源>`
```bash
# 启用特定优化
kotlinc -Xopt=kotlin.classes.aligned Main.kt -d out
```

---

**基本写法：禁用内联**
`kotlinc -Xinline-classes=<模式>`
```bash
# 控制内联类生成
kotlinc -Xinline-classes=true Main.kt -d out
```

---

## 反编译与文档

**基本写法：生成 Kotlin 文档**
`kotlinx-javadoc <源>`
```bash
# 使用 Dokka 生成文档（推荐）
./gradlew dokkaHtml
```

---

**基本写法：反编译查看字节码**
`javap -p -c <class文件>`
```bash
# 查看编译产物字节码
javap -p -c out/Main.class
```

---

## Gradle Kotlin 编译任务

**基本写法：编译命令**
`./gradlew compileKotlin`
```bash
# 触发 Kotlin 编译任务
./gradlew compileKotlin
```

---

**基本写法：编译多平台**
`./gradlew compileKotlinJvm compileKotlinJs`
```bash
# 编译指定目标
./gradlew compileKotlinJvm
./gradlew compileKotlinWasmJs
```

---

**基本写法：增量编译**
`./gradlew compileKotlin -Pkotlin.incremental=true`
```bash
# 启用增量编译（默认开启）
./gradlew compileKotlin --info
```

---

**基本写法：守护进程编译**
`./gradlew compileKotlin --daemon`
```bash
# 使用 Gradle 守护进程加速
./gradlew compileKotlin --daemon
```

---

## Maven Kotlin 编译

**基本写法：Maven 编译**
`mvn compile`
```bash
# 通过 kotlin-maven-plugin 编译
mvn compile
```

---

**基本写法：指定 Kotlin 版本**
`mvn -Dkotlin.version=2.1.0 compile`
```bash
# 覆盖 Kotlin 版本
mvn -Dkotlin.version=2.1.0 compile
```

---

## 调试与诊断

**基本写法：输出编译时间**
`kotlinc --verbose <源>`
```bash
# 详细编译信息
kotlinc --verbose Main.kt -d out
```

---

**基本写法：输出 K2 警告**
`kotlinc -Xrender-internal-diagnostic-names <源>`
```bash
# 显示诊断内部名称
kotlinc -Xrender-internal-diagnostic-names Main.kt -d out
```

---

**基本写法：生成 .kotlin 缓存**
`-Pkotlin.incremental.useClasspathSnapshot=true`
```bash
# 启用类路径快照加速编译
./gradlew compileKotlin -Pkotlin.incremental.useClasspathSnapshot=true
```
