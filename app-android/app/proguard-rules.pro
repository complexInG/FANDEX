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

# LaTeX 数学公式渲染（JLatexMath，反射加载字体与符号资产）
-keep class ru.noties.jlatexmath.** { *; }
-keep class org.scifont.** { *; }
-keep class org.scilab.forge.jlatexmath.** { *; }
-dontwarn ru.noties.jlatexmath.**
-dontwarn org.scilab.forge.jlatexmath.**
