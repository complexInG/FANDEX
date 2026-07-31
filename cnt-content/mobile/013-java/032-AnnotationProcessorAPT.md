# Java 注解处理器 APT

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 定义注解

**基本写法：定义运行时注解**
`@Retention(RetentionPolicy.RUNTIME) @Target(<目标>) @interface <名称> {}`
```java
// 定义运行时保留的字段注解
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface MyField {
    String value();
}
```

---

**基本写法：定义源码级注解**
`@Retention(RetentionPolicy.SOURCE) @interface <名称> {}`
```java
// 仅源码保留的注解（用于 APT 处理）
@Retention(RetentionPolicy.SOURCE)
@Target(ElementType.TYPE)
public @interface Builder {
}
```

---

**基本写法：定义元注解的成员**
`@interface <名称> { <类型> <成员>() [default <默认值>]; }`
```java
// 注解带默认值
public @interface Cache {
    int ttl() default 60;
    String name() default "";
}
```

---

## 编写注解处理器

**基本写法：声明处理器**
`@SupportedAnnotationTypes("<注解全名>") @SupportedSourceVersion(<版本>) public class <类> extends AbstractProcessor {}`
```java
// 自定义注解处理器
@SupportedAnnotationTypes("com.example.Builder")
@SupportedSourceVersion(SourceVersion.RELEASE_21)
public class BuilderProcessor extends AbstractProcessor {
    @Override
    public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment env) {
        return true;
    }
}
```

---

**基本写法：获取被注解元素**
`env.getElementsAnnotatedWith(<注解类>);`
```java
// 收集所有被注解的元素
Set<? extends Element> set = env.getElementsAnnotatedWith(Builder.class);
```

---

**基本写法：获取 Filer 生成文件**
`processingEnv.getFiler().createSourceFile("<类名>");`
```java
// 生成 Java 源文件
JavaFileObject f = processingEnv.getFiler().createSourceFile("com.example.Generated");
```

---

**基本写法：获取 Messager 输出**
`processingEnv.getMessager().printMessage(<类型>, <消息>, <元素>);`
```java
// 编译期输出错误信息
processingEnv.getMessager().printMessage(Diagnostic.Kind.ERROR, "missing field", element);
```

---

## 注册处理器

**基本写法：SPI 注册文件**
`META-INF/services/javax.annotation.processing.Processor`
```
# 文件内容为处理器全限定名
com.example.BuilderProcessor
```

---

## Maven 编译配置

**基本写法：Maven 编译插件配置**
`<plugin> <artifactId>maven-compiler-plugin</artifactId> <configuration>`
```xml
<!-- 配置编译器使用的注解处理器 -->
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <annotationProcessors>
      <processor>com.example.BuilderProcessor</processor>
    </annotationProcessors>
  </configuration>
</plugin>
```

---

**基本写法：禁用注解处理**
`<proc>none</proc>`
```xml
<!-- 编译时关闭注解处理 -->
<configuration>
  <proc>none</proc>
</configuration>
```

---

## Gradle 编译配置

**基本写法：Gradle 配置注解处理器**
`annotationProcessor '<依赖坐标>'`
```groovy
// Gradle 注册注解处理器依赖
dependencies {
  annotationProcessor 'com.example:builder-processor:1.0'
}
```

---

**基本写法：Kotlin 使用 KSP**
`ksp('<依赖坐标>')`
```groovy
// Kotlin 符号处理 KSP
plugins { id("com.google.devtools.ksp") }
dependencies {
  ksp 'com.example:builder-processor:1.0'
}
```

---

## javac 命令

**基本写法：编译时指定处理器**
`javac -processor <处理器类> <源文件>`
```bash
# 编译时显式指定注解处理器
javac -processor com.example.BuilderProcessor src/Main.java
```

---

**基本写法：指定处理器路径**
`javac -processorpath <路径> -processor <类> <源文件>`
```bash
# 指定处理器所在 jar 路径
javac -processorpath processor.jar -processor com.example.BuilderProcessor src/Main.java
```

---

**基本写法：输出生成源码目录**
`javac -s <输出目录> <源文件>`
```bash
# 指定生成源文件输出目录
javac -s build/generated -processor com.example.BuilderProcessor src/Main.java
```

---

**基本写法：禁用注解处理**
`javac -proc:none <源文件>`
```bash
# 仅编译不执行注解处理
javac -proc:none src/Main.java
```

---

## 元素模型 Element

**基本写法：获取元素类型**
`<element>.getKind()`
```java
// 判断元素是类还是方法
if (element.getKind() == ElementKind.CLASS) { }
```

---

**基本写法：获取元素注解**
`<element>.getAnnotation(<注解类>);`
```java
// 读取元素上的注解
Builder b = element.getAnnotation(Builder.class);
```

---

**基本写法：获取类元素字段**
`<typeElement>.getEnclosedElements();`
```java
// 获取类中所有成员
List<? extends Element> members = typeElement.getEnclosedElements();
```

---

## 类型模型 Types / Elements

**基本写法：获取 Types 工具**
`processingEnv.getTypeUtils();`
```java
// 获取类型工具类
Types types = processingEnv.getTypeUtils();
```

---

**基本写法：获取 Elements 工具**
`processingEnv.getElementUtils();`
```java
// 获取元素工具类
Elements elements = processingEnv.getElementUtils();
```

---

**基本写法：按名获取 TypeElement**
`elements.getTypeElement("<全限定名>");`
```java
// 通过全限定名获取类型元素
TypeElement e = elements.getTypeElement("java.lang.String");
```

---

## 编译参数传递

**基本写法：读取编译选项**
`processingEnv.getOptions().get("<键>");`
```java
// 获取 -A 传递的参数
String v = processingEnv.getOptions().get("myOption");
```

---

**基本写法：javac 传递参数**
`javac -A<键>=<值> <源文件>`
```bash
# 通过 -A 选项向处理器传参
javac -AmyOption=value -processor com.example.BuilderProcessor src/Main.java
```
