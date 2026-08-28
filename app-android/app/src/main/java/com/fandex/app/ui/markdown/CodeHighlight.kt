package com.fandex.app.ui.markdown

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.produceState
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.buildAnnotatedString
import com.fandex.app.ui.theme.LocalExtendedColors
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

/**
 * 组合内的高亮代码文本（异步计算）
 *
 * 统一文档代码块与语法速查卡片的取色与缓存逻辑。
 * 高亮为 CPU 密集操作，放在 Default 调度器执行：
 * 先以纯文本立即呈现（无阻塞），完成后无缝替换为高亮版本，
 * 避免长代码块在主线程解析造成滚动与页面切换卡顿
 */
@Composable
fun rememberHighlightedCode(code: String, language: String): AnnotatedString {
    val extendedColors = LocalExtendedColors.current
    return produceState(
        initialValue = buildAnnotatedString { append(code) },
        code,
        language,
        extendedColors
    ) {
        value = withContext(Dispatchers.Default) {
            val palette = SyntaxHighlighter.Palette(
                text = 0,
                keyword = extendedColors.codeKeyword.toArgb(),
                string = extendedColors.codeString.toArgb(),
                number = extendedColors.codeNumber.toArgb(),
                comment = extendedColors.codeComment.toArgb(),
                annotation = extendedColors.codeAnnotation.toArgb(),
                function = extendedColors.codeFunction.toArgb(),
                tag = extendedColors.codeTag.toArgb()
            )
            SyntaxHighlighter.highlight(code, language, palette)
        }
    }.value
}
