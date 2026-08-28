# Kotlin Multiplatform

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 项目结构

**基本写法：build.gradle.kts 配置**
`kotlin { androidTarget(); jvm(); iosX64(); iosArm64() }`
```kotlin
// 声明多平台目标
kotlin {
    androidTarget()
    jvm()
    iosX64(); iosArm64(); iosSimulatorArm64()
}
```

---

**基本写法：层级 sourceSets**
`val commonMain by getting; val androidMain by getting`
```kotlin
// 公共代码与平台代码目录
kotlin {
    sourceSets {
        val commonMain by getting
        val androidMain by getting
        val iosMain by creating { dependsOn(commonMain) }
    }
}
```

---

## expect/actual 机制

**基本写法：声明 expect**
`expect fun <方法>(): <类型>`
```kotlin
// commonMain 中声明平台差异函数
expect fun currentTimeMillis(): Long
```

---

**基本写法：实现 actual**
`actual fun <方法>(): <类型> { }`
```kotlin
// androidMain 中实现
actual fun currentTimeMillis(): Long = System.currentTimeMillis()
```

---

**基本写法：expect 类**
`expect class <类名>()`
```kotlin
// common 声明平台类
expect class DateFormatter() {
    fun format(millis: Long): String
}
```

---

**基本写法：actual 类**
`actual class <类名> { }`
```kotlin
// 平台实现具体类
actual class DateFormatter {
    actual fun format(millis: Long): String = java.text.SimpleDateFormat().format(Date(millis))
}
```

---

**基本写法：expect 属性**
`expect val <属性>: <类型>`
```kotlin
// 声明平台相关常量
expect val platformName: String
```

---

## 跨平台依赖

**基本写法：commonMain 依赖**
`commonMain { dependencies { implementation("<坐标>") } }`
```kotlin
// 公共代码使用跨平台库
commonMain.dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.0")
}
```

---

**基本写法：平台专属依赖**
`androidMain { dependencies { implementation("<坐标>") } }`
```kotlin
// 仅 Android 平台依赖
androidMain.dependencies {
    implementation("androidx.core:core-ktx:1.13.0")
}
```

---

## 平台特定调用

**基本写法：Android 调用**
`import android.util.Log; Log.d(...)`
```kotlin
// androidMain 中调用 Android API
android.util.Log.d("tag", "msg")
```

---

**基本写法：iOS 调用**
`import platform.Foundation.NSDate`
```kotlin
// iosMain 中调用 Objective-C API
import platform.Foundation.NSDate
val now = NSDate()
```

---

**基本写法：JVM 调用**
`import java.io.File`
```kotlin
// jvmMain 中调用 JVM API
import java.io.File
val f = File("a.txt")
```

---

## 跨平台 IO

**基本写法：使用 okio 跨平台 IO**
`okio.FileSystem.SYSTEM.read(<path>) { }`
```kotlin
// okio 提供跨平台文件 IO
import okio.FileSystem
FileSystem.SYSTEM.read(path) { readUtf8() }
```

---

## kotlinx 库

**基本写法：kotlinx-datetime**
`Clock.System.now()`
```kotlin
// 跨平台日期时间
import kotlinx.datetime.Clock
val now = Clock.System.now()
```

---

**基本写法：kotlinx.coroutines 协程**
`runBlocking { }`
```kotlin
// 跨平台协程
import kotlinx.coroutines.runBlocking
runBlocking { doWork() }
```

---

**基本写法：kotlinx-serialization**
`@Serializable class <类>`
```kotlin
// 跨平台序列化
import kotlinx.serialization.Serializable
@Serializable
data class User(val name: String)
```

---

## expect/actual 扩展函数

**基本写法：扩展 expect**
`expect fun <<T>> <类型>.<方法>(): <返回>`
```kotlin
// 声明跨平台扩展函数
expect fun Long.toDateString(): String
```

---

## 共享业务逻辑

**基本写法：commonMain 编写业务**
`class <仓库> { suspend fun <方法>() = <实现> }`
```kotlin
// 共享业务代码不依赖平台
class UserRepository {
    suspend fun load(): User = api.fetch()
}
```

---

## 构建与运行

**基本写法：构建所有目标**
`./gradlew build`
```bash
# 编译所有平台目标
./gradlew build
```

---

**基本写法：构建特定目标**
`./gradlew :shared:assembleAndroid`
```bash
# 仅构建 Android 目标
./gradlew :shared:assembleAndroid
```

---

**基本写法：发布 iOS Framework**
`./gradlew :shared:linkDebugFrameworkIosArm64`
```bash
# 生成 iOS Framework
./gradlew :shared:linkDebugFrameworkIosArm64
```

---

## CocoaPods 集成

**基本写法：cocoapods 配置**
`cocoapods { summary = "<描述>"; version = "1.0" }`
```kotlin
// 配置 iOS CocoaPods 集成
kotlin {
    cocoapods {
        summary = "Shared Library"
        version = "1.0"
        ios.deploymentTarget = "14.0"
    }
}
```

---

## 目标简写

**基本写法：iOS 目标简写**
`ios() // 等价 iosX64 + iosArm64 + iosSimulatorArm64`
```kotlin
// 一行配置所有 iOS 目标
kotlin { ios() }
```

---

**基本写法：macos 目标**
`macosX64(); macosArm64()`
```kotlin
// macOS 目标
kotlin { macosX64(); macosArm64() }
```

---

## 中间层 sourceSet

**基本写法：iOS 共享代码**
`val iosMain by creating { dependsOn(commonMain) }`
```kotlin
// iOS 多架构共享代码
val iosMain by creating { dependsOn(commonMain) }
val iosX64Main by getting { dependsOn(iosMain) }
val iosArm64Main by getting { dependsOn(iosMain) }
```
