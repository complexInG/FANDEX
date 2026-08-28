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
 * 卡片按压缩放反馈
 *
 * 对齐 web 端卡片的按压微交互（active 下沉 / scale 0.98）：
 * 按住时轻微缩小，松开回弹，时长与缓动引用 web 动效令牌
 * （instant 75ms 反馈 + out 减速）
 */
fun Modifier.pressScale(
    interactionSource: MutableInteractionSource
): Modifier = composed {
    val pressed by interactionSource.collectIsPressedAsState()
    val scale by animateFloatAsState(
        targetValue = if (pressed) 0.98f else 1f,
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
fun Modifier.pressScale(): Modifier = composed {
    val interactionSource = remember { MutableInteractionSource() }
    pressScale(interactionSource)
}
