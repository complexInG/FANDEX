package com.fandex.app.ui.theme

import androidx.compose.ui.graphics.Color

/**
 * FANDEX 原始颜色令牌
 *
 * 与 app-web/src/styles/shared/tokens.css 逐值对齐（同步自 shd-shared/tokens）：
 * - 中性色阶：纯黑到冷雾灰白（无色相偏移），支撑双主题背景体系
 * - 青色色阶：浅色模式强调色为深青 cyan-300，深色模式为亮青 cyan-500
 * - 状态色：成功 / 警告 / 危险 / 信息，深色模式整体提亮
 */
object PrimitiveColors {
    // 中性色阶
    val Neutral0 = Color(0xFF000000)
    val Neutral50 = Color(0xFF0A0A0A)
    val Neutral100 = Color(0xFF141414)
    val Neutral200 = Color(0xFF1F1F1F)
    val Neutral300 = Color(0xFF2A2A2A)
    val Neutral400 = Color(0xFF404040)
    val Neutral500 = Color(0xFF525252)
    val Neutral550 = Color(0xFF596671)
    val Neutral600 = Color(0xFF737373)
    val Neutral700 = Color(0xFFA3A3A3)
    val Neutral800 = Color(0xFFBCC8D0)
    val Neutral900 = Color(0xFFCCD5DB)
    val Neutral950 = Color(0xFFDAE1E6)
    val Neutral1000 = Color(0xFFE2E8EC)
    val Neutral1050 = Color(0xFFEBEFF3)

    // 青色色阶
    val Cyan100 = Color(0xFF053645)
    val Cyan200 = Color(0xFF085263)
    val Cyan300 = Color(0xFF0B6E7E)
    val Cyan400 = Color(0xFF00BCD4)
    val Cyan500 = Color(0xFF00E5FF)
    val Cyan600 = Color(0xFF4FF2FF)

    // 状态色
    val SuccessLight = Color(0xFF16A34A)
    val SuccessDark = Color(0xFF22C55E)
    val WarningLight = Color(0xFFEA580C)
    val WarningDark = Color(0xFFF97316)
    val DangerLight = Color(0xFFDC2626)
    val DangerDark = Color(0xFFEF4444)
    val InfoLight = Color(0xFF0B6E7E)
    val InfoDark = Color(0xFF00E5FF)
}

/**
 * 模块分类颜色
 *
 * 与 shd-shared/metadata/modules.json categoryColors 一致
 */
object CategoryColors {
    val Tools = Color(0xFF4F5BD5)
    val Frontend = Color(0xFFD63031)
    val Backend = Color(0xFFE17055)
    val Database = Color(0xFF00B894)
    val Cs = Color(0xFF8854D0)
    val Math = Color(0xFF6C5CE7)
    val Cloud = Color(0xFFE05A2B)
}
