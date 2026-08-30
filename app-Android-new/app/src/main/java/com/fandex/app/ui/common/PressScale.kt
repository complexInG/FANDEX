package com.fandex.app.ui.common

import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.composed
import androidx.compose.ui.graphics.graphicsLayer

/**
 * 按压缩放反馈
 *
 * 对齐 web 端的按压微交互（active 下沉）：
 * 按住时轻微缩小，松开回弹，时长与缓动引用 web 动效令牌
 * （instant 75ms 反馈 + out 减速）
 *
 * @param interactionSource 绑定的交互源（与 clickable 共用以感知按压）
 * @param pressedScale 按住时的缩放比例（卡片 0.98，小图标按钮可传 0.94 增强反馈）
 */
fun Modifier.pressScale(
    interactionSource: MutableInteractionSource,
    pressedScale: Float = 0.98f
): Modifier = composed {
    val pressed by interactionSource.collectIsPressedAsState()
    val scale by animateFloatAsState(
        targetValue = if (pressed) pressedScale else 1f,
        animationSpec = tween(durationMillis = 75),
        label = "pressScale"
    )
    graphicsLayer {
        scaleX = scale
        scaleY = scale
    }
}

/**
 * 便捷重载：内部自建 interactionSource（供 clickable 使用）
 */
fun Modifier.pressScale(pressedScale: Float = 0.98f): Modifier = composed {
    val interactionSource = remember { MutableInteractionSource() }
    pressScale(interactionSource, pressedScale)
}
