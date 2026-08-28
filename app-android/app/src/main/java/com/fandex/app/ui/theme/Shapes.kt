package com.fandex.app.ui.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Shapes
import androidx.compose.ui.unit.dp

/**
 * FANDEX 形状系统
 *
 * 对齐 app-web tokens.css 圆角令牌：
 * 按钮与徽章 4px（radius-control）、卡片 8px（radius-card）、模态 12px（radius-modal）
 * 按仓库规则：按钮、徽章、状态指示器使用直角小圆角（radius-md 以内）
 */
val FandexShapes = Shapes(
    // 小型组件：按钮、徽章、输入框（4px）
    small = RoundedCornerShape(4.dp),
    // 中型组件：卡片、面板（8px）
    medium = RoundedCornerShape(8.dp),
    // 大型组件：模态、对话框（12px）
    large = RoundedCornerShape(12.dp),
    // 超大组件
    extraLarge = RoundedCornerShape(16.dp),
)
