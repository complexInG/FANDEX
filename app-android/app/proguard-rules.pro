# FANDEX ProGuard 规则

# commonmark-java
-keep class org.commonmark.** { *; }
-dontwarn org.commonmark.**

# Kotlinx 序列化
-keepattributes *Annotation*, InnerClasses
-dontnote kotlinx.serialization.AnnotationsKt

# Compose
-keep class androidx.compose.** { *; }
-dontwarn androidx.compose.**
