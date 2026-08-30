package com.fandex.app.ui.common

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.LinearOutSlowInEasing
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.animation.core.tween
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.dp

/**
 * FANDEX 全局动效令牌
 *
 * 对齐 web 端 motion 令牌体系，统一全应用过渡时长与缓动，
 * 避免各页面自行定义造成节奏不统一
 */
object FandexMotion {

    /** 快速反馈（按压、图标切换等微交互） */
    const val DurationFast = 120

    /** 常规过渡（入场、颜色状态切换、内容淡入淡出） */
    const val DurationNormal = 220

    /** 慢速过渡（大区块转场、强调性动效） */
    const val DurationSlow = 320

    /** 列表入场 stagger 步长（毫秒），按下标递增 */
    const val StaggerStep = 40

    /** 列表入场 stagger 延迟上限（毫秒），超出后统一取上限 */
    const val StaggerMax = 240
}

/** 快速过渡：120ms 减速曲线，适合按压与图标切换等微交互 */
fun <T> tweenFast() = tween<T>(
    durationMillis = FandexMotion.DurationFast,
    easing = FastOutSlowInEasing
)

/** 常规过渡：220ms 减速曲线，适合入场与状态切换 */
fun <T> tweenNormal() = tween<T>(
    durationMillis = FandexMotion.DurationNormal,
    easing = FastOutSlowInEasing
)

/** 低刚度弹簧：无回弹的柔和趋近，适合布局与位移类过渡 */
fun springGentle() = spring<Float>(
    dampingRatio = Spring.DampingRatioNoBouncy,
    stiffness = Spring.StiffnessLow
)

/** 适度回弹弹簧：MediumBouncy 阻尼，适合选中脉冲等强调反馈 */
fun springBouncy() = spring<Float>(
    dampingRatio = Spring.DampingRatioMediumBouncy,
    stiffness = Spring.StiffnessMediumLow
)

/**
 * 入场动效组合：alpha 0->1 + translateY 12dp->0
 *
 * 通过 [visible] 门控播放：首次从 false 翻转为 true 时按 stagger 延迟播放入场；
 * 组合时 visible 已为 true（列表项滚动回收后重组）则直接静止在终态，不重播。
 * 调用方需在屏幕层用 remember 保存 visible 状态（如 hasEntered），
 * 在内容就绪后的下一帧置 true，即可实现"仅首次进入播放一次"的 stagger 入场
 *
 * @param index 列表下标，决定 stagger 延迟：(index * 40ms).coerceAtMost(240ms)
 * @param visible 是否已就绪（true 时播放入场或保持终态）
 */
@Composable
fun Modifier.fandexEntrance(
    index: Int,
    visible: Boolean
): Modifier {
    val density = LocalDensity.current
    val startOffsetY = with(density) { 12.dp.toPx() }
    val delayMillis = (index * FandexMotion.StaggerStep).coerceAtMost(FandexMotion.StaggerMax)

    // 进度 0->1：初始值跟随 visible（visible 已为 true 时初始即 1，不重播）
    val progress by animateFloatAsState(
        targetValue = if (visible) 1f else 0f,
        animationSpec = tween(
            durationMillis = FandexMotion.DurationNormal,
            delayMillis = delayMillis,
            easing = LinearOutSlowInEasing
        ),
        label = "fandexEntranceProgress"
    )

    return graphicsLayer {
        alpha = progress
        translationY = startOffsetY * (1f - progress)
    }
}

/**
 * 选中脉冲动效：selected 翻转为 true 的瞬间播放 1->0.96->1 的弹性缩放
 *
 * 供筛选 chips 等需要"选中瞬间强调"的元素使用，
 * 与 pressScale（按压反馈）叠加时变换相乘，互不干扰
 */
@Composable
fun Modifier.selectionPulse(selected: Boolean): Modifier {
    val scale = remember { Animatable(1f) }

    LaunchedEffect(selected) {
        if (selected) {
            // 先轻微收缩，再以适度回弹弹簧回到原尺寸
            scale.animateTo(0.96f, tweenFast())
            scale.animateTo(1f, springBouncy())
        }
    }

    return graphicsLayer {
        scaleX = scale.value
        scaleY = scale.value
    }
}
