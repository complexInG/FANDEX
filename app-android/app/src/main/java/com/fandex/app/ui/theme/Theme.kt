package com.fandex.app.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.graphics.Color

/**
 * 浅色主题 ColorScheme
 *
 * 逐值对齐 app-web tokens.css 浅色语义层：
 * 冷雾灰背景 #EBEFF3 + 深青强调 #0B6E7E
 */
private val LightColorScheme = lightColorScheme(
    primary = PrimitiveColors.Cyan300,
    onPrimary = PrimitiveColors.Neutral1050,
    primaryContainer = PrimitiveColors.Cyan100,
    onPrimaryContainer = PrimitiveColors.Cyan300,
    inversePrimary = PrimitiveColors.Cyan500,

    secondary = PrimitiveColors.Neutral500,
    onSecondary = PrimitiveColors.Neutral1050,
    secondaryContainer = PrimitiveColors.Neutral1000,
    onSecondaryContainer = PrimitiveColors.Neutral500,

    tertiary = PrimitiveColors.Cyan400,
    onTertiary = PrimitiveColors.Neutral1050,
    tertiaryContainer = PrimitiveColors.Cyan200,
    onTertiaryContainer = PrimitiveColors.Cyan300,

    background = PrimitiveColors.Neutral1050,
    onBackground = PrimitiveColors.Neutral50,
    surface = PrimitiveColors.Neutral1050,
    onSurface = PrimitiveColors.Neutral50,
    surfaceVariant = PrimitiveColors.Neutral1000,
    onSurfaceVariant = PrimitiveColors.Neutral500,
    surfaceTint = PrimitiveColors.Cyan300,
    inverseSurface = PrimitiveColors.Neutral200,
    inverseOnSurface = PrimitiveColors.Neutral1000,

    error = PrimitiveColors.DangerLight,
    onError = PrimitiveColors.Neutral1050,
    errorContainer = PrimitiveColors.DangerLight,
    onErrorContainer = PrimitiveColors.Neutral1050,

    outline = PrimitiveColors.Neutral900,
    outlineVariant = PrimitiveColors.Neutral950,
    scrim = PrimitiveColors.Neutral0,
)

/**
 * 深色主题 ColorScheme
 *
 * 逐值对齐 app-web tokens.css 深色语义层：
 * 近黑背景 #0A0A0A + 亮青强调 #00E5FF
 */
private val DarkColorScheme = darkColorScheme(
    primary = PrimitiveColors.Cyan500,
    onPrimary = PrimitiveColors.Neutral0,
    primaryContainer = PrimitiveColors.Cyan200,
    onPrimaryContainer = PrimitiveColors.Cyan500,
    inversePrimary = PrimitiveColors.Cyan300,

    secondary = PrimitiveColors.Neutral700,
    onSecondary = PrimitiveColors.Neutral0,
    secondaryContainer = PrimitiveColors.Neutral200,
    onSecondaryContainer = PrimitiveColors.Neutral700,

    tertiary = PrimitiveColors.Cyan400,
    onTertiary = PrimitiveColors.Neutral0,
    tertiaryContainer = PrimitiveColors.Cyan100,
    onTertiaryContainer = PrimitiveColors.Cyan400,

    background = PrimitiveColors.Neutral50,
    onBackground = PrimitiveColors.Neutral1050,
    surface = PrimitiveColors.Neutral50,
    onSurface = PrimitiveColors.Neutral1050,
    surfaceVariant = PrimitiveColors.Neutral200,
    onSurfaceVariant = PrimitiveColors.Neutral700,
    surfaceTint = PrimitiveColors.Cyan500,
    inverseSurface = PrimitiveColors.Neutral1000,
    inverseOnSurface = PrimitiveColors.Neutral50,

    error = PrimitiveColors.DangerDark,
    onError = PrimitiveColors.Neutral0,
    errorContainer = PrimitiveColors.DangerDark,
    onErrorContainer = PrimitiveColors.Neutral0,

    outline = PrimitiveColors.Neutral300,
    outlineVariant = PrimitiveColors.Neutral100,
    scrim = PrimitiveColors.Neutral0,
)

/**
 * FANDEX 扩展颜色
 *
 * 提供 Material 3 ColorScheme 之外的语义颜色，字段名与 web 语义令牌一一对应
 */
data class FandexExtendedColors(
    /** 当前是否深色主题（mermaid 图表主题等需要） */
    val isDark: Boolean,
    val bgSecondary: Color,
    val bgTertiary: Color,
    val bgElevated: Color,
    val bgSunken: Color,
    val bgHover: Color,
    val bgActive: Color,
    val fgSecondary: Color,
    val fgTertiary: Color,
    val fgDisabled: Color,
    val fgInverse: Color,
    val borderSubtle: Color,
    val borderDefault: Color,
    val borderStrong: Color,
    val borderFocus: Color,
    val codeBg: Color,
    val codeText: Color,
    val codeComment: Color,
    val codeKeyword: Color,
    val codeString: Color,
    val codeNumber: Color,
    val codeAnnotation: Color,
    val codeFunction: Color,
    val codeTag: Color,
    val success: Color,
    val warning: Color,
    val info: Color,
)

/**
 * 浅色扩展颜色
 *
 * 代码块在浅色模式下使用亮色底（凹陷背景）与深色文字，
 * 高亮色板同步为亮色可读配色，避免深色块突兀
 */
private val LightExtendedColors = FandexExtendedColors(
    isDark = false,
    bgSecondary = PrimitiveColors.Neutral1000,
    bgTertiary = PrimitiveColors.Neutral950,
    bgElevated = PrimitiveColors.Neutral1050,
    bgSunken = PrimitiveColors.Neutral950,
    bgHover = PrimitiveColors.Neutral1000,
    bgActive = PrimitiveColors.Neutral950,
    fgSecondary = PrimitiveColors.Neutral500,
    fgTertiary = PrimitiveColors.Neutral550,
    fgDisabled = PrimitiveColors.Neutral800,
    fgInverse = PrimitiveColors.Neutral1050,
    borderSubtle = PrimitiveColors.Neutral950,
    borderDefault = PrimitiveColors.Neutral900,
    borderStrong = PrimitiveColors.Neutral800,
    borderFocus = PrimitiveColors.Cyan300,
    codeBg = PrimitiveColors.Neutral950,
    codeText = PrimitiveColors.Neutral50,
    codeComment = PrimitiveColors.Neutral600,
    codeKeyword = Color(0xFF0B6E7E),
    codeString = Color(0xFF15803D),
    codeNumber = Color(0xFFB45309),
    codeAnnotation = Color(0xFF7C3AED),
    codeFunction = Color(0xFF1D4ED8),
    codeTag = Color(0xFFBE123C),
    success = PrimitiveColors.SuccessLight,
    warning = PrimitiveColors.WarningLight,
    info = PrimitiveColors.InfoLight,
)

/** 深色扩展颜色 */
private val DarkExtendedColors = FandexExtendedColors(
    isDark = true,
    bgSecondary = PrimitiveColors.Neutral100,
    bgTertiary = PrimitiveColors.Neutral200,
    bgElevated = PrimitiveColors.Neutral200,
    bgSunken = PrimitiveColors.Neutral0,
    bgHover = PrimitiveColors.Neutral100,
    bgActive = PrimitiveColors.Neutral200,
    fgSecondary = PrimitiveColors.Neutral700,
    fgTertiary = PrimitiveColors.Neutral600,
    fgDisabled = PrimitiveColors.Neutral400,
    fgInverse = PrimitiveColors.Neutral50,
    borderSubtle = PrimitiveColors.Neutral100,
    borderDefault = PrimitiveColors.Neutral300,
    borderStrong = PrimitiveColors.Neutral400,
    borderFocus = PrimitiveColors.Cyan500,
    codeBg = PrimitiveColors.Neutral0,
    codeText = PrimitiveColors.Neutral900,
    codeComment = PrimitiveColors.Neutral500,
    codeKeyword = PrimitiveColors.Cyan500,
    codeString = Color(0xFF22C55E),
    codeNumber = Color(0xFFFBBF24),
    codeAnnotation = Color(0xFFA78BFA),
    codeFunction = Color(0xFF60A5FA),
    codeTag = Color(0xFFFB7185),
    success = PrimitiveColors.SuccessDark,
    warning = PrimitiveColors.WarningDark,
    info = PrimitiveColors.InfoDark,
)

val LocalExtendedColors = staticCompositionLocalOf { LightExtendedColors }

/**
 * FANDEX 主题入口
 *
 * 双主题支持（浅色/深色），跟随系统或用户手动切换
 * 提供 Material 3 ColorScheme + FANDEX 扩展颜色
 */
@Composable
fun FandexTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme
    val extendedColors = if (darkTheme) DarkExtendedColors else LightExtendedColors

    CompositionLocalProvider(LocalExtendedColors provides extendedColors) {
        MaterialTheme(
            colorScheme = colorScheme,
            typography = FandexTypography,
            shapes = FandexShapes,
            content = content
        )
    }
}
