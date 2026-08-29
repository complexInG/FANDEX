package com.fandex.app.ui.markdown

import android.graphics.Bitmap
import android.graphics.Canvas
import androidx.compose.foundation.Image
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.produceState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import ru.noties.jlatexmath.JLatexMathDrawable
import kotlin.math.roundToInt

/**
 * LaTeX 数学公式离线渲染（基于 ru.noties:jlatexmath-android）
 *
 * - 块级公式（$$...$$）：MathBlockView，居中展示，超宽横向滚动
 * - 行内公式（$...$）：由 MarkdownRenderer 以 InlineTextContent 内嵌到文本流
 * - 全部离线渲染，字体与符号资产随包分发
 * - 解析失败返回 null，由调用方回退展示 LaTeX 源文本
 */

/** 同步渲染单条公式为位图（行内公式走此路径，公式极小、耗时可忽略） */
fun renderMathBitmap(latex: String, colorArgb: Int, textSizePx: Float): ImageBitmap? {
    if (latex.isBlank()) return null
    return runCatching {
        val drawable = JLatexMathDrawable.builder(latex)
            .textSize(textSizePx)
            .color(colorArgb)
            .build()
        val w = drawable.intrinsicWidth.coerceAtLeast(1)
        val h = drawable.intrinsicHeight.coerceAtLeast(1)
        // 防御异常超大的公式位图（渲染引擎偶发的病态输入）
        if (w.toLong() * h.toLong() > 64_000_000L) return null
        val bitmap = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888)
        val canvas = Canvas(bitmap)
        drawable.setBounds(0, 0, w, h)
        drawable.draw(canvas)
        bitmap.asImageBitmap()
    }.getOrNull()
}

/**
 * 异步渲染块级公式（CPU 密集，先占位后替换，避免主线程卡顿）
 */
@Composable
fun rememberMathBitmapAsync(latex: String, colorArgb: Int, textSizePx: Float): ImageBitmap? {
    return produceState<ImageBitmap?>(initialValue = null, latex, colorArgb, textSizePx) {
        value = kotlinx.coroutines.withContext(kotlinx.coroutines.Dispatchers.Default) {
            renderMathBitmap(latex, colorArgb, textSizePx)
        }
    }.value
}

/**
 * 块级公式视图（$$...$$）
 *
 * 对齐 web 端 KaTeX display 块的观感：无背景、水平居中、超宽可横向滚动
 */
@Composable
fun MathBlockView(
    latex: String,
    modifier: Modifier = Modifier,
    fallbackTextColor: Color = Color.Unspecified
) {
    val density = LocalDensity.current
    val textColor = mathTextColor(fallbackTextColor)
    val textSizePx = with(density) { 19.sp.toPx() }
    val bitmap = rememberMathBitmapAsync(latex.trim(), textColor.toArgb(), textSizePx)

    if (bitmap == null) {
        // 渲染失败 / 未完成：失败时回退展示源码（未完成时同样先可见，完成后替换）
        Box(modifier.fillMaxWidth(), contentAlignment = Alignment.CenterStart) {
            androidx.compose.material3.Text(
                text = latex,
                style = androidx.compose.material3.MaterialTheme.typography.bodySmall,
                color = textColor,
                modifier = Modifier
                    .horizontalScroll(rememberScrollState())
                    .padding(vertical = 4.dp)
            )
        }
        return
    }
    Box(
        modifier = modifier.fillMaxWidth(),
        contentAlignment = Alignment.Center
    ) {
        Image(
            bitmap = bitmap,
            contentDescription = "数学公式",
            contentScale = ContentScale.FillWidth,
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 4.dp)
        )
    }
}

/** 块级公式文字色（未显式指定时跟随主题正文色） */
@Composable
private fun mathTextColor(fallback: Color): Color {
    if (fallback != Color.Unspecified) return fallback
    return androidx.compose.material3.MaterialTheme.colorScheme.onSurface
}

/**
 * 行内公式占位尺寸（sp）
 *
 * 高度按 1.5em 行内固定，宽度按位图比例换算并限制区间，
 * 超宽公式压缩宽度以尽量不打断行文
 */
fun inlineMathPlaceholder(w: Int, h: Int): Pair<Float, Float> {
    if (w <= 0 || h <= 0) return 24f to 24f
    val heightSp = 24f
    val widthSp = (heightSp * w / h).coerceIn(10f, 260f)
    return widthSp to heightSp
}

/** 供行内公式使用的文本大小（px），由调用方按屏幕密度换算 */
fun inlineMathTextSizePx(density: androidx.compose.ui.unit.Density): Float =
    with(density) { 15.sp.toPx() }
