# Java 模块系统 JPMS

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## module-info.java 声明

**基本写法：声明模块**
`module <模块名> {}`
```java
// 定义模块 com.example.app
module com.example.app {
}
```

---

**基本写法：导出包**
`exports <包名>;`
```java
// 导出包供其他模块使用
module com.example.app {
    exports com.example.api;
}
```

---

**基本写法：导出到指定模块**
`exports <包名> to <模块名>;`
```java
// 仅向指定模块导出
module com.example.app {
    exports com.example.internal to com.example.other;
}
```

---

**基本写法：依赖模块**
`requires <模块名>;`
```java
// 声明依赖模块
module com.example.app {
    requires java.net.http;
}
```

---

**基本写法：传递依赖**
`requires transitive <模块名>;`
```java
// 依赖可传递给下游模块
module com.example.app {
    requires transitive java.sql;
}
```

---

**基本写法：静态依赖**
`requires static <模块名>;`
```java
// 仅编译期需要的依赖
module com.example.app {
    requires static java.annotation;
}
```

---

## 服务声明与使用

**基本写法：提供服务**
`provides <服务接口> with <实现类>;`
```java
// 声明模块提供的服务实现
module com.example.app {
    provides com.example.Service with com.example.ServiceImpl;
}
```

---

**基本写法：使用服务**
`uses <服务接口>;`
```java
// 声明模块使用 ServiceLoader 加载的服务
module com.example.app {
    uses com.example.Service;
}
```

---

**基本写法：打开包用于反射**
`opens <包名>;`
```java
// 允许其他模块反射访问
module com.example.app {
    opens com.example.entity;
}
```

---

**基本写法：打开包到指定模块**
`opens <包名> to <模块名>;`
```java
// 仅对指定模块开放反射
module com.example.app {
    opens com.example.entity to com.fasterxml.jackson.databind;
}
```

---

## java 命令运行模块

**基本写法：运行模块主类**
`java -m <模块>/<主类>`
```bash
# 运行模块化应用
java -m com.example.app/com.example.app.Main
```

---

**基本写法：指定模块路径**
`java --module-path <路径> -m <模块>/<主类>`
```bash
# 指定模块路径运行
java --module-path mods -m com.example.app/com.example.app.Main
```

---

**基本写法：升级模块路径**
`java --upgrade-module-path <路径> -m <模块>/<主类>`
```bash
# 替换可升级模块
java --upgrade-module-path upgrades -m com.example.app/com.example.app.Main
```

---

**基本写法：限制模块**
`java --limit-modules <模块1>,<模块2> -m <模块>/<主类>`
```bash
# 限制可观察的模块集合
java --limit-modules java.base,com.example.app -m com.example.app/com.example.app.Main
```

---

## javac 编译模块

**基本写法：编译模块源码**
`javac -d <输出> --module-source-path <路径> --module <模块>`
```bash
# 编译指定模块
javac -d out --module-source-path src --module com.example.app
```

---

**基本写法：编译所有模块**
`javac -d <输出> --module-source-path <路径> --module-source-path <路径> *`
```bash
# 编译源码路径下所有模块
javac -d out --module-source-path src --module *
```

---

## 打包模块 jar

**基本写法：打包模块 jar**
`jar --create --file=<jar> --module-version=<版本> -C <类目录> .`
```bash
# 创建带版本的模块 jar
jar --create --file=mods/com.example.app.jar --module-version=1.0 -C out/com.example.app .
```

---

**基本写法：jar 包含 module-info**
`jar --create --file=<jar> --main-class=<主类> -C <目录> .`
```bash
# 创建可执行模块 jar
jar --create --file=app.jar --main-class=com.example.app.Main -C out .
```

---

## jlink 创建运行时镜像

**基本写法：创建自定义 JRE**
`jlink --module-path <路径> --add-modules <模块> --output <目录>`
```bash
# 生成仅含所需模块的运行时镜像
jlink --module-path mods --add-modules com.example.app --output myimage
```

---

**基本写法：指定启动器**
`jlink --launcher <名称>=<模块>/<主类> --add-modules <模块> --output <目录>`
```bash
# 生成带启动脚本的可执行镜像
jlink --launcher app=com.example.app/com.example.app.Main --module-path mods --add-modules com.example.app --output myimage
```

---

**基本写法：压缩镜像**
`jlink --compress=<级别> --add-modules <模块> --output <目录>`
```bash
# 压缩级别 0-2 减小镜像体积
jlink --compress=2 --module-path mods --add-modules com.example.app --output myimage
```

---

## 模块相关 API

**基本写法：获取模块**
`<类>.class.getModule();`
```java
// 获取类所属模块
Module m = String.class.getModule();
```

---

**基本写法：获取模块名**
`<module>.getName();`
```java
// 获取模块名称
String name = m.getName();
```

---

**基本写法：加载类**
`<module>.getClassLoader().loadClass("<类名>");`
```java
// 通过模块的类加载器加载类
Class<?> c = m.getClassLoader().loadClass("com.example.App");
```

---

## jdeps 依赖分析

**基本写法：分析模块依赖**
`jdeps --module-path <路径> -m <模块>`
```bash
# 分析模块的依赖关系
jdeps --module-path mods -m com.example.app
```

---

**基本写法：生成 module-info**
`jdeps --generate-module-info <输出目录> <jar>`
```bash
# 为已有 jar 生成模块描述
jdeps --generate-module-info out lib.jar
```

---

**基本写法：列出依赖**
`jdeps -s <jar>`
```bash
# 简洁列出 jar 包依赖
jdeps -s app.jar
```
