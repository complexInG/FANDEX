# Java 构建工具 Maven/Gradle 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Maven 常用命令

**基本写法：清理构建产物**
`mvn clean`
```java
// 删除 target 目录，确保全新构建
mvn clean
```

---

**基本写法：编译主代码**
`mvn compile`
```java
// 编译 src/main/java 到 target/classes
mvn compile
```

---

**基本写法：编译测试代码**
`mvn test-compile`
```java
// 编译 src/test/java 到 target/test-classes
mvn test-compile
```

---

**基本写法：运行测试**
`mvn test`
```java
// 执行所有单元测试，报告输出到 target/surefire-reports
mvn test
```

---

**基本写法：打包**
`mvn package`
```java
// 打包为 jar/war，输出到 target/
mvn package
```

---

**基本写法：安装到本地仓库**
`mvn install`
```java
// 安装到 ~/.m2/repository 供其他本地项目依赖
mvn install
```

---

**基本写法：部署到远程仓库**
`mvn deploy`
```java
// 上传构件到 Nexus/Artifactory 等远程仓库
mvn deploy
```

---

**基本写法：跳过测试打包**
`mvn package -DskipTests`
```java
// 编译测试代码但不执行测试
mvn clean package -DskipTests
```

---

**基本写法：完全跳过测试**
`mvn package -Dmaven.test.skip=true`
```java
// 既不编译也不执行测试
mvn clean package -Dmaven.test.skip=true
```

---

**基本写法：激活 Profile**
`mvn package -P<profileId>`
```java
// 激活指定 profile 进行打包
mvn clean package -Pprod
```

---

**基本写法：离线构建**
`mvn -o <goal>`
```java
// 不访问远程仓库，仅使用本地依赖
mvn -o clean package
```

---

**基本写法：多线程构建**
`mvn -T <threads> <goal>`
```java
// 使用 4 线程并行构建
mvn -T 4 clean install
```

---

**基本写法：查看依赖树**
`mvn dependency:tree`
```java
// 排查依赖冲突必备
mvn dependency:tree
```

---

**基本写法：过滤依赖**
`mvn dependency:tree -Dincludes=<groupId>:<artifactId>`
```java
// 只查看指定依赖的引入路径
mvn dependency:tree -Dincludes=org.springframework:spring-core
```

---

**基本写法：分析依赖**
`mvn dependency:analyze`
```java
// 检查未使用与未声明依赖
mvn dependency:analyze
```

---

**基本写法：查看有效 POM**
`mvn help:effective-pom`
```java
// 输出合并父 POM 后的最终 POM
mvn help:effective-pom
```

---

**基本写法：创建项目骨架**
`mvn archetype:generate`
```java
// 交互式生成 Maven 项目结构
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

---

**基本写法：Spring Boot 运行**
`mvn spring-boot:run`
```java
// 直接从源码启动 Spring Boot 应用
mvn spring-boot:run
```

---

**基本写法：多模块构建**
`mvn -pl <module> -am <goal>`
```java
// 只构建指定模块及其依赖模块
mvn -pl my-module -am clean install
```

---

## Maven 依赖 Scope

**基本写法：编译期依赖**
`<scope>compile</scope>`
```java
// 默认 scope，全阶段可用
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-core</artifactId>
    <scope>compile</scope>
</dependency>
```

---

**基本写法：测试期依赖**
`<scope>test</scope>`
```java
// 仅测试阶段可用
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <scope>test</scope>
</dependency>
```

---

**基本写法：已提供依赖**
`<scope>provided</scope>`
```java
// 编译测试可用，打包时不包含（由容器提供）
<dependency>
    <groupId>jakarta.servlet</groupId>
    <artifactId>jakarta.servlet-api</artifactId>
    <scope>provided</scope>
</dependency>
```

---

**基本写法：运行时依赖**
`<scope>runtime</scope>`
```java
// 编译不需要，运行时需要
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

---

## Gradle 常用命令

**基本写法：列出所有任务**
`./gradlew tasks`
```java
// 查看项目可用的所有 Gradle 任务
./gradlew tasks
```

---

**基本写法：清理构建**
`./gradlew clean`
```java
// 删除 build 目录
./gradlew clean
```

---

**基本写法：编译代码**
`./gradlew build`
```java
// 完整构建（编译、测试、打包）
./gradlew build
```

---

**基本写法：跳过测试构建**
`./gradlew build -x test`
```java
// 排除 test 任务
./gradlew build -x test
```

---

**基本写法：运行测试**
`./gradlew test`
```java
// 执行所有测试
./gradlew test
```

---

**基本写法：运行指定测试类**
`./gradlew test --tests <类名>`
```java
// 只运行某个测试类
./gradlew test --tests com.example.UserServiceTest
```

---

**基本写法：运行 Spring Boot**
`./gradlew bootRun`
```java
// 启动 Spring Boot 应用
./gradlew bootRun
```

---

**基本写法：打包**
`./gradlew bootJar`
```java
// 生成可执行 fat jar
./gradlew bootJar
```

---

**基本写法：查看依赖树**
`./gradlew dependencies`
```java
// 打印项目依赖树
./gradlew dependencies
```

---

**基本写法：查看指定配置的依赖**
`./gradlew dependencies --configuration <配置>`
```java
// 只查看 runtimeClasspath 的依赖
./gradlew dependencies --configuration runtimeClasspath
```

---

**基本写法：依赖分析**
`./gradlew dependencyInsight --dependency <名称>`
```java
// 查看某个依赖的详细解析过程
./gradlew dependencyInsight --dependency spring-core
```

---

**基本写法：刷新依赖**
`./gradlew --refresh-dependencies build`
```java
// 强制重新下载依赖
./gradlew --refresh-dependencies build
```

---

**基本写法：并行构建**
`./gradlew build --parallel`
```java
// 多模块并行构建
./gradlew build --parallel
```

---

**基本写法：构建缓存**
`./gradlew build --build-cache`
```java
// 启用 Gradle 构建缓存
./gradlew build --build-cache
```

---

**基本写法：查看任务详情**
`./gradlew help --task <任务名>`
```java
// 查看某任务的描述与依赖
./gradlew help --task build
```

---

**基本写法：初始化 Wrapper**
`gradle wrapper --gradle-version <版本>`
```java
// 生成 gradlew 脚本，统一团队 Gradle 版本
gradle wrapper --gradle-version 8.5
```

---

## build.gradle 关键配置

**基本写法：插件声明**
`plugins { id '<plugin>' version '<version>' }`
```java
// Groovy DSL 声明插件
plugins {
    id 'org.springframework.boot' version '3.2.0'
    id 'java'
}
```

---

**基本写法：依赖声明**
`implementation '<group>:<name>:<version>'`
```java
// Groovy DSL 添加依赖
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.2.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.12.1'
}
```

---

**基本写法：Kotlin DSL 依赖**
`implementation("<group>:<name>:<version>")`
```java
// build.gradle.kts 写法
dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web:3.2.0")
    testImplementation("org.junit.jupiter:junit-jupiter:5.12.1")
}
```

---

**基本写法：Java 版本配置**
`java { sourceCompatibility = JavaVersion.VERSION_17 }`
```java
// 指定编译目标版本
java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}
```

---

**基本写法：仓库配置**
`repositories { mavenCentral() }`
```java
// 配置依赖仓库
repositories {
    mavenCentral()
    maven { url 'https://maven.aliyun.com/repository/public' }
}
```

---

**基本写法：自定义任务**
`task <name> { doLast { ... } }`
```java
// Groovy DSL 定义任务
task printVersion {
    doLast {
        println "Project version: ${project.version}"
    }
}
```

---

## 仓库镜像配置

**基本写法：Maven 阿里云镜像**
`<mirror>` in settings.xml
```java
// ~/.m2/settings.xml 配置镜像加速
<mirror>
    <id>aliyun</id>
    <mirrorOf>central</mirrorOf>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>
```

---

**基本写法：Gradle 阿里云镜像**
`repositories { maven { url '...' } }`
```java
// settings.gradle 或 build.gradle 配置
repositories {
    maven { url 'https://maven.aliyun.com/repository/public' }
    mavenCentral()
}
```

---

## 版本管理

**基本写法：Maven 版本号约定**
`<major>.<minor>.<patch>-<qualifier>`
```java
// 语义化版本号约定
// 1.0.0-SNAPSHOT 快照版本
// 1.0.0-RELEASE 正式版本
```

---

**基本写法：Maven 版本更新检查**
`mvn versions:display-dependency-updates`
```java
// 列出可用的依赖新版本
mvn versions:display-dependency-updates
```

---

**基本写法：Gradle 版本目录**
`libs.versions.toml`
```java
// gradle/libs.versions.toml 集中管理版本
[versions]
junit = "5.12.1"
[libraries]
junit = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }
```

---

## 发布构件

**基本写法：Maven 发布到远程仓库**
`<distributionManagement>`
```java
// pom.xml 配置发布目标
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>https://repo.example.com/releases</url>
    </repository>
</distributionManagement>
```

---

**基本写法：Gradle 发布**
`maven-publish` 插件
```java
// build.gradle 配置发布
publishing {
    publications {
        maven(MavenPublication) {
            from components.java
            groupId = 'com.example'
            artifactId = 'my-lib'
            version = '1.0.0'
        }
    }
}
```
